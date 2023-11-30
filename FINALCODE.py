Dictionary= {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

def encrypt_to_morse(phrase):
    return ' '.join(Dictionary.get(char.upper(), ' ') for char in phrase)

def decrypt_from_morse(morse_code):
    morse_code = morse_code.split(' ')
    return ''.join(key for code in morse_code for key, value in Dictionary.items() if code == value)

def start_app():
    print("WELCOME TO THE MORSE CODE TOOL")
    while True:
        print("Select an action:")
        print("'!' for Encryption")
        print("'$' for Decryption")
        print("'#' to Exit")

        user_choice = input().upper()

        if user_choice == '!':
            plaintext = input("Enter the text to encrypt: ")
            encrypted_text = encrypt_to_morse(plaintext)
            print(f"Encrypted text: {encrypted_text}\n")
        elif user_choice == '$':
            morse_code = input("Enter Morse code to decrypt: ")
            decrypted_text = decrypt_from_morse(morse_code)
            print(f"Decrypted text: {decrypted_text}\n")
        elif user_choice == '#':
            print("Thank you for using this application, goodbye.")
            break
        else:
            print("Unknown option. Please select '!' for Encryption, '$' for Decryption, or '#' to Exit.\n")


if __name__ == "__main__":
    start_app()