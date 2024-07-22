def read_calls(file: open) -> {(str, str): int}:

    my_dict = {}
    lines = file.readlines()

    # to put lines into the list
    for line in lines:
        my_list = line.strip().split(':')
        my_dict_key = my_list[0]

        # to make the list into the dictionary
        for i in range(1, len(my_list)):
            my_tuple = (my_dict_key, my_list[i])
            if my_tuple not in my_dict:
                my_dict[my_tuple] = 1
            else:
                my_dict[my_tuple] += 1

    return my_dict





def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    my_dict = {}
    for my_tuple in calls:
        # print(my_tuple, calls[my_tuple])

        # if it is not in the new one. get it. to not get overwritten

        dict_key = my_tuple[0]
        inner_dict_key = my_tuple[1]
        # dictionary[key][innerkey] = value
        # create innerkey in the inner loop -> i will overwrite the previous one.
        # i should make a inner dict and create another one
        if dict_key not in my_dict:
            my_dict[dict_key] = {}

        my_dict[dict_key][inner_dict_key] = calls[my_tuple]
        """
        if inner_dict_key not in my_dict:
         #   my_inner_dict = {}
            my_dict[dict_key][inner_dict_key] = calls[my_tuple]
        else:
            my_dict[dict_key][inner_dict_key] = calls[my_tuple]
        """
        return my_dict
'''
        if my_inner_dict not in my_dict:
            my_dict[dict_key] = my_inner_dict
        else:
            my_dict[dict_key] += my_inner_dict
        '''

read_calls(open(r"call_data.txt", 'r'))

call1to2(read_calls(open(r"call_data.txt", 'r')))