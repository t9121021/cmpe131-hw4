def allcaps(func):
    def wrapper():
        return func().upper()
    return wrapper
