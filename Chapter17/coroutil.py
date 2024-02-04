from functools import wraps


def coroutine(func):
    """
    装饰器：向前执行到第一个yield表达式，预激func
    :param func:
    :return:
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

