'''Gevent useful decorators'''

from functools import wraps, partial
import gevent


def async(func=None, timeout=10):
    '''
    Decorator to make functions asynchronous

    @param timeout: seconds to timeout
    '''

    if not callable(func):
        return partial(async, timeout=timeout)

    @wraps(func)
    def wrapper(*args):
        job = gevent.spawn(func, *args)
        job.join(timeout=timeout)
        return job.value

    return wrapper
