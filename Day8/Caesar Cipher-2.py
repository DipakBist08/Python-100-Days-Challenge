alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode'  to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Enter shift number: \n"))

def encrypt(plain_text,shift_amount):
    cipher_text = ""

    for letter in plain_text:

        position = alphabets.index(letter)
        new_position =position + shift_amount
        new_letter = alphabets[new_position]
        cipher_text +=new_letter
    print(f"The encoded text is {cipher_text}")

#Decode the inputted text
def decrept(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = position- shift_amount
        plain_text += alphabets[new_position]
    print(f"The decoded tex is {plain_text} ")

if direction =="encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrept(cipher_text=text,shift_amount=shift)




