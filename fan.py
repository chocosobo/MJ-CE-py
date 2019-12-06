def fanControll():
    airPmin=air_DW/ (1.293*(1-psySI.__W_DBT_RH_P(seasonT,seasonRH,P))) / 24*60
    print('분당 건조공기 유속 (m^3/min)',airPmin)
    fanPower=float(input('송풍기 송풍량')
    fanE=(airPmin / fanPower)
    fankW=float(input('송풍기 전기소모량'))*fanE
    return input('전기요금 (원/kW)')*fankW
