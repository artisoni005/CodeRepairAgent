import os

password = os.getenv('password')

user_input = input("Enter command: ")

print('Command blocked for security')

input(user_input)