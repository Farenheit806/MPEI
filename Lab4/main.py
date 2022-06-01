from numpy import array, hstack, sqrt, linalg, zeros

def getCalibrationFactor(x,y,z,u,v):
  A = zeros((14, 11))
  B = []
  for i in range(7):
      A[i] = array([x[i], y[i], z[i], 1, 0, 0, 0, 0, -x[i]*u[i], - y[i]*u[i], - z[i]*u[i]])
  for i in range(7):
      A[i+7] = array([0, 0, 0, 0, x[i], y[i], z[i], 1, -x[i]*v[i], - y[i]*v[i], - z[i]*v[i]])
  B = u
  C = hstack((B, v))
  return linalg.lstsq(A, C, rcond=None)

def std(u,ut):
    sum=0
    for i in range(7):
        sum+=(ut[i]-u[i])**2
    return(sqrt(sum/7))

x = array([0,75,50,0,25,125,100])
y = array([0,0,100,150,200,175,250])
z = array([50,150,75,200,100,40,200])

u_1 = array([411,475,657,721,827,877,1039])
v_1 = array([411,309,373,59,253,487,1117])

u_2 = array([350,556,484,350,424,653,597])
v_2 = array([788,578,559,231,371,513,105])

c_1, res, _, _ = getCalibrationFactor(x,y,z,u_1,v_1)
c_2, res1, _, _ = getCalibrationFactor(x,y,z,u_2,v_2)

xx=[]
yy=[]
zz=[]
pusto=[]

for i in range(7):
    biba=array([u_1[i],v_1[i],u_2[i],v_2[i]])
    mama=array([
    [c_1[0]-c_1[8]*u_1[i], c_1[1]-c_1[9]*u_1[i], c_1[2]-c_1[10]*u_1[i], c_1[3]],
    [c_1[4]-c_1[8]*v_1[i], c_1[5]-c_1[9]*v_1[i], c_1[6]-c_1[10]*v_1[i], c_1[7]],
    [c_2[0]-c_2[8]*u_2[i], c_2[1]-c_2[9]*u_2[i], c_2[2]-c_2[10]*u_2[i], c_2[3]],
    [c_2[4]-c_2[8]*v_2[i], c_2[5]-c_2[9]*v_2[i], c_2[6]-c_2[10]*v_2[i], c_2[7]],
    ])
    XY=linalg.solve(mama,biba)
    xx.append(XY[0])
    yy.append(XY[1])
    zz.append(XY[2])


print(xx,std(xx,x))
print(yy,std(yy,y))
print(zz,std(zz,z))

