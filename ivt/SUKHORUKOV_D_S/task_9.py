# Задача 9.
#  Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать,
# есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет".
# Вслед за тем игрок должен попробовать отгадать слово.

# Сухоруков Д. С.

# 04.04.17

import random, string

WORDS = ('адвокат','библтотека','волшебник',
         'грамота','деканат','ежевика',
         'журналист','заложник','игрок',
         'компьютер','лифт','математика',
         'носитель','оптимист','пессимист',
         'работодатель','садист','текстура',
         'урожай','фасад','халва','инизм',
         'чудовище','шедевр','щебень',
         'эгоист','ювелир','ящер')

word            = random.choice(WORDS)
length          = len(word)
max_helps       = 5
curr_helps      = 0

# начало игры
print(
"""
                 Добро пожаловать в игру 'Отгадай'!
     Надо переставить буквы так. чтобы получилось осмысленное слово.
         (Для выхода нажмите Enter. не вводя своей версии.)
"""
)

print("В слове всего", length, "букв.")
print("У Вас есть", max_helps, "попыток узнать какая бука есть в слове.")
while curr_helps < max_helps :
	q_char = input("Введите любую букву: ")
	if q_char == '': break
	curr_helps += 1
	if q_char in word:
		print('Да, есть!')
	else: print('Нет такой буквы в этом слове...')

#  Сама логика игры тут
guess = input("Попробуйте отгадать исходное слово:  ")

while guess != word and guess != "" :
	print("K сожалению вы неправы. ")
	guess = input("\nПопробуйте ещё раз отгадать исходное слово:  ") 

# в случае верного ответа:
if guess == word: 
	print("Дa. именно так! Вы отгадали!\n")
print("Cnacибo за игру.")
input("\nHaжмитe Enter. чтобы выйти.") 
