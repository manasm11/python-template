"""Logging functions."""

import inspect
import json
import os
import traceback

levels = {
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "EXCEPTION": 4,
}

LOG_PARSED_JSON = True


def _p(type, caller, *args, **kwargs):
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    isPrintLog = levels[LOG_LEVEL] <= levels[type]
    if isPrintLog:
        if not LOG_PARSED_JSON:
            args = [json.dumps(arg) if isinstance(arg, dict) else arg for arg in args]
        print(f"[{type}] ({caller}): ", *args, **kwargs, flush=True)


def debug(msg, *args, **kwargs):
    """Print a debug message."""
    _p("DEBUG", inspect.stack()[1].function, msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """Print a info message."""
    _p("INFO", inspect.stack()[1].function, msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    """Print a warn message."""
    _p("WARN", inspect.stack()[1].function, msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """Print a error message with stacktrace."""
    _p("ERROR", inspect.stack()[1].function, msg, *args, **kwargs)
    traceback.print_exc()


def exception(msg, exceptionType, *args, **kwargs):
    """Raise a 'exceptionType' exception with stacktrace."""
    _p("EXCEPTION", inspect.stack()[1].function, msg, *args, **kwargs)
    raise exceptionType()
