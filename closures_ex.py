

def make_division_by(n):
    def division(x):
        return x/n
    return division

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))

if __name__ == '__main__':
    run()