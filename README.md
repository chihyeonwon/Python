# 혼자 공부하는 파이썬 공부 노트

# 자료형과 문자열 

## 표현식과 문장

파이썬에서는 어떠한 값을 만들어 내는 간단한 코드를 표현식이라고 부릅니다.
표현식이 하나 이상 모이면 문장이 되는데, 파이썬은 한 줄이 하나의 문장이 됩니다.

## 키워드

키워드는 특별한 의미가 부여된 단어로, 파이썬이 만들어질 때 이미 사용하겠다고 예약해 놓은 것입니다.
사용자가 키워드인지 아닌지를 구분해야 하는 이유는 프로그래밍 언어에서 사용자가 이름을 정할 때 키워드를 사용하면 안되기 때문입니다.

파이썬의 키워드를 확인해야 하는 경우 다음 코드로 확인할 수 있습니다.
```python
import keyword
print(keyword.kwlist)
```

## 식별자

식별자는 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어입니다. 주로 변수 또는 함수 이름 등으로 사용됩니다.

식별자는 다음과 같은 규칙을 지켜 만들어야 합니다.

1. 키워드를 사용하면 안 됩니다.
2. 특수 문자는 언더 바만 허용됩니다.
3. 숫자로 시작하면 안 됩니다.
4. 공백을 포함할 수 없습니다.

## 스네이크 케이스와 캐멀 케이스

스네이크 케이스 : 단어 사이에 언더 바 기호를 붙여 식별자를 만듭니다. 
캐멀 케이스 : 단어들의 첫 글자를 대문자로 만들어 식별자를 만듭니다.

### 식별자를 구분하기

파이썬에서는 첫 번째 글자를 소문자로 적는다라는 캐멀 케이스는 사용하지 않습니다.
캐멀케이스로 작성되어 있으면 클래스이며, 스네이크 케이스로 작성되어 있으면 함수 또는 변수입니다.
그리고 뒤에 괄호가 붙어 있으면 함수이고, 괄호가 없으면 변수입니다.

## 주석

주석은 프로그램의 진행에 전혀 영향을 주지 않는 코드로, 프로그램을 설명하기 위해 사용합니다. # 이후의 글자는 주석 처리되어 프로그램에 어떠한 영향도 주지 않습니다.

## 연산자와 자료

연산자는 스스로 값이 되는 것은 아니고 값과 값 사이에 무언가 기능을 적용할 때 사용하는 것을 말합니다. 
자료는 리터럴이라고도 하는데, 숫자이든지 문자이든지 어떠한 값 자체를 의미합니다.

## 출력 print()

현재 무엇을 하는지 알 수 있또록 메시지를 출력하는 기본 방법입니다. print()함수는 다음과 같이 함수의 괄호 안에 출력하고 싶은 것을 나열해서 사용합니다.

## 줄바꿈하기

print 명령의 괄호 안에 아무것도 입력하지 않으면 단순하게 줄바꿈을 합니다.

output.py
```python
# 하나만 출력합니다.

print('# 하나만 출력합니다.')
print("Hello Python Progamming...!!")
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은",)
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 입력하지 않습니다.")
print("--- 확인 전용선 ---")
print()
print()
print("--- 확인 전용선 ---")
```

## 자료형과 기본 자료형

파이썬 프로그램도 수많은 자료를 다룹니다. 구분된 종료를 자료형이라고 부릅니다. 기본적인 자료형으로는 문자열, 숫자, 불이 있습니다.

문자열: 메일 제목, 메시지 내용 등
숫자: 물건의 가격, 학생의 성적 등
불: 친구의 로그인 상태 등


### 자료형 확인하기

자료형이란 자료의 형식을 말합니다. 파이선에서 자료의 형식을 확인할 때는 type()함수를 사용합니다. 

type() 함수를 사용하는 예
```python
print(type("안녕하세요"))
<class 'str'>
print(type(273))
<class 'int'>
```
### 문자열 만들기

프로그래밍 언어에서는 글자들이 나열된 것을 문자열이라고 부릅니다. 문자열은 영어로 string이라고 부릅니다.

큰따옴표, 작은따옴표 둘 다 사용 가능한데 이는 구문 오류를 피하기 위함입니다.

큰따옴표를 문자열 내부에 넣고 싶을 때는 작은따옴표로 문자열을 만들어 주면 됩니다.
```python
print('"안녕하세요"라고 말했습니다')
```

반대로 작은따옴표를 문자열 내부에 넣고 싶을 때는 큰따옴표로 문자열을 만들어 주면 됩니다.
```python
print("'안녕하세요'라고 말했습니다")
```

#### 이스케이프 문자를 사용해 문자열 만들기

이스케이프 문자는 역슬래시 기호와 함께 조합해서 사용하는 특수한 문자를 의미합니다. 
이스케이프 문자를 기호 앞에 사용하면 기호 문자 본연의 의미를 가집니다.

이스케이프를 사용하여 따옴표를 온전하게 사용하는 예
```python
print("\"안녕하세요\"라고 말했습니다")
#"안녕하세요"라고 말했습니다
print('\'안녕하세요\'라고 말했습니다')
#'안녕하세요'라고 말했습니다.
```

이 외에도 다양한 이스케이프 문자가 있습니다.

\n : 줄바꿈을 의미합니다.
\t : 탭을 의미합니다.

이스케이프 문자(\t)로 표 형식을 만드는 예입니다.
```python
print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")
```

## 여러 줄 문자열 만들기

\n 이스케이프 문자를 사용하여 줄바꿈을 하면 한 줄에 긴 코드를 입력했을 때 읽기가 힘들뿐더러 한 줄에 줄바꿈 문자도 많아 어떤 부분에서 줄바꿈이 일어나는지 확인하기 번거롭습니다.
파이썬은 이때 여러 줄 문자열이라는 기능을 지원합니다. 큰따옴표 또는 작은따옴표를 세 번 반복해 입력한 후 문자열을 입력하면 엔터를 누르는 곳 마다 줄바꿈이 일어나 코드를 훨씬 더 쉽게 읽을 수 있습니다.

여러 줄 문자열 """, '''을 사용한 예입니다.
```python
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
대한으로 길이 보전하세""")
```

#### 줄바꿈 없이 문자열 만들기

위와 같이 여러 줄 문자열을 사용하면 첫 번째 줄과 마지막 줄에 의도하지 않은 줄바꿈이 들어가게 됩니다.
이때 따옴표 뒤에 이스케이프 문자를 사용하여 코드를 쉽게 보려고 한 줄바꿈이라는 의미를 주면서 첫 번째줄과 마지막 줄의 의도치 않은 줄바꿈을 없애줄 수 있습니다.

## 문자열 연산

### 문자열 연결 연산자 +

문자열에는 + 기호로 문자열 연산을 적용할 수 있습니다.

다음은 + 문자열 연결 연산자를 사용한 예시 코드입니다.
```python
print("안녕" + "하세요")
#안녕하세요
print("안녕하세요"+"!")
#안녕하세요!
```

문자열은 무조건 문자열끼리 +기호를 사용해야하고 숫자라 하더라도 문자열과 함께 +연산하려면 큰따옴표를 붙여 문자열로 인식시켜야합니다.
숫자를 더할 때는 숫자와 숫자 사이에 + 기호를 사용해서 연산해야 합니다.

### 문자열 반복 연산자 *

문자열을 숫자와 * 연산자로 연결하면 문자열을 반복할 수 있습니다.
다음은 문자열을 숫자와 * 연산자로 연결하여 반복하는 예시 코드입니다.
```python
print("안녕하세요" * 3)
#안녕하세요안녕하세요안녕하세요
```
순서를 바꿔서 숫자 * 문자열과 같이 입력해도 됩니다.

### 문자 선택 연산자(인덱싱): []

문자 선택 연산자는 문자열 내부의 문자 하나를 선택하는 연산자입니다. 이때 대괄호 [] 안에는 선택할 문자의 위치를 지정하며, 이 숫자를 인덱스라고 부릅니다.
인덱스의 유형은 크게 두가지로 0부터 세는 제로 인덱스, 다른 하나는 1부터 세는 원 인덱스로 구분합니다.
파이썬은 제로 인덱스 유형을 사용하는 언어로 문자열의 위치를 셀 때 0부터 세어 주어야 합니다.

다음은 문자 선택 연산자의 결과를 출력하는 코드입니다.
string_operator01.py
```python
print("문자 선택 연산자에 대해 알아봅시다")
print("안녕하세요[0]")
print("안녕하세요[1]")
print("안녕하세요[2]")
print("안녕하세요[3]")
print("안녕하세요[4]")
```

## 문자열 범위 선택 연산자(슬라이싱): [:]

문자열의 특정 범위를 선택할 때 사용하는 연산자도 있습니다. 범위는 대괄호 안에 위치를 콜론으로 구분해서 지정합니다.
뒤의 값을 생략할 때는 자동으로 가장 최대 위치(마지막 글자)까지, 앞의 값을 생략할 때는 가장 앞쪽의 위치(첫 번째 글자)까지 지정합니다.

다음은 문자열 범위 선택자(슬라이싱)을 사용하는 예시코드입니다.
```python
print("안녕하세요"[1:3])
print("안녕하세요"[1:])
print("안녕하세요"[:4])
```

꼭 기억해야 할 것은 문자열 선택 연산자로 슬라이싱을 하더라도 원본은 변하지 않는다는 것입니다.

## IndexError(index out of range) 예외

프로그래밍을 할 때 가장 많이 만나는 예외로 IndexError 예외는 리스트/문자열의 수를 넘는 요소/글자를 선택할 때 발생합니다.

IndexError 예외의 예시 코드입니다.
```python
print("안녕하세요"[10])
```

## 문자열의 길이 구하기

문자열의 길이를 구할 때는 len() 함수를 사용한비다. len()도 식별자 뒤에 괄호가 있으므로 함수 입니다
다음은 len()함수를 사용해서 문자열의 길이(문자의 개수)를 세어주는 예시코드입니다.
```python
print(len("안녕하세요"))
5
```
# 숫자

## 숫자의 종류

숫자를 만들려면 그냥 단순히 숫자를 입력하면 됩니다. print() 함수의 괄호 안에 숫자를 입력하면 숫자를 출력합니다.
소수점이 없는 숫자를 정수형(integer)이라고 하고, 소수점이 있는 숫자를 실수형 또는 부동 소수점(floating point)이라고 합니다.

## 숫자 연산자

사칙 연산자에는 기본적으로 덧셈(+), 뺄셈(-), 곱셉( * ), 나눗셈(/)과 같은 사칙연산자가 있습니다.

## 정수 나누기 연산자 : //

정수 나누기 연산자 //는 숫자를 나누고 소수점 이하의 자릿수를 떼어 버린 후, 정수 부분만 남기는 정수 나누기 연산자입니다.

```python
print("3/2=", 3/2)
3/2 = 1.5
print("3//2=", 3//2)
3//2 = 1
```

## 나머지 연산자 : %

나머지 연산자는 A를 B로 나누었을 때 남은 나머지를 구하는 연산자입니다.
```python
print("5%2 =", 5%2)
5%2 = 1
```

## 제곱 연산자 : **

숫자를 제곱하는 ** 연산자가 있습니다. 2를 4번 곱하는 것을 파이썬에서는 2**4로 씁니다.
```python
print("2**1 = ", 2**1)
2**1 = 2
print("2**2 = ", 2**2)
2**2 = 4
print("2**3 = ", 2**3)
2**3 = 8
print("2**4 = ", 2**4)
2**4 = 16
```

## 연산자의 우선순위

연산자에는 우선순위가 존재합니다. 숫자를 계산할 때는 곱셈과 나눗셈이 덧셈과 뺄셈보다 우선합니다.
먼저 연산하고 싶은 부분은 괄호로 감싸주는 데 연산자 우선순위가 확실한 경우에도 괄호로 감싸 주는 것이 좋습니다.

## TypeError 예외

문자열과 숫자를 + 연산자로 연결한 예시입니다.
```python
string = "문자열"
number = 273
string + number
```

문자열은 + 연산자를 '문자열 연결 연산자'로 사용하려고 하고, 숫자는 + 연산자를 '덧셈 연산자'로 사용하려다 보니 충돌이 발생합니다.


# 변수와 입력

변수는 값을 저장할 때 사용하는 식별자입니다. pi라는 이름의 상자(저장 공간)을 만든 후, pi 상자 내부에 값을 넣어 놨다가 필요할 때 이를 호출하여 사용합니다. 이때 pi를 '변수'라고 하며 숫자뿐만 아니라 모든 자료형을 저장할 수 있습니다.

## 변수 만들기/사용하기

1. 변수를 선언하는 방법

변수를 생성하는 것을 의미합니다. pi를 '사용하겠다'라고 선언하는 것을 말합니다.

2. 변수에 값을 할당하는 방법

변수에 값을 넣는 것을 의미합니다. pi=3.14159265 이때 = 기호는 '같다'는 의미가 아니라 우변의 값을 좌변에 '넣겠다', '할당하겠다'를 의미합니다.

3. 변수를 참조하는 방법

변수에서 값을 꺼내는 것을 의미합니다. 변수 안에 있는 값을 사용하는 것을 '변수 참조'라고 합니다.

다음은 pi라는 변수를 선언하고 이를 참조하는 방법을 사용해 원의 둘레와 넓이를 구하는 코드입니다.

variable.py
```python
# 변수 선언과 할당

pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r) # 원의 둘레
print("원의 넓이 =", pi*r*r) # 원의 넓이
```

## 파이썬의 유연성

C, C++, JAVA, C# 등에서는 기본적으로 변수를 사용할 때 변수의 자료형을 미리 선언해줘야 합니다. 하지만 파이썬은 다른 프로그래밍 언어와는 다르게 변수에 자료형을 지정하지 않습니다. 
유연해서 좋다고 말할 수도 있지만, 이러한 유연성 때문에 변수에 어떠한 자료형이 들어 있는지 모르고 실수해서 실행 중에 TypeError를 발생할 확률이 높습니다. 그러므로 하나의 변수에는 되도록 하나의 자료형을 넣어 활용하는 것이 좋습니다.

## 복합 대입 연산자

변수를 활용하면 기존의 연산자와 조합해서 사용할 수 있는 연산자가 있는데 이를 복합 대입 연산자라고 합니다.
복합 대입 연산자는 자료형에 적용하는 기본 연산자와 = 연산자를 함께 사용해 다음과 같이 구성하는 연산자입니다.

복합 대입 연산자의 예

+= : 숫자 덧셈 후 대입
-= : 숫자 뺄셈 후 대입
\*= : 숫자 곱셈 후 대입
/= : 숫자 나눗셈 후 대입
%= 숫자의 나버지를 구한 후 대입
\*\*= : 숫자 제곱 후 대입

다음은 number 변수에 숫자 100을 할당하고 10, 20, 30을 덧셈 복합 대입 연산자를 사용하는 예시 코드입니다.
```python
number = 100
number += 10 # number = number + 10 결과 : 110
nubmer += 20 # number = number + 20 결과 : 130
number += 30 # number = number + 30 결과 : 160
print("number =", number)
number= 160
```

다음은 문자열 복합 대입 연산자를 활용한 예시 코드입니다.
```python
string = "안녕하세요"
string += "!"
string += "!"
print("string =", string)
string = 안녕하세요!!!
```
## 사용자 입력 : input()

실무에서 프로그램을 만들 때는 명령 프롬프트에 글자를 입력하고 그 입력을 읽어 활용하는 경우가 드물지만, 프로그램을 공부하는 과정에서는 사용자로부터 입력을 받아 여러 가지 프로그램을 만들어 보는 것이 좋습니다. 파이썬은 명령 프롬프트에서 사용자로부터 데이터를 입력받을 때 input()함수를 사용합니다.

## input() 함수로 사용자 입력받기

사용자로부터 데이터를 입력받기 위해 다음 코드를 입력합니다. 이때 input 함수 괄호 안에 입력한 내용을 프롬프트 문자열이라고 하며, 사용자로부터 입력을 요구하는 안내 내용을 포함합니다.

```python
input("인사말을 입력하세요> ")
```
실행하면 다음과 같이 "인사말을 입력하세요> "라는 문자열이 뜨고 프로그램이 종료되지 않은 상태에서 대기가 됩니다. 이렇게 프로그램이 실행 도중에 잠시 멈추는 것을 블록이라고 하는데, input()함수가 사용자에게 자료 입력을 요구하면서 코드 진행을 블록하고 있다고 할 수 있습니다.

사용자가 입력한 내용은 input 함수의 결과로 나오는데, 이 값은 다른 변수에 대입해서 사용할 수 있습니다. print() 함수를 사용해서 변수에 제대로 대입되었는지 확인하는 코드입니다.
```python
string = input("인사말을 입력하세요>")
인사말을 입력하세요> 안녕하세요 enter키 
print(string)

안녕하세요
```

## input() 함수의 입력 자료형

앞서 input()함수의 결과를 string이라는 변수에 대입했는데, 자료형을 알아볼 때는 type()함수를 사용합니다.

```python
string = "안녕하세요"
print(type(string))
<class 'str>
```
string 변수에는 "안녕하세요"라는 문자열을 입력해 대입했으니 다영히 자료형도 문자열입니다.

다음은 숫자를 입력하고 숫자를 출력하는 코드입니다.
```python
number = input("숫자를 입력하세요>)
숫자를 입력하세요> 12345 enter키 입력
print(number)
12345
```

그렇다면 입력받은 number의 자료형은 어떻게 될까요
```python
print(type(nubmer))
<class 'str'>
```

input()함수는 사용자가 무엇을 입력해도 결과는 무조건 문자열 자료형입니다. number에 대입한 12345도 'str'로 확인이 되는 것을 알 수 있습니다.

## 문자열을 숫자로 바꾸기

input()함수의 입력 자료형은 항상 문자열이기 때문에 입력받은 문자열을 숫자로 변환해야 숫자 연산에 활용할 수 있습니다. 영어로는 캐스트 cast 라고 하는데, 영어로도 자주 언급되므로 기억하는 게 좋습니다.

문자열을 숫자 자료형으로 변환해야 하는 경우는 매우 많습니다. 예를 들어, 파이썬을 사용해 인터넷에서 환율 정보를 가져온다고 합시다. 이때도 인터넷에 있는 글자는 모두 문자열이므로 숫자로 변환해야 활용할 수 있습니다.

문자열을 숫자로 변환할 때는 다음과 같은 함수를 사용합니다.

int()함수 : 문자열을 int자료형으로 변환합니다. int는 정수를 의미합니다.
float()함수 : 문자열을 float자료형으로 변환합니다. float는 실수 또는 부동 소수점을 의미합니다.

int()함수 활용하는 예시 코드입니다.

int_convert.py
```python
string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)
```

int()함수와 float()함수 활용하기

int_float01.py
```python
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)
```

## ValueError 예외

첫째, 숫자가 아닌 것을 숫자로 변환하려고 할 때

int("안녕하세요")
float("안녕하세요")

이와 같은 코드를 실행하면 곧바로 예외가 발생합니다. "안녕하세요"라는 문자열은 int() 함수로 변환할 수 없는 값이기 때문입니다. int() 함수와 float() 함수는 매개변수로 변환할 수 없는 형태가 들어가면 항상 오류를 발생시킵니다.

둘째, 소수점이 있는 숫자 형식의 문자열을 int()함수로 변환하려고 할 때

int("52.273")

int는 정수인데, 부동 소수점이 있는 자료를 정수로 바꾸라고 하면 이 또한 에러를 발생합니다.

## 숫자를 문자열로 바꾸기

문자열을 숫자로 변환하는 것처럼 숫자를 문자열로 변환하는 것도 가능합니다. 사실 문자열로 변환하는 방법은 매우 다양합니다. 여기서는 str()함수를 사용하는 방법을 살펴보겠습니다.
str()함수는 앞서 했던 int()함수 그리고 float() 함수와 비슷한 형태를 가집니다. 즉 다른 자료형의 값을 str()함수의 매개변수에 넣으면 문자열로 변환됩니다.

str(다른 자료형)

다음은 str()함수를 사용해 숫자를 문자열로 변환하는 예시코드입니다.

str.py
```python
output_a = str(52)
output_b = str(52.273)
print(type(output_a), output_a)
print(type(output_b), output_b)
```

# 숫자와 문자열의 다영한 기능

## 문자열의 format() 함수

format() 함수로 숫자를 문자열로 변환하는 몇 가지 형태를 살펴보겠습니다.

format() 함수는 문자열이 가지고 있는 함수입니다. 중괄호 {}를 포함한 문자열 뒤에 마침표(.)를 찍고 format() 함수를 사용하는 데, 중괄호의 개수와 format 함수 괄호 안 매개변수의 개수는 반드시 같아야합니다.

"{}".format(10)
"{} {}".format(10, 20)
"{} {} {} {}".format(101, 202, 303, 404, 505)

이러한 형태로 함수를 사용하면 앞쪽에 있는 문자열의 {} 기호가 format() 함수 괄호 안에 있는 매개변수로 차례로 대치되면서 숫자가 문자열이 되는 것입니다. 즉 아래의 예시에서 10은 문자열의 중괄호 부분에 들어가 숫자 10이 문자열 "10"이 되는 것입니다.

다음은 format() 함수로 숫자를 문자열로 변환하는 예시코드입니다.

format_basic.py
```python
  # format() 함수로 숫자를 문자열로 변환하기
string_a = "{}".format(10)

# 출력하기
print(string_a)
print(type(string_a))   
```

다음은 {} 기호 양쪽에 다른 문자열을 같이 넣은 형태, {} 기호와 매개변수를 여러개 넣은 형태를 실행해보겠습니다.

format01.py
```python
# format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

# 출력하기
print(format_a) 
print(format_b)
print(format_c)
print(format_d)
```

## IndexError 예외

{} 기호의 개수가 format() 함수의 매개변수 개수보다 많으면 IndexError 예외가 발생합니다. 아래의 예시에서 첫 번째는 매개변수가 {}보다 많은  경우로 {} 개수만큼 적용되고 나머지 매개변수는 버려져 아무 문제 없이 실행됩니다. 두 번째는 {}가 매개변수보다 많은 경우로 IndexError 예외가 발생합니다.

```python
"{} {}".format(1, 2, 3, 4, 5)
'1 2'
"{} {} {}".format(1, 2)
>IndexError 발생
```

## format() 함수의 다양한 기능

정수 출력의 다양한 형태

정수를 특정 칸에 출력하기

format02.py
```python
# 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)  # 5칸
output_c = "{:10d}".format(52)  # 10칸

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)  # 양수
output_e = "{:05d}".format(-52)  # 음수

print("# 기본")
print(output_a)
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
```

다음은 기호를 붙여 출력하는 예시코드입니다.

format03.py
```python
# 기호와 함께 출력하기
output_f = "{:+d}".format(52)  # 양수
output_f = "{:+d}".format(-52)  # 음수
output_f = "{: d}".format(52)  # 양수: 기호 부분 공백
output_f = "{: d}".format(-52)  # 음수: 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
```

기호와 공백을 조합할 때는 = 기호를 앞에 붙일 수 있습니다. 이는 5칸의 공간을 잡았을 때 기호를 빈칸 앞에 붙일 것인지, 숫자 앞에 붙일 것인지 지정하는 기호입니다.

format04.py
```python
output_h = "{:+5d}".format(52)  # 기호를 뒤로 밀기: 양수
output_i = "{:+5d}".format(-52)  # 기호를 뒤로 밀기: 음수
output_j = "{:=+5d}".format(52)  # 기호를 뒤로 밀기: 양수
output_k = "{:=+5d}".format(-52)  # 기호를 뒤로 밀기: 음수
output_l = "{:+05d}".format(52)  # 0으로 채우기 : 양수
output_m = "{:+05d}".format(-52)  # 0으로 채우기 : 음수

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
```

## 부동 소수점 출력의 다양한 형태

일단 float 자료형 출력을 강제로 지정할 때는 {:f}를 사용하고 이전에 살펴보았 던 형태들을 적용할 수 있습니다.

format05.py
```python
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)  # 15칸 만들기
output_c = "{:+15f}".format(52.273)  # 15칸에 부호 추가하기
output_d = "{:+015f}".format(52.273)  # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)
```

소수점 아래 자릿수를 지정하는 예시코드입니다.

format06.py
```python
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
```

15칸을 잡고 소수점을 각각 3자리, 2자리, 1자리로 출력합니다. 이때 자동으로 반올림도 일어납니다.

## 의미없는 소수점 제거하기

0.0과 0을 출력했을 때 내부적으로 자료형이 다르므로 서로 다른 값으로 출력합니다. 의미 없는 0을 제거한 후 출력하고 싶을 때 {:g} 를 사용합니다.

format07.py
```python
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)
```

## 대소문자 바꾸기 : upper() 와 lower()

upper()함수는 문자열의 알파벳을 대문자로, lower()함수는 문자열의 알파벳을 소문자로 만듭니다.

a = "Hello Python Programming ...!"
a.upper()
'HELLO PYTHON PROGRAMMING ...!
a.lower()
'hello python programming ...!

이 때 upper(), lower() 함수는 원본을 변하시키지 않는 비파괴적 함수입니다.

## 문자열 양옆의 공백 제거하기 : strip()

strip() 함수는 문자열 양옆의 공백을 제거합니다. 왼쪽의 공백을 제거하는 lstrip() 함수와 오른쪽의 공백을 제거하는 rstrip()함수도 있습니다. 이때 공백이란 "띄어쓰기", "탭", "줄바꿈" 모두를 포합합니다.

큰따옴표 또는 작은따옴표를 세 번 반복한 기호는 여러 줄 문자열을 입력할 때 사용하는 것으로 이때 의도치 않는 줄바꿈이 들어갑니다. 이때 strip() 함수를 사용해서 쉽게 제거 할 수 있습니다.

이렇게 strip()함수를 사용하여 공백 제거를 하는 기능을 trim이라고도 부릅니다. 공백을 제거할 때는 strip 또는 trim을 활용한다고 기억하는게 좋습니다.

## 문자열의 구성 파악하기 : isOO()

문자열이 소문자로만 구성되있는지 알파벳으로만 구성되어있는지 숫자로만 구성되어있는지 등을 확인할 때는 is로 시작하는 이름의 함수를 사용합니다.

isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어있는지 확인합니다.
isalpha() : 문자열이 알파벳만으로만 구성되어 있는지 ~
isidentifier() : 문자열이 식별자로 사용할수 ~
isdecimal() : 문자열이 정수 형태인지 확인합니다.
isdigit() : 문자열이 숫자로 인식될 수 ~
isspace() : 문자열이 공백으로만 ~
islower() : 문자열이 소문자로만 ~
isupper() : 문자열이 대문자로만 ~

## 문자열 찾기 : find()와 rfind()

문자열 내부에 특정 문자가 어디에 위치하는 지 확인할 때 find()함수와 rfind() 함수를 사용합니다.

find() : 왼쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.

output_a = "안녕안녕하세요".find("안녕")
print(output_a)
0

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
2

## 문자열과 in 연산자

문자열 내부에 어떤 문자열이 있는지 확인하려면 in 연산자를 사용합니다. 출력은 True(맞다) 또는 False(아니다)라고 나옵니다.
print("안녕" in "안녕하세요")
True

print("잘자" in "안녕하세요")
False

## 문자열 자르기 : split()

문자열을 특정한 문자로 자를 때 split()함수를 사용합니다. split 함수 괄호 안의 문자열인 공백(띄어쓰기)을 기준으로 자릅니다

a = "10 20 30 40 50".split(" ")
print(a)
['10', '20', '30', '40', '50' ]

실행결과로 리스트가 나옵니다

# 불 자료형과 if 조건문

## 불 만들기 : 비교 연산자

Boolean은 불린 또는 불리언이라는 발음으로 부릅니다. 불은 오직 True(참)과 False(거짓) 값만 가질 수 있습니다.
불은 비교 연산자를 통해 만들 수 있습니다. 

== : 같다
> : 크다
!= : 다르다
<= : 작거나 같다
< : 작다
>= : 크거나 같다

비교 연산자는 숫자 또는 문자열에 적용할 수 있습니다.

다음은 숫자의 대소 비교를 비교연산자를 이용하는 예시 코드입니다.
```python
print(10 == 100)
False
print(10 != 100)
True
print(10 < 100)
True
print(10 > 100)
False
print(10 <= 100)
True
print(10 >= 100)
False
```

파이썬은 문자열에도 비교 연산자를 적용할 수 있습니다. 
다음은 문자열의 비교 연산자를 이용하는 예시 코드입니다.
```python
print("가방" === "가방")
True
print("가방" != "하마")
False
print("가방" < "하마")
True
print("가방" > "하마")
False
```

가방과 하마를 비교하면 사전 순서로 가방이 앞에 있으므로 가방이 하마보다 작은 값을 갖습니다.

파이썬은 다음과 같은 코드를 사용해 변수의 범위 등도 구할 수 있습니다.
```python
x = 25
print(10 < x < 30)
True
print(40 < x < 60)
False
```

## 불 연산하기 : 논리 연산자

불끼리는 논리 연산자를 사용할 수 있습니다.
다음과 같은 세 개의 논리 연산자가 있습니다.

not 아니다 : 불을 반대로 전환합니다.
and 그리고 : 피연산자 두 개가 모두 참일 때 True를 출력하며, 그 외는 모두 False를 출력합니다.
or 또는 : 피연산자 두 개 중에 하나만 참이라도 True를 출력하며, 두 개가 모두 거짓일 때만 False를 출력합니다.

## not 연산자

not 연산자는 단항 연산자로, 참과 거짓을 반대로 바꿀 때 사용합니다. 실행하면 단순하게 True와 False가 서로 바뀝니다.

print(not True)
False
print(not False)
True

not 연산자 조합하는 예시코드입니다.

boolean.py
```python
x = 10
under_20 = x < 20
print("under_20:", under_20)
print("not under_20", not under_20)
```

## and 연산자와 or 연산자

and 연산자는 양쪽 변의 값이 모두 참 일때만 True를 결과로 냅니다.

반면 or 연산자는 둘 중 하나만 참이어도 True를 결과로 냅니다.

다음은 and와 or 연산자를 공부하는 예시코드입니다.
```python
print(True and True)
True
print(True and False)
False
print(False and True)
False
print(False and False)
False
print(True or True)
True
print(True or False)
True
print(False or True)
True
print(False or False)
False
```

## if 조건문이란?

if 조건문은 조건에 따라 코드를 실행하거나, 실행하지 않게 만들고 싶을 때 사용하는 구문입니다. 이는 코드의 실행 흐름을 변경한다는 뜻입니다. 이렇게 조건을 기반으로 실행의 흐름을 변경하는 것을 조금 어려운 용어로 조건 분기라고 부릅니다.

if 조건문의 기본적인 구조는 다음과 같습니다.

if 불 값이 나오는 표현식: 
    불 값이 참일 때 실행할 문장
    불 값이 참일 때 실행할 문장
    
다음은 if문을 사용하여 양수를 입력하면 "양수입니다"를, 음수를 입력하면 "음수입니다"를, 0을 입력하면 "0입니다"를 출력하는 예시코드입니다.
```python
# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 양수 조건
if number > 0:
    print("양수입니다.")

# 음수 조건
if number < 0:
    print("음수입니다.")

# 0 조건
if number == 0:
    print("0입니다.")
```

## 날짜/시간 활용하기

여러 가지 조건문 중 몇 가지를 더 살펴보겠습니다. 
먼저 시간을 조건으로 구분하여 오전인지 오후인지를 출력하는 프로그램을 작성해 보겠습니다.

다음은 날짜/시간을 출력하는 예시코드입니다.
```python
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
```

이전에 배웠던 format() 함수를 활용하여 날짜를 한눈에 볼 수 있게 출력하는 예시 코드입니다.
```python
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print("{}년 {}월 {}일 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.minute,
    now.second
))
```

다음은 오전과 오후를 구분하는 프로그램의 예시코드입니다.

```python
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

# 오후 구분
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))
```

다음은 계절을 구분하는 프로그램의 예시코드입니다.

```python
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

# 여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))
xx`
    print("이번 달은 {}월로 가울입니다!".format(now.month))

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
```

다음은 끝자리로 짝수와 홀수 구분하는 프로그램의 예시 코드입니다.

```python
# 입력을 받습니다.
number = input("정수 입력> ")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

# 짝수 확인
if last_number == 0 \
        or last_number == 2 \
        or last_number == 4 \
        or last_number == 6 \
        or last_number == 8:
    print("짝수입니다.")

# 홀수 확인
if last_number == 1 \
        or last_number == 3 \
        or last_number == 5 \
        or last_number == 7 \
        or last_number == 9:
    print("홀수입니다.")
```

다음은 in 문자열 연산자를 활용해서 짝수와 홀수 구분하는 프로그램의 예시코드입니다.

```python
# 입력을 받습니다.
number = input("정수 입력> ")
last_character = number[-1]

# 짝수 조건
if last_character in "02468":
    print("짝수입니다.")

# 홀수 조건
if last_character in "13579":
    print("홀수입니다.")
```

다음은 나머지 연산자를 활용해서 짝수와 홀수 구분하는 프로그램의 예시코드입니다.
```python
# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 짝수 조건
if number % 2 == 0:
    print("짝수입니다.")

# 홀수 조건
if number % 2 == 1:
    print("홀수입니다.")
```

# if~else와 elif 구문

정반대되는 상황에서 두 번이나 조건을 비교해야 하는 것을 프로그램의 관점에서 봤을 때 낭비라고 할 수 있습니다.

## else 조건문의 활용

파이썬은 else 구문이라는 기능을 제공합니다. else 구문은 if 조건문 뒤에 사용하며, if 조건문의 조건이 거짓일 때 실행되는 부분입니다.

if 조건 :
    조건이 참일 때 실행할 문장
else:
    조건이 거짓일 때 실행할 문장
    
다음은 if 조건문에 else 구문을 추가해서 짝수와 홀수를 구분하는 프로그램의 예시코드입니다.
```python
# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 조건문을 사용합니다.
if number % 2 == 0:
    # 조건이 참일 때, 즉 짝수 조건
    print("짝수입니다.")
else:
    # 조건이 거짓일 때, 즉 홀수 조건
    print("홀수입니다.")
```

조건이 오로지 두 가지로만 구분될 때 if else 구문을 사용하면 조건 비교를 한 번만 하므로 이전의 코드보다 두 배 효율적이라고 할 수 있습니다. 사실 간단한 프로그램에서는 이런 차이가 크지 않지만 조건 비교를 100만 번, 100억 번 저이도 한다고 가정하면 시간 차이가 크게 발생합니다.

## elif 구문

그런데 딱 두가지만으로 구분되지 않는 것도 있습니다. 예를 들어 계절만 해도 네 개가 있으며, 요일만 해도 일곱 개가 있습니다. 따라서 세 개 이상의 조건을 연결해서 사용하는 방법이 필요합니다. 그것이 바로 elif 구문입니다.

elif 구문은 if 조건문과 else 구문 사이에 입력하며, 다음과 같은 형태로 사용합니다.

if 조건A:
    조건A가 참일 때 실행할 문장
elif 조건B:
    조건B가 참일 때 실행할 문장
elif 조건C:
    조건C가 참일 때 실행할 문장
else:
    모든 조건이 거짓일 때 문장
    
다음은 현재 월을 구하고 이를 기반으로 계절을 구하는 elif 구문을 사용한 프로그램의 예시코드입니다.
```python
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구하고
# 쉽게 사용할 수 있게 월을 변수에 저장합니다.
now = datetime.datetime.now()
month = now.month

# 조건문으로 계절을 확인합니다.
if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")
```

## False로 변환되는 값

if 조건문이 매개변수에 불이 아닌 다른 값이 올 때는 자동으로 이를 불로 변환해서 처리합니다. 따라서 어떤 값이 True로 변환되고, 어떤 값이 False로 변환되는지 알고 있어야 코드를 이해할 수 있습니다. False로 변환되는 값은 None, 숫자 0과 0.0 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)입니다. 이 외에는 모두 True로 변환되므로 위에 언급한 세 가지만 기억하세요.

False로 변환되는 값들의 예시코드입니다.
```python
print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 반환됩니다.")
else:
    print("0은 False로 반환됩니다.")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("0은 True로 반환됩니다.")

else:
    print("0은 False로 반환됩니다.")
```

## pass 키워드

프로그래밍을 하다 보면 일단 프로그래밍의 전체 골격을 잡아 놓고 내부에서 처리할 내용은 차근차근 생각하며 만들겠다는 의도로 다음과 같이 코딩하는 경우가 많습니다. 이때 골격은 일반적으로 조건문, 반복문, 함수, 클래스 등의 기본 구문을 말합니다.

다음은 나중에 구현하려고 비워 둔 구문의 예시 코드입니다.

```python
# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때 : 아직 미구현 상태입니다.
else:
    # 음수일 때 : 아직 미구현 상태입니다.
```

다른 프로그래밍 언어에서는 위와 같이 아무 내용을 작성하지 않아도 실행이 정상적으로 되지만, 파이썬의 경우에는 if 조건문 사이에는 무조건 들여쓰기 4칸을 넣고 코드를 작성해야만 구문이 성립되기 때문에 위와 같이 작성한 경우에는 IndentationError를 발생합니다.

IndentationError는 '들여쓰기가 잘못되어 있다'라는 의미인데 그렇기 때문에 if 구문 사이에는 어떤 내용이라도 넣어 줘야 합니다. 다음과 같이 0을 넣어도 일단 실행은 정상적으로 됩니다.

if number > 0:
    0
else:
    0

하지만 이렇게 0을 넣어놓은 상태의 코드를 다른 개발자들이 보면 "왜 0이 있지?"라고 이상하게 생각할 수 있습니다. 그래서 파이썬에서는 이러한 고민을 덜어주기 위해 pass라는 키워드를 제공합니다. 코드를 살펴보던 중 pass 키워드를 만나면 "진짜 아무것도 안함" 또는 "곧 개발하겠음" 이라는 의미로 생각하면 됩니다.

다음은 pass 키워드를 사용한 미구현 부분 입력을 하는 프로그램의 예시코드입니다.
```python

number = input("정수 입력> ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때 : 아직 미구현 상태입니다.
    pass
else:
    # 음수일 때 : 아직 미구현 상태입니다.
    pass
```

## raise NotImplementedError

pass 키워드를 입력해 놨어도 내일이면 잊어버리는 경우가 많습니다. 이후에 배우는 raise 키워드와 미구현 상태를 표현하는 NotImplementedError를 조합해 raise NotImplementError를 사용하면 "아직 구현하지 않은 부분이에요!"라는 오류를 강제로 발생시킬 수 있습니다.

다음은 raise NotImplementError 키워드를 사용하여 강제로 오류를 발생시키는 프로그램의 예시코드입니다.
```python
# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때 : 아직 미구현 상태입니다.
    raise NotImplementedError
else:
    # 음수일 때 : 아직 미구현 상태입니다.
    raise NotImplementedError
    
  
