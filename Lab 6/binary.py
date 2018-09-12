def indexMatch(list1):
    global listMedian
    left, right = 0, len(list1)
    while (right - left) > 1:
        median = (right + left)// 2
        listMedian.append(median)
        if median == list1[median]:
            return median
        if median > list1[median]:
                left = median
        else:
                right = median
    else:
        if left == list1[left]:
            return left
        if right == list1[right]:
            return right
    return ("No Match Found!") # the function should return "No Match Found!" if there is no list1[i] = i

listMedian = [] # this line must be kept for submission