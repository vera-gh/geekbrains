user_words = input("Введите несколько слов через пробел>>>")
word_list = user_words.split(" ")
print(word_list)
for num, words in enumerate(word_list):
    print(f"{num + 1}) {words}")

