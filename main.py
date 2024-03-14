import streamlit as st
import randomstre
import string

def generate_password(length, special_char):
    chr = string.ascii_letters + string.digits
    password = ''
    if (special_char == 'y'):
        chr += string.punctuation
    for i in range(length):
        password += random.choice(chr)
    return password

#User Input
length = int(input("Enter the length of the password: "))
special_char = input("Contain special characters? (y/n): ").lower()

#Generate and print the password
password = generate_password(length, special_char)
print("Generated password:", password)
