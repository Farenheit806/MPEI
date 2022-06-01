# Импорты
from FourierTransform import getFreqFiltered, showFilteredImages, showPlotsDFT1, showPlotsSpectr1
from Data import getFunctions, getGrayScaledMatrix, getArgs
from matplotlib.pyplot import plot, subplots, show, imshow
from numpy.fft import fft, fft2, fftshift
from numpy import abs

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Задание переменных
N = 1 # номер варианта

length = 1000 # длина
D = 100 # длина сигнала / 2

t, freq = getArgs(length, D)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# # Одномерные преобразования
# functions = getFunctions(N, t) # получение массива из 2 необходимых для ОДФП функций
# filteredArrays, spectr = getFreqFiltered(functions, False, freq) # получение отфильтрованного списка (также для обеих функций сразу)
# npFiltered, spectrNP = getFreqFiltered(functions, True, freq) # получение отфильтрованного списка с использованием numpy


# showPlotsSpectr1(spectr, spectrNP, freq)
# showPlotsDFT1(filteredArrays, functions, npFiltered, t) # построение графиков для одномерного преобразования
# # ---------------------------------------------------------------------------------------------------------------------------------------------------
# # Двухмерные преобразования
image = getGrayScaledMatrix("pepe.jpg")
# filteredImage, filteredFTs = getFreqFiltered(image, True)
filteredImage, filteredFTs = getFreqFiltered(image, False)

showFilteredImages(image, filteredFTs)
showFilteredImages(image, filteredImage)

# # ---------------------------------------------------------------------------------------------------------------------------------------------------
