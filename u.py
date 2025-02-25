import random

import time
import math

def loops(file_path):
    while 1==1:
        print(str(measure_loops_in_one_second_saving(file_path)))
        input()

def save(file_path,text):
    with open(file_path, "a") as file:
        file.write(f'{text:.2f}\n')
        


def solve_equation(equation_type, coefficients, constants=None):
    def solve_linear_equation(coefficients, constants):
        from sympy import symbols, linsolve
        x = symbols('x:{}'.format(len(coefficients[0])))
        eqs = [sum(coefficients[i][j] * x[j] for j in range(len(x))) - constants[i] for i in range(len(coefficients))]
        solutions = linsolve(eqs, *x)
        return solutions

    def solve_polynomial_equation(coefficients):
        from sympy import symbols, solve
        x = symbols('x')
        equation = sum(c * x**i for i, c in enumerate(coefficients[::-1]))
        solutions = solve(equation, x)
        return solutions

    if equation_type == 'linear':
        return solve_linear_equation(coefficients, constants)
    elif equation_type == 'polynomial':
        return solve_polynomial_equation(coefficients)
    else:
        return "Invalid equation type. Please choose 'linear' or 'polynomial'."

def read_specific_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1].strip()
            else:
                return "Invalid line number."
    except FileNotFoundError:
        return "File not found."
    
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "File not found."

def average(file_path):
    x=0
    summ=0
    while x < count_lines_in_file(file_path):
        x+=1
        summ += float(read_specific_line(file_path,x))
    avr = summ/count_lines_in_file(file_path)
    return avr

def measure_loops_in_one_second_saving(file_path):
    start_time = time.time()
    count = 0
    while time.time() - start_time < 1:
        count += 1
    save(file_path,count)
    return count

def averagenew(file_path):
    x=0
    sum=0
    while x < count_lines_in_file(file_path):
        x+=1
        try:
         sum+=float(read_specific_line(file_path,x))
        except:
         sum=sum       
    return str(float(sum)/count_lines_in_file(file_path))