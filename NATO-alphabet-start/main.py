import pandas

nato_panda = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in nato_panda.iterrows()}
print(phonetic_dict)

def generate_ph():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("sorry, only letters in the alphabet please")
        generate_ph()

    else:
        print(output_list)

generate_ph()

