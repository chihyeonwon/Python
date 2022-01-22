# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 광고",
    "type": "당절임",
    "ingredient": ["망고", "설탕"],
    "origin": "필리핀"
}

# 존재하지 않는 키에 접근해봅니다.
value = dictionary.get("존재하지 않는 키")
print("값:", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
