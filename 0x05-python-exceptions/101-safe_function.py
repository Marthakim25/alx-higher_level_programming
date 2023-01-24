#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Executes a function safely.
    Args:
    fct: the function to execute.
    args: Argument for fct.
    Returns:
    if an error occurs - None.
    otherwise - the result of the call to fct.
    """
    try:

        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
