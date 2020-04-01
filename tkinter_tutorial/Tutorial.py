import tkinter as tk


flag = True    #Label&Button 标签和按钮
if flag:
    window = tk.Tk()
    window.title("my window")
    window.geometry("300x200")
    # l = tk.Label(window,
    #              text='OMG! this is TK!',  # 标签的文字
    #              bg='red',  # 背景颜色
    #              font=('Arial', 12),  # 字体和字体大小
    #              width=15, height=2  # 标签长宽
    #              )
    var = tk.StringVar()  # 这时文字变量储存器
    l = tk.Label(window,
                 textvariable=var,  # 使用 textvariable 替换 text, 因为这个可以变化
                 bg='green',
                 font=('Arial', 12),
                 width=15, height=2)

    l.pack()  # 固定窗口位置
    #l.place() #具体放在某个点上

    on_hit = False  # 默认初始状态为 False
    def hit_me():
        global on_hit
        if on_hit == False:  # 从 False 状态变成 True 状态
            on_hit = True
            var.set('you hit me')  # 设置标签的文字为 'you hit me'
        else:  # 从 True 状态变成 False 状态
            on_hit = False
            var.set('')  # 设置 文字为空

    b = tk.Button(window,
                  text='hit me',  # 显示在按钮上的文字
                  width=15, height=2,
                  command=hit_me)  # 点击按钮式执行的命令
    b.pack()  # 按钮位置

    window.mainloop()

flag = False    #Entry & text 输入文本框
if flag:
    window = tk.Tk()
    window.title("trigonometric function")
    window.geometry("300x200")

    e = tk.Entry(window,
                 width=20,)
    e.pack()

    def insert_point():
        var = e.get()
        t.insert('insert', var)
    def insert_end():
        var = e.get()
        t.insert('end', var)

    b1 = tk.Button(window,
                  text="insert point",
                  # width=15,height=2,
                  width=15,height=1,
                  command=insert_point,)
    b1.pack()

    b2 = tk.Button(window,
                   text="insert end",
                   width=15, height=1,
                   command=insert_end)
    b2.pack()

    t = tk.Text(window,
                width=20,height=2,)
    t.pack()

    window.mainloop()

flag = False     #Listbox 列表部件
if flag:
    window = tk.Tk()
    window.title('my window')
    window.geometry('300x200')

    var1 = tk.StringVar()  # 创建变量
    l = tk.Label(window, bg='yellow', width=10, textvariable=var1)
    l.pack()

    def print_selection():
        value = lb.get(lb.curselection())  # 获取当前选中的文本
        var1.set(value)  # 为label设置值

    b1 = tk.Button(window, text='print selection', width=15,
                   height=2, command=print_selection)
    b1.pack()

    var2 = tk.StringVar()
    var2.set((11, 22, 33, 44))  # 为变量设置值

    # 创建Listbox
    lb = tk.Listbox(window, listvariable=var2)  # 将var2的值赋给Listbox

    # 创建一个list并将值循环添加到Listbox控件中
    list_items = [1, 2, 3, 4]
    for item in list_items:
        lb.insert('end', item)  # 从最后一个位置开始加入值
    lb.insert(1, 'first')  # 在第一个位置加入'first'字符
    lb.insert(2, 'second')  # 在第二个位置加入'second'字符
    lb.delete(2)  # 删除第二个位置的字符
    lb.pack()

    window.mainloop()

flag = False     #Radiobutton 选择按钮
if flag:

    window = tk.Tk()
    window.title('my window')
    window.geometry('400x300')

    var = tk.StringVar()
    l = tk.Label(window, bg='yellow', width=20, text='empty')
    l.pack()

    def print_selection():
        l.config(text='you have selected ' + var.get()) #表示对label所有参数重新配置

    r1 = tk.Radiobutton(window, text='Option A',
                        variable=var, value='A',
                        command=print_selection)    #变量名为var，变量值为A，执行print_selection命令
    r1.pack()
    r2 = tk.Radiobutton(window, text='Option B',
                        variable=var, value='B',
                        command=print_selection)
    r2.pack()
    r3 = tk.Radiobutton(window, text='Option C',
                        variable=var, value='C',
                        command=print_selection)
    r3.pack()

    window.mainloop()

flag = False     #Scale尺度
if flag:
    window = tk.Tk()
    window.title('my window')
    window.geometry('200x200')

    l = tk.Label(window, bg='yellow', width=20, text='empty')
    l.pack()

    def print_selection(v):
        l.config(text='you have selected ' + v)

    s = tk.Scale(window, label='try me', from_=5, to=11,
                 orient=tk.HORIZONTAL,  #表示bar是横向的
                 length=200, #pixel 以像素为单位，在窗口中的长度。width是以字符为单位的长度
                 showvalue=0,   #是否直接显示在bar上 0=False 1=True
                 tickinterval=2, #标签间隔的长度5-7-9-11
                 resolution=0.01, #保留两位小数
                 command=print_selection)   #每次拖动都会执行命令，默认有返回值
    s.pack()

    window.mainloop()

flag = False     #checkButton 勾选项可以勾选多个，radio_button 只能勾选一个选项
if flag:

    window = tk.Tk()
    window.title('my window')
    window.geometry('200x200')

    l = tk.Label(window, bg='yellow', width=20, text='empty')
    l.pack()

    def print_selection():
        if (var1.get() == 1) & (var2.get() == 0):
            l.config(text='I love only Python ')
        elif (var1.get() == 0) & (var2.get() == 1):
            l.config(text='I love only C++')
        elif (var1.get() == 0) & (var2.get() == 0):
            l.config(text='I do not love either')
        else:
            l.config(text='I love both')

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c1 = tk.Checkbutton(window, text='Python', variable=var1,
                        onvalue=1, offvalue=0,  #选中赋值为1，否则为0
                        command=print_selection)
    c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                        command=print_selection)
    c1.pack()
    c2.pack()

    window.mainloop()

flag = False     #Canvas 画布或图片
if flag:
    window = tk.Tk()
    window.title('my window')
    window.geometry('200x200')

    canvas = tk.Canvas(window, bg='blue',
                       height=100, width=200)   #像素点
    image_file = tk.PhotoImage(file='ins.gif')
    image = canvas.create_image(10, 10, #放在的像素点
                                anchor='nw', #，锚定点，像素点放在图片的哪个角
                                image=image_file)
    x0, y0, x1, y1 = 50, 50, 80, 80
    line = canvas.create_line(x0, y0, x1, y1)
    oval = canvas.create_oval(x0, y0, x1, y1, fill='red')#圆形
    arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30,
                            start=0, extent=180)#扇形
    rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
    canvas.pack()

    def moveit():
        canvas.move(rect, 0, 2) #对象rect, x移动0，y移动2

    b = tk.Button(window, text='move',
                  command=moveit).pack()

    window.mainloop()

flag = False     #Menubar 菜单
if flag:
    window = tk.Tk()
    window.title('my window')
    window.geometry('200x200')

    l = tk.Label(window, text='', bg='yellow')
    l.pack()
    counter = 0

    def do_job():
        global counter
        l.config(text='do ' + str(counter))
        counter += 1


    #创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
    menubar = tk.Menu(window)

    #定义一个空菜单单元
    filemenu = tk.Menu(menubar, tearoff=0) #tearoff 可以单独出来
    #将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='File', menu=filemenu)
    #在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    #如果点击这些单元, 就会触发`do_job`的功能
    filemenu.add_command(label='New', command=do_job)
    filemenu.add_command(label='Open', command=do_job)  #同样的在`File`中加入`Open`小菜单
    filemenu.add_command(label='Save', command=do_job)  #同样的在`File`中加入`Save`小菜单
    filemenu.add_separator()    #这里就是一条分割线
    # 同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
    filemenu.add_command(label='Exit', command=window.quit)

    editmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=editmenu)
    editmenu.add_command(label='Cut', command=do_job)
    editmenu.add_command(label='Copy', command=do_job)
    editmenu.add_command(label='Paste', command=do_job)

    submenu = tk.Menu(filemenu)
    filemenu.add_cascade(label='Import', menu=submenu, underline=0)
    submenu.add_command(label="Submenu1", command=do_job)

    window.config(menu=menubar)

    window.mainloop()

flag = False     #Frame框架
if flag:
    window = tk.Tk()
    window.title('my window')
    window.geometry('200x200')
    # 定义一个`label`显示`on the window`
    tk.Label(window, text='on the window').pack()#表示在主window上
    # 在`window`上创建一个`frame`
    frm = tk.Frame(window)
    frm.pack()
    # 在刚刚创建的`frame`上创建两个`frame`，
    # 我们可以把它理解成一个大容器里套了一个小容器，
    # 即`frm`上有两个`frame` ，`frm_l`和`frm_r`
    frm_l = tk.Frame(frm, )#表示在frame上
    frm_r = tk.Frame(frm)
    # 这里是控制小的`frm`部件在大的`frm`的相对位置，
    # 此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
    frm_l.pack(side='left')
    frm_r.pack(side='right')

    # 这里的三个label就是在我们创建的frame上定义的label部件，
    # 还是以容器理解，就是容器上贴了标签，来指明这个是什么，解释这个容器。
    tk.Label(frm_l, text='on the frm_l1').pack()#这个`label`长在`frm_l`上，显示为`on the frm_l1`
    tk.Label(frm_l, text='on the frm_l2').pack()
    tk.Label(frm_r, text='on the frm_r1').pack()
    window.mainloop()

flag = False     #messagebox 弹窗
from tkinter import messagebox

if flag:
    window = tk.Tk()
    window.title('my window')
    window.geometry('200x200')

    def hit_me():
        # tk.messagebox.showinfo(title='Hi', message='hahahaha')   # return 'ok'  提示信息对话窗
        # tk.messagebox.showwarning(title='Hi', message='nononono')   # return 'ok'  提出警告对话窗
        # tk.messagebox.showerror(title='Hi', message='No!! never')   # return 'ok'  提出错误对话窗
        # print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))   # return 'yes' , 'no'  询问选择对话窗
        print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))   # return True, False
        # print(tk.messagebox.asktrycancel(title='Hi', message='hahahaha'))  # return True, False
        # print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))  # return True, False
        # print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))  # return, True, False, None


    tk.Button(window, text='hit me', command=hit_me).pack()
    window.mainloop()

flag = False     #pack grid place 放置位置
'''
***在同一个窗口不要同时使用pack和grid
'''
if flag:
    window = tk.Tk()
    window.geometry('200x200')

    # canvas = tk.Canvas(window, height=150, width=500)
    # canvas.grid(row=1, column=1)
    # image_file = tk.PhotoImage(file='welcome.gif')
    # image = canvas.create_image(0, 0, anchor='nw', image=image_file)

    # tk.Label(window, text='1').pack(side='top')
    # tk.Label(window, text='1').pack(side='bottom')
    # tk.Label(window, text='1').pack(side='left')
    # tk.Label(window, text='1').pack(side='right')

    # for i in range(4):
    #     for j in range(3):
    #         tk.Label(window,
    #         text=1).grid(row=i, column=j, padx=10, pady=10)
    #grid是用表格的形式定位的
    #这里的参数 row为行，colum为列
    #padx就是单元格左右间距，pady就是单元格上下间距 ipadx/ipady表示内部扩展

    # tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

    window.mainloop()



