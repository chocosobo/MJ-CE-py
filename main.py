
import psySI as psySI








loop=0
pros=0
Q=0
while loop==0:
    
    
    while pros==0:
        print('기본 설정')
        
        #1기압
        P=float(101325)
        
        #콩 설정
        bean_W=float(input('콩 질량 Kg/Day'))
        bean_h2oB=float(input('콩 수분 wt%'))                    #14
        bean_h2oA=float(input('건조 후 콩 수분 목표 wt%'))        #10
        h2oOut_bean=(bean_W-bean_W*(1-bean_h2oB*0.01)/(1-bean_h2oA*0.01))
        beanE_B=round(1.4435*(1+4.06*0.01*bean_h2oB),4)               #2.2625
        beanE_A=round(1.4435*(1+4.06*0.01*bean_h2oA),4)               #2.03
        
        heater_Max=float(input('입구 공기 최고 가열온도 °C'))+273.15  #120
        heater_Min=float(input('입구 공기 최저 가열온도 °C'))+273.15  #100
        
        
        beanOutT=float(input('출구 콩 온도 °C'))+273.15               #45
        
    
        ObjT_min=float(input('최저 출구 온도 °C (출구콩 온도 +5 권장)')) +273.15     #K                         #최저 온도
        ObjT_max=float(input('최고 출구 온도 °C (출구콩 온도 +10 권장)')) +273.15     #K                         #최고 온도
        ObjRH_min=float(input('최저 출구 상대습도 % (20 권장)')) *0.01      #0.18                #%                         #최저 습도
        ObjRH_max=float(input('최고 출구 상대습도 % (30 권장)')) *0.01      #0.32                #%                         #최고 습도
        pros=1
    
    while pros==1:
        print('\n\n계절설정')
        seasonT=float(input('통계 온도 °C'))+273.15
        seasonRH=float(input('통계 습도 %'))*0.01
        heaterEff=float(input('가열기 효율 %'))/100                  #90
        dryerEff=float(input('건조기 효율 %'))/100 
        pros=2
    
    
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
    
    while pros==2:
        final=[]
        chT=0
        heaterT=heater_Max
        
        while heaterT>=heater_Min :
            
            if chT==1:
                break
            
            if chT==2:
                #print('이하 온도 불충분')
                #del DAlist[-1]
                #print(DAlist)
                break
            
            air_min=bean_W*2
            air_max=bean_W*4
            
            dif=1000
            
            BeanE_change=((beanOutT-273.15)*beanE_A*(bean_W-h2oOut_bean)) - ((seasonT-273.15)*beanE_B*bean_W)
            DryerE= BeanE_change / dryerEff
            
            
            seasonW=psySI.__W_DBT_RH_P(seasonT,seasonRH,P)
            seasonE=psySI.__H_DBT_W(seasonT,seasonW)
            print('기본 엔탈피',seasonE)
            HeaterE=psySI.__H_DBT_W(heaterT,seasonW)
            print('히터 엔탈피',HeaterE)
            chDA=0
            while dif>1:
            
                if chDA==1:
                    #print('온도 낮추기')
                    break
                
                if chT==1:
                    break
                
                elif chT==2:
                    break
                air_W=air_min
                dif=dif/10
                #print('첫세팅',air_W,air_min,air_max,dif)
                
                while air_W<=air_max:
                    #print('스타트',air_W)
                    DA_W=air_W*(1-psySI.__W_DBT_RH_P(seasonT,seasonRH,P))
                    
                    
                    
                    DryedE=HeaterE - (DryerE/DA_W)
                    OutW=(h2oOut_bean + DA_W*seasonW)/DA_W
                    
                    
                    OutTemp=psySI.__DBT_H_W(DryedE,OutW)
                    OutRH= psySI.__RH_DBT_W_P(OutTemp,OutW,P)
                    
                    
                    #print('출구온도',OutTemp,'출구상대습도',OutRH)
                    #print('건조후에너지',DryedE,'출구절대습도',OutW,'건조공기량',DA_W,'계절엔탈피',seasonE,'계절절대습도',seasonW)
                    
                    if OutTemp<ObjT_min:
                        #print(air_W,'공기 부족')
                        chTRH=1
                    elif OutTemp>=ObjT_min and OutTemp<=ObjT_max:
                        #print('적절한 온도')
                        #print(OutTemp-273.15)
                        if OutRH>ObjRH_max:
                            #print(OutRH)
                            #print('공기 부족')
                            chTRH=1
                        elif OutRH>=ObjRH_min and OutRH<=ObjRH_max:
                            #print('적합한 값',air_W)
                            #a=input('적합한번')
                            Q=DA_W*(HeaterE-seasonE) #총 에너지 KJ
                            chTRH=0
                            chT=1
                        elif OutRH<ObjRH_min:
                            #print('온도 적합,공기 넘침',OutRH)
                            chTRH=2
                    elif OutTemp>ObjT_max:
                        #print('과열, 다음으로')
                        chTRH=2
                        
                    if chTRH==0:
                        #print('적합 공기량',air_W)
                        air_max=air_W
                        air_min=air_max-dif
                        #print('적합 공기위아래',air_max,air_min)
                        break
                        
                    elif chTRH==1:
                        #print('추가전',air_W,dif)
                        air_W=air_W+dif
                        #print('추가후',air_W)
                        
                    elif chTRH==2:
                        chDA=1
                        break
                    
                    if air_W>air_max:
                        chT=2
                                    
                    
            #DAlist.append([Q,air_W,heaterT-273.15,OutTemp,OutRH])
            
            
            heaterT=heaterT-1
        if chT==1:
            heaterT=heaterT+1
            final.append([Q,air_W,seasonT-273.15,seasonW,heaterT-273.15,seasonW,OutTemp-273.15,OutW,OutRH])
            print('최소 공기량',air_W,'kg')
            print('효율 무시한 에너지 소모 총량',Q/1000,'MJ')
            print('계절 온도',seasonT-273.15,'°C')
            print('계절 절대습도',seasonW,'kg/kg(DA)')
            print('가열 후 온도',heaterT-273.15,'°C')
            print('출구 온도',OutTemp-273.15,'°C')
            print('출구 상대습도 ',OutRH*100,'%')
            print('출구 절대습도',OutW,'kg/kg(DA)')
        pros=3
       # print(DAlist.sort)
    
    while pros==3:
        print('\n\n건설 및 비용 설정\n')
        drytime=float(input('콩 건조시간'))
        bulkD=0.1149*(bean_h2oB**2)+10.832*bean_h2oB+758.51
        bean_flow=(bean_W/bulkD)*drytime/24
        
        exspace=float(input('여유공간 %'))*0.01
        bean_Trueflow=bean_flow*(1+exspace)
        
        air_D=1.293
        
        beantoair=float(input('콩 대비 공기 비'))
        air_flowW=air_W/air_D/(60*60*24)
        
        
        air_flowV=air_W/(air_D*(seasonT/273))/(27*60)
        print('공기 유속 m^3/min',air_flowV)
        air_time=(bean_Trueflow*beantoair)/air_flowW
        
        print('이 후 폭:깊이:높이 비 입력:')
        dryerW=float(input('폭 비율'))
        dryerD=float(input('깊이 비율'))
        dryerH=float(input('높이 비율'))
        
        length=pow((bean_Trueflow*2)/(dryerW*dryerD*dryerH),1/3)
        print('폭 깊이 높이 =',dryerW*length,dryerD*length,dryerH*length)
        
        fanE=float(input('송풍기 전략소모량'))
        fanP=float(input('송풍기 풍량 CMM'))
        fanEff=(air_flowV/fanP)
        fankW=(fanE*fanEff)*(24*90)
        
        Elecprice=float(input('전기 요금 원/kw'))
        LNGprice=float(input('LNG 요금 원/MJ'))
    
        print('송풍기 필요 수',fanEff)
        print('90일간 전기요금 원',fankW*Elecprice)
        print('90일간 LNG 요금 원',((Q/heaterEff)/1000)*LNGprice*90)
        
        pros=4
        
    while pros==4:
        print('\n\n최종\n')
        
        print('\n온습도')
        print('최소 공기량',air_W)
        print('최소 에너지 소모량 KJ',Q)
        print('최소 에너지 소모량 kWh',Q/3600)
        print('계절 온도 절대습도',seasonT-273.15,seasonW)
        print('가열 후 온도 절대습도',heaterT-273.15,seasonW)
        print('출구 온도 절대습도',OutTemp-273.15,OutW)
        
        print('\n건조기 크기')
        print('폭 깊이 높이 =',dryerW*length,dryerD*length,dryerH*length)
        
        print('\n비용산정')
        print('송풍기 필요 수',fanEff)
        print('90일간 전기요금 원',fankW*Elecprice)
        print('90일간 LNG 요금 원',((Q/heaterEff)/1000)*LNGprice*90)
        
        print('다시하기')
        pros=float(input('0=기본설정,1=계절설정,3=건설 및 비용산정'))