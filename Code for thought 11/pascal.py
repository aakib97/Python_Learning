### Code for thought #11
### Pascal triangle
### In this assignment, we use recursion and list comprehension to
### generate a line of Pascal triangle.
### For an input n, we generate the n-th line of the Pascal triangle.
### For your information, a Pascal triangle looks like the following.
###             1
###           1    1
###        1    2    1
###      1    3    3    1
###    1    4    6    4    1
### 1    5    10    10    5    1
def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n - 1)
        line = [sum(p_line[x:x + 2]) for x in range(len(p_line) - 1)]
        line.insert(0, 1)
        line.append(1)
    return line
