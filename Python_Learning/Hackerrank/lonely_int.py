items = [1,2,3,1,2,3,4]

def lonelyinteger(a):
    for x in a:
        if a.count(x) == 1:
            return x


print(lonelyinteger(items))

