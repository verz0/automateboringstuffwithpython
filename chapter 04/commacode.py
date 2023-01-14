spam = ['apples', 'bananas', 'tofu', 'cats']


def listo(list):
   
    count = 0
    a = ''
    while count < len(list) - 2:
        a += list[count] + ', '
        count += 1
    a += list[-2] + ' and '
    a += list[-1] + '.'
    return a
print(listo(spam))