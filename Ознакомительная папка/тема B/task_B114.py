# Написать функцию duplicate_encode, которая получает строку и преобразует ее: 
# если символ в строке появляется один раз, то заменить на "(", 
# иначе заменить на ")", если символ появляется больше одного раза. Регистр не должен иметь значение.
#
# Примеры:
# duplicate_encode("hello world") ==> "(()))(()()("

import traceback


def duplicate_encode(word):
    # Тело функции
    newword=[]
    ans=""
    for i in range(len(word)):
        letter=word[i].lower()
        
        newword.append(word.count(letter))
    for i in range(len(newword)):
        #print(newword[i])
        if (newword[i]>1):
            ans+=")"
        else:
            ans+="("
    #5print (ans)
    return ans


# Тесты
try:
    assert duplicate_encode("hello world") == "(()))(()()("
    assert duplicate_encode("abc") == "((("
    assert duplicate_encode("(( @") == "))(("
    assert duplicate_encode("Success") == ")())())"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

