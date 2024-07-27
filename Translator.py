#This translator will translate every vowels into r
#Like Dog -> Drg , Cat -> Crt
#Vowel are -> a e i o u
#Consonants will remain intact

def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation+="R"
            else:
                translation+="r"
        else:
            translation+=letter
    return translation
print(translate(input("Enter a phrase: ")))
