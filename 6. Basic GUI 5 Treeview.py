from logging import exception
from msilib.schema import Font
from tkinter import *
from tkinter import ttk, messagebox # messagebox คือไว้สำหรับ pop-up เด้ง Error
import csv
from datetime import datetime
from unittest import result

#ต้องการโปรแกรมที่สามารถเก็บข้อมูล สินค้า,ราคา,จำนวนที่ซื้อ,ราคารวมของสินค้านั้นๆ

'''------------------
    # ลำดับการวางใน GUI
    # 1. GUI = ผนังบ้าน
    # 2. Tab = Wallpaper
    #   2.1 Frame = กระดานที่แปะอยู่บน Wallpaper   
    #   2.2 Label, Entry etc. = สิ่งของที่แปะอยู่บน Wallpaper
-------------------'''  

GUI = Tk()

GUI.title('คำนวณง่ายๆ')
GUI.geometry('600x600')

"""----------------------------Menu Bar----------------------------"""

menubar = Menu(GUI)
    # สร้างตัวแปร menubar เป็นแถบ Menu ของ GUI
GUI.config(menu = menubar)
    # เขียนโค้ดตามไป
#-------File-------#
filemenu = Menu(menubar,tearoff = 0)
    # สร้างตัวแปร filemenu ว่าเป็น Bar ของ Menubar ที่สร้างไว้
    # tearoff = 0 คือ ไม่สามารถดึงแถบ bar ออกมาได้
menubar.add_cascade(label = 'File',menu = filemenu)
    # .add_cascade(label = 'ชื่อ Menu ที่ต้องการให้แสดง',menu = 'สิ่งที่อยู่ใน Menu ที่ต้องการ')
    # .add cascade คือ การเอาไปแปะใน GUI
    # label คือ การให้ใส่ชื่อ Menu
    # menu คือ การกำหนดว่าใน Menu นั้น ๆ ดึงมาจากตัวแปร menu ไหนที่สร้าง
filemenu.add_command(label = 'Import CSV')
    # .add_command คือ เป็นการเพิ่มไปว่าใน menu ต้องการให้มีอะไรบ้าง
filemenu.add_command(label = 'Export to Googlesheet')   
#-------------------#

#-------Help-------#
def About():
    messagebox.showinfo('About','เขียนโปรแกรมครั้งแรก\n\n\t\tBy ARM')    

helpmenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'Help', menu = helpmenu)
helpmenu.add_command(label = 'About',command= About)

#------------------#

#-------Donate-------#
donatemenu = Menu(menubar)
menubar.add_cascade(label = 'Donate', menu = donatemenu)
donatemenu.add_command(label= 'Account')  
#--------------------#

"""----------------------------------------------------------------"""


Tab = ttk.Notebook(GUI)
    # Tab = ttk.Notebook(GUI) คือการสร้างตัวแปร Tab ให้เป็น Tab ของ GUI
    # Notebook(GUI) คือนำ Tab ไปใส่ไว้ใน GUI
T1 = Frame(Tab)    
        # T1 = Frame(Tab, width= 400, height= 400)
        # ด้านหลังคือกำหนดความกว้าง ยาวของ Tab
T2 = Frame(Tab)
    # T2 = Frame(Tab) หมายถึง ให้ T2 คือตัวแปรที่ไป Frame ไว้ใน Tab
Tab.pack(fill= BOTH, expand = 1)
    # fill = BOTH คือขยายทั้งแกน x และแกน y
    # fill = X คือขยายในแนวแกน x
    # fill = Y คือขยายในแนวแกน y
    # expand = 1 ต้องใส่ตลอด

icon_t1 = PhotoImage(file = 't1_expense.png')
icon_t2 = PhotoImage(file= 't2_expenselist.png')

    # ภาพที่ใช้ใน Tab ควรมีขนาด 24x24 pixel
    # Photoimage คือคำสั่งที่เรียกรูปภาพ
    # file = 'ชื่อไฟล์รูปภาพ หรือตำแหน่งของรูปภาพ *ใส่นามสกุลไฟล์ต้องเป็น .png เท่านั้น*
    # สามารถเติม .subsample(2) ไว้ข้างหลังเพื่อย่อรูปได้




Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{25}}',image= icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{25}}',image=icon_t2,compound='top')
    # ตรง text ให้ไปดูไฟล์ Basic Print
    # .add(tab) ที่ต้องการจะให้โชว์, ชื่อที่จะโชว์ของ tab)
    # .add คือการเพิ่ม tab ถ้ายังไม่ใช้ .add tab ก็จะยังไม่โชว์ในโปรแกรม

    # image คือคำสั่งที่จะให้นำรูปไปแปะ
    # compound คือคำสั่งที่เอาไว้เลือกตำแหน่งรูปภาพ
        # คำสั่งที่ใช้กับ compound คือ none, image, text, center, left, right, top ,bottom
F1 = Frame(T1)
#F1.place(x=130 , y=20)
F1.pack()

FONT = (None,16)
days = {'Mon':'จันทร์'
        ,'Tue':'อังคาร'
        ,'Wed':'พุธ'
        ,'Thu':'พฤหัสบดี'
        ,'Fri':'ศุกร์'
        ,'Sat':'เสาร์'
        ,'Sun':'อาทิตย์'}




"""----------------------------Tab 1----------------------------"""

#-------Image--------#
main_icon = PhotoImage(file='main_icon.png')

Mainicon = Label(F1,image=main_icon).pack(pady=20)

#---------------------#

#-------Text 1--------#

L = ttk.Label(F1,text='คำนวณราคาง่ายๆ~~',font = FONT).pack()

#---------------------#

#-------Text 2--------#


L = ttk.Label(F1,text = 'ชื่อสินค้า',font = FONT)
L.pack()

Gorder = StringVar()
E1 = ttk.Entry(F1,textvariable = Gorder,font = FONT)
E1.pack()
E1.focus()

#---------------------#

#-------Text 3--------#

L = ttk.Label(F1,text = 'ราคาสินค้า (บาท)',font = FONT)
L.pack()

Gprice = StringVar()
Gprice.set('')

E2 = ttk.Entry(F1,textvariable = Gprice,font = FONT)
E2.pack()

#---------------------#

#-------Text 4--------#

L = ttk.Label(F1,text = 'จำนวนสินค้า',font = FONT)
L.pack()

Gnum = StringVar()
Gnum.set('')

E3 = ttk.Entry(F1,textvariable = Gnum,font = FONT)
E3.pack()

#---------------------#


#-------Function Save-------#

def Save(even = None):
    order = Gorder.get()
    price = Gprice.get()
    num = Gnum.get()

    if len(order.split()) == 0 and int(price) >= 0 and int(num) >= 0:
        # len(order.split()) คือการนับ word ใน order
        messagebox.showinfo('Error','กรุณากรอกรายชื่อสินค้า') 
        return
    elif len(order.split()) == 0 or price == '' or num =='':
        messagebox.showinfo('Error','กรุณากรอกข้อมูลให้ครบ') 
        return
    
    try:
        total = int(price) * int(num)
        
        #----------การแสดงผลตรง Label ล่างสุด---------#
        textshow = f'\tสินค้า: {order}\n\tราคา: {price} บาท, จำนวน: {num} ชิ้น\n\t ราคารวม: {total} บาท '
        v_result.set(textshow)
        R = ttk.Label(F1,textvariable = v_result,font = FONT,foreground='blue')
        #----------การแสดงผลตรง Label ล่างสุด---------#

        #การบันทึกเวลาลงใน
        #หารายละเอียดเกี่ยวกับฟังค์ชั่นเวลาเพิ่ม search: strftime python ใน google
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        today = datetime.now().strftime('%a')
        dt = days[today]+'-'+ dt
        # .now() จะแสดงข้อมูลที่เป็นปัจจุบัน

        print(f'เวลาบันทึก {dt}') 
        print(f'\tสินค้า: {order}\n\tราคา: {price} บาท, จำนวน: {num} ชิ้น\n\t ราคารวม: {total} บาท ')
                                    

        Gorder.set('')
        Gprice.set('')
        Gnum.set('')

        with open('Savedata.csv','a',encoding='utf-8',newline = '') as f:

            writ = csv.writer(f)
            data = [dt,order,price,num,total]
            writ.writerow(data)

        E1.focus()
        update_table()
    except Exception as e:
        print('Error',e)
        Gorder.set('')
        Gprice.set('')
        Gnum.set('')
        #messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ ดังนี้ \n1. กรอกแค่ตัวเลขในช่องราคาและช่องจำนวนสินค้า\n2. ไม่ต้องใส่หน่วย')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ ดังนี้ \n1. กรอกแค่ตัวเลขในช่องราคาและช่องจำนวนสินค้า\n2. ไม่ต้องใส่หน่วย')
        #messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ ดังนี้ \n1. กรอกแค่ตัวเลขในช่องราคาและช่องจำนวนสินค้า\n2. ไม่ต้องใส่หน่วย')

        # .showerror('ชื่อหน้าต่างด้านซ้ายบนสุด','ข้อความที่ต้องการแสดงในหน้าต่าง')
        E1.focus()
GUI.bind('<Return>',Save)

#----------------------------#


   

#-------ปุ่มบันทึก-------#

icon_b1 = PhotoImage(file='b_save.png')

b1 = ttk.Button(F1, text=f'{"บันทึกและคำนวณ":^{10}}',command = Save,image= icon_b1,compound='left')

b1.pack(ipadx = 15, ipady = 5, pady = 10)


#---------------------#

#-------Text 5 result--------#

v_result = StringVar()
v_result.set('---------ผลลัพธ์---------')
R = ttk.Label(F1,textvariable = v_result,font = FONT,foreground= 'green')
    # foreground คือเปลี่ยนสีตัวอักษร 
R.pack(pady=30)
#-----------------------------#



"""----------------------------Tab 2----------------------------"""

F2 = Frame(T2)
F2.pack()

#-------Text 1-------#

L = ttk.Label(F2,text = 'แสดงค่าที่บันทึก',font= FONT)
L.pack(pady=20)

#-------การสร้างฟังค์ชั่นอ่านข้อมูลใน CSV-------#
def read_csv():
    with open('Savedata.csv',newline='',encoding='utf-8') as f:
        # จะทำตัว reader ไม่ต้องใส่ mode
        fr = csv.reader(f)
        data = list(fr)
            # list() หมายถึงทำให้แสดงผลที่บันทึกใน csv
            # ถ้ายังไม่มี list() ตอน print จะแสดงเป็นอะไรก็ไม่รู้

        # print(data)
        # print('------')
        # print(data[0])
        # print(data[0])
        # for a,b,c,d,e in data:
            #การอ่านค่า list ใน list
        #     print(d)

    return data
        # return คือการส่งค่ากลับ
        # return ค่า data กลับไปยัง read_csv()
        # ถ้าไม่ return ค่าก็จะไม่ return ไปยัง read_csv() ซึ่งใน read_csv() ที่เรียกใช้ก็จะไม่มีอะไรอยู่เลย
        # ฟังค์ชั่นที่ไม่ต้องการนำค่ากลับไปใช้งานต่อก็ไม่ต้องใช้ return ก็ได้
        # อย่างฟังค์ชั่นนี้เตรียม return ค่าไปกรอกไว้ใน Tree view    
#---------------------------------------------#
#-------การสร้าง Table-------#
header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
    # กำหนดชื่อ column 
resulttable = ttk.Treeview(F2, columns = header,show='headings',height= 10)
    # ใน Treeview ไปแปะไว้ใน Tab T2
    # columns = header คือ หัวตารางให้โชว์ค่า list ของ Header ที่สร้างไว้
    # show = 'headings' คือ ให้ค่าที่โชว์ไม่เป็นแบบ Dropdown เป็นแบบ Head ทั้งหมด
    # height = 10 คือ ให้ Treeview ที่ความสูง 10 ช่อง
resulttable.pack()

# for i in range(len(header)):
#     resulttable.heading(header[i],text = header[i])
# การรันลูปแบบใช้ len เพื่อให้รันตามจำนวนใน list

for i in header:
    resulttable.heading(i,text=i)
    # เทคนิคการรันลูปใน list

'''# .heading ('ชื่อ cell',text = 'ข้อความที่กรอกใน cell นั้น')'''

headerwidth = [150,170,80,80,80]

# for i in range(len(header)):
#     resulttable.column(header[i],width = headerwidth[i])

for h,w in zip(header,headerwidth):
    # zip คือการรวม list 2 list เข้าด้วยกัน
    # zip(list 1, list 2)
    resulttable.column(h, width = w)
    # .column สามารถกำหนดความกว้างของ column
#---------------------#

#-------การอัพเดทข้อมูลใน Table-------#



def update_table():
    resulttable.delete(*resulttable.get_children())
        #.delete(*ตารางที่ต้องการจะลบข้อมูล.get_children())
        # เครื่องหมาย * คือ บอกให้ทำซ้ำ

    # for c in resulttable.get_children():
    #     resulttable.delete(c)   
        # ถ้าไม่ใช้ * ก็ใช้ for loop ได้

    data = read_csv()
    '''resulttable.insert('','end',value = ['จันทร์','น้ำดื่ม','30','5','150'])'''
    # .insert('','บรรทัดที่จะแทรกข้อมูล',value = [สิ่งที่ต้องการจะกรอกลงในตาราง])
    # .insert คือ การใส่ข้อมูลลงไปในตาราง
    # 'end' คือ ส่ข้อมูลต่อจากบรรทัดสุดท้าย # 0 คือแทรกข้อมูลขึ้นมาบนบรรทัดแรก
    # value คือ สิ่งที่ต้องการจะกรอกลงไปในตาราง
    
    for d in data:
        resulttable.insert('',0 ,values= d)

update_table()
GUI.mainloop()
