import math


#def beanTrueD():
#    return -0.4036*(bean_h2oB**2)+22.236*(bean_h2oB)+893.21

def beanBulkD():
    return 0.1149*(bean_h2oB**2)+10.832*(bean_h2oB)+758.51

#def beanPorosity():
#    return -0.333*(bean_h2oB**2)+2.146*(bean_h2oB)+20.497

def beanV():
    return ((bean_W * beanDrytime)/ (beanBulk() * 24)) * float(input('여유공간비'))

def airVS():
    return (air_DW / (1.293 * (heaterT/273.15)))
#공기 0도씨 밀도 1.293 kg/m3

def airV():
    return beanV()*float(input('콩 : 공기 비 = 1 : x'))

def airTime():
    return airV()/airVS()

def dryerV():
    V=(airV()+beanV())
    print('가로 세로 높이 비')
    a=input('가로')
    b=input('세로')
    c=input('높이')
    x=math.pow((V/a*b*c),(1/3))
    print('가로 :',a*x,'세로 :',b*x,'높이 :',c*x)
