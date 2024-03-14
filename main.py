import streamlit as st
import random
import string
st.write("""
         Password Generator
         """
         )

def generate_password(length, special_char):
    chr = string.ascii_letters + string.digits
    password = ''
    if (special_char == 'y'):
        chr += string.punctuation
    for i in range(length):
        password += random.choice(chr)
    return password

#User Input
length = st.slider("Password Length", min_value=6, max_value=20, value=10, step=1)
special_char = st.radio("Contain special characters?", ("Yes", "No"))

#Generate and print the password
password = generate_password(length, special_char)
print("Generated password:", password)
