z =5

def uno():
    z = 3

    def dos():
        z = 2
        print(z)
    
    dos()
    print(z)

uno()
print(z)