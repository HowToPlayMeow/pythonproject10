try :
    f_iot = open('iot2.txt','x',encoding='utf-8')
    f_iot.write('meow')
    f_iot.write(':3\n')
    f_iot.write('ดีฮะ\n')

    f_iot.close()
    
except FileExistsError :
    print('กรุณาเปลี่ยนชื่ิไฟล์ใหม่')
