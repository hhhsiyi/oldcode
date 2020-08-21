import requests
import json
import re
import bs4
import os
url="http://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18103353494952086171_1586840488510&params=%7B%22type%22%3A%220%22%7D&_=1586840489457"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
def loads_jsonp(_jsonp):
        try:
            return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
        except:
            raise ValueError('Invalid Input')
a=requests.get(url,headers=headers)
b=loads_jsonp(a.text)
c=b['data']
d=c['html']


public
e=bs4.BeautifulSoup(d,'html.parser')
f=e.findAll(attrs={'class':'tn-item clearfix'})

try:
    os.mkdir("./note")
except:
    pass

for i in range(0,len(f)):
    filename="./note/note"+str(i+1)+".txt"
    with open(filename,'w+',encoding='utf-8') as wf:
        image=f[i].find(attrs={'class':'tn-image'})
        wf.write("图片地址1:"+ image.a.img['data-src'])
        wf.write("\n图片地址2:"+ image.a.img['data-rt-src'])
        wf.write("\n文章地址:"+image.a['href'])

        wrapper=f[i].find(attrs={'class':'tn-wrapper'})
        wf.write("\n文章标题:"+ wrapper.dl.dt.a.text)
        wf.write("\n文章摘要:"+ wrapper.dl.dd.a.text)


        extra=wrapper.find(attrs={'class':'tn-extra'})

        ding=extra.find(attrs={'class':'tn-ding'})
        wf.write("\nding数:"+ding.em.text)
        place=extra.find(attrs={'class':'tn-place'})
        wf.write("\n地点:"+place.text)

        user=extra.find(attrs={'class':'tn-user'})
        userName=user.a.text
        wf.write("\n用户名:"+userName.strip())
        userAvatar=user.img['src']
        wf.write("\n用户头像地址:"+userAvatar)


        nums=extra.find(attrs={'class':'tn-nums'})
        wf.write("\nnums:"+nums.text)





        





