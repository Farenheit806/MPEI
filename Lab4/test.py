from numpy import append, array, hstack, zeros, linalg



def getCalibration(XYZ: list, UV: list):
  result = zeros((3,4))
  x,y,z = XYZ
  u, v = UV
  A = zeros((14,11))
  for i in range(7):
    A[i] = array([x[i], y[i], z[i], 1, 0, 0, 0, 0, -x[i]*u[i], - y[i]*u[i], - z[i]*u[i]])
    A[i+7] = array([0, 0, 0, 0, x[i], y[i], z[i], 1, -x[i]*v[i], - y[i]*v[i], - z[i]*v[i]])    
  B = hstack((u[:7], v[:7]))
  c, res, _, _ = linalg.lstsq(A, B, rcond=None)
  index = 0
  c = append(c, 1.0)
  for i in range(result.shape[0]):
    for j in range(result.shape[1]):
      result[i][j] = c[index]
      index += 1
  return result

def getTeorUV(XYZ, C):
  length = sum(C.shape)
  height = C.shape[0]
  uv = zeros((2,length))
  for i in range(length):
    current = [0, 0, 0]
    for k in range(height):
      for j in range(height):
        current[k] += C[k][j] * XYZ[j][i]
      current[k] += C[k][height]
    for l in range(2):
      uv[l][i] = current[l] / current[2]
  return uv

def getDif(UV, teorUV):
  dif = zeros(teorUV.shape)
  for i in range(dif.shape[0]):
    for j in range(dif.shape[1]):
      dif[i][j] = teorUV[i][j] - UV[i][j]
  return dif

def printC(arrayToPrint):
  for i in range(len(arrayToPrint)):
    print(f'Калибровочные коэффициенты изображения {i + 1}')
    print(arrayToPrint[i])

def printUVs(arraysToPrint):
  values = ["u", "v"]
  category = ["Практические значения", "Теоретические значения", "Ошибка репроекции"]
  for imageIndex in range(2):
    print(f"Изображение {imageIndex + 1}:")
    for i in range(len(category)):
      for j in range(len(values)):
        print(category[i], values[j])
        print(arraysToPrint[i][imageIndex][j])

def getValues(XYZ, UV):
  c = []
  teorUV = []
  dif = []
  for imageIndex in range(len(UV)):
    c.append(getCalibration(XYZ, UV[imageIndex]))
    teorUV.append(getTeorUV(XYZ, c[imageIndex]))
    dif.append(getDif(UV[imageIndex], teorUV[imageIndex]))
  return c, teorUV, dif

XYZ = [array([0,75,50,0,25,125,100]), array([0,0,100,150,200,175,250]), array([50,150,75,200,100,40,200])]
UV_1 = [array([411,475,657,721,827,877,1039]), array([411,309,373,59,253,487,1117])]
UV_2 = [array([350,556,484,350,424,653,597]), array([788,578,559,231,371,513,105])]
UV = array([UV_1, UV_2])

C, teorUV, dif = getValues(XYZ, UV)

printC(C)
printUVs([UV,teorUV,dif])
