# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:25:04 2020

@author: Awam Victor
"""

class Staff():
    """An Object representation of Staffs"""
    def __init__(self, password="", username=""):
        """Initialize a staff"""
        self.password = password
        self.username = username
        
    def attemptLogin(self):
            
            username = input(" What is your username")
            
            password =input(" What is your password")
            username= username.lower()
            
            Staff.login(username, password)
        
    def login(username, password):
            """perform the login"""
            """read the staff.txt file"""
            staff_file = 'staff.txt'
            with open(staff_file,'r') as staff_data:
                
                if username in staff_data.read():
                    Staff.loginSuccess("")
                else:
                    print("Invalid username")
                    Staff.attemptLogin("")
                    
    def loginSuccess(self):
        print("A: Create Account")
        print("B: Check Account Details")
        print(" C: Logout")
        
        choice = input("What do you want to do")
        if choice == 'A':
            print("Start creating account")
        elif choice =='B':
            print('check account details')
        else:
            print("log the user out")
        
                    
        