# coding: utf-8

import polib


def entries_with_missing_translations(po):
    """
    Генератор непереведенных записей в po-файле.

    @type po: POFile
    @rtype: POEntry
    """
    for entry in po:
        if not entry.translated():
            if not entry.occurrences:
                continue
            if not entry.msgstr and entry.msgstr_plural:
                # У некоторых записей есть msgstr_plural, но нет msgstr.
                # Их считаем переведенными, если они не obsolete и не fuzzy!
                if not entry.obsolete and 'fuzzy' not in entry.flags:
                    continue
            yield entry


def missing_keys(po):
    """
    Генератор непереведенных ключей.

    @type po: POFile
    @rtype: str
    """
    for entry in entries_with_missing_translations(po):
        if not entry.msgstr:
            yield entry.msgid
        else:
            yield entry.msgid_plural


def check_files(filenames, skip_keys=None):
    """
    Генератор отсутствующих ключей из po-файлов.

    @type filenames: iterable
    @param skip_keys: Пропускать заданные ключи.
    @type skip_keys: list
    @rtype: str
    """
    if skip_keys is None:
        skip_keys = tuple()
    for filename in filenames:
        for key in missing_keys(polib.pofile(filename)):
            if key in skip_keys:
                continue
            yield key
