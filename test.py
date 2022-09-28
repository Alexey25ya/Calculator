import parsing
import parsecomplex

# expr = '2'                                # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '2,5'                                # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '2+3'                                # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '2.5-3'                              # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '7/2'                                # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '2.5*8'                              # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '(2+3)*4'                            # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '(1.5-3)*4+3.6*(8-9.2)'              # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '((2+3.2)*5-16)/2'                   # Задаём выражение, можно через input()
# print(expr,'=',parsing.calculate(expr))      # Обрабатываем список и выводим результат

# expr = '((2+3.2)*5-16)/2'                   # Задаём выражение, можно через input()
# print(parsing.checkstring(expr))            # Корректируем, ищем ошибки

# expr = '(2+3.2)*5-16)/2'                   # Задаём выражение, можно через input()
# print(parsing.checkstring(expr))            # Корректируем, ищем ошибки

# expr = '((2+3,2)*5-16)/2'                   # Задаём выражение, можно через input()
# print(parsing.checkstring(expr))            # Корректируем, ищем ошибки

# expr = '((2 + 3,2)*5-16) / 2'               # Задаём выражение, можно через input()
# print(parsing.checkstring(expr))            # Корректируем, ищем ошибки

# expr = '((2 + 3,2)*5-16g) / 2'               # Задаём выражение, можно через input()
# print(parsing.checkstring(expr))            # Корректируем, ищем ошибки

# expr = '((2 + 3,2)*5-16) / 2' 
# expr = '((2 + 3,2)*5-16g) / 2'
# if parsing.checkstring(expr) != -1 :
#     print(expr,'=',parsing.calculate(parsing.checkstring(expr)))      # Обрабатываем список и выводим результат

# expr = '[5 + i] + [-1 - 1.2i]'
# print(parsecomplex.calculate(expr))

# expr = '[5 + i] - [-1 - 1.2i]'
# print(parsecomplex.calculate(expr))

# expr = '[5 + i] * [-1 - 1.2i]'
# print(parsecomplex.calculate(expr))

# expr = '[5 + i] / [-1 - 1.2i]'
# print(parsecomplex.calculate(expr))