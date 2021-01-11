def ProductSum(L):
    total = 0
    for i in range(len(L)):
        if isinstance(L[i], list):
            if i % 2 == 0:
                total += (2 * ProductSum(L[i]))
            else:
                total += (3* ProductSum(L[i]))
        else:
            total += L[i]
    return total

#print(ProductSum([[6,[[[6,8]]]]]))