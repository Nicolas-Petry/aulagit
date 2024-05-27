def count_vowels_and_consonants(sentence):
    vowels="AaEeIiOoUu"
    num_vowels=0
    num_consonants=0
    for char in sentence:
        if char.isalpha(): 
            if char in vowels:
                num_vowels+=1
            else:
                num_consonants+=1
    
    return num_vowels, num_consonants

def main():
    user_sentence = input("Digite uma sentença: ")
    vowels, consonants = count_vowels_and_consonants(user_sentence)
    print(f"A sentença tem {vowels} consoantes e {consonants} vogais.")

if __name__ == "__main__":
    main()