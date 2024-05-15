# 제가 작성한 예시들 
import math


# 단일 입력받기 
A = input("A를 입력해주세요")
print(A) # 파이썬에서는 print로 값을 출력합니다. 

# 다중 입력받기 (문자열)
# split 메서드를 이용해서 공백을 기준으로 입력받습니다.
A, B = input("A, B를 입력해주세요").split()
 
# 다중 입력받기 (숫자)
# 1. split 메서드로 이용해서 공백을 기준으로 입력받은 값들이 숫자로 변환됩니다.
# 2. A, B 라는 변수에 값이 저장됩니다.
A, B = map(int , input("A B를 입력해주세요").split())

# 국, 영, 수, 사, 과 입력받은 값으로 합과 평균 구하기 
Kor,Eng,Math,Soc,Sic = input("국, 영, 수, 사, 과").split()
total = int(Kor) + int(Eng) + int(Math) + int(Soc) + int(Sic)
avg = total / 5

# 더보기: 만약에 값이 여러개라면... 5개가 아니라 100개 라면 
# 1. 파이썬에서 입력받은 값들을 list, 즉 배열로 만듭니다. 
subList = list(map(int ,input("다음 과목 5개의 점수를 입력해주세요").split()))
# 2. for in range 문을 이용해서 배열을 순회하여 입력값을 더하는 과정을 반복합니다. 
# len() 메서드를 이용해서 배열의 길이를 가져옵니다.
tot = 0
for i in range(len(subList)-1):
    tot = tot + subList[i]
    
print(tot)
# 느낀점 : 입력받은 변수 하나하나 형변환 해주지 않아도 되는군요


# 더보기: 평균에 따라 범위를 나눈다면 
 
# 점수	       90 - 100	     80 - 90	      70 - 80	       60 - 70	      60 ~
# 등급	           A	      B	                C 	              D	           F


# 일단 math 라이브러리를 임포트해옵니다. 

# 결과로 나온 평균의 소수점 아래 부분을 math 라이브러리의 floor를 이용해서 내림해줍니다.
# 예시 : 4.2 => 4 
# 예를 들어서
평균 = 4.2
변수 = math.floor(평균)

if 평균 >= 90 & 평균<= 100:
  print("A")
elif 평균 >=80 & 평균 <= 90:
 print("B")
elif 평균 >= 70 & 평균 <= 80:
 print("C")
elif 평균 >= 60 & 평균 <= 70:
 print("D")
elif 평균 < 60:
 print("F")

# 느낀점: math 라이브러리는 수학계산에 유용하는구나....

    



