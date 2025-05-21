
import logoart
from logoart import logo
start= True
print(f"{logo}\n")
while start:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceaser(original_text=text,shift_amount=shift):
        cipher_text = ""
        if direction=="decode":
            shift_amount*=-1
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text+=letter

        print(f"Here is the {direction}d message: {cipher_text}\n")


    ceaser()
    restart=input("Would you like to go again?(Type yes or no)\n").lower()
    if restart=="no":
        start=False
        print("Goodbye!")
