# grade_checker.py
def main():
    try:
        score = float(input("请输入一个分数："))
        if score < 0 or score > 100:
            print("分数必须在0-100之间")
            return
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        else:
            grade = 'C'
        print(f"等级为: {grade}")
    except ValueError:
        print("输入无效，请输入下一个数字")


if __name__ == "__main__":
    main()
