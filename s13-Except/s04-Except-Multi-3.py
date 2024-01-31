# -*- coding: utf-8 -*-

# 예외처리
# 여러 예외를 처리

x = 10
y = 0
z = None

# 아래 변수(c)를 주석으로 막으면 NameError 예외발생
c = 0

try:
    print("x=", x)
    print("y=", y)
    print("c=", c) # NameError
    z = x / y      # ZeroDivisionError
except Exception as e: # 모든 예외를 처리
    print("[예외발생] 알 수 없는 예외가 발생했습니다.", e)    
    
    
print(f"결과:{x} / {y} -> {z}")    