import pandas as pd
morse = pd.read_csv("morse.csv", names=["letter", "code"])
user_string = input("Type your message to encrypt: ")
morse_code = ""

for letter in range(len(user_string)):
    try:
        morse_code += morse.code[morse.letter == user_string[letter].capitalize()].values + " "
    except ValueError:
        if user_string[letter] == " ":
            morse_code += " / "
        elif user_string[letter] == '"':
            morse_code += morse.code[morse.letter == "asps"].values + " "
        elif user_string[letter] == ",":
            morse_code += morse.code[morse.letter == "comma"].values + " "
        else:
            continue
print(f"You message in Morse code is: {morse_code[0]}")
