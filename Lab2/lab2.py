import numpy as np
import matplotlib.pyplot as plt

# Функция создания графиков для всех зависимостей
def createPlot(y,x,noise, axnums):  
  ax = []
  for i in range(len(y)):
    ax.append(plt.subplot(axnums[i]))
    ax[i].plot(x,y[i])
    ax[i].plot(x,y[i]+noise)
    ax[i].set_title(f"График {i+1}")
    ax[i].grid()
    ax[i].set(ylabel="y",xlabel="x")
  plt.show()

# Функция получения параметров каждой зависимости
def getSpecs(function, isNP: bool):
  specs = []
  for el in function:
    if isNP:
      specs.append(
      [
        maxStd(el),
        minStd(el),
        avgStd(el),
        medStd(el),
        stdStd(el)
      ])
    else:
      specs.append(
      [
        np.amax(el),
        np.amin(el),
        np.average(el),
        np.median(el),
        np.std(el)
      ])
  return specs 
# Функция поиска максимума для зависимости y
# здесь и в аналогичных функциях y не массив данных, а его элемент!
def maxStd(y):
  max = y[0]
  for element in y:
    if element > max:
      max = element
  return max

# Функция поиска минимума для зависимости y
def minStd(y):
    min = y[0]
    for element in y:
        if element < min:
            min = element
    return min

# Функция поиска среднего значения для зависимости y
def avgStd(y: list):
    sum = 0
    for element in y:
        sum += element
    return sum / len(y)

# Функция поиска медианного значения для зависимости y
def medStd(y):
    y_sorted = np.sort(y)
    if len(y)/2: 
        med = (y_sorted[len(y)//2 - 1] + y_sorted[len(y)//2])/2
    else:
        med = y_sorted[len(y)//2 - 1]
    return med

# Функция поиска среднеквадратичного значения для зависимости y
def stdStd(y):
    sum = 0
    for element in y:
        sum +=element
    avg = sum / len(y)
    sum = 0
    for el in y:
        sum += (el - avg)**2
    return np.sqrt(sum / (len(y)))

# Функция сравнения значений, полученных двумя способами
def compSpecs(specs,specsStd):
  rows = []
  for i in range (len(specs)):
    cols = []
    for j in range (len(specs[0])):
      cols.append(specs[i][j] - specsStd[i][j])
    rows.append(cols)
  return rows

def printSpecs(specs,string):
  print(string)
  for i in range (len(specs)):
    print(f'{i+1} график: max - {specs[i][0]}, min - {specs[i][1]}, avg - {specs[i][2]}, med - {specs[i][3]}, std - {specs[i][4]};')

# Номер варианта по списку
N = 1

# Диапазон значений для переменной x, num - количество значений
num = 100
x = np.linspace(0.0, 20.0, num)

# Зависимости y(x), заданные как элементы одного массива
y = [
  0.3*N*x + 10*N,
  np.cos(0.5*N*x) + N*np.sin(x+N),
  N*np.cos(2*np.pi*x)*np.exp(-0.1*N*x)
]

# Значение шума, получаемое случайно для каждого из значений x
noise = 0.2*np.random.randn(num)

# Запись в переменные результатов работы функций получения параметров зависимостей
specs_np = getSpecs(y, True)
specs = getSpecs(y, False)
dif = compSpecs(specs_np, specs)

# Вывод значений в консоль
printSpecs(specs_np, 'Значения для функций numpy')
printSpecs(specs, 'Значения для стандартных функций')
printSpecs(dif, 'Разница полученных значений')

# Выполнение функции построения графика
createPlot(y,x,noise, [221,222,212])