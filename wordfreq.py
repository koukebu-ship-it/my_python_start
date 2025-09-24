# wordfreq.py
from collections import Counter
import argparse
import re
import sys
from typing import List

STOPWORDS = {
    "a", "an", "the", "is", "am", "are", "was", "were", "be", "been", "being",
    "and", "or", "but", "of", "to", "in", "on", "for", "with", "as", "by",
    "at", "from", "that", "this", "it", "its", "into", "than", "then", "so"
}

def tokenize(text: str) -> List[str]:
    text = text.lower()
    # 只保留 英文和数字，其他当分隔符
    text = re.sub(r"[^a-z0-9]+", " ", text)
    tokens = [t for t in text.split() if t and t not in STOPWORDS]
    return tokens

def main():
    parser = argparse.ArgumentParser(description="统计文本词频")
    parser.add_argument("--file", "-f", help="输入文件路径")
    parser.add_argument("--text", "-t", help="直接输入一段文本")
    parser.add_argument("--top", type=int, default=10, help="显示前 N 个高频词（默认 10）")
    parser.add_argument("--debug", action="store_true", help="打印调试信息")
    args = parser.parse_args()

    if not args.file and not args.text:
        print("请使用 --file 或 --text 提供输入。示例：python wordfreq.py --text 'Hello world'")
        sys.exit(1)

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"读取文件失败：{e}")
            sys.exit(1)
    else:
        text = args.text

    tokens = tokenize(text)
    if args.debug:
        print(f"[DEBUG] args.top = {args.top}")
        print(f"[DEBUG] 原始文本长度 = {len(text)}")
        print(f"[DEBUG] tokens = {tokens}")

    counter = Counter(tokens)
    for word, cnt in counter.most_common(args.top):
        print(f"{word}\t{cnt}")

if __name__ == "__main__":
    main()
