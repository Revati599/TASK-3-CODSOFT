#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string
def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lower + upper + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

while True:
    length = int(input("Enter the length of the password (should be 8 or more): "))

    if length <8:
        print("Password length should be  more than 8")
        continue

    password = generate_password(length)
    print("Generated Password:", password)

    again = input("Do you want to generate another password? (yes/no): ").lower()
    if again != 'yes':
        break


# In[ ]:




