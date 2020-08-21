import openpyxl
import xlrd
import os
import random
import tkinter
from tkinter import ttk
import tkinter.messagebox

menu_list = []

def takeSecond(element):
    return element[1]

def Load_Data(leek_number, vege_number, soup_number, total_amount, path):
    menu_list.clear()
    leek_list = []
    vege_list = []
    soup_list = []
    
    
    # load data from file
    wb = openpyxl.load_workbook(path, data_only = True)
    sheet = wb.active
    
    for leek_name_cell, leek_price_cell in zip(sheet['A'], sheet['B']):
        if (leek_name_cell.value is not None) and (leek_price_cell.value is not None):
            leek_list.append([leek_name_cell.value, leek_price_cell.value])
            
    for vege_name_cell, vege_price_cell in zip(sheet['C'], sheet['D']):
        if (vege_name_cell.value is not None) and (vege_price_cell.value is not None):
            vege_list.append([vege_name_cell.value, vege_price_cell.value])
            
    for soup_name_cell, soup_price_cell in zip(sheet['E'], sheet['F']):
        if (soup_name_cell.value is not None) and (soup_price_cell.value is not None):
            soup_list.append([soup_name_cell.value, soup_price_cell.value])
            
    del leek_list[0]
    del vege_list[0]
    del soup_list[0]
    
    leek_list.sort(key = takeSecond)
    vege_list.sort(key = takeSecond)
    soup_list.sort(key = takeSecond)
    
    
    return Process_Data(leek_list, vege_list, soup_list, leek_number, vege_number, soup_number, total_amount)
    

def Process_Data(leek_list,vege_list, soup_list, leek_number, vege_number, soup_number, amount):
    total_amount = amount
    total_dish_number = leek_number + soup_number + vege_number
    
    # soup
    total_dish_number, total_amount = Generate_Combinations(soup_number, soup_list, total_dish_number, total_amount, menu_list)
    # leek
    total_dish_number, total_amount = Generate_Combinations(leek_number, leek_list, total_dish_number, total_amount, menu_list)
    # vege
    total_dish_number, total_amount = Generate_Combinations(vege_number, vege_list, total_dish_number, total_amount, menu_list)
    
    return total_amount

def Generate_Combinations(dish_number, dish_list, total_dish_number, total_amount, menu_list):
    for i in range(dish_number):
        if i%2 == 0:
            index = random.randint(0, len(dish_list)-1)
            
            total_amount -= dish_list[index][1]
            menu_list.append(dish_list[index])
            del dish_list[index]
        else:
            balance = total_amount/(total_dish_number - i)
            if balance >= dish_list[len(dish_list)-1][1]:
                total_amount = total_amount - dish_list[len(dish_list)-1][1]
                menu_list.append(dish_list[len(dish_list)-1])
                del dish_list[len(dish_list)-1]
            elif balance <= dish_list[0][1]:
                total_amount = total_amount - dish_list[0][1]
                menu_list.append(dish_list[0])
                del dish_list[0]
            else:
                for j in range(len(dish_list)):
                    if balance <= dish_list[j+1][1] and balance >= dish_list[j][1]:
                        if abs(balance - dish_list[j][1]) < abs(balance - dish_list[j+1][1]):
                            j = j+1
                        total_amount = total_amount - dish_list[j][1]
                        menu_list.append(dish_list[j])
                        del dish_list[j]
                        break
    return (total_dish_number-dish_number, total_amount)


def func(path_entry, leek_entry, vege_entry, soup_entry, amnt_entry, output_text):
    path = path_entry.get()
    leek = leek_entry.get()
    vege = vege_entry.get()
    soup = soup_entry.get()
    amount = amnt_entry.get()
    
    if path is '' or leek is '' or vege is '' or soup is '' or amount is '':
        tkinter.messagebox.showerror(title='Error', message='请将信息填写完整')
    else:
        total_amount = Load_Data(int(leek), int(vege), int(soup), int(amount), path)
    
        output_text.delete(1.0, tkinter.END)
        for ele in menu_list:
            output_text.insert(1.0, '{} : {}\n'.format(ele[0], ele[1]))
        output_text.insert(1.0, '差额 : {}\n'.format(total_amount))
        output_text.insert(1.0, '总金额 : {}\n'.format(int(amount)-total_amount))

def main():
    # path = '/Users/stevenzhang/Documents/test.xlsx'
    # input("please enter your file path:")
    # map(int, input("输入菜、汤的数量，以及预算（空格隔开）:").split())
    auto_path = os.path.abspath('../../..') + '/caidan.xlsx'
    ### ------------------ UI -------------------------
    window = tkinter.Tk()
    window.title('菜单生成')
    window.geometry('800x600')

    
    ## 'frame up' add label and entry
    fu = tkinter.Frame(window, bg='grey')
    # 'frame up left' add label
    ful = tkinter.Frame(fu)
    path_label = tkinter.Label(ful, text='文件路径', bg='grey', font=('Arial', 12), width=30, height=2)
    path_label.pack(side=tkinter.TOP)
    leek_label = tkinter.Label(ful, text='荤菜', bg='grey', font=('Arial', 12), width=30, height=2)
    leek_label.pack(side=tkinter.TOP)
    vege_label = tkinter.Label(ful, text='素菜', bg='grey', font=('Arial', 12), width=30, height=2)
    vege_label.pack(side=tkinter.TOP)
    soup_label = tkinter.Label(ful, text='汤', bg='grey', font=('Arial', 12), width=30, height=2)
    soup_label.pack(side=tkinter.TOP)
    amnt_label = tkinter.Label(ful, text='金额', bg='grey', font=('Arial', 12), width=30, height=2)
    amnt_label.pack(side=tkinter.TOP)
    ful.pack(side=tkinter.LEFT)
    # 'frame up right' add entry
    fur = tkinter.Frame(fu)
    text = tkinter.StringVar()
    path_entry = tkinter.Entry(fur, textvariable=text, font=('Arial', 14))
    text.set(auto_path)
    path_entry.pack(side=tkinter.TOP)
    leek_entry = tkinter.Entry(fur, show=None, font=('Arial', 14))
    leek_entry.pack(side=tkinter.TOP)
    vege_entry = tkinter.Entry(fur, show=None, font=('Arial', 14))
    vege_entry.pack(side=tkinter.TOP)
    soup_entry = tkinter.Entry(fur, show=None, font=('Arial', 14))
    soup_entry.pack(side=tkinter.TOP)
    amnt_entry = tkinter.Entry(fur, show=None, font=('Arial', 14))
    amnt_entry.pack(side=tkinter.TOP)
    fur.pack(side=tkinter.RIGHT)
    fu.pack(side=tkinter.TOP, pady=10)
    
    
    ## 'frame middle' add list
    fm = tkinter.Frame(window)
    output_text = tkinter.Text(fm, bg='Lavender')
    output_text.pack()
    fm.pack(side=tkinter.TOP)
    
    
    ## 'frame bottom' add button
    fb = tkinter.Frame(window, bg='Lavender', width=100, height=10)
    submit_button = ttk.Button(fb, text='提交', command=lambda:func(path_entry, leek_entry, vege_entry, soup_entry, amnt_entry, output_text))
    submit_button.pack(side=tkinter.TOP)
    fb.pack(side=tkinter.TOP)
    
    
    window.mainloop()
    ### -------------------- UI --------------------------


if __name__ == '__main__':
    main()
