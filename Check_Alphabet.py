def Check_Alphabet(character):
    print("Alphabet")
try:
    input_ = input().strip()
    if input_.isalpha() and len(input_) == 1:
        Check_Alphabet(input_)
    else:
        raise
except:
    print("No")
