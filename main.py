import numpy as np
from scipy.stats import poisson
import math

def normal(size):
    result = np.random.normal(size=size)
    result = sorted(result)
    return result

def standart_Cauchy(size):
    result = np.random.standard_cauchy(size=size)
    sorted(result)
    return result

def laplace(size):
    result = np.random.laplace(size=size)
    sorted(result)
    return result

def puasson(size):
    result = poisson.rvs(size=size, mu=10)
    sorted(result)
    return result

def uniform(size):
    x = range(size)
    result = [np.random.uniform(-(3 ** 0.5), (3 ** 0.5)) for j in x]
    sorted(result)
    return result

def average(x, size):
    num = 0.
    for i in x:
        num += i
    num /= size
    return num

def mediana(x, size):
    if size % 2 == 1:
        num = (size - 1) / 2 + 1
        result = x.index(num)
    else:
        num = math.ceil(size / 2)
        result = (x[num] + x[num + 1]) / 2.
    return result

def sum_Extremum(x, size):
    return (x[0] + x[size - 1]) / 2

def quartile(x, size):
    p = .25
    num1 = math.floor(size * p + 1)
    num2 = math.floor(size * (1 - p) + 1)
    return (x[num1] + x[num2]) / 2

def trace(x, size):
    r = math.floor(size / 4)
    result = 0.
    for i in range(r, size - r):
        result += x[i]
    result /= (size - 2 * r)
    return result

def despertion(x, size):
    y = average(x, size)
    result = 0.
    for i in x:
        result += (i - y) * (i - y)
    result /= size
    return result

size_arr = {10, 100, 1000}
selection = {normal, standart_Cauchy, laplace, puasson, uniform}
function = {average, mediana, sum_Extremum, quartile, trace}

for sel in selection:
    print(str(sel))
    for func in function:
        print(str(func))
        for i in size_arr:
            nums = np.zeros(1000)
            for j in range(0, 1000):
                x = sel(i)
                nums[j] = func(x, i)
            print("nums = " + str(i) + " average = " + str(average(nums, 1000)) + " despertion = " + str(despertion(nums, 1000)))