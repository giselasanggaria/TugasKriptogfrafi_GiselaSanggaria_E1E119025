def encript(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def decript(chipertext, key):
    return encript(chipertext, key)

def main():
    print("Pilihan: \n1. Enkripsi\n2. Dekripsi")
    menu = int(input("Menu: "))

    if menu == 1:
        plaintext = str(input("Plaintext: "))
        key = str(input("Key: "))

        print("Hasil : ")
        print("Plaintext: ", plaintext)
        print("Enkripsi: ", encript(plaintext, key))
    elif menu == 2:
        chipertext = str(input("Chipertext: "))
        key = str(input("Key: "))

        print("Hasil : ")
        print("Chipertext: ", chipertext)
        print("Dekripsi: ", decript(chipertext, key))
    else:
        exit()

main()