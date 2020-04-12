#author Chris Pidgeon
#This is my attempt at the Censor Dispenser challenge project on the Computer Science path of Codecademy.

#This challenge is focused around creating functions to interact with a few large strings (emails).
#These emails must be censored according to multiple formats, lists of phrases to be censored, etc.
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#This exercise requires me to define a function that can censor a specific word or 
# phrase from a body of text, and then return the text.
def censor_phrase(text, to_censor):
    to_censor_all_cases = []
    to_censor_all_cases.append(to_censor)
    to_censor_all_cases.append(to_censor.upper())
    to_censor_all_cases.append(to_censor.lower())
    to_censor_all_cases.append(to_censor.title())

    text_clean = text
    for item in to_censor_all_cases:
        censor = ""
        for x in range(0, len(item)):
            if to_censor[x] == " ":
                censor += " "
            else:
                censor += "!"
        text_clean = text_clean.replace(item, censor)
    return text_clean

#This exercises requires me to write a function that can censor not just a specific word or 
#phrase from a body of text, but a whole list of words and phrases, and then return the text.
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
def censor_phrase_list(text, censor_list):
    text_clean = text
    for word in censor_list:
        text_clean = censor_phrase(text_clean, word)
    return text_clean

def exercise_three():
    pass

def exercise_four():
    pass

        
print("FIRST EXERCISE: \n", censor_phrase(email_one, "learning algorithms"))
print("SECOND EXERCISE: \n", censor_phrase_list(email_two, proprietary_terms))
