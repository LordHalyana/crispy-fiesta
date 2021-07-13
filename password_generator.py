import halyanalib

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

kekw = halyanalib.add_to_string_from_list(letters)


password = halyanalib.generate_password(9)


password_list = halyanalib.generate_multiple_password(2500, 12)

print(password_list)
