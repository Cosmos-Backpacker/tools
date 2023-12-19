"""使用须知：文件名必须带有.zip"""
import shutil
import os
import time
print("本程序用法：请将所有带有.zip后缀的文件放在同一个文件夹下，且不能隐藏后缀")
print("请输入文件地址：")
dizhi=input()
if "" in dizhi:
    dizhi=dizhi.strip('"')
def scan_files():
    files=os.listdir(dizhi)
    for f in files:
        if f.endswith('.zip'):
            return dizhi+'\\'+f
def unzip(f):
    folder_name1=f.split('\\')[-1]
    folder_name=folder_name1.split('.')[0]
    target_path=dizhi+'\\'+folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(f,target_path)

def delet(f):
    os.remove(f)

count=0
while True:
    zipfile=scan_files()
    if zipfile:
        unzip(zipfile)
        delet(zipfile)
        count+=1
        print("已完成"+str(count)+'个')
    else:
        print("三秒后将退出程序")
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        break