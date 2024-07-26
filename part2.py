'''
q1.
dictA = {key: value}
dictB = {value:key}
-> question1{key:value} -> return {value:key}
for dictA I can put in any key and value

q2.
original_dict = {'a':1, 'b':2, 'c':1, 'd':2}
return_dict = {1:['a','c'], 2:['b','d']}
return_dict -> key are integer, values are strings
question2(original_dict) -> return return_dict

q3.
dictA {a:1}
dictB {a:2, b:1}
return {a:3, b:1}

q4.
input and output both list
select all of number more than one time in original list.
input_list -> [[1, 2], [3, 2], [1, 5, 3], [6, 5]],
return -> [1,2,3,5]
return the list of numbers, where it appears more than one time
'''


def question1(n: dict) -> dict:
    '''
    my_dict = {}
    for k, v in n.items():
        my_dict[v] = k
    '''
    return {v: k for k, v in n.items()}


def question2(n: dict) -> dict:
    '''
    my_dict = {}
    for k, v in n.items():
        if v not in my_dict:
            my_dict[v] = [k]
        else:
            my_dict[v].append(k)
    '''
    return {v: [k for k in n if n[k] == v] for v in set(n.values())}


def question3(n1: dict, n2: dict) -> dict:
    my_dict_list = list(n1.keys())

    for i in range(len(n1)):
        if my_dict_list[i] in n2:
            n2[my_dict_list[i]] += n1[my_dict_list[i]]
        else:
            n2[my_dict_list[i]] = n1[my_dict_list[i]]

    return n2


def question4(n: list) -> list:

    my_dict = {}

    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j] not in my_dict:
                my_dict[n[i][j]] = 1
            else:
                my_dict[n[i][j]] += 1

    my_list = []

    for i in my_dict.keys():
        if my_dict[i] > 1:
            my_list.append(i)

    return my_list

    return my_list

print("Question1는:")
print(question1({'a': 1, 'b': 2, 'c': 1, 'd': 2}))

print("Question2는:")
print(question2({'a': 1, 'b': 2, 'c': 1, 'd': 2}))

print("Question3는:")
print(question3({'a': 1, 'c': 3, 'd': 5}, {'a': 2, 'b': 1, 'c': 4, 'e': 2, 'f': 6}))

print("Question4는:")
print(question4([[1, 2], [3, 2], [1, 5, 3], [6, 5]]))
