# telephone-assistant

Телефонный асистент

На ввод поступают несколько чисел, асистент ищет возможные продолжения этого номера.
Использовались регулярные выражения. Возможные альтернативы: select * like или какой-то алгоритм перебора.

Например
In: 380 
Out: [380675674432, 380672832500, 380983567721]

In: 38067 
Out: [380675674432, 380672832500]

In: 380983 
Out: [380983567721]

Запуск на локальной машине:

>cd [директория с проектом]

>virtualenv env

>env\Scripts\activate

>pip install -r requirements.txt

>python telephone_assistant.py

тесты:
>pytest test_telephone_assistant.py
