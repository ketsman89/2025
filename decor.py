def check_len(fun):
    def dec(*args, **kwargs):
        if len(args[0]) > 5:
            return "too many"
        
        value = fun(*args, **kwargs)
        value = value/2
        return value
    return dec

@check_len
def my_len(lst):
    return len(lst)

print(my_len([1, 2, 3, 4, ]))
        