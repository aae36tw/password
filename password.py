password = 'a123456'

x = 3

while True:
    pwd = input('請輸入密碼')
    if pwd == password:
        print('登入正確')
        break
    else:
        x = x - 1
        print('登入錯誤，還剩', x, '次機會')
        if x == 0:
            break
