try :
    f_iot = open('iot2.txt','a',encoding='utf-8')
    f_iot.write('111\n')
    f_iot.write('222\n')
    f_iot.write('333\n')

    f_iot.close()
    
except FileExistsError :
    print('กรุณาเปลี่ยนชื่ิไฟล์ใหม่')
