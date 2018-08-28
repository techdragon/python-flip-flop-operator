import inspect
import logging

from infix import or_infix

LOG = logging.getLogger(__name__)


@or_infix
def flip_flop(condition_one, condition_two):
    frame = inspect.currentframe()
    unique_func_identifier = f'{frame.f_back.f_back.f_code.co_filename}_{frame.f_back.f_back.f_code.co_name}_{frame.f_back.f_back.f_lineno}'
    LOG.debug(f'Created unique function identifier. {unique_func_identifier}')
    if unique_func_identifier not in globals():
        globals()[unique_func_identifier] = False
    if condition_one and not globals()[unique_func_identifier]:
        globals()[unique_func_identifier] = True
        LOG.debug(f"{unique_func_identifier} flipped on.")
        return False
    elif not condition_one and not condition_two and globals()[unique_func_identifier]:
        return True
    elif not condition_one and condition_two and globals()[unique_func_identifier]:
        globals()[unique_func_identifier] = False
        LOG.debug(f"{unique_func_identifier} flipped off.")
        return False
    elif not condition_one and not condition_two and not globals()[unique_func_identifier]:
        return False


ꓺ = flip_flop
