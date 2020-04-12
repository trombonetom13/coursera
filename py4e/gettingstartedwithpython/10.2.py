name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)





def prefix():

    prefix = input("Enter line prefix to consider: ")

    if len(prefix) < 1 : prefix = "From"

    return prefix



def numof(lines,s):

    counts = dict()

    for line in lines:

        if line.startswith(s) and not line.startswith(s+':'):

            line = ((line.rstrip()).lstrip()).split()

            str = line[5]

            hour = str[0:str.find(":"):1]

            counts[hour] = counts.get(hour,0) + 1

        return counts



def sortTimes(d):

    lst = list()

    for key, val in d.items():

        lst.append((key,val))

        lst.sort()

        for val,key in lst:

            print (val,key)
