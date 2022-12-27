mysentence = "loves the color"

color_list = ['red', 'blue', 'purp',  'green', 'pink']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name, mysentence, i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name  = input('what is your name: ')
        if name == '':
            print("provide a name")
        elif name == "Sally":
            print('no')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


get_name()
