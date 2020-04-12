#author Chris Pidgeon
#This is my attempt at the Censor Dispenser challenge project on the Computer Science path of Codecademy.

#This challenge is focused around creating functions to interact with a few large strings (emails).
#These emails must be censored according to multiple formats, lists of phrases to be censored, etc.
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


#This exercise requires me to define a function 
#that can censor a specific word or phrase from a body of text, and then return the text.
def exercise_one(text, to_censor):
    censor = ""
    for x in range(0, len(to_censor)):
        if to_censor[x] == " ":
            censor += " "
        else:
            censor += "!"
    return text.replace(to_censor, censor)

print(exercise_one(email_one, "learning algorithms"))

def exercise_two():
    pass

def exercise_three():
    pass

def exercise_four():
    pass