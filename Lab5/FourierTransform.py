from numpy import asarray, ndarray, pi, exp, abs, size, zeros
from numpy.fft import fft, ifft, fftshift, fft2, ifft2
from Data import freqFiltration
from matplotlib import pyplot as plt

def listCycle(arr, isInv):
  N = len(arr)
  invMult, invFact = checkInv(N, isInv)
  
  transformedArr = []
  for k in range(N):
    sum_ = sum(arr[m]*(exp(-2*pi*1j*k*m*invFact/N)) for m in range(N))
    transformedArr.append(sum_ / invMult)
  return transformedArr

def imageCycle(image, isInv):
  M, N = image.shape
  invMult, invFact = checkInv(N*M, isInv)
  print(invMult, invFact)
  array = zeros((M,N),complex)
  transformedImage = zeros((M,N),complex)
  for m in range(M):
    for n in range(N):
      sum=0
      for l in range(N):
        sum+=image[m,l]*exp(-2*pi*1j*l*n*invFact/N)
      array[m,n]=sum
    for l in range(N):
      for m in range(M):
        sum=0
        for k in range(M):
          sum+=array[k,l]*exp(-2*pi*1j*m*k*invFact/M)
        transformedImage[m,l]=sum / invMult

  # for k in range(M):
  #   transformedImageCol = []
  #   for l in range(N):
  #     sumM = 0
  #     for m in range(M):
  #       sumN = 0
  #       for n in range(N):
  #         sumN += image[m][n] * exp(-2*pi*1j*k*m*invFact/M)
  #       sumM += sumN * exp(-2*pi*1j*l*n*invFact/N)
  #     transformedImageCol.append(sumM / invMult)
  #   transformedImage.append(transformedImageCol)
  return transformedImage

def checkInv(N: int, isInv: bool):
  if isInv:
    invMult = N
    invFact = -1
  else:
    invMult = 1
    invFact = 1
  return invMult, invFact

def fourierTransform(source, isInv: bool):
  N = len(source) # длина массива
  transformedArr = [] # задание пустого массива для преобразованных значений

  # Определение коэффициентов, необходимых для обратного преобразования
  print(type(source[0]))
  if (type(source[0]) == ndarray):
    transformedArr = imageCycle(source, isInv)
  else:
    transformedArr = listCycle(source, isInv)
  return transformedArr

def getFreqFiltered(source, isNP: bool, freq = 0):
  filtered_source = []
  filtered_fts = []
  if (type(source[0]) != list):
    for filterIndex in range(3):
      if isNP:
        ft = fftshift(fft2(source))
        ft_filtered = freqFiltration(ft, filterIndex)
        filtered_f = ifft2(ft_filtered)
      else:
        ft = fftshift(fourierTransform(source, False))
        ft_filtered = freqFiltration(ft, filterIndex)
        filtered_f = fourierTransform(source, True)
      filtered_source.append(filtered_f)
      filtered_fts.append(ft_filtered)
  else:
    for function in source:
      for filterIndex in range(3):
        if isNP: # Условие, при выполнении которого преобразования проводятся с использованием numpy
          ft = fourierTransform(function, False) # Прямое преобразование
          ft_filtered = freqFiltration(ft, filterIndex, freq) # Фильтрация
          filtered_function = fourierTransform(ft_filtered, True) # Обратное преобразование
        else:
          ft = fft(function) # Прямое преобразование
          ft_filtered = freqFiltration(ft, filterIndex, freq) # Фильтрация
          filtered_function = ifft(ft_filtered) # Обратное преобразование

        filtered_source.append(filtered_function)
        filtered_fts.append(ft_filtered)
  return filtered_source, filtered_fts

# ---------------------------------------------------------------------------------------------
def showPlotsSpectr1(ft, npft, v):
  fig, axs = plt.subplots(2, 3)
  index = 0
  for i in range(2):
    filterType = ["Низкочастотный","Высокочастотный", "Полосный"]
    for filterIndex in range(3):
      axs[i,filterIndex].plot(v, abs(ft[index]), label="not np", color="black", lw=2)
      axs[i,filterIndex].plot(v, abs(npft[index]), label="np", color="red", lw=1)
      axs[i,filterIndex].set_title(f'{filterType[filterIndex]} фильтр, {i + 1} функция')
      axs[i,filterIndex].legend()
      axs[i,filterIndex].grid()
      axs[i,filterIndex].set(xlabel='v', ylabel='y')
      index += 1
  plt.show()


def showPlotsDFT1(filteredArrays:list, source: list, npFiltered: list, t: list):
  fig, axs = plt.subplots(2, 3)
  index = 0
  for i in range(len(source)):
    for filterIndex in range(3):
      if filterIndex == 0:
          filterType = "Низкочастотный"
      if filterIndex == 1:
          filterType = "Высокочастотный"
      if filterIndex == 2:
          filterType = "Полосный"
      axs[i,filterIndex].plot(t,source[i], label="not filtered", color="black", lw=0.5)
      axs[i,filterIndex].plot(t,filteredArrays[index], label="filtered", color="red", lw=2)
      axs[i,filterIndex].plot(t,npFiltered[index], label="np filtered")
      axs[i,filterIndex].set_title(f'{filterType} фильтр, {i + 1} функция')
      axs[i,filterIndex].legend()
      axs[i,filterIndex].grid()
      axs[i,filterIndex].set(xlabel='t', ylabel='y')
      index += 1
  plt.show()
        
def showFilteredImages(image: ndarray, filteredImages):
  fig, axs = plt.subplots(2,2)
  filteredImages.append(image)
  index = 0
  for i in range(2):
    for filterIndex in range(2):
      nar= asarray(filteredImages[index])
      axs[i,filterIndex].imshow(abs(nar),vmax="5000",  cmap="gray")
      index += 1
  plt.show()