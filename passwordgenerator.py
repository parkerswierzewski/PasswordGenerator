"""
PasswordGenerator

file: passwordgenerator.py
author: Parker J Swierzewski
language: python3
desc: This program will generate secure and strong passwords for you to use.

Last Update: 05-09-2020
"""
import datetime # Used to obtain the timestamp.
import os       # Used get the path of the output file.
import random   # Used to pick random values.
import string   # Used to access a string of letters and special characters.
import time     # Used to determine how long it took to generate the passwords.

VERSION = "1.0"
AUTHOR = "Parker J Swierzewski"

def generate_password(amount, length, special):
	"""
	This function generates the password based on the length provided
	and a the boolean value specialchar, 
	
	:param amount: Integer value represeting how many passwords to generate.
	:param length: Integer value representing the length of the password.
	:param specialchar: Boolean value representing whether or not to use special characters.
	:return: A list of the password(s) and the time it took as a tuple. 
	"""
	passwords = []                    # A list containing the password(s).
	chars = string.ascii_letters      # A string of all uppercase and lowercase characters.
	specialchars = string.punctuation # A string of all the special characters.
	start_time = 0                    # The start time of the generation
	end_time = 0                      # The end time of the generation.
	total_time = 0                    # The total amount of time it took.
	
	if special:
		start_time = time.time()
		for password in range(0, amount):
			password = "" # The password generated 
			for character in range(0, length):
				# 0 = A letter will be picked.
				# 1 = A special char will be picked.
				choice = random.randint(0, 1)
			
				if choice == 0:
					password += random.choice(chars)
				else:
					password += random.choice(specialchars)
			passwords.append(password)
		end_time = time.time()
	else:
		start_time = time.time()
		for password in range(0, amount):
			password = "" # The password generated 
			for character in range(0, length):
				password += random.choice(chars)
			passwords.append(password)
		end_time = time.time()
	
	total_time = (end_time - start_time)
	return (passwords, total_time)

def save_results(passwords):
	"""
	This function will save the results of the generator to an output file.
	
	file: generated-passwords.txt
	
	:param passwords: A list of passwords.
	:return: None
	"""
	filename = "generated-passwords.txt"
	path = os.path.realpath(filename)
	now = datetime.datetime.now()
	timestamp = f"{now.day}/{now.month}/{now.year} at {now.hour}:{now.minute}:{now.second}"

	# A flag to determine whether or not a file needs to be created.
	# By default it will assume it has to create the file.
	flag = True
	
	try:
		f = open(filename)
		print("\n[!] The file used previously was found!")
		flag = False
		f.close()
	except FileNotFoundError:
		print("\n[!] No file was found! Creating output file now.")
		
	if flag:
		with open(filename, 'w') as f:
			f.write("PasswordGenerator\n\n")
			f.write("Notice:\n")
			f.write("After you've copied and pasted the passwords to a new secure location (i.e. Password Manager\n")
			f.write("or encrypted file), delete this file so that the passwords are safe and can't be stolen from\n")
			f.write("the machine easily. If the program cannot detect this file it will create a new one exactly\n")
			f.write("like this one with different passwords. If you'd like to generate more passwords rerun the\n")
			f.write("program and save the results (the same way as earlier). The program will keep appending onto\n")
			f.write("this file until you delete it.\n\n")
			f.write("Time Format: DD/MM/YYYY at HH:MM:SS\n\n")
			f.write("Results from " + timestamp + ":")
			
			accum = 1
			for password in passwords:
				f.write("\n\t" + str(accum) + ") " + password)
				accum += 1
	else:
		with open(filename, 'a') as f:
			f.write("\n\nResults from " + timestamp + ":")
			
			accum = 1
			for password in passwords:
				f.write("\n\t" + str(accum)  + ") " + password)
				accum += 1
				
	print("[!] The file has been updated!")
	print("[!] Path to file:", path)
	
def format_results(passwords, total_time):
	"""
	This function will simply format the output to make it
	easier to view.
	
	:param passwords: A list of passwords.
	:param total_time: The time it took to generate the passwords.
	:return: None
	"""
	accum = 1
	
	print("\n[!] Results of the generator:")
	for password in passwords:
		print("\t", str(accum) + ")", password)
		accum += 1
	print("\n[!] Total time:", str(total_time) + "s")
	
if __name__ == "__main__":
	# Displays the program name, version, and some information on passwords.
	print("PasswordGenerator v" + VERSION, "by", AUTHOR, "\n")
	
	# Asking the user how many passwords should be generated.
	amount = input("[+] How many passwords would you like to generate: ")
	try:
		while int(amount) <= 0:
			print("[!]", amount, " is not a valid option (x>=1).")
			amount = input("[+] How many passwords would you like to generate: ")
	except ValueError:
		print("[!] You must enter an integer value! Rerun to try again.")
		exit(0)
	
	# Asking the user how long the password should be.
	print("\n[!] Secure passwords should have at least 20 characters.")
	length = input("[+] How many characters should the password be: ")
	try:
		while int(length) <= 0:
			print("[!]", length, " is not a valid option (x>=1).")
			length = input("[+] How many characters should the password be: ")
	except ValueError:
		print("[!] You must enter an integer value! Rerun to try again.")
		exit(0)
	
	# Asking the user whether or not they want t include special characters.
	special_chars = string.punctuation
	print("\n[!] Special characters make it harder for passwords to be cracked.")
	print("[!] Special characters include:", special_chars)
	special = input("[+] Do you want to include special characters? (y/n): ")
	
	if special.lower() == "y" or special.lower() == "yes":
		special = True
	elif special.lower() == "n" or special.lower() == "no":
		special = False
	else:
		print("[!] You must answer yes (y) or no (n)! Rerun to try again.")
		exit(0)
	
	# Calls the function to generate the passwords.
	passwords, total_time = generate_password(int(amount), int(length), special)
	
	# Formats the output and prints it to the screen.
	format_results(passwords, total_time)
	
	# Asks the user if they want to regenerate the passwords.
	regenerate_flag = True
	while regenerate_flag:
		print("\n[!] If you're not satisfied with the generated passwords above for any reason" + \
				"\n    you can regenerate a new set!")
		regenerate = input("[+] Would you like to regenerate the passwords seen above (y/n): ")
		if regenerate.lower() == "y" or regenerate == "yes":
			# Calls the function to generate the passwords.
			passwords, total_time = generate_password(int(amount), int(length), special)
			# Formats the output and prints it to the screen.
			format_results(passwords, total_time)
		elif regenerate.lower() == "n" or regenerate == "no":
			regenerate_flag = False
		else:
			print("[!] You must answer yes (y) or no (n)! Rerun to try again.")
			exit(0)
	
	# Asks the user if they'd like to save the passwords to a file.
	# The file will be saved in the same directory as the script.
	print("\n[!] It is recommended that you save these passwords to an output file and" + \
			"\n    save them to a password manager, like LastPass, or encrypt a new file" + \
			"\n    with the passwords stored within it.")
	save = input("[+] Would you like to store the results (y/n): ")
	
	if save.lower() == "y" or save.lower() == "yes":
		save = True
	elif save.lower() == "n" or save.lower() == "no":
		save = False
	else:
		print("[!] You must answer yes (y) or no (n)! Rerun to try again.")
		exit(0)
	
	if save:
		save_results(passwords)
	
	# End of the program.
	print("\n[!] The program has concluded.")
