from caesar_cipher_art import logo 
print(logo)
should_start = True
while should_start == True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26

        def cipher_caesar(text_direction, input_text, text_shift):
            cipher = ""
            if text_direction == 'decode':
                text_shift *= -1
            for char in input_text:
                if char in alphabet:
                    position = alphabet.index(char)
                    new_position = position + text_shift
                    new_letter = alphabet[new_position]
                    cipher += new_letter
                else:
                    cipher += char
            print(f"The {direction}d text is: {cipher}")

        cipher_caesar(text_direction = direction, input_text = text, text_shift = shift)
        restart = input("Would you like to restart the program? Type 'yes' or 'no' ").lower()
        
        if restart == 'no':
            should_start = False
            print("Bye bye!")

    else:
        print("Please enter correct type")