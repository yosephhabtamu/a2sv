import math
def flagstone(value):
    n, m ,a = value.split()
    n = int(n)
    m = int(m)
    a = int(a)
    row = math.ceil(n/a)
    col = math.ceil(m/a)
    counter = row*col
    return counter

value = input()
print(flagstone(value))