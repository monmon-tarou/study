"""
1から100までの間の素数を出力する.
"""

print("1から100までの素数を出力します")

limit = 100
# 上限値を設定

for num in range(2, limit + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime == True:
        print(num)
