import time

print('please insert your CARD')

time.sleep(2)

bank_name = input("please enter your bank name ?")
password = 1234

pin = int(input('enter your pin:'))

balance = 10000


if pin == password:
    while True:
        print('''
                1. Balance
                2. Withdraw balance
                3. Deposit balance
                4. Create account
                5. Create Pin
                6. Exit
        ''')

        try:
            option = int(input("please enter your option:"))
        except:
            print("please enter valid option:")

        if option == 1:
            print(f"your current balance is {balance}")


        if option == 2:
            withdraw_amount = int(input("please enter withdraw_amount:"))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your accuont")
            print(f"your current balance is {balance}")


        if option == 3:
            deposit_amount = int(input("please enter deposit_amount"))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your current balance is{balance}")



        if option == 4:
            print('''
                 Welcome to new account
                 ''')
            print(       f"Welcome {bank_name}"   )
            Name = input("Enter your name:")
            Aadhar_number = int(input("Enter your aadhar number:"))
            phone_number = int(input("Enter your phone number:"))
            print("            🙏🙏🙏Your account is successfully created🙏🙏🙏  \n                 Thank you for creating new account       ")
            print("                   You will get new account number to your register phone number!!            ")



        if option == 5:
            print('''
                     Welcome To Pin Gen
            ''')
            name = input('Enter Your Name:')
            Number = int(input('Enter Your Phone Number:'))
            New_Pin = int(input('Enter New Pin:'))
            Conform_Pin = int(input('conform your pin:'))
            print('Successfully completed 😊')


        if option == 6:
            break

else:
    print("wrong pin please try again😒")
