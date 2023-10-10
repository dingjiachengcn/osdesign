import traceback

def foo():
    boo()

def boo():
    zoo()

def zoo():
    traceback.print_stack()

foo()