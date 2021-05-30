# on  every year that is evenly divisible by 4
# 2021 / 4 = 502.25 (not leap)

# except every year that is evenly divisible by 100
#  2021 / 100 =  (not leap)

# unless the year is also evenly divisible by 400
# 2021 /400 = 5.0525 (not leap)


year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("That is a leap year.")
else:
    print("Not a leap year.")
