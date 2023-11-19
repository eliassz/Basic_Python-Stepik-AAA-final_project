import time
from functools import wraps
from typing import Any, Callable


def log(func: Callable) -> Callable:
    """
    A decorator that logs the execution time of the function it decorates.

    :param func: The function to be decorated.
    :type func: Callable
    :return: The wrapper function.
    :rtype: Callable
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"{func.__name__} — {execution_time:.2f}s!")
        return result

    return wrapper


def log_with_template(template: str) -> Callable:
    """
    A decorator factory that creates a decorator to log the execution time
    of the function it decorates, using a custom template for the log message.

    :param template: The template string to be used for formatting the log message.
    :type template: str
    :return: The decorator.
    :rtype: Callable
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            print(template.format(round(execution_time, 2)))
            return result

        return wrapper

    return decorator
