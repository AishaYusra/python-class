# file = open('demo.txt', 'rt')

# result = file.read()
# result2 = file.readline()
# print(file.readlines())
# print(result)
# print(result2)

# file = open('demo.txt', 'w')
# # file.write('I was born in August.')

# # More lines
# # file.writelines(['I was born in August\n', 'I love Nigeria\n', 'I use glasses\n'])
# # # file.close()

# with open('demo.txt', 'w') as anything:
#     anything.write('welcome')

# with open('demo.txt', 'r') as file:
#     result = file.read()

# print(result)


# f = open('demo.txt', 'r')

# contents = f.read()
# print(contents)

# f = open('demo.txt', 'r')
# content = f.readline()
# content2 = f.readline(7)
# print(content2)

# f = open('demo.txt','w')
# f.write('Hello World')

# with open('demo.txt','w') as f:
#     f.write('This is a nice day')

# with open('demo.txt','a') as f:
#     f.write('This is a nice month\n')

with open('demo.txt', 'w+') as f:
    f.write('Adding this information')
    f.seek(0)
    print(f.read())


