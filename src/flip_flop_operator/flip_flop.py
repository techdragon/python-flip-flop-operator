# -*- coding: utf-8 -*-
import inspect
import logging

from infix import or_infix

LOG = logging.getLogger(__name__)


@or_infix
def flip_flop(condition_one, condition_two):
    """
    A Flip Flip Operator, as seen in Ruby and Perl.

    Returns a boolean that flips from false to true when condition_one is True and
    then back to false when condition_two is True.

    :param condition_one:
    :param condition_two:
    :return bool:
    """
    frame = inspect.currentframe()
    unique_func_identifier = '_'.join([
        str(frame.f_back.f_back.f_code.co_filename),
        str(frame.f_back.f_back.f_code.co_name),
        str(frame.f_back.f_back.f_lineno),
    ])
    LOG.debug('Created unique function identifier. {}'.format(unique_func_identifier))
    if unique_func_identifier not in globals():
        globals()[unique_func_identifier] = False
    if condition_one and not globals()[unique_func_identifier]:
        globals()[unique_func_identifier] = True
        LOG.debug('{} flipped on.'.format(unique_func_identifier))
        return False
    elif not condition_one and not condition_two and globals()[unique_func_identifier]:
        return True
    elif not condition_one and condition_two and globals()[unique_func_identifier]:
        globals()[unique_func_identifier] = False
        LOG.debug('{} flipped off.'.format(unique_func_identifier))
        return False
    elif not condition_one and not condition_two and not globals()[unique_func_identifier]:
        return False


# TODO: This doesnt work in python 2. Find a way to fix that.
# ꓺ = flip_flop
