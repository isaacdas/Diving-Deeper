# Task 1

user_year = int(input("Input a year: "))
if user_year %4 != 0: #Not a leap year
    print(user_year, "is not a leap year")
elif user_year %100 == 0 and not user_year %400 == 0: #finds the special condition
    print(user_year, "is not a leap year")
else:
    print(user_year, "is a leap year!")
