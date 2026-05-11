* Password Manager

Description
* A python desktop application with a GUI for generating, managing, and storing passwords securely using basic encryption and local file storage


Features
* Generates passwords with customizable options (lowercase letters, capital letters, symbols, numbers)
* Length option from 1 - 30
* Persistent storage with json files
* Simulated password encryption
* Able to copy password from clipboard
* Loads and decrypts previously saved passwords
* Scrambles generated passwords
* Able to hide password
* User feedback for loading, saving, and copying
* Password Strength Indicator

How the application works
* GUI application for managing password (saving, loading, copying, generating)
* Before passwords are saved to a file, they are encrypted with a basic encryption algorithm
* Passwords are decrypted upon being loaded

Tools used
* Python
* Tkinter (GUI)
* JSON (Password Storage)
* Random Module (Password Generation)

NOTE
* The encryption algorithm in this program is custom and is used for educational purpose only, while the algorithm does hide the true password
when its saved to the JSON file, the encryption is not secure since anyone with access to the source code of this program will be able to decrypt the saved password

Author - Nathan Cohen
