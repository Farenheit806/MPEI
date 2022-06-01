from PIL import Image
from numpy import array
import matplotlib.pyplot as plt
from masks import getMasks
from getFilteredImage import getFilteredImage

def filterImage(image, B, masks):
  imgArray = array(image) # массив исходного изображения
  grayImage = image.convert('L') # конвертация изображения в монохроматические цвета
  grayImgArray = array(grayImage) # массив конвертированного в монохроматические цвета исходного изображения
  
  filteredImage = [] # пустой список, в котором в дальнейшем будут храниться отфильтрованные массивы
  ax = [] # список, необходимый для хранения изображений при построении subplot
  nums = [331,332,333,334,335,336,337,338,339] # список входных параметров положения для функции subplot
  for i in range(len(masks)+1):
    ax.append(plt.subplot(nums[i]))
    if (i != 0):
      filteredImage.append(getFilteredImage(grayImgArray,masks[i-1], B))
      ax[i].imshow(filteredImage[i-1],cmap="gray")
      ax[i].set_title(f'{i+1}-ое изображение')
    else:
      ax[i].imshow(imgArray)
      ax[i].set_title("Исходное изображение")     
  plt.show()

masks = getMasks()
image = Image.open('1.jpg')
B = 0

filterImage(image,B,masks)
