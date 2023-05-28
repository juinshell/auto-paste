import subprocess
import time
import pyperclip
from pynput.keyboard import Key, Controller
keyboard = Controller()

import platform
print("Current OS playform: {}".format(platform.system().lower()))

if platform.system().lower() == 'windows':
    def getClipboardData():
        data = pyperclip.paste()
        return data
elif platform.system().lower() == 'linux':
    def getClipboardData():
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        data = p.stdout.read()
        txt=str(data,'utf-8')
        txt=txt.strip().replace('\r\n',' ').replace('\r',' ').replace('\n',' ')
        return txt
else:
    def getClipboardData():
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        data = p.stdout.read()
        txt=str(data,'utf-8')
        txt=txt.strip().replace('\r\n',' ').replace('\r',' ').replace('\n',' ')
        return txt

while True:
    pyperclip.copy("")
    while pyperclip.paste() == '':
        time.sleep(0.1)
    #获取剪切板内容
    txt=getClipboardData()
    print("--------get clipboard data--------")
    print(txt)
    print("--------end end end end end--------")
    time.sleep(3)
    list = [one for one in txt]
    # 写入剪切板
    for one in list:
        # print(one)
        keyboard.type(one)
        time.sleep(0.05)