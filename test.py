import pyupbit

access = "zx33xkyMyBDnO9vWB6i9A5FMOfMOB2vGwYSYAqpx"          # 본인 값으로 변경
secret = "Z2tigXGYapYE7jsrR1HoeRPlELMdaxW5zxA2Tyb5"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-VET"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

