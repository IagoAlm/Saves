list_string = ['\t\t\t\t', '\t\t\n\t\t', '\t']

for i in range(len(list_string)):
    firstChar = list_string[i][0]
    contr = bool()
    for char in list_string[i]:
        if len(list_string[i]) <= 1:
            contr = False
            break
        if firstChar != char:
            contr = False
            break
            print('dif')
        else:
            contr = True
    if contr:
        list_string[i] = '-middle-'
print(list_string)
