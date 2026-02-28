"""
自動販売機.
"""
items = {
    "コーラ": 120,
    "お茶": 100,
    "水": 80
}

# 入金処理
money = int(input("お金を入れてください: "))

# 商品一覧表示
print("\n商品一覧:")
for name, price in items.items():
    print(f"{name}: {price}円")

# 商品選択
choice = input("\n購入する商品名を入力してください: ")

# 購入処理
if choice not in items:
    print("その商品はありません。")
else:
    price = items[choice]
    if money >= price:
        change = money - price
        print(f"\n{choice} を購入しました！")
        print(f"お釣りは {change} 円です。")
    else:
        print("\nお金が足りません。")
