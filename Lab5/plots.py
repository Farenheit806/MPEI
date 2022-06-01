from matplotlib import pyplot as plt

# Графики отфильтрованных функций и изображения
def showFilteredImages(image, filteredImages):
  fig, axs = plt.subplots(2,2)
  filteredImages.append(image)
  index = 0
  for i in range(2):
    for filterIndex in range(2):
      axs[i,filterIndex].imshow(abs(filteredImages[index]), cmap="gray")
      index += 1
  plt.show()

def showFilteredFunctions(t, source, filteredArrays, npFiltered):
  fig, axs = plt.subplots(2, 3)
  index = 0
  filterType = ["Низкочастотный","Высокочастотный","Полосный"]
  for i in range(len(source)):
    for filterIndex in range(3):
      axs[i,filterIndex].plot(t,source[i], label="not filtered", color="black", lw=0.5)
      axs[i,filterIndex].plot(t,filteredArrays[index], label="filtered", color="red", lw=2)
      axs[i,filterIndex].plot(t,npFiltered[index], label="np filtered")
      axs[i,filterIndex].set_title(f'{filterType[filterIndex]} фильтр, {i + 1} функция')
      axs[i,filterIndex].legend()
      axs[i,filterIndex].grid()
      axs[i,filterIndex].set(xlabel='t', ylabel='y')
      index += 1
  plt.show()
  
# Графики отфильтрованных образов функций и изображения
def showFilteredFTImages():
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

def showFilteredFTFunctions():
  plt.show()

# Графики неотфильтрованных функций и изображения
def showUnfilteredFunctions():
  fig, axs = plt.subplots(2,2)
  axs[0,0].plot(t,functions[0])
  axs[0,1].plot(freq,abs(fft(functions[0])))
  axs[1,0].plot(t,functions[1])
  axs[1,1].plot(freq,abs(fft(functions[1])))
  plt.show()

def showUnfilteredImages():
  fig, axs = plt.subplots(1,2)
  axs[0].imshow(image, cmap="gray")
  axs[1].imshow(abs(fftshift(fft2(image))),cmap="gray")
  plt.show()