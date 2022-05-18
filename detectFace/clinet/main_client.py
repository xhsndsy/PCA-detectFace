import tkinter as tk
import threading
import tkinter.messagebox as mb
import tkinter.filedialog as filedialog

def main_thead():
    threading.Thread(target=gui_thread()).start()


def gui_thread():
    top = tk.Tk()
    top.geometry('800x600')
    app = App(top)
    top.mainloop()

class App:
    def __init__(self, top):

        frame = tk.Frame(top)
        frame.pack()

        filepath = tk.StringVar()

        tk.Label(frame, text = '主窗口').grid(row = 0, column= 0)
        tk.Entry(frame, textvariable=filepath).grid(row =1 , column =0)
        tk.Button(frame, text="上传", command=self.pop_dialog).grid(row = 1, column = 1)
        # mb.showinfo('消息框', 'tk自带')

    @staticmethod
    def pop_dialog():
        result = mb.askokcancel('对话框：提示', '是否确定')
        if result:
            file_path = filedialog.askopenfilename()
            print(file_path)
            filepath.set(file_path)





if __name__ == '__main__':
    main_thead()