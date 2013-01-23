'''Gevent useful decorators'''



def async(func, timeout=2):
    '''
    Decorator for make functions asynchronous
    '''

    @wraps(func)
    def wrapper(*args):
        jobs = [gevent.spawn(func, *args)]
        gevent.joinall(jobs, timeout=timeout)
        return jobs[0].value

    return wrapper
