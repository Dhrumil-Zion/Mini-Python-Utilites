import random


def get_char(typex, num):
    temp_list = []
    for i in range(num):
        temp_list.append(random.choice(typex))
    return temp_list


while True:
    pass_len = int(input("Enter the lenth og password you want :"))
    num_upper_char = int(input("Enter the number of upper case in password you want :"))
    num_lower_char = int(input("Enter the number of lower case in password you want :"))
    num_digits = int(input("Enter the number of digits in password you want :"))
    num_symbols = int(input("Enter the number of symbols in password you want :"))
    if pass_len < num_digits + num_symbols + num_lower_char + num_upper_char:
        print("The enter value doesn't match with the length os the passsword length you have entered above")
    else:
        break

list_upper_char = [chr(i) for i in range(65, 65 + 26)]
char_upper = get_char(list_upper_char, num_upper_char)

list_lower_char = [chr(i) for i in range(97, 97 + 26)]
char_lower = get_char(list_lower_char, num_lower_char)

list_digits = [str(i) for i in range(0, 10)]
char_digit = get_char(list_digits, num_digits)

list_symbols = [chr(i) for i in range(33, 48)]
list_symbols += [chr(i) for i in range(58, 65)]
list_symbols += [chr(i) for i in range(91, 97)]
list_symbols += [chr(i) for i in range(123, 127)]
char_symbol = get_char(list_symbols, num_symbols)

num_unfilled_char = pass_len - num_upper_char - num_lower_char - num_digits - num_symbols

whole_list = list_upper_char + list_digits + list_lower_char + list_symbols
remaining_list = get_char(whole_list, num_unfilled_char)

password = char_digit + char_lower + char_symbol + char_upper + remaining_list

random.shuffle(password)
password = ''.join(password)
print(password)
