import requests
keyword = "python"
url = "https://www.amazon.cn/dp/B07C3WY33S?ref_=Oct_ETopRankingC_desktop_NA&pf_rd_r=XV7NM8VFV3DNACY2JKQP&pf_rd_p=b301916d-9153-4f26-b649-e413f1049092&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-8"
try:
    kv = {'wd':keyword}
    r = requests.get("https://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))

except:
    print("爬取失败")




# from bs4 import BeautifulSoup
# url = 'http://www.cntour.cn/'
# strhtml = requests.get(url)
# soup=BeautifulSoup(strhtml.text)
# data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
# for i in data:
#     res={
#         'title':i.get_text(),
#         'link':i.get('href')
#     }
# print(res)



















# import PyQt5
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
#
# import sys
#
# class MainWindow(QMainWindow):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#
#
#         # set title
#         self.setWindowTitle('my first app')
#         layout = QHBoxLayout()
#
#
#         for i in range(5):
#             button = QPushButton(str(i))
#             button.pressed.connect(lambda x=i:self._my_func(x))
#             layout.addWidget(button)
#
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#         label = QLabel('welcome 这是我的第一个标签')
#         label.setAlignment(Qt.AlignCenter)
#         self.setCentralWidget(label)
#
#     def _my_func(self, n):
#         print('click button %s' % n)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
