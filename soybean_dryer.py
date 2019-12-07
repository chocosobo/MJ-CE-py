
import psySI as psySI
import gang as gang
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
    W= air_W*(1-psySI.__W_DBT_H(seasonT,seasonH))
    return W


#콩에 소비된 엔탈피  총량
def BeanE_change():
    E_drying= ((beanOutT-273.15)*beanE_A*(bean_W-h2oOut_bean)) - ((seasonT-273.15)*beanE_B*bean_W)
    return E_drying

#건조기에서 콩에 사용된 엔탈피 총량
def DryerE():
    return (BeanE_change()) / DryerE


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



#print('건조후엔탙ㄹ피','출구절ㄹ대습도',OutH())
#print('건조후 공기총엔탈',airDryedE())
#print('가열후공기',airHeatE())
#print('계절ㅈ절대습도',seasonHumidity())
#print(OutTemp,OutRH)

