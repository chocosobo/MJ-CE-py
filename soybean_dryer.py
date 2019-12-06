
import psySI.py as psySI
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



#def _DB__RHT_W_P(DBT, W, P):
#    if __valid_DBT(DBT):
#        return W*P/((0.621945+W)*__Pws(DBT))

#def __RH_DBT_W_P(DBT, W, P):
#    if __valid_DBT(DBT):
#        return W*P/((0.621945+W)*__Pws(DBT))

#def __DBT_H_W(H, W):
#    [DBTa, DBTb]=[Min_DBT, Max_DBT]
#    DBT=(DBTa+DBTb)/2
#    while DBTb-DBTa>TOL:
#        ya=W-__W_DBT_H(DBTa, H)
#        y=W-__W_DBT_H(DBT, H)
#        if __is_positive(y)==__is_positive(ya):
#            DBTa=DBT
#        else:
#            DBTb=DBT
#        DBT=(DBTa+DBTb)/2
#    return DBT

#def __V_DBT_W_P(DBT, W, P):
#    if __valid_DBT(DBT):
#        return 287.042*DBT*(1+1.607858*W)/P

#def __W_DBT_RH_P(DBT, RH, P):
#    if __valid_DBT(DBT):
#        Pw=RH*__Pws(DBT)
#        return 0.621945*Pw/(P-Pw)

#print(psySI.__DBT_H_W(H, W))
#print(psySI.__RH_DBT_W_P(psySI.__DBT_H_W(H, W), W, P))


#건조공기량
def DA_W():
    W= air_W*(1-psySI.__W_DBT_H(seasonT,seasonH))
    return W


#콩에 소비된 엔탈피  총량
def BeanE_change():
    E_drying= ((beanOutT-273.15)*beanE_A*(bean_W-h2oOut_bean)) - ((seasonT-273.15)*beanE_B*bean_W)
    return E_drying


season_DryerE=dryerE_spring
#건조기에서 콩에 사용된 엔탈피 총량
def DryerE():
    DryerE_total= (BeanE_change()) / season_DryerE
    return DryerE_total


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


OutTemp= psySI.__DBT_H_W(airDryedE(),OutH())
OutRH= psySI.__RH_DBT_W_P(OutTemp,OutH(),P)

print('건조후엔탙ㄹ피','출구절ㄹ대습도',OutH())
print('건조후 공기총엔탈',airDryedE())
print('가열후공기',airHeatE())
print('계절ㅈ절대습도',seasonHumidity())
print(OutTemp,OutRH)

def checkingTRH():
    if OutTemp>=ObjT_min and OutTemp<=ObjT_max:
        if OutRH>=ObjH_min and OutRH<=ObjH_min:
            return True
        else:
            print('습도 안맞음',OutRH)
    else:
        print('온도 안맞음',OutTemp)

def checkingAir():
    dif=(air_max-air_mean)/10
    for i in 10:
        if checkingTRH()==True:
            air_max=

        air_min=+dif

def finalQ():
    return min(answers)

#습도도표에 표시 
1 계절 온습도 -> 
2 가열후 온습도(heaterT,seasonHumidity()) ->
3 건조 후 온습도(OutTemp,OutRH)


    
