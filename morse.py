alphabet_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

def main():
    choose = input("code or decode ?: ").lower()
    if choose == "code":
        code()
    elif choose == "decode":
        decode()
    else:
        print("Invalid input...")

def code():
    coded = []
    text = input("To encode: ").lower()
    for i in text:
        if i.isalpha():
            coded.append(alphabet_morse[i])
            coded.append(" ")
        elif i == " ":
            coded.append("/")

    result = "".join(coded)
    print(result)

def decode():
    morse = input("To decode: ")
    words = morse.split("/")
    letters = []
    for i in words:
        letter = i.split()
        letters.append(letter)

    convert = []
    for i in letters:
        for j in i:
            conv = get_key(j)
            convert.append(conv)
        convert.append(" ")

    result = "".join(convert)
    print(result)


def get_key(my_value):
    for key, i in alphabet_morse.items():
        if i == my_value:
            return key

main()
