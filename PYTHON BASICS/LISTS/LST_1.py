my_list = [4, 3, 6, 1, 7]
print(my_list)
deleted_item1= my_list.pop(0)
deleted_item2= my_list.pop(3)
my_list.insert(0, deleted_item2)
my_list.insert(4, deleted_item1)
print(my_list)