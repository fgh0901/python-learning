import random
a = []
n= 5
def random_char(upper = True):
    if upper:
        t = random.randint(ord('A'),ord('Z'))
        return chr(t)
    else:
        t = random.randint(ord('a'),ord('Z'))
        return chr(t)

def random_string(length):
    s = ''
    for i in range(length):
        s+=random_char()
    return s
