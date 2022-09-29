# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в нее систему логирования.

## Команда:

1. Виталий Гирик
2. Анастасия Банк
3. Алексей Ершов
4. Елена Данилова

## Модули:
- check.py - Алексей
- controller.py - Алексей, Анастасия
- log.py - Елена, Алексей
- operations.py - Виталий, Лена, Алексей
- scheme.drawio.png - Елена
- user_iterface.py - Анастасия, Алексей
- readme.md - Елена, Анастасия

## Модуль [***check.py***](https://github.com/dtnfktu/Calculator/blob/main/check.py)
Реализованы проверки чисел, принятых с UI

## Модуль [***controller.py***](https://github.com/dtnfktu/Calculator/blob/main/controller.py)
Модуль берет данные с UI, производит расчет, передает рузультат обратно и записывает его в журнал.

## Модуль [***log.py***](https://github.com/dtnfktu/Calculator/blob/main/log.py)
Записывает дату, время и результат проведения операций в файл.

## Модуль [***operations.py***](https://github.com/dtnfktu/Calculator/blob/main/operations.py)
Модуль возможных операций нашего калькулятора.

## Модуль [***parsing.py***](https://github.com/dtnfktu/Calculator/blob/main/parsing.py)
Функция calculate модуля принимает заданное арифметическое выражение в виде строки, возвращает результат - полученное число. Работа с **рациональными** числами.

## Модуль [***parsecomplex.py***](https://github.com/dtnfktu/Calculator/blob/main/parsecomplex.py)
Функция calculate модуля принимает заданное арифметическое выражение в виде строки, возвращает результат - комплексное число (строковый тип данных). Работа с **комплексными** числами.

=======
# Calculator (дополнительно)
## Папка Additional (Виталий)
Модули с более усложненным алгоритмом, не включены в общую программу из-за нехватки времени. Просим дать отдельно обратную связь.

## Модуль [***parsing.py***](https://github.com/dtnfktu/Calculator/blob/main/parsing.py). **Для работы с рациональными числами.**

В данном модуле реализованы несколько функций:
*checkstring(st : str)* принимает строку - арифметическое выражение, заданное пользователем. Например *2+3*.
- Заменяет запятые на точки: checkstring('2,5') = '2.5'
- Заменяет левый слеш на правый: checkstring('2\5') = '2/5'
- Убирает пробелы: checkstring('2,5 + 3') = '2.5+3'
- Проверяет количество открывающих и закрывающих скобок:
    checkstring('(2,5 + 3)') = '(2.5+3)'
    checkstring('(2,5 + 3') = 'Введено некорректное выражение - количество открывающих и закрывающих скобок не совпадает'
- Проверяет на наличие недопустипых символов в выражении:
    checkstring('((2 + 3,2)*5-16g) / 2') = 'Введено некорректное выражение - в выражении присутствует недопустимый символ'

*calculate(expr : str)* принимает строку - арифметическое выражение, вызвает функцию *checkstring(st : str)*, и, если ошибок нет, то возвращает число - результат вычислений. Вызвает функцию *parse_num(oper : str)*, которая переводит исходную строку в список. Использует как вспомогательную функцию *def mixed_operation(oper : list)*.

*parse_num(oper : str)* - принимает исходную строку, возвращает список. Список состоит из символов ('+','-','*','/','(',')','.') и вещественных чисел. Например, parse_num('(2+3)') = ['(', 2.0, '+', 3.0, ')']

*mixed_operation(oper : list)* принимает список, в котром нет скобок. Точнее - в принимаемом списке присутствуют только числа и знаки арифметических операций между ними (арифметическое выражение, взятое между парой открывающей и закрывающей скобок). Возвращает число - результат арифметических операций. Использует функцию *primitive_oper(oper : list)*.

*primitive_oper(oper : list)* принимает список, состоящий из трех элементов: первый и третий - числа, второй элемент - знак арифметического действия между числами. Возвращает результат операции.

  Из модуля *parsing.py* в других модулях используются только функции ***calculate(expr : str)*** и ***checkstring(st : str)***

 ## Модуль [***parsecomplex.py***](https://github.com/dtnfktu/Calculator/blob/main/parsecomplex.py). **Для работы с комплексными числами.**
  Аналогичен модулю *parsing.py*, но расчитан на работу с комплексными числами. Здесь каждое комплексное число заключаем в прямоугольные скобки *[]* и у мнимой части числа справа ставим *i*.
  Т.е., например, мы хотим сложить два комплексных числа. Корректно ввести их следует следующим образом:
  **[1.5 + 2i] + [0,25 - i]**
  Или более сложное выражение:
  **([1-0.5i]+[2i])/[5]**
  Каждое число в калькуляторе комплексных чисел должно быть представлено в прямоугольных скобках. Даже если мнимая часть отсутствует, как в данном примере.
  Калькулятор комплексных чисел можно использовать для работы с рациональными числами, т.к. множество рациональных чисел является подмножеством комплексных. Но тогда, всё равно, каждое число надо будет заключать в прямоугольные скобки.
  В данном модуле используется функция ***calculate(expr : str)***, которая принимает строку - арифметическое выражение с комплексными числами. Результатом работы функции является строка вида *A+Bi*. Если в результате вычислений одна из составляющих комплексного числа равна нулю, то она не показывается.