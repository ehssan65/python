import random
def national_code_generator():
    number_list = []
    _sum = 0
    out = ""
    for i in reversed(range(2, 11)):
        _j = random.randint(0, 9)
        number_list.append(str(_j))
        _sum += _j * i
    _m = _sum % 11
    if _m < 2:
        number_list.append(str(_m))
    elif _m >= 2:
        number_list.append(str(11 - _m))
    #print(number_list)
    return out.join(number_list)
for i in range(480):
    numcod = national_code_generator()+'\n'
    print(numcod)
    with open("cod.txt", "a") as f:
        f.write(numcod)
        #f.writelines(multiple_lines)
    f.close()
