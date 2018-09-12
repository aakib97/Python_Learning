s = list(input())
if len(s) != 4:
    sys.exit()
for i in range(len(s)):
    if s[i] not in d.keys():
        sys.exit()
results = set()
s1 = [0, 1, 2, 3]
for L in list(itertools.permutations([0, 1, 2, 3], 4)):
    for i in range(4):
        s1[i] = s[L[i]]

    ops1 = [ops[0], ops[0], ops[0]]
    for i in range(len(ops)):
        for j in range(len(ops)):
            for k in range(len(ops)):
                ops1[0] = ops[i]
                ops1[1] = ops[j]
                ops1[2] = ops[k]
                results = results | evaluatefive(ops1, s1)
for result in results:
    print(result)
print(str(len(results)) + " solutions.")

