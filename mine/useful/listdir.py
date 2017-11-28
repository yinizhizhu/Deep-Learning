from os import listdir

for x in listdir('data'):
    print x


list1 = ["This", "is", "a", "test."]
for index, item in enumerate(list1):
    print index, item
