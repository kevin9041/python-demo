

try:
    # file_obj = open('demo.txt','a+',encoding='utf-8')
    # content = file_obj.read()
    # print('content:',content)
    
    with open('demo.txt','r',encoding='utf-8') as file_obj:
        content = file_obj.read()
        print(content)
except Exception as e:
    print("报错了====》",e)
else:
    print("程序结束")
finally:
    pass
    # print("别忘了关闭文件！")
    # file_obj.close()