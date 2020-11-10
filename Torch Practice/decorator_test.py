
def add_wrapping(item):
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item

@add_wrapping
def new_gpu():
    return 'a new Tesla P100 GPU'

print(new_gpu.__name__)