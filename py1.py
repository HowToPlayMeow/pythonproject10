try :
    num1 = int(input('ตัวเลขตัวที่ 1 :'))
    num2 = int(input('ตัวเลขตัวที่ 2 :'))

    sum = num1 + num2
    result = num1 / num2

    print(f'ผลรวมของ {num1} + {num2} คือ {sum}')
    print(f'ผลรวมของ {num1} / {num2} คือ {result}')

except ValueError :
    print('ใส่ตัวเลขเท่านั้นห้ามใส่ตัวอักษร')

except ZeroDivisionError :
    print(f'ผลรวมของ {num1} + {num2} คือ {sum}')
    print('หาค่าตอบไม่ได้')

except Exception :
    print('มีข้อพลาดเกิดขึ้น')

finally :
    print('wow...')
    print('meow...')