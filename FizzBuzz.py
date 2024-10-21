def fizz_buzz(list_of_numbers):
    for item in list_of_numbers:
        if item % 15 == 0:
            print(f"{item}: fizzbuzz!")
        elif item % 5 == 0:
            print(f"{item}: fizz!")
        elif item % 3 == 0:
            print(f"{item}: buzz!")
        else:
            print(f"{item}")

list_of_numbers = [x for x in range(1,101)]

fizz_buzz(list_of_numbers)
