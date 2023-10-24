#name: Mirah Blanchard
def encode(password):
    current_password = ""
    for i in password:
            i = (int(i) + 3) % 10
            current_password += str(i)
    return current_password

if __name__ == "__main__": 
    #loop to keep program running
    while True:
        #print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        #ask user to enter an option
        userchoice = int(input("\nPlease enter an option: "))

        #user chooses 1 - encode
        if userchoice == 1:
            password = input("Please enter your password to encode: ")
            #store encoded password
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        #user chooses 2 - decode
        if userchoice == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n")
        #user chooses 3 - exit
        if userchoice == 3:
            exit()