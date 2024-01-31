# -*- coding: utf-8 -*-

# 예외처리
# 예외 발생시키기 : raise

# 새(bird)
# 제약: fly() 메소드의 기능 구현하도록 강제
# 예외발생: NotImplementedError, 기능구현이 되어 있지 않다.
#  
class Bird:
    def fly(self): # 날다
        raise NotImplementedError("날 수 없습니다")
    
#%%

# 예외처리
try:
    bird = Bird()
    bird.fly()
except NotImplementedError as e:
    print(f"[예외발생] 기능 미구현: ({e})") 
    
    