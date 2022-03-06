PLACEHOLDER = "[name]"

#TODO: Create a letter using starting_letter.txt 
with open("Input/Letters/starting_letter.txt", mode="r") as s_letter:
    content = s_letter.read()

#for each name in invited_names.txt
with open("Input/Names/invited_names.txt", mode="r") as i_names:
    names = i_names.readlines()
    #Replace the [name] placeholder with the actual name.
    for name in names:
        new_letter = content.replace(PLACEHOLDER, name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as new_file:
            #Save the letters in the folder "ReadyToSend".
            new_file.write(new_letter)
