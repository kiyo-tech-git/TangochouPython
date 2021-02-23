import tkinter as tk
import time

tango_dict = {'林檎': ['ringo', '0','赤い'], 'バナナ': ['banana','1','黄色い'], '葡萄': ['budou','0','紫']}
length = len(list(tango_dict.values()))

print(list(tango_dict.keys()))
print(list(tango_dict.values()))

class Application(tk.Frame):

    def __init__(self, master = None, tango_dict=tango_dict):
        
        self.count = 0
        self.entry_user = tk.Entry()

        tk.Frame.__init__(self, master)
        self.master.geometry("250x400")
        self.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.display_word()
        self.createWidgets()
        self.display_result()

        self.display_kaitou()


    def display_word(self):
        self.text = tk.StringVar()
        self.text.set(list(tango_dict.keys())[self.count])
        self.label = tk.Label(textvariable=self.text)
        self.label.pack()

    def display_result(self):
        self.text_judge = tk.StringVar()
        self.text_judge.set("")
        self.label_judge = tk.Label(textvariable=self.text_judge)
        self.label_judge.pack()
    
    def display_kaitou(self):
        self.text_kaitou = tk.StringVar()
        self.text_kaitou.set("")
        self.label_kaitou = tk.Label(textvariable=self.text_kaitou)
        self.label_kaitou.pack()




    def callback(self,i):
        print(str(i)+"が押されました")
        self.num = str(i)


    def createWidgets(self):
        tk.Label(text="How to read this tango?", font=("System",12)).pack()
        self.entry_user.pack()
        tk.Label(text="What type is the accent?", font=("System",12)).pack()

        self.btn0 = tk.Button(text='0', command=lambda:[self.callback(0),self.judge()], height=1,width=10)
        self.btn1 = tk.Button(text='1', command=lambda:[self.callback(1),self.judge()], height=1,width=10)
        self.btn2 = tk.Button(text='2', command=lambda:[self.callback(2),self.judge()], height=1,width=10)
        self.btn3 = tk.Button(text='3', command=lambda:[self.callback(3),self.judge()], height=1,width=10)
        self.btn4 = tk.Button(text='4', command=lambda:[self.callback(4),self.judge()], height=1,width=10)
        self.btn5 = tk.Button(text='5', command=lambda:[self.callback(5),self.judge()], height=1,width=10)

        self.btn0.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn1.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn2.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn3.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn4.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        self.btn5.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)

        self.btn_Next = tk.Button(text='Next', command=lambda:[self.change_word()], height=1,width=10,bg = "blue").pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        
        self.btn_Kaito = tk.Button(text='Knowledge', command=lambda:[self.show_kaitou()], height=1,width=10).pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)

    def judge(self):

        entry_user = self.entry_user.get()
        print(entry_user)
        
        print(list(tango_dict.values())[self.count])
        if entry_user == list(tango_dict.values())[self.count][0] \
            and self.num == list(tango_dict.values())[self.count][1]:
            self.text_judge.set("Congratulations!!")
            print("Congratulations!!")
        elif entry_user != list(tango_dict.values())[self.count][0] \
            and self.num == list(tango_dict.values())[self.count][1]:
            print("Read wrong!")
            self.text_judge.set("Read wrong!")
        elif entry_user == list(tango_dict.values())[self.count][0] \
            and self.num != list(tango_dict.values())[self.count][1]:
            print("Accent wrong!")
            self.text_judge.set("Accent wrong!")
        else:
            print("Read/Accent both wrong!")
            self.text_judge.set("Read/Accent both wrong!")

        

    def change_word(self):
        if self.count < length - 1:
            self.count += 1
            self.text.set(list(tango_dict.keys())[self.count])
            self.text_judge.set("")
            self.text_kaitou.set("")
            self.entry_user.delete(0, tk.END)
        else:
            self.text.set("終了")
            self.label.configure(background='red')
            self.text_judge.set("Everything is done!")
            self.text_kaitou.set("Everything is done!")

    def show_kaitou(self):
        self.text_kaitou.set(list(tango_dict.values())[self.count][2])



root = tk.Tk().title("TangoChou")
app = Application(master = root)
app.mainloop()