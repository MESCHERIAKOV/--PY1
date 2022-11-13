import random
def get_random_password() -> str:
    num = "0123456789"
    ll = "abcdefghijklmnopqrstuvwxyz"
    Bl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    summ = ''.join([num, ll, Bl])
    a = random.sample(summ, 8)
    b = (''.join(map(str,a)))
    return b

print(get_random_password())
