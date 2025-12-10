message = input("what is your message?")
key = int(input("what is your shift value?"))
def encryption(message, key):
    encryption_message = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encryption_message += new_char
        else:
            encryption_message += char
    return encryption_message
encrypted_message = encryption(message, key)
print("Encrypted message:", encrypted_message)