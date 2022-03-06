import pandas as pd

df = pd.read_csv("nato_alphabet/nato_phonetic_alphabet.csv")

alphabet_dict = {
    row.letter: row.code for (index, row) in df.iterrows()
}

def generate_phonetic():
    try:
        result = [alphabet_dict[letter.upper()] for letter in list(input("Enter a word: "))]
    except KeyError:    
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()