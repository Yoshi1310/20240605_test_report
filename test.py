import random as rd

def display(count):
    if count < 5:
        eva = "Great!"
    elif count <10:
        eva = "Good!"
    else:
        eva = "Bad"
    
    print(eva,"正解")
    return

print("*数当てゲーム*")
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
 