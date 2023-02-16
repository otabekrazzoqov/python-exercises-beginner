import random
from englishwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)    
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Men {len(word)} ta harfli so'z o'yladim. Topa olasizmi?")
    # print(word)
    while word_letters:
        print(display(user_letters,word))
        if user_letters:
            print(f"Kiritgan harflaringiz: {user_letters}")
        
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print("Bu harf avval kiritilgan.Boshqa harf kiriting:")
            continue        
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} Harfi to'g'ri.")
        else:
            print("Bunday harf yo\'q.")
        user_letters += letter
    print(f" {word} so'zini {len(user_letters)} ta urinishda topdingiz.")
    
