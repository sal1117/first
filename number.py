import random

secret = random.randint(1, 100)
tries = 0

print("1부터 100 사이의 숫자를 맞혀보세요!")

while True:
    guess = int(input("입력: "))
    tries += 1

    if guess < secret:
        print("너무 작아요!")
    elif guess > secret:
        print("너무 커요!")
    else:
        print(f"정답입니다! 시도 횟수: {tries}")
        break
