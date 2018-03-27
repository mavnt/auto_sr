# coding=utf-8
from typing import List

from .logging_utils import logging


class auto_sr(object):
    def __init__(self, keys: List[str] = None, repr_: bool = True):
        logging.debug("keys (__init__) = {}".format(keys))
        self.keys = keys
        self.repr_ = repr_

    def __call__(self, *args, **kwargs):
        def generic_str_repr(*args__, **kwargs__) -> str:
            d: dict = args__[0].__dict__
            if self.keys is None:
                return str(d)
            else:
                return str(dict([(k, d[k]) for k in d.keys() if k in self.keys]))

        logging.debug("Replacing methods __str__ and __repr__ of {}.".format(args[0]))
        args[0].__str__ = generic_str_repr
        if self.repr_:
            args[0].__repr__ = generic_str_repr
        else:
            args[0].__repr__ = object.__repr__
        return args[0]
