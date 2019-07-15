def Sequential_Search(dlist, item):
    position = 0
    found = False

    while position < len(dlist) and not found:
        if dlist[position] == item:
            found = True
        else:
            position = position + 1

    return found, position


print(Sequential_Search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31))
print(Sequential_Search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 43))