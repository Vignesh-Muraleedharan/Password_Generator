import streamlit as st
import random
import string

def generate_password(length, special_char):
    characters = string.ascii_letters + string.digits
    if special_char == 'Yes':
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Password Generator")

    # User Input
    length = st.slider("Password Length", min_value=6, max_value=20, value=10, step=1)
    special_char = st.radio("Contain special characters?", ("Yes", "No"))

    # Generate and display the password
    password = generate_password(length, special_char)
    st.write("Generated Password:", password)

if __name__ == '__main__':
    main()
