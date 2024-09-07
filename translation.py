import pyperclip
import time
import webbrowser
# import nltk
# #nltk.download()    #首次运行需要开启 弹出对话框选择 package --> words --> download
# #from nltk.corpus import wordnet
# from nltk.corpus import words as words_range
import enchant

d = enchant.Dict("en_US")
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

            # if wordnet.synsets(lastword):    #'a' 'the' 'that' return []不准确！
            # if (lastword in words_range.words() or lastword.rstrip('s') in words_range.words() or lastword.rstrip('es') in words_range.words() or lastword.rstrip('ed') in words_range.words() or lastword.rstrip('ing') in words_range.words()):  #单词在words中，库使用复杂，更新接口变更...
            if ( d.check(lastword) or d.check(lastword.rstrip('s')) or d.check( lastword.rstrip('es')) or d.check(lastword.rstrip('ed')) or d.check(lastword.rstrip('ing')) ) :
                strBuff =  strBuff.replace('\r\n', ' ',1)    #正常换行
            else :
                print(lastword)
                # strBuff.replace('\r\n', '',1)    #死循环
                strBuff =  strBuff.replace('\r\n', '',1)    #断词换行
        strBuff =  strBuff.replace('%', '%25')    #url转义 %一定要在最前面
        strBuff =  strBuff.replace('+', '%2B')
        strBuff =  strBuff.replace('/', '%2F')
        strBuff =  strBuff.replace('?', '%3F')
        strBuff =  strBuff.replace('#', '%23')
        strBuff =  strBuff.replace('&', '%26')

        # chrome
        # url='https://translate.google.co.jp/?hl=zh-CN&tab=wT&sl=auto&tl=zh-CN&text=' + strBuff + '&op=translate'
        # chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"    #r代表不转义，否则\替换为\\ 此处更改为自己本地的chrome的安装路径
        # webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        # webbrowser.get('chrome').open(url)

        # edge
        url='https://cn.bing.com/translator?ref=TThis&text=' + strBuff + '&from=english&to=zh-Hans'
        webbrowser.register('edge', None,webbrowser.BackgroundBrowser(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
        webbrowser.get('edge').open(url)

    else:
        pass
