#author Chris Pidgeon
#This is my attempt at the Censor Dispenser challenge project on the Computer Science path of Codecademy.

#This challenge is focused around creating functions to interact with a few large strings (emails).
#These emails must be censored according to multiple formats, lists of phrases to be censored, etc.
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

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
def censor_phrase_list(text):
    text_clean = text
    for word in proprietary_terms:
        text_clean = censor_phrase(text_clean, word)
    return text_clean

#This exercise required me to write a function that can censor any occurance of a word from the 
#“negative words” list after any “negative” word has occurred twice, as well as censoring everything 
#from the list from the previous step as well and use it to censor email_three. 
def censor_phrase_list_and_negative_words(text):
    words_to_censor = []
    text_clean = text
    for word in negative_words:
        if text_clean.find(word) >= 0:
            words_to_censor.append(word)
    if len(words_to_censor) >= 2:
        for word in words_to_censor:
            text_clean = censor_phrase(text_clean, word)
    text_clean = censor_phrase_list(text_clean)
    return text_clean

def censor_all_plus_before_after(text):
    list_of_censors = proprietary_terms + negative_words
    words_in_text = []
    for item in text.split(" "):
        split_item = item.split("\n")
        for word in split_item:
            words_in_text.append(word)
    for i in range(0,len(words_in_text)):
        checked_word = words_in_text[i].lower()
        for x in punctuation:
            checked_word = checked_word.strip(x)
        if checked_word in list_of_censors:
            # Censoring the targeted word
            word_clean = words_in_text[i]
            censored_word = ""
            for x in punctuation:
                word_clean = word_clean.strip(x)
            for x in range(0,len(word_clean)):
                censored_word = censored_word + "X"
            words_in_text[i] = words_in_text[i].replace(word_clean, censored_word)

            # Censoring the word before the targeted word
            word_before = words_in_text[i-1]
            for x in punctuation:
                word_before = word_before.strip(x)
            censored_word_before = ""
            for x in range(0,len(word_before)):
                censored_word_before = censored_word_before + "X"
            words_in_text[i-1] = words_in_text[i-1].replace(word_before, censored_word_before)

            # Censoring the word after the targeted word
            word_after = words_in_text[i+1]
            for x in punctuation:
                word_after = word_after.strip(x)
            censored_word_after = ""
            for x in range(0,len(word_after)):
                censored_word_after = censored_word_after + "X"
            words_in_text[i+1] = words_in_text[i+1].replace(word_after, censored_word_after)
    return " ".join(words_in_text)   

print("FIRST EXERCISE:\n", censor_phrase(email_one, "learning algorithms"))
print("SECOND EXERCISE:\n", censor_phrase_list(email_two))
print("THIRD EXERCISE:\n", censor_phrase_list_and_negative_words(email_three))
print("FOURTH EXERCISE:\n", censor_all_plus_before_after(email_four))
