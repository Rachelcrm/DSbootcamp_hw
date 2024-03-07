#1
def count_vowels(word):
    vowel_num = 0
    for letter in word:
        if letter in "aeoui":
            vowel_num += 1
    return vowel_num

#2
def print_capital():
    animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
    for word in animals:
        print(word.upper())

#3
def print_and_odd_even():
    for i in range(1,20):
        print(i, end = ' ')
        if (i % 2 == 1):
            print("odd")
        else:
            print("even")

#4
def sum_of_integers(a, b):
    return a+b