def parse_float(text: str) -> float:
    """把用户输入转成 float，并在失败时抛出 ValueError。"""
    try:
        return float(text.strip())
    except ValueError as e:
        raise ValueError("请输入数字，例如 3 或 2.5") from e

def compute(a: float, op: str, b: float) -> float:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("除数不能为 0")
        return a / b
    else:
        raise ValueError("不支持的运算符，只能是 + - * /")

def main():
    print("简单计算器：支持 + - * /，输入 q 退出。")
    while True:
        op = input("运算符 (+ - * /)，或 q 退出：").strip()
        if op.lower() == "q":
            print("已退出计算器。")
            break
        a_str = input("第一个数：")
        b_str = input("第二个数：")
        try:
            a = parse_float(a_str)
            b = parse_float(b_str)
            result = compute(a, op, b)
            print(f"结果：{a} {op} {b} = {result}")
        except Exception as exc:
            print(f"错误：{exc}")

if __name__ == "__main__":
    main()
