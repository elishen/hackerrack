
[N, I] = input().strip().split()
N = int(N)
I = int(I)

dict_ast = {}
for n in range(N):
    dict_ast[n] = [n]

lst_ast = list(range(N))

for i in range(I):
    [a, b] = input().strip().split()
    a = int(a)
    b = int(b)
    cntry_a = lst_ast[a]
    cntry_b = lst_ast[b]

    cntry_high = cntry_a
    cntry_low = cntry_b

    if (cntry_low > cntry_high):
        cntry_high, cntry_low = cntry_low, cntry_high

    if cntry_low != cntry_high:

        lst_ast[a] = cntry_low
        lst_ast[b] = cntry_low

        ast_high = dict_ast[cntry_high]
        ast_low = dict_ast[cntry_low]

        for ast in ast_high:
            lst_ast[ast] = cntry_low
            ast_low.append(ast)

        del dict_ast[cntry_high]
        dict_ast[cntry_low] = ast_low


keys = list(dict_ast.keys())
kisolated = 0
for key in keys:
    if len(dict_ast[key]) == 1:
        del dict_ast[key]
        kisolated += 1

keys = list(dict_ast.keys())
k = len(keys)
res = 0
for i in range(0, k-1):
    for j in range(i+1, k):
        k1 = len(dict_ast[keys[i]])
        k2 = len(dict_ast[keys[j]])
        res += k1 * k2
        # print(res)

# print(dict_ast)
# print(res)

res += int((kisolated * (kisolated-1) / 2)) + (kisolated * (N-kisolated))

print(res)
