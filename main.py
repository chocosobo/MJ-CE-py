
import psySI as psySI


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


heater_Max=float(input('입구 공기 최고 가열온도 °C'))+273.15  #120
heater_Min=float(input('입구 공기 최저 가열온도 °C'))+273.15  #100

heaterT=heater_Max
beanOutT=float(input('출구 콩 온도 °C'))+273.15               #45

#송풍기 전력량
fanE=float(input('송풍기 전력소모 kW'))*24*30

seasonT=float(input('통계 온도 °C'))+273.15
seasonRH=float(input('통계 습도 %'))*0.01
heaterEff=float(input('가열기 효율 %'))/100                  #90
dryerEff=float(input('건조기 효율 %'))/100                   #70


#출구 최종조건
ObjT_min=(beanOutT+5)      #K                         #최저 온도
ObjT_max=(beanOutT+10)     #K                         #최고 온도
ObjRH_min=20                #%                         #최저 습도
ObjRH_max=30                #%                         #최고 습도
print(ObjT_min,ObjT_max,ObjRH_min,ObjRH_max)



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
    air_W=air_min
    return air_W*(1-psySI.__W_DBT_RH_P(seasonT,seasonRH,P))


#콩에 소비된 엔탈피  총량
def BeanE_change():
    return ((beanOutT-273.15)*beanE_A*(bean_W-h2oOut_bean)) - ((seasonT-273.15)*beanE_B*bean_W)

#건조기에서 콩에 사용된 엔탈피 총량
def DryerE():
    return (BeanE_change()) / dryerEff


#계절 절대습도
def seasonW():
    return psySI.__W_DBT_RH_P(seasonT,seasonRH,P)

#계절 엔탈피
def seasonE():
    return psySI.__H_DBT_W(seasonT,seasonW())


#가열후 공기 엔탈피
def HeaterE():
    return psySI.__H_DBT_W(heaterT,seasonW())
    

#건조 후 공기 총 엔탈피
def DryedE():
    E= HeaterE() - (DryerE()/DA_W())
    return E


#출구 절대습도  w
def OutW():
    return (h2oOut_bean + air_W*seasonW())/DA_W()

#출구 온도
def OutT():
    return psySI.__DBT_H_W(OutW(),DryedE())

#출구 상대습도
def OutRH():
    return psySI.__RH_DBT_W_P(OutT(),DryedE(),P)

#가열기 소모 엔탈피
def Heating():
    return DA_W()*(HeaterE() - seasonE())


#정보받기

    
    
#    '습도도표에 표시'
#    '1 계절 온습도(seasonT,seasonRH)' 
#    '2 가열후 온습도(heaterT,seasonHumidity()) ->'
#    '3 건조 후 온습도(OutTemp,OutRH)'
    


def checkingT():
    
    while heaterT>=heater_Min :
        checkingDA()

        #for item in list
        heaterT=-1
    return min([리스트중 heaterT]*([리스트중 air_max]*(1-psySI.__W_DBT_RH_P(seasonT,seasonRH,P)))*(__H_DBT_W( T,((h2oOut/DA)+seasonHumidity()))-(airseasonE())))




def checkingDA():
    air_min=bean_W*2
    air_max=bean_W*4
    
    dif=100
    
    
    while dif>1:
        
        air_W=air_min
        dif=dif/10
        
        while (1):
            if checkingTRH()==0:
                air_max=air_W
                air_min=air_max-dif
                break
                
            elif checkingTRH()==1:
                air_W=+dif
                
            elif checkingTRH()==2:
                return False
            
    list.append([air_max,heaterT,OutTemp,outRH])



list=[]

def checkingTRH():
    OutTemp= psySI.__DBT_H_W(DryedE(),OutW())
    OutRH= psySI.__RH_DBT_W_P(OutTemp,soydry.OutW(),P)
    
    
    if OutTemp<ObjT_min:
        print('공기 부족')
        return 1

    elif OutTemp>=ObjT_min and OutTemp<=ObjT_max:
        print('적절한 온도')
        if OutRH>ObjRH_max:
            print('공기 부족')
            return 1
        
        elif OutRH>=ObjH_min and OutRH<=ObjRH_max:
            print('적합한 값')
            return 0
        elif OutRH<ObjRH_min:
            print('온도 적합,공기 넘침')
            return 2
    
    if OutTemp>ObjT_max:
        print('과열, 다음으로')
        return 2
    

#print(checkingTRH())
#print(checkingAir())
#print(checkingT())

        
def finalQ():
    return min(HeaterE()-seasonE())#측정값중




##csv로 계절별통계만들기



#비용
LNGprice=float(input('LNG 요금 (원/MJ)'))*1000
ELECprice=float(input('전기 요금 (원/KW)'))
