def Check_VowelOrConsonant(character):
    if character in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")        
try:
    input_ = input().strip()
    if input_.isalpha() and len(input_) == 1:
        Check_VowelOrConsonant(input_)
    else:
        raise
except:
    print("Invalid")
