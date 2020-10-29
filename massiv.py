import time


start_time = time.monotonic()


def binary_search(mylist, item):
    low = 0
    higt = len(mylist) - 1
    while low <= higt:
        mid = (low + higt) // 2
        guess = mylist[mid]
        if item == guess:
            return mid
        if item < guess:
            higt = mid - 1
        else:
            low = mid + 1
    return None

mass = list(range(1, 100, 1))
mass2 = list(range(1,200,1))
mass3 = list(range(1,600,1))
mass4 = list(range(1,1000,1))
my_list = [1, 5, 6, 7, 8, 10, 11]
print(binary_search(mass4, 675))
end_time = time.monotonic() - start_time

print("Час виконання:",end_time,"сек")