def max_integer(my_list=[]):
    if len(my_list) != 0:
        max_int = my_list[0]
        for i in range (len(my_list)):
            if my_list[i] > max_int:
                max_int = my_list[i]
        return (max_int)
    else:
        return (None)
