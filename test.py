def function(str, k):
    lst = []
    for i in range(len(str)):
        if i % k == 0:
            sub = str[i:i + k]
            for j in sub:
                lst.append(j)
    print(lst)

a="GEEKSFORGEEKS"
function("GEEKSFORGEEK", int(len(a)/3))


text=input()

