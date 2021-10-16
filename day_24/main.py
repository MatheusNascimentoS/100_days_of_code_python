#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"day_24\Input\Letters\starting_letter.txt") as starting_letter:
                text = starting_letter.read()

with open(r"day_24\Input\Names\invited_names.txt") as names:
    for name in names.readlines():
        with open(rf"day_24\Output\ReadyToSend\{str(name.strip())}.txt", mode="w") as invite_name:
            invite_name.write(text.replace("[name]", name.strip()))
