# Now I have to combine both the encode and decrypt function


alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode'  to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Enter shift number: \n"))


def caeser(start_text,shift_amount,cipher_direction):
    end_text =""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabets.index(letter)
        if cipher_direction=="decode":
            shift_amount*=-1
        new_position=position +shift_amount
        end_text+=alphabets[new_position]
    print(f"The {cipher_direction}d text is {end_text} ")

caeser(start_text=text,shift_amount=shift,cipher_direction=direction)


