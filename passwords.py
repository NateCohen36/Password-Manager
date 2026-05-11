import random
class Password():
    lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
    capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "~!@#$%^&*()-_=+[]|;:',.<>/?"
    numbers = "1234567890"

    lowercaseEncryption = "qzmbxkefyudjopvhnrcswtlgia"
    capitalEncryption = "QWZMKJXPNBVTCLARHYEDFGOSUI"
    symbolEncryption = "|@^#%~<)&*+]-_=;[]/?$!:>,.'"
    numberEncryption = "7482910635"

    @staticmethod
    def generatePassword(length, lowercaseNeeded, capitalNeeded, symbolsNeeded, numbersNeeded):
        if not lowercaseNeeded and not capitalNeeded and not symbolsNeeded and not numbersNeeded:
            return ""
        password = ""
        for i in range(length):
            characterNotPicked = True
            characterIndex = 0
            while(characterNotPicked):
                characterType = random.randint(1,4)
                if(characterType == 1 and lowercaseNeeded):
                    characterNotPicked=False
                    characterIndex = random.randint(0,(len(Password.lowercaseLetters)-1))
                    password += Password.lowercaseLetters[characterIndex]

                elif(characterType == 2 and capitalNeeded):
                    characterNotPicked=False
                    characterIndex = random.randint(0,(len(Password.capitalLetters)-1))
                    password += Password.capitalLetters[characterIndex]
                
                elif(characterType == 3 and symbolsNeeded):
                    characterNotPicked=False
                    characterIndex = random.randint(0,(len(Password.symbols))-1)
                    password += Password.symbols[characterIndex]

                elif(characterType == 4 and numbersNeeded):
                    characterNotPicked = False
                    characterIndex = random.randint(0,(len(Password.numbers))-1)
                    password += Password.numbers[characterIndex]
        return password

    @staticmethod
    def scramblePassword(password):
        characters = []
        for i in range(len(password)):
            characters.append(password[i])
        
        
        for i in range(len(characters)):
            tempChar = characters[i]
            randomIndex = random.randint(0, (len(characters)-1))
            characters[i] = characters[randomIndex]
            characters[randomIndex] = tempChar
        
        newPassword = ""
        for char in characters:
            newPassword += char
        return newPassword
    
    @staticmethod
    def calculatePasswordStrength(length, lowercaseNeeded, capitalNeeded, symbolsNeeded,numbersNeeded):
        percentage = 0
        if length == 0:
            return 0
        if not lowercaseNeeded and not capitalNeeded and not symbolsNeeded and not numbersNeeded:
            return 0
    
        if length <= 12:
            percentage += length*6
        else:
            percentage += 72
        
        if lowercaseNeeded:
            percentage += 7
        if capitalNeeded:
            percentage += 7
        if symbolsNeeded:
            percentage += 7
        if numbersNeeded:
            percentage += 7
        return percentage

    @staticmethod
    def encryptPassword(password):
        encryptedPassword = ""
        for i in range(len(password)):
            if password[i] in Password.lowercaseLetters:
                index = Password.lowercaseLetters.find(password[i])
                encryptedPassword += Password.lowercaseEncryption[index]
            
            elif password[i] in Password.capitalLetters:
                index = Password.capitalLetters.find(password[i])
                encryptedPassword += Password.capitalEncryption[index]

            elif password[i] in Password.symbols:
                index = Password.symbols.find(password[i])
                encryptedPassword += Password.symbolEncryption[index]

            else:
                index = Password.numbers.find(password[i])
                encryptedPassword += Password.numberEncryption[index]
        return encryptedPassword

    @staticmethod
    def decryptPassword(encryptedPassword):
        password = ""
        for i in range(len(encryptedPassword)):
            if encryptedPassword[i] in Password.lowercaseEncryption:
                index = Password.lowercaseEncryption.find(encryptedPassword[i])
                password += Password.lowercaseLetters[index]
            
            elif encryptedPassword[i] in Password.capitalEncryption:
                index = Password.capitalEncryption.find(encryptedPassword[i])
                password += Password.capitalLetters[index]

            elif encryptedPassword[i] in Password.symbolEncryption:
                index = Password.symbolEncryption.find(encryptedPassword[i])
                password += Password.symbols[index]

            else:
                index = Password.numberEncryption.find(encryptedPassword[i])
                password += Password.numbers[index]
        return password

        
            
        

            
        


                

        