from pprint import pprint
list1 = []
for i in range(16):
    dict_one = {'bin':bin(i), 'dec' : i, 'hex':hex(i), 'oct':oct(i)}
    list1.append(dict_one)
pprint(list1)
