import time
def timestamp(func):
    def wrapper():
        print(time.ctime())
        return func()
    return wrapper
