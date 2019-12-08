
import psySI.py as psySI


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
#'air_W=92000'
air_DW=air_W*(1-psySI.__W_DBT_RH_P(seasonT,seasonRH,P))


#건조 가열  효율
#heaterE_summer=float(input('가열기 효율 %'))                 #90
#dryerE_summer=float(input('건조기 효율 %'))                  #70
#heaterE_fall=float(input('가열기 효율 %'))                   #90
#dryerE_fall=float(input('건조기 효율 %'))                    #70
#heaterE_winter=float(input('가열기 효율 %'))                 #90
#dryerE_winter=float(input('건조기 효율 %'))                  #60

heaterT=float(input('입구 공기 가열온도 °C'))+273.15          #90~120
beanOutT=float(input('출구 콩 온도 °C'))+273.15               #45

#송풍기 전력량
fanE=float(input('송풍기 전력소모 kW'))*24*30




#출구 최종조건
ObjT_min=(beanOutT+5)      #K                         #최저 온도
ObjT_max=(beanOutT+10)     #K                         #최고 온도
ObjH_min=20                #%                         #최저 습도
ObjH_max=30                #%                         #최고 습도
print(ObjT_min,ObjT_max,ObjH_min,ObjH_max)


OutTemp= psySI.__DBT_H_W(soydry.airDryedE(),soydry.OutH())
OutRH= psySI.__RH_DBT_W_P(OutTemp,soydry.OutH(),P)


import psySI as psySI
# All functions expect base SI units for any arguments given
# DBT   - Dry bulb temperature          - Kelvins, K
# DPT   - Dew point temperature         - Kelvins, K
# H     - Specific enthalpy             - kiloJoules per kilogram, kJ/kg
# P     - Atmospheric pressure          - Pascals, Pa
# Pw    - Water vapor partial pressure  - Pascals, Pa
# RH    - Relative humidity             - Decimal (i.e. not a percentage)
# V     - Specific volume               - Cubic meters per kilogram, m^3/kg
# W     - Humidity ratio                - kilograms per kilograms, kg/kg
# WBT   - Wet bulb temperature          - Kelvins, K


#건조공기량
def DA_W():
    return air_W*(1-psySI.__W_DBT_H(seasonT,seasonH))


#콩에 소비된 엔탈피  총량
def BeanE_change():
    return ((beanOutT-273.15)*beanE_A*(bean_W-h2oOut_bean)) - ((seasonT-273.15)*beanE_B*bean_W)

#건조기에서 콩에 사용된 엔탈피 총량
def DryerE():
    return (BeanE_change()) / DryerEff


#계절 절대습도
def seasonHumidity():
    return psySI.__W_DBT_RH_P(seasonT,seasonH,P)

#계절 엔탈피
def airseasonE():
    enthalpy=psySI.__H_DBT_W(seasonT,seasonHumidity())
    return enthalpy


#가열후 공기 엔탈피
def airHeatE():
    E= psySI.__H_DBT_W(heaterT,psySI.__W_DBT_RH_P(seasonT,seasonH,P))
    return E

#가열기  엔탈피


#건조 후 공기 총 엔탈피
def airDryedE():
    E= airHeatE() - (DryerE()/DA_W())
    return E


#출구 절대습도  w
def OutH():
    Humid= (h2oOut_bean + air_W*seasonHumidity())/air_W
    return Humid

def OutT():
    return psySI.__DBT_H_W(OutH(),airDryedE())
    
def OutRH():
    return psySI.__RH_DBT_W_P(OutT(),airDryedE(),P)

    


#print('건조후엔탙ㄹ피','출구절ㄹ대습도',OutH())
#print('건조후 공기총엔탈',airDryedE())
#print('가열후공기',airHeatE())
#print('계절ㅈ절대습도',seasonHumidity())
#print(OutTemp,OutRH)


def GetseasonInfo():
    seasonT=float(input('통계 온도 °C'))+273.15
    seasonRH=float(input('통계 습도 %'))*0.01
    heaterEff=float(input('가열기 효율 %'))/100                  #90
    dryerEff=float(input('건조기 효율 %'))/100                   #70
    
    
    
    '습도도표에 표시'
    '1 계절 온습도(seasonT,seasonRH)' 
    '2 가열후 온습도(heaterT,seasonHumidity()) ->'
    '3 건조 후 온습도(OutTemp,OutRH)'
    


def checkingT():
    for i=heaterT i>=Tmin i=i-1:
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
