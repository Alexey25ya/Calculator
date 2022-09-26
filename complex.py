def sum_num(a : tuple, b : tuple) :
    '''Принимает два кортежа - два комплексных числа, складывает и возвращает результат - кортеж'''
    return (a[0] + b[0], a[1] + b[1])

def sub_num(a : tuple, b : tuple) :
    '''Принимает два кортежа - два комплексных числа, возвращает кортеж - первое минус второе'''
    return (a[0] - b[0], a[1] - b[1])

def mul_num(a : tuple, b : tuple) :
    '''Принимает два кортежа - два комплексных числа, возвращает их произведение'''
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + b[0]*a[1])

def div_num(a : tuple, b: tuple) :
    '''Принимает два комплексных числа, возвращает результат деления первого на второе'''
    return ((a[0]*b[0] + a[1]*b[1]) / (b[0]*b[0] + b[1]*b[1]), (b[0]*a[1] - a[0]*b[1]) / (b[0]*b[0] + b[1]*b[1]))



num_a = (4.5, 2.3)
num_b = (-0.23, 5)
print('a + b =',sum_num(num_a, num_b))
print('a - b =', sub_num(num_a, num_b))
print('a * b =', mul_num(num_a, num_b))
print('a * b =', mul_num((5,0), (3,0)))
print('a * b =', mul_num((3,0), (0,5)))
print('a / b =', div_num(num_a, num_b))
print('a / b =', div_num((0,14), (2,0)))