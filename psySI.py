

import soybean_dryer as soydry
import psySI

#1기압
P=float(101325)

#콩 설정
bean_W=float(input('콩 질량 Kg/Day'))
bean_h2oB=float(input('콩 수분 질량비 %'))                    #14
bean_h2oA=float(input('건조 후 콩 수분 목표 질량비 %'))        #10
h2oOut_bean=(bean_W-bean_W*(1-bean_h2oB*0.01)/(1-bean_h2oA*0.01))
beanE_B=round(1.4435*(1+4.06*0.01*bean_h2oB),4)               #2.2625
beanE_A=round(1.4435*(1+4.06*0.01*bean_h2oA),4)               #2.03
#유입량 설정
beanDrytime=float(input('콩 건조시간 (h)'))

air_min=bean_W*2
air_max=bean_W*4



#건조 가열  효율
#heaterE_summer=float(input('가열기 효율 %'))                 #90
#dryerE_summer=float(input('건조기 효율 %'))                  #70
#heaterE_fall=float(input('가열기 효율 %'))                   #90
#dryerE_fall=float(input('건조기 효율 %'))                    #70
#heaterE_winter=float(input('가열기 효율 %'))                 #90
#dryerE_winter=float(input('건조기 효율 %'))                  #60

Tmax=float(input('입구가열 최고온도 °C'))+273.15               #120
Tmin=float(input('입구가열 최저온도 °C'))+273.15               #100
heaterT=Tmax
beanOutT=float(input('출구 콩 온도 °C'))+273.15               #45

#송풍기 전력량
fanE=float(input('송풍기 전력소모 kW'))*24*30




#출구 최종조건
ObjT_min=(beanOutT+5)      #K                         #최저 온도
ObjT_max=(beanOutT+10)     #K                         #최고 온도
ObjH_min=20                #%                         #최저 습도
ObjH_max=30                #%                         #최고 습도
print(ObjT_min,ObjT_max,ObjH_min,ObjH_max)




##계절선택
#i=0
#
#def perSeason():
#    global i
#    if i==0:
#        print('현재 봄입니다')
#        season='spring'
#    if i==1:
#        print('현재 여름입니다')
#        season='summer'
#    if i==2:
#       print('현재 가을입니다')
#        season='fall'
#    if i==3:
#        print('현재 겨울입니다')
#        season='winter'
#    else:
#        print('모든 계절이 끝났습니다')


def GetseasonInfo():
    seasonT=float(input('통계 온도 °C'))+273.15
    seasonRH=float(input('통계 습도 %'))*0.01
    heaterEff=float(input('가열기 효율 %'))/100                  #90
    dryerEff=float(input('건조기 효율 %'))/100                   #70


    
#    '습도도표에 표시'
#    '1 계절 온습도(seasonT,seasonRH)' 
#    '2 가열후 온습도(heaterT,seasonHumidity()) ->'
#    '3 건조 후 온습도(OutTemp,OutRH)'
    


def checkingT():
    for i=heaterT; i>=Tmin; i=i-1:
        checkingAir()

        #for item in list
    return min([리스트중 heaterT]*([리스트중 air_max]*(1-psySI.__W_DBT_RH_P(seasonT,seasonRH,P)))*(__H_DBT_W( T,((h2oOut/DA)+seasonHumidity()))-(airseasonE())))




def checkingAir():
    IsFinded = False
    while True:
        dif=(air_max-air_min)/100

        if dif < 1:
            break

        elif checkingTRH()==False:
            air_min+=dif
        elif checkingTRH()==True:
            IsFinded = True
            air_max=air_min
            air_min=air_max-dif
    if IsFinded:
        list.append([air_max,heaterT,OutTemp,outRH])



list=[]

OutTemp = 0
OutRH = 0

def checkingTRH():
    OutTemp= psySI.__DBT_H_W(soydry.airDryedE(),soydry.OutH())
    OutRH= psySI.__RH_DBT_W_P(OutTemp,soydry.OutH(),P)

    if OutTemp>=ObjT_min and OutTemp<=ObjT_max:
        if OutRH>=ObjH_min and OutRH<=ObjH_max:
            return True
        else:
            print('습도 안맞음',OutRH)
            return False
    if OutTemp>ObjT_max:
        print('과열')
        return False
    if OutTemp<ObjT_min and OutRH>ObjH_max:
        print('공기불충분')
        return False

print(checkingTRH())
print(checkingAir())
print(checkingT())

        
def finalQ():
    return min(soydry.airHeatE()-soydry.airseasonE())#측정값중




##csv로 계절별통계만들기



#비용
LNGprice=float(input('LNG 요금 (원/MJ)'))*1000
ELECprice=float(input('전기 요금 (원/KW)'))
