from turtle import *

color('blue', 'yellow')
begin_fill()

for _ in range(4):
    forward(100)  # 각 변의 길이
    left(90)      # 각도 90도로 회전

end_fill()
done()
