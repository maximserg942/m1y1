meme_dict = {"КРИНЖ": "Что-то очень странное или стыдное", "ЛОЛ": "Что-то очень смешное", "РОФЛ": "шутка"}
word = input("Введите не понятно слово(Большими буквами): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Слово не нашлось, Увы! Попробуйте вписать своё слово сново без ошибок(Или его не существует)")