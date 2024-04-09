import time
def typetime(unit):
    def time_decorator(func):
        def functime(*args, **kwargs):
            t1=time.time()
            func(*args, **kwargs)
            t2=time.time()
            if unit=='seconds':
                print(f'Time of function: {t2-t1} seconds')
            elif unit=='miliseconds':
                print(f'Time of function: {(t2-t1)*1000} miliseconds')
        return functime
    return time_decorator


@typetime('miliseconds')
def sleep():
    time.sleep(2)

sleep()