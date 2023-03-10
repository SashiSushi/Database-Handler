import hashlib
import time
import random


def main():
    def salting():
        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5"]
        salt = ""
        n = 10

        for i in range(n):
            number = random.randint(0, len(letter) - 1)
            salt += letter[number]

        return salt

    def countDown():
        seconds = 10
        for i in range(seconds):
            if i == 0:
                print("00:" + str(seconds - i))
                time.sleep(1)
            else:
                print("00:0" + str(seconds - i))
                time.sleep(1)
        print("00:00" + "\n")
        time.sleep(1.5)
        main()

    # Login function
    def checkTables(password):
        for i in range(len(listUsers)):
            listUsers[i] = listUsers[i].split(",")

            if listUsers[i][0] == user:
                saltCheck = listUsers[i][2]
                password += saltCheck

                encryptedPassword = hashlib.md5(password.encode()).hexdigest()
                if encryptedPassword == listUsers[i][1]:
                    return True
        return False

    # check if username is already taken
    def checkUsernames():
        for i in range(len(listUsers)):
            listUsers[i] = listUsers[i].split(",")

        for i in range(len(listUsers)):
            if listUsers[i][0] == user:
                return True
        return False

    question = input("Press S to Sign up or L to log in ")

    # signup

    if question.upper() == "S":
        user = input("Username: ")
        password = input("Password: ")

        saltHash = salting()
        password += saltHash
        passwordEncoded = hashlib.md5(password.encode()).hexdigest()

        file = open("userTable.csv", "r")
        readFile = file.read()
        # print(readFile)
        file.close()

        listUsers = readFile.split("\n")

        if checkUsernames():
            print("Username already taken \n")
            main()

        else:

            file = open("userTable.csv", "w")
            newText = readFile + "\n" + user + "," + passwordEncoded + "," + saltHash
            file.write(newText)
            file.close()

            # DeBug
            file = open("userTable.csv", "r")
            readFile = file.read()
            # print(readFile)
            file.close()

    if question.upper() == "L":

        attempts = 0

        while attempts <= 3:

            user = input("Username: ")
            password = input("Password: ")

            file = open("userTable.csv", "r")
            readFile = file.read()
            file.close()

            listUsers = readFile.split("\n")
            # print(listUsers)

            if checkTables(password):
                print("Access Granted")
                exit()

            else:
                if attempts != 3:
                    print("\n" + "User not found or incorrect password")
                    print("Attempts remaining: " + str(3 - attempts) + "\n")
                attempts += 1

        print("Maximum attempts reached! Retry in: ")
        countDown()


main()
