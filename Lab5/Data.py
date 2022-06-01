from PIL import Image
from numpy import abs, cos, linspace, ndarray, sin, array, pi, sqrt
from numpy.fft import fftfreq

def getFunctions(N, t):
  y1 = []
  y2 = []
  for i in range(len(t)):
    y1.append(cos(0.5 * N * t[i]) + N * sin(t[i]+(2 * N + 1) * t[i]))
    if (abs(t[i])<=N):
      y2.append(1/(20*N))
    else:
      y2.append(0)
  return [y1,y2]

def getArgs(length: int, D: int):
  samplingRate = 2*D/length # частота дискретизации
  t = linspace(-D,D,length)
  freq = fftfreq(length, samplingRate)
  return t, freq

def getGrayScaledMatrix(src):
  return array(Image.open(src).convert("L"))

def freqFiltration(ft, filterIndex, freq = 0):
  if type(ft[0]) == ndarray:
    filtered_ft = matrixCycle(ft, filterIndex)
  else:
    filtered_ft = listCycle(ft, filterIndex, freq)
  return filtered_ft

def matrixCycle(ft, filterIndex):
  M, N = ft.shape
  limit_1 = 10
  limit_2 = 20
  limit_3 = 20
  limit_4 = 10
  for m in range(M):
    for n in range(N):
      currentFreq = (sqrt((m-M/2)**2 + (n-N/2)**2))
      if (filterIndex == 0) and (currentFreq <= limit_1) or (filterIndex == 1) and (currentFreq >= limit_2) or (filterIndex == 2) and (currentFreq <= limit_3) and (currentFreq >= limit_4):
        ft[m][n] = 0
  return ft

def listCycle(ft, filterIndex, freq):
  M = len(ft)
  limit_1 = 0.3
  limit_2 = 0.5
  limit_3 = 1
  limit_4 = 0.3
  for m in range(M):
    currentFreq = abs(freq[m])
    if (filterIndex == 0) and (currentFreq <= limit_1) or (filterIndex == 1) and (currentFreq >= limit_2) or (filterIndex == 2) and (currentFreq <= limit_3) and (currentFreq >= limit_4):
      ft[m] = 0
  return ft