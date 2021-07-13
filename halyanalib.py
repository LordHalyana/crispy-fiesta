import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Adds all things in a list to a string
def add_to_string_from_list(letter):
	new_string = ""
	for l in letter:

		new_string += str(l)

	return new_string



# Generates a password with a length of passed int
def generate_password(lenght):
	kekw = add_to_string_from_list(letters)
	new_list = []
	count = 0
	while count < lenght:
		new_list.append(random.choice(kekw))
		new_list.append(random.randint(0, 9))
		count += 1

	a = add_to_string_from_list(new_list)
	return a


# Generates multiple passwords, takes amount and lenght of password as params
def generate_multiple_password(amount, lenght):
	count = 0
	password_list = []
	while count < amount:
		a = generate_password(lenght)
		password_list.append(a)
		count += 1

	return password_list