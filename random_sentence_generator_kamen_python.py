import random


def choose_random_word(word):
    return random.choice(word)

names = ["Peter", "Michell", "Jane", "Steve", "Kamen", "Sonya", "Jack"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Smolyan", "Pazardzhik", "New York"]
actions = ["eats", "holds", "sees", "plays with", "brings", "gives", "throws", "kicks", "cuts"]
objects = ["stones", "cake", "apple", "laptop", "bikes", "books", "eggs", "dog", "tree"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park", "at work", "at the school", "on the street"]

while True:
    input("I will generate a sentence...press Enter to do it..")
    random_name = choose_random_word(names)
    random_place = choose_random_word(places)
    random_action = choose_random_word(actions)
    random_object = choose_random_word(objects)
    random_adverb = choose_random_word(adverbs)
    random_detail = choose_random_word(details)
    print(f"{random_name} from {random_place} {random_action} {random_object} {random_adverb} {random_detail}")
    another_sentence = input("Do you want another sentence? yes or no...." )
    while another_sentence not in ['yes', 'no']:
        print("Invalid Input. Try again...")
        another_sentence = input("Type [yes] if you would like to play again and [no] to exit: ")
    if another_sentence == "no":
        print("Thank you for playing!")
        break

    another_sentence = ""
