
string = "13999999999"
newstring = ''
conunt = 0
for i in string:
    conunt += 1
    if conunt < 4:
        newstring += i
    else:
        if conunt > 7:
            newstring += i
        else:
            newstring += "*"

print(newstring)


# string1 = list(string)
# print(string1)
# string2 = str(string1[0:3]) + "****" + str(string1[6:10])
# print(string2)
#
# print(string3)