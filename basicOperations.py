x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []
i = 0; 
while i < 9:
    x_list.append(x) 
    y_list.append(y)
    i +=1
big_list.extend(x_list)
big_list.extend(y_list)
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")