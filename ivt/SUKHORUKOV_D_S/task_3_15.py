# Задача 3. Вариант 15.
# Напишите программу, которая выводит имя "Лариса Петровна Косач-Квитка", и
# запрашивает его псевдоним. Программа должна сцеплять две эти строки и
# выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Сухоруков Д. С.

# 14.03.17
name = "Лариса Петровна Косач-Квитка"
print("Герой нашей сегодняшней программы - ", name)
answer = input("Под каким же именем мы знаем этого человека? \n\tВаш ответ: ")
if answer == "Леся Украинка":
	print("Все верно:", name,"-",answer)
else:
	print("Неправильно!")
input("\nНажмите Enter для выхода")
