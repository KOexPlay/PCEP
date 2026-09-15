list2 = [1,2,3,2,1]
list1 = [5, 3, 1, 7, 7, 8, 3, 9, 10]



def Min(tList):
    minNum = 100000000000000000000
    for i in tList:
        if i < minNum:
            minNum = i
    return minNum


def counting(tList, num):
    count = 0
    for i in tList:
        if i == num:
            count += 1
    return count


def removeDupe(tList):
    return list(set(tList))

def palindrome(tList):
    midPoint = len(tList)//2
    if tList[:] == tList[::-1]:
        return True
    else:
        return False

print(palindrome(list2))



