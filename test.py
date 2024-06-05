import random as rd
import string

def display(count):
    if count < 5:
        eva = "Great!"
    elif count <10:
        eva = "Good!"
    else:
        eva = "Bad"
    
    print(eva,"正解")
    return

print("*数当てゲームor文字当てゲーム*")
print("ゲームを選択してください")

while True:
    game=input("(a)数当てゲーム  (b)文字当てゲーム")
    if game=="a":
        print("1-100の数を入力してください。end入力で終了です")

        ans =rd.randint(1,100)

        count = 0
        while True:
            num = input("数字を入力して下さい")
            if num == "end":
                break
            num = int(num)
            if(num<ans):
                print("もっと大きいです")
            elif ans<num:
                print("もっと小さいです")
            elif ans==num:
                display(count)
                break
            else:
                print("error")
            count=count+1

    elif game=="b":
        print("a-zの数を入力してください。end入力で終了です")

        ans =rd.choice(string.ascii_lowercase)

        count = 0
        while True:
            char = input("文字を入力して下さい")
            if char == "end":
                break

            if(char<ans):
                print("もっと大きいです")
            elif ans<char:
                print("もっと小さいです")
            elif ans==char:
                display(count)
                break
            else:
                print("error")
            count=count+1
    else:
        print("error")
    break

 