def sum_for(n: int) -> int:
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def sum_formula(n: int) -> int:
    return n * (n + 1) // 2

def main():
    text = input("请输入正整数 n：").strip()
    if not text.isdigit():
        print("请输入正整数，例如 100")
        return
    n = int(text)
    s1 = sum_for(n)
    s2 = sum_formula(n)
    print(f"for 循环：1..{n} 的和 = {s1}")
    print(f"公式法 ：1..{n} 的和 = {s2}")
    print("两种方法一致吗？", "是" if s1 == s2 else "否")

if __name__ == "__main__":
    main()
