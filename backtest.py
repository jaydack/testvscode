import pyupbit
import numpy as np

#ohlcv(open, high, low, close, volume) 시가, 고가, 저가, 종가,거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC",count=7)
#변동성 돌파 기준 범위 계산, (고가- 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

#range 컬럼을 한칸씩 밑으로 내림 (.shift(1))
df['target'] = df['open'] + df['range'].shift(1)


print(df)

#ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

#누적 곱 계산(cumprod)= 누적수익율
df['hpr'] = df['ror'].cumprod()
#draw down(하락폭) 계산 (누적 최대값과 현제 hpr 차이 / 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#mdd (dd값중 최대 값)
print("MDD(%): ", df['dd'].max())

#계산된 값을 엑셀로 저장
df.to_excel("dd.xlsx")