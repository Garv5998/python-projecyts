from cryptography.fernet import Fernet  #module used to encrypt the passowrds


#function used to create a key file it is used only one time for generating the key file
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #wb= write in bytes mode 
        key_file.write(key)'''

#function to load the key
def load_key():
    file = open("key.key", "rb") #rb= read in bytes mode
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key) #inititalising key by this 

#b'hello'=byptes string is diff from normal string
#"hello"=normalstring


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
#convet pwd encrypted version into decrypted version we need encode the password 1st to convert it into bytes 
#than we decode our byte string into normal string usimg .decode()


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
#convet pwd in encrypted version we need encode the password 1st to convert it into bytes 
#than we decode our byte string into normal string usimg .decode()


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
