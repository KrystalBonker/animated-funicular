# Krystal Bonker 8/11/23

def hello_name(user_name):
   name = input("USERNAME")
   print("Hello, " + name.upper() + "!")


def first_odds():
    odd_numbers = list(range(1,100 +1, 2))
    print(odd_numbers)
    return


def max_num_in_list(a_list):
    max_num = max(a_list)
    print(max_num)


def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    if a_year % 100 == 0:
        return False
    return a_year % 400 == 0

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list),max(a_list)+1))

