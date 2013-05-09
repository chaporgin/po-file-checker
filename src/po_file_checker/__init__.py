# coding: utf-8

from .base import check_files


def check(filename, skip_keys=None):
    """
    Вернуть список с непереведенными ключами.

    @type filename: str
    @type skip_keys: list
    @rtype: list
    """
    return list(check_files([filename], skip_keys))
