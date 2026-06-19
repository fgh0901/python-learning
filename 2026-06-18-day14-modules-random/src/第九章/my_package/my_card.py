cards = []

def menu():
    print('*'*30)
    print("""欢迎使用名片管理系统
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统""")
    print('*' * 30)

def new_card(name,phone,qq,email):
    user = {
        'name':name,
        'phone':phone,
        'qq':qq,
        'email':email
    }
    cards.append(user)
    return True


def show_card():
    for card in cards:
        print(card)

def query_card(kw):
    for card in cards:
        for k,v in card.items():
            if kw == v:
                return card
    return False
def modify_card(result):
    for card in cards:
        if card == result:
            card['name'] = input("请输入姓名：")
            card['phone'] = input("请输入电话：")
            card['qq'] = input("请输入qq：")
            card['email'] = input("请输入邮箱：")

def delete_card():
    pass

def quit():
    print("欢迎下次使用")



def main():
    menu()
    while True :
        op = input("请输入你的操作序号:")
        if op == '1':
            name = input("请输入姓名：")
            phone = input("请输入电话：")
            qq = input("请输入qq：")
            email = input("请输入邮箱：")
            result = new_card(name,phone,qq,email)
            if result:
                print("添加成功")
            else:
                print("请重试")
        elif op == '2':
            show_card()
        elif op =='3':
            kw = input("请输入查询的关键字")
            result = query_card(kw)
            if result:
                print(result)
                op2 = input("输入4修改名片，输入5删除名片")
                if op2 == '4':
                    modify_card(result)
                elif op2 == '5':
                    delete_card()

            else:
                print("查无此人")
        elif op == '0':
            quit()
            break
        else:
            print("请输入一个数字，在0-3之间")