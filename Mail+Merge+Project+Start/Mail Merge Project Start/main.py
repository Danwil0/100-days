#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/Names/invited_names.txt") as list_of_names:
    name_list = list_of_names.readlines()

for name in name_list:
    with open("input/letters/starting_letter.txt") as letters:
        txt = letters.read()
        name = name.strip()
        x = txt.replace("name", name)

    with open(f"output/ReadyToSend/letter_to_{name}", mode="w") as final:
        final.write(x)








