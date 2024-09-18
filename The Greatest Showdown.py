# Task 1

num_1 = int(input("Input your first number: "))
num_2 = int(input("Input your second number: "))
num_3 = int(input("Input your third number: "))

#checks num_ to see which is greater than the other two
if num_1 > num_2 and num_3:
    print(num_1, "is the biggest number")
elif num_2 > num_1 and num_3:
    print(num_2, "is the biggest number")
elif num_3 > num_1 and num_2:
    print(num_3, "is the biggest number")

#checks num_ to see which is less than the other two 
if num_1 < num_2 and num_3:
    print(num_1, "is the smallest number")
elif num_2 < num_1 and num_3:
    print(num_2, "is the smallest number")
elif num_3 < num_1 and num_2:
    print(num_3, "is the smallest number")