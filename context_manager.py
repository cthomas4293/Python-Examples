
class Test(object):
    # init method used to initialize your db or file I/O
    def __init__(self):
        print('init method called')

    # __enter__ method used for setting up your data for use and returning it to FileManager object
    def __enter__(self):
        print("__enter__ method called")
        return self

    # __exit__ method is where CM really are used, it closes the operations automatically.
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ method called")


# using this syntax you can either create your own variables and enter into
# with statement with those variables or use example below.
with Test() as T:
    print("with block called")
