import string

# List of printable characters
myCharacters = list(string.printable)

# Function to decrypt the substitution cipher
def decrypt(encryptedWord, key=10):
    actual = ""
    maxIndex = len(myCharacters)
    for char in encryptedWord:
        currentIndex = myCharacters.index(char)
        newIndex = (currentIndex - key) % maxIndex
        newChar = myCharacters[newIndex]
        actual += newChar
    return actual

# Main function to get user input and perform decryption
def main():
    print("Welcome to the Decryption Program!")

    while True:
        encryptedWord = input("\nPlease enter the word to decrypt: ").strip()
        if not encryptedWord:
            print("You didn't enter any word. Please try again.")
            continue

        decrypted = decrypt(encryptedWord)
        print(f"\nDecrypted word: {decrypted}")

        example_encrypted_word = "K$WZSXfecb"
        example_decrypted_word = decrypt(example_encrypted_word)
        print(f"\nExample: Decrypted '{example_encrypted_word}' to '{example_decrypted_word}' (ATMPIN5421)")

        another = input("\nWould you like to decrypt another word? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Decryption Program. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
