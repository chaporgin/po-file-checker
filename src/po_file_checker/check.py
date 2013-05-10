#!/usr/bin/env python
# coding: utf-8

import sys
from po_file_checker.base import check_files

if __name__ == 'main':
    missing = tuple(check_files(sys.argv))
    if missing:
        sys.stderr.write(
            "\n".join(missing)
        )
        sys.exit(1)

    sys.exit(0)
