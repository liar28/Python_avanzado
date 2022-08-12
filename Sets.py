def remove_duplicates(some_list):
    wo_duplicates = []
    for element in some_list:
        if element not in wo_duplicates:
            wo_duplicates.append(element)
    return wo_duplicates


def run():
    random_list = [1, 1, 2, 4]
    print(remove_duplicates(random_list))


def main():
    random_list = [1, 1, 1, 1, 1, 2, 4]
    rm_duplicates = list(set(random_list))
    print(rm_duplicates)


if __name__  == '__main__':
    main()