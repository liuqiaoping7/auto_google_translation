import pyperclip
import time
import webbrowser
import nltk
#nltk.download()
#from nltk.corpus import wordnet
from nltk.corpus import words as words_range

tempBuff=''    #仅仅用于暂存判定
while True:
    time.sleep(3)
    pasteText=pyperclip.paste()
    if tempBuff != pasteText:
        tempBuff=pasteText

        strBuff=pasteText
        # strBuff = strBuff.replace('\r\n', ' ')    #过于简单,如果是断词就出现词间空格
        while  strBuff.find('\r\n') != -1:
            lines= strBuff.split('\r\n',1)
            line=lines[0]
            words=line.rsplit(' ',1)
            lastword=words[-1].lower()

            #if not wordnet.synsets(lastword):    #'a' 'the' 'that' return []，不准确！
            if (lastword in words_range.words() or lastword.rstrip('s') in words_range.words() or lastword.rstrip('es') in words_range.words()):  #复数形式不在其中...
                # strBuff.replace('\r\n', ' ',1)    #死循环
                strBuff =  strBuff.replace('\r\n', ' ',1)    #正常换行
            else :
                print(lastword)
                # strBuff.replace('\r\n', '',1)    #死循环
                strBuff =  strBuff.replace('\r\n', '',1)    #断词换行
        strBuff =  strBuff.replace('%', '%25')    #url转义 %一定要在最前面
        strBuff =  strBuff.replace('+ ', ' %2B')
        strBuff =  strBuff.replace('/', '%2F')
        strBuff =  strBuff.replace('?', '%3F')
        strBuff =  strBuff.replace('#', '%23')
        strBuff =  strBuff.replace('&', '%26')
        url='https://translate.google.com/?hl=zh-CN&tab=wT#en/zh-CN/'+ strBuff
        chrome_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"    #r代表不转义，否则\替换为\\
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)

    else:
        pass
