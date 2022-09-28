import parsing

expr = '2+3'                                # Задаём выражение, можно через input()
lst = parsing.parse_num(expr)               # Парсим выражение в список
print(expr,'=',parsing.calculate(lst))      # Обрабатываем список и выводим результат

expr = '2.5-3'                              # Задаём выражение, можно через input()
lst = parsing.parse_num(expr)               # Парсим выражение в список
print(expr,'=',parsing.calculate(lst))      # Обрабатываем список и выводим результат

expr = '7/2'                                # Задаём выражение, можно через input()
lst = parsing.parse_num(expr)               # Парсим выражение в список
print(expr,'=',parsing.calculate(lst))      # Обрабатываем список и выводим результат

expr = '2.5*8'                              # Задаём выражение, можно через input()
lst = parsing.parse_num(expr)               # Парсим выражение в список
print(expr,'=',parsing.calculate(lst))      # Обрабатываем список и выводим результат

expr = '(2+3)*4'                            # Задаём выражение, можно через input()
lst = parsing.parse_num(expr)               # Парсим выражение в список
print(expr,'=',parsing.calculate(lst))      # Обрабатываем список и выводим результат

expr = '(1.5-3)*4+3.6*(8-9.2)'              # Задаём выражение, можно через input()
lst = parsing.parse_num(expr)               # Парсим выражение в список
print(expr,'=',parsing.calculate(lst))      # Обрабатываем список и выводим результат

expr = '((2+3.2)*5-16)/2'                   # Задаём выражение, можно через input()
lst = parsing.parse_num(expr)               # Парсим выражение в список
print(expr,'=',parsing.calculate(lst))      # Обрабатываем список и выводим результат