# def my_gen():

#     print('Hello world')
#     n = 0
#     yield n

#     print('Hello heaven')
#     n = 1
#     yield n

#     print('Hello hell')
#     n = 2
#     yield n

# a = my_gen()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



my_list = [1, 2, 3 ,7, 8, 10]

second_list = [x*2 for x in my_list]
second_gen = (x*2 for x in my_list)

print(second_list)