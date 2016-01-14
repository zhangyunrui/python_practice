def quiksort(array):
    less = []; greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot: less.append(x)
        else: greater.append(x)
    return quiksort(less) + [pivot] + quiksort(greater)

if __name__ == "__main__":
    print quiksort([1, 100, 10, 2])