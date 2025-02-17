from DataStructures.List import single_linked_list as sl

def new_stack():
    return sl.new_list()

def push(my_stack, element):
    return sl.add_last(my_stack, element)

def pop(my_stack):
    return sl.remove_last(my_stack)

def is_empty(my_stack):
    return sl.is_empty(my_stack)

def top(my_stack):
    return sl.last_element(my_stack)

def size(my_stack):
    return sl.size(my_stack)