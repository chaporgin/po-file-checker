po-file-checker
===============

Checks whether your PO-files are fully translated.

Supports command-line interface
---------------

If there are keys without translations, exits with non-zero code and prints such keys into stderr.

```
/usr/share/pyshared/po_checker/check.py /usr/python/project/locale/ru/LC_MESSAGES/django.po || echo 'Failed'
myproject:Key
```

Can be called from Python
---------------

```
# coding: utf-8

import po_checker

missing = po_checker.check(
    '/usr/python/project/locale/ru/LC_MESSAGES/django.po',
    skip_keys=['key to skip']
)

if len(missing) > 0:
      print u'Error: Некоторые переводы в проекте отсутствуют'
```

Can be used inside django
-----------------

It does not depend on django, but you are free to use it as a management command.

```
django-admin.py makemessages --no-obsolete ... # This is a must before the checks - you should have a non-obsolete translations in your po-files.
./manage.py check_po_files -v0 -s 'key to skip' -s 'another key to skip'
```


