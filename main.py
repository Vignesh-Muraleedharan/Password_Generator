import streamlit as st
import random
import string
import pyperclip

#---STREAMLIT CONFIG HIDE---#
hide_st_style = """<style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("🔒Password Generator")

def generate_password(length, special_char):     
    chr = string.ascii_letters
    password = ''
    if (num == 'Yes'):
        chr += string.digits
    if (special_char == 'Yes'):
        chr += string.punctuation
    for i in range(length):
        password += random.choice(chr)
    return password

#User Input
length = st.slider("Password Length", min_value=6, max_value=24, value=10, step=1)
special_char = st.radio("Contain special characters?", ("Yes", "No"))
num = st.radio("Contain numbers?", ("Yes", "No"))

# Generate and print the password
password = generate_password(length, special_char)
st.write("Generated Password: ", password) 

#st.button("🔁")

if st.button("Copy to Clipboard"):
    pyperclip.copy(password)
    st.write("Password Copied to Clipboard")