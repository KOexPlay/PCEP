def evenNum(list):
    count = 0
    for item in list:
        if item % 2 == 0:
            count += 1
    return count


def checkSort(list, type):
    for i in range(len(list)-1):
        if type == "integerF":
            if list[i] > list[i + 1]:
                return False
                break
        else:
            if list[i] > list[i + 1]:
                return False
    return True


def sumList(list):
    total = 0
    for item in list: total += item
    return total
    

print(sumList([2, 3, 4]))