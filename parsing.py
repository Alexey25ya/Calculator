def parse_num(oper : str) :
    '''Переводит заданное выражение в из строки список'''
    ans = []
    num = ''
    for sym in oper :
        if sym in {'+','-','*','/','(',')'} :
            if num != '' :
                ans.append(float(num))
                num = ''
            ans.append(sym)
        else :
            num = num + sym
    # Если в выражении последний элемент - число
    if num != '' :
        ans.append(float(num))
    # Если первым стоит отрицательное число
    if ans[0] == '-' and type(ans[1]) == float :
        ans[1] = -ans[1]
        ans.pop(0)

    return ans

def primitive_oper(oper : list) :
    '''Выполняет операцию между двумя числами'''
    if oper[1] == '+' :
        return oper[0] + oper[2]
    if oper[1] == '-' :
        return oper[0] - oper[2]
    if oper[1] == '*' :
        return oper[0] * oper[2]
    if oper[1] == '/' :
        return oper[0] / oper[2]

def mixed_operation(oper : list) :
    '''Обрабатывает смешанную операцию'''
    res = oper.copy()

    while ('*' in res) or ('/' in res) :
        # определяем что раньше - умножение или деление
        index1 = len(res) if not '*' in res else res.index('*')
        index2 = len(res) if not '/' in res else res.index('/')
        index_begin = min(index1, index2)
        tmp_num = primitive_oper(res[index_begin - 1:index_begin + 2])
        res = res[:index_begin - 1] + [tmp_num] + res[index_begin + 2 :]

    while ('+' in res) or ('-' in res) :
        # определяем что раньше - умножение или деление
        index1 = len(res) if not '+' in res else res.index('+')
        index2 = len(res) if not '-' in res else res.index('-')
        index_begin = min(index1, index2)
        tmp_num = primitive_oper(res[index_begin - 1:index_begin + 2])
        res = res[:index_begin - 1] + [tmp_num] + res[index_begin + 2 :]    

    return res[0]

# Еще не готово...
def calculate(number : list) :
    '''Вычисляем значение выражения'''
    
    # Заменяем выражения в скобках на их значения
    while '(' in number :
        # Берём начало и конец выражения в скобках
        index_begin = len(number) - 1 - number[::-1].index('(')     # открывающая скобка
        index_end = index_begin + number[index_begin:].index(')')   # закрывающая скобка
        # Заменяем его на число - результат операции(й)
        tmp_num = mixed_operation(number[index_begin + 1:index_end])
        # Заменяем скобки числом в исходном выражении
        number = number[:index_begin] + [tmp_num] + number[index_end + 1:]
   
    return mixed_operation(number)
