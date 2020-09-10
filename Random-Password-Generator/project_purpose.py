import random


def get_char(typex, num):
    temp_list = []
    for i in range(num):
        temp_list.append(random.choice(typex))
    return temp_list


pass_len = 8
num_upper_char = 2
num_lower_char = 3
num_digits = 2
num_symbols = 1

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

password = char_digit + char_lower + char_symbol + char_upper

random.shuffle(password)
password = ''.join(password)
print(password)
