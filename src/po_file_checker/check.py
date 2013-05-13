#!/usr/bin/env python
# coding: utf-8

import sys
from po_file_checker.base import check_files

if __name__ == '__main__':
    missing = tuple(check_files(sys.argv[1:]))
    if missing:
        sys.stderr.write(
            "\n".join(missing)
        )
        sys.exit(1)

    sys.exit(0)
