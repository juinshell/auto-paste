import subprocess
import time
import pyperclip
from pynput.keyboard import Key, Controller
keyboard = Controller()

def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    #这里的data为bytes类型，之后需要转成utf-8操作
    return data

while True:
    pyperclip.copy("")
    while pyperclip.paste() == '':
        time.sleep(0.1)
    #获取剪切板内容
    txt=str(getClipboardData(),'utf-8')
    txt=txt.strip().replace('\r\n',' ').replace('\r',' ').replace('\n',' ')
    print(txt)
    time.sleep(3)
    #重新转成bytes型
    list = [one for one in txt]
    # 写入剪切板
    for one in list:
        print(one)
        keyboard.type(one)
        time.sleep(0.05)