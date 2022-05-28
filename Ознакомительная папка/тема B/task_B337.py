# Написать функцию spin_words, которая возвращает заданную строку,
# но переворачивает в обратном порядке все слова, состоящие из 5 или более букв
#
# Примеры:
# spin_words("This is a test") ==> "This is a test"
# spin_words("This is another test" ) ==> "This is rehtona test"

import traceback


def spin_words(sentence):
    # Тело функции
    oldlist = sentence.split()
    for i in range(len(oldlist)):
        if (len(oldlist[i])>=5):
            oldlist[i] = oldlist[i][::-1]
    ans = " ".join(oldlist)
    return ans


# Тесты
try:
    #assert spin_words("This is a test") == "This is a test"
    assert spin_words("notsuoH we have a melborp") == "Houston we have a problem"
    assert spin_words("Elementary my dear Watson") == "yratnemelE my dear nostaW"
    assert spin_words("Run tserroF run") == "Run Forrest run"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
