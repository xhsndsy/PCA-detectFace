# import tkinter as tk
# import threading
# import tkinter.messagebox as mb
# import tkinter.filedialog as filedialog
# from tkinter import *
#
# def main_thead():
#     threading.Thread(target=App).start()
#
# def main_gui():
#     top = tk.Tk()
#     top.geometry('800x600')
#     top.title('人脸特征分析罪犯追讨系统')
#     app = App(top)
#     top.mainloop()
#
# class App():
#
#     def __init__(self, top):
#
#         frame = tk.Frame(top)
#         frame.pack()
#         filepath = StringVar()
#         filepath.set('请选择视频文件')
#         tk.Label(frame, text = '主窗口').grid(row = 0, column= 0)
#         tk.Entry(frame, textvariable=filepath).grid(row=1, column=0)
#         tk.Button(frame, text="上传", command=self.pop_dialog).bind('<Button-1>', self.pop_dialog()).grid(row = 1, column = 1)
#
#
#         # mb.showinfo('消息框', 'tk自带')
#
#     @staticmethod
#     def pop_dialog(filepath=None):
#         result = mb.askokcancel('对话框：提示', '是否确定')
#         if result:
#             file_path = filedialog.askopenfilename()
#             file_path = file_path.replace('/', '\\')
#
#             filepath.set(file_path)
#
#
#
#
#
#
# if __name__ == '__main__':
#     main_gui()
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk



def handler_button():
    file_path = filedialog.askopenfilename()
    file_path = file_path.replace('/', '\\')
    paramStr.set(file_path)

def video_loop():
    success, img = camera.read()  # 从摄像头读取照片
    if success:
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
        current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
        imgtk = ImageTk.PhotoImage(image=current_image)
        panel.imgtk = imgtk
        panel.config(image=imgtk)
        root.after(1, video_loop)

if __name__ == '__main__':

    root = Tk()
    root.title('人脸识别特征分析系统')
    root.geometry('600x200')
    paramStr = StringVar()

    camera = cv2.VideoCapture(paramStr)

    paramStr.set('选择文件路径')
    Entry(root, textvariable=paramStr, width = 50).pack()
    btn1 = Button(root, text='上传', command=handler_button)  # 默认左键点击
    btn1.pack()
    panel = Label(root)
    panel.pack(padx=10, pady=10)
    root.config(cursor="arrow")
    video_loop()

    root.mainloop()
    camera.release()
    cv2.destroyAllWindows()
