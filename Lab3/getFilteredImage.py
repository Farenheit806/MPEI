from numpy import sum

def getD(mask):
  res = sum(mask)
  return res if res != 0 else 1

def filterPixel(k,l,image,mask, D, B, length):
  res = 0
  sum_ = 0
  for i in range(length):
    for j in range(length):
      sum_ += image[i-length//2+k][j - length//2 + l]*mask[i - length//2][j - length//2]
  res = sum_ * 1 / D + B
  return res

def getFilteredImage(image, mask, B):
  res = []
  lenx, leny = image.shape
  lenM, lenMy = mask.shape
  q = lenM // 2
  D = getD(mask)
  for k in range (1,lenx - q):
    resForRow = []
    for l in range (1,leny - q): 
      resForPixel = filterPixel(k,l,image,mask, D, B, lenM)
      resForRow.append(resForPixel)
    res.append(resForRow)
  return res
    