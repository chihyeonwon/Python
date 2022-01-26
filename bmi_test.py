# 이름, 몸무게, 키를 입력받습니다.
name = input("이름을 입력하세요> ")
weight = input("몸무게를 입력하세요> ")
height = input("키를 입력하세요>")

# 결과를 계산합니다.
bmi = int(weight) / ((int(height) / 100) ** 2)
result = ""
if 25 <= bmi:
    result = "과체중"
elif 18.5 <= bmi:
    result = "정상 체중"
else:
    result = "저체중"

# 출력합니다.
print("{}은 {}kg, {}cm로 {}입니다.".format(name, weight, height, result))
