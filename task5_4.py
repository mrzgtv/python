from googletrans import Translator

with open('text_4.txt', 'r') as my_list:
    eng_to_rus = []
    translator = Translator()
    new_list = my_list.read().split('\n')
    for el in new_list:
        el = el.split(" - ")
        eng_to_rus.append(el[0])
    for el in eng_to_rus:
        result = translator.translate(eng_to_rus, src='en', dest='ru')
    for el in result:
        print(f'{el.origin} -> {el.text}')

with open('text_4_rus.txt', 'w') as final_list:
    for el in result:
        el.text = str(el.text)
        final_list.write(el.text + '\n')

# Примечание: просьба дать комментарии, не слишком ли много кода? возможно ли более кратко написать код для такого перевода с помощью Google Translate API? #


