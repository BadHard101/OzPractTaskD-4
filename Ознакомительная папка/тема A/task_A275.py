# Написать функцию list_of_sums(lst), которая получает на вход список чисел и возвращает только те, 
# которые равны сумме всех предшествующих элементов этого списка.
#
# Пример:
# list_of_sums([2,3,5,6]) ==> [5] -> 5 = 2 + 3
# list_of_sums([10,20,30,60,-120,0]) ==> [30,60,0]


import traceback


def list_of_sums(lst):
    new_list = []
    for i in range(2,len(lst)):
        sum_pred=0
        for j in range(0,i):
            sum_pred+=lst[j]
        if(sum_pred==lst[i]):
            #print (lst[i-2],lst[i-1],lst[i])
            new_list.append(lst[i])
    #print (new_list)
    return new_list

# Тесты
try:
    assert list_of_sums([2,3,5,6]) == [5]
    assert list_of_sums([1,2,3,6,12,24]) == [3,6,12,24]
    assert list_of_sums([10,20,30,60,-120,0]) == [30,60,0]
    assert list_of_sums([1,-1,0,0,0]) == [0,0,0]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

