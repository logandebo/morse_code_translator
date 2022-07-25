import morse_code

again = "Y"

while again == "Y":

    user_input = input("Type a message that will be converted into morse code:\n")

    for char in user_input:
        try:
            if char != " ":
                print(morse_code.morse_translation[char.upper()], end="   ")
            else:
                print("       ", end="")
        except KeyError:
            pass

    again = input('\nEnter "Y" to translate another message, or any other key to quit the program: ').upper()
