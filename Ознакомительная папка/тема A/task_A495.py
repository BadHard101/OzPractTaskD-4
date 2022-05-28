# Написать функцию highest_rank(arr), которая возвращает самое часто встречающееся число в списке,
# если таких чисел несколько - вернуть наибольшее.
#
# Пример:
# highest_rank([1,0,1,0,1,0,1) => 1


import traceback


def highest_rank(arr):
    maxx=max(arr)
    listt=[0]*(maxx+1)
    for i in range(0,len(arr)):
        listt[arr[i]]+=1
    #print (listt)
    maxx=max(listt)
    for i in range(0,len(listt)):
        if (listt[i]==maxx):
            maxx_i=i
    return maxx_i


# Тесты
try:
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
    assert highest_rank([2, 10, 8, 2, 7, 6, 4, 10, 2, 10]) == 10
    assert highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]) == 3
    assert highest_rank([1, 2, -3, 1, 2, -3, 1, 2, -3, 1, 2, -3]) == 2
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
