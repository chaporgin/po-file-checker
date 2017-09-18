# -*- coding: utf-8 -*-

import os
import sys
from collections import namedtuple

from django.conf import settings
from django.core.management.base import BaseCommand

from po_file_checker.base import check_files

Domain = namedtuple('domain', ['name', 'must_exist'])
DOMAINS = (
    Domain('django', must_exist=True),
    Domain('djangojs', must_exist=False),
)


ERROR_MISSING_FILES = 1
ERROR_FILE_DOES_NOT_EXIST = 2


class Command(BaseCommand):
    help = "Check all po-files in project"

    requires_system_checks = False

    def add_arguments(self, parser):
        parser.add_argument('--skip', '-s', action='append', dest='skip',
                            help='Don\'t check the key (may be applied multiple times)')

    def handle(self, *args, **options):
        verbosity = int(options['verbosity'])

        missing = tuple(check_files(
            self.generate_filenames(verbosity),
            skip_keys=options['skip'] or tuple()
        ))

        if missing:
            for key in missing:
                print 'The key is not fully translated: "%s"' % key
            sys.exit(ERROR_MISSING_FILES)

    def generate_filenames(self, verbosity):
        """
        Вернуть список имен po-файлов.

        @type verbosity: int
        @rtype: list
        """
        filenames = []

        for domain in DOMAINS:
            localedir = os.path.abspath('locale')
            languages = [lang[0] for lang in settings.LANGUAGES]
            for locale in languages:
                basedir = os.path.join(localedir, locale, 'LC_MESSAGES')
                pofile = os.path.join(basedir, '%s.po' % domain.name)

                if verbosity > 0:
                    print 'processing file "{0}"'.format(pofile)

                if domain.must_exist and not os.path.exists(pofile):
                    sys.stderr.writelines(
                        'pofile is obligatory and does not exist: "{0}"'.format(
                            pofile
                        )
                    )
                    sys.exit(ERROR_FILE_DOES_NOT_EXIST)

                if os.path.exists(pofile):
                    filenames.append(pofile)

        return filenames
