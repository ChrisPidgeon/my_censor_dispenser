#author Chris Pidgeon
#This is my attempt at the Censor Dispenser challenge project on the Computer Science path of Codecademy.

#This challenge is focused around creating functions to interact with a few large strings (emails).
#These emails must be censored according to multiple formats, lists of phrases to be censored, etc.
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#This exercise required me to define a function that can censor a specific word or 
#phrase from a body of text, and then return the text.
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

#This exercise required me to write a function that can censor not just a specific word or 
#phrase from a body of text, but a whole list of words and phrases, and then return the text.
def censor_phrase_list(text, censor_list):
    text_clean = text
    for word in censor_list:
        text_clean = censor_phrase(text_clean, word)
    return text_clean

#This exercise required me to write a function that can censor any occurance of a word from the 
#“negative words” list after any “negative” word has occurred twice, as well as censoring everything 
#from the list from the previous step as well and use it to censor email_three. 
#Originally I planned to have each function linked together to create an integrated series
#of function calls; however, with this function, it became too complicated to manage, 
#so I shifted to completing this and the following exercise internally. 
def censor_phrase_list_and_negative_words(text, censor_list, negative_words_list):
    pass

def exercise_four():
    pass

        
print("FIRST EXERCISE: \n", censor_phrase(email_one, "learning algorithms"))
print("SECOND EXERCISE: \n", censor_phrase_list(email_two, proprietary_terms))
