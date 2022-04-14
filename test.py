from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil

username = os.getlogin()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x700+100+50")
        self.root.resizable(False, False)

        def main_page():
            frame_login = Frame(self.root, bg="white")
            frame_login.place(x=330, y=150, width=500, height=400)

            Label(frame_login, text="הלבנות ליעול מערכת", font=("Impact", 30, "bold"), fg="#6162FF",
                  bg="white").place(
                x=60,
                y=30)
            Label(frame_login, text=":העברה סוג", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                  bg="white").place(x=190, y=100)
            Label(frame_login, text='אל בית משוב צוות ידי על פותחה זו מערכת', font=("Goudy old style", 15, "bold"),
                  fg="#1d1d1d",
                  bg="white").place(x=50, y=300)
            Button(frame_login, cursor="hand2", text="אבן", bd=0, command=to_even,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=50, y=150, width=180,
                                                                                 height=40)
            Button(frame_login, cursor="hand2", text="צהלנט", bd=0, command=to_idf,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=255, y=150, width=180,
                                                                                 height=40)
            Button(frame_login, cursor="hand2", text="אבן & צהלנט", bd=0, command=to_both,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=170, y=200, width=170,
                                                                                 height=40)

        def both_t_page():
            Frame(root, bg="white", ).place(x=330, y=150, width=500, height=400)

            def prog():
                ff = []

                def file_copy():
                    with open(fr'C:\Users\{username}\Desktop\FT2_logs.txt') as file:
                        for line in file:
                            ff.append(line)

                def copyx():
                    tt = []
                    with open(fr'C:\Users\{username}\Desktop\FT_logs.txt') as file:
                        for line in file:
                            tt.append(line.strip())

                    for f in ff:
                        print(f)
                        for a in tt:
                            shutil.copy(src=a, dst=f)

                def delete_logs():
                    os.remove(fr'C:\Users\{username}\Desktop\FT_logs.txt')
                    os.remove(fr'C:\Users\{username}\Desktop\FT2_logs.txt')

                file_copy()
                copyx()
                delete_logs()
                messagebox.showinfo(title=None,
                                    message="הקבצים הועברו בהצלחה, לפרטים בנוגע לשעות הלבנה, ניתן לפנות למשוב בית אל - "
                                            "0506235336")
                main_page()

            def files():

                root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                           filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
                path = f"C:/Users/{username}/Desktop/FT_logs.txt"
                if os.path.isfile(path) is True:
                    with open(rf'C:\Users\{username}\Desktop\FT_logs.txt', 'a+') as f:
                        f.write(root.filename + '\n')

                else:
                    open(rf"C:/Users/{username}/Desktop/FT_logs.txt", "a")
                    with open(rf'C:\Users\{username}\Desktop\FT_logs.txt', 'a+') as f:
                        f.write(root.filename + '\n')

            Label(text="אבן & צהלנט", font=("Impact", 35, "bold"), fg="black", bg="white").place(x=470, y=180)
            Button(cursor="hand2", text="חזור", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="קבצים העלאה", bd=0, command=files, font=("Goudy old style", 15),
                   fg="black").place(x=470, y=300, width=200, height=100)
            Button(cursor="hand2", text="אישור", bd=0, command=prog, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

        def even_t_page():
            Frame(root, bg="white", ).place(x=330, y=150, width=500, height=400)

            def prog():
                ff = []

                def file_copy():
                    with open(fr'C:\Users\{username}\Desktop\FT2_logs.txt') as file:
                        for line in file:
                            ff.append(line)

                def copyx():
                    tt = []
                    with open(fr'C:\Users\{username}\Desktop\FT_logs.txt') as file:
                        for line in file:
                            tt.append(line.strip())

                    for f in ff:
                        print(f)
                        for a in tt:
                            shutil.copy(src=a, dst=f)

                def delete_logs():
                    os.remove(fr'C:\Users\{username}\Desktop\FT_logs.txt')
                    os.remove(fr'C:\Users\{username}\Desktop\FT2_logs.txt')

                file_copy()
                copyx()
                delete_logs()
                messagebox.showinfo(title=None,
                                    message="הקבצים הועברו בהצלחה, לפרטים בנוגע לשעות הלבנה, ניתן לפנות למשוב בית אל - "
                                            "0506235336")
                main_page()

            def files():

                root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                           filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
                path = f"C:/Users/{username}/Desktop/FT_logs.txt"
                if os.path.isfile(path) is True:
                    with open(rf'C:\Users\{username}\Desktop\FT_logs.txt', 'a+') as f:
                        f.write(root.filename + '\n')

                else:
                    open(rf"C:/Users/{username}/Desktop/FT_logs.txt", "a")
                    with open(rf'C:\Users\{username}\Desktop\FT_logs.txt', 'a+') as f:
                        f.write(root.filename + '\n')

            Label(text="אבן & צהלנט", font=("Impact", 35, "bold"), fg="black", bg="white").place(x=470, y=180)
            Button(cursor="hand2", text="חזור", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="קבצים העלאה", bd=0, command=files, font=("Goudy old style", 15),
                   fg="black").place(x=470, y=300, width=200, height=100)
            Button(cursor="hand2", text="אישור", bd=0, command=prog, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

        def idf_t_page():
            Frame(root, bg="white", ).place(x=330, y=150, width=500, height=400)

            def prog():
                ff = []

                def file_copy():
                    with open(fr'C:\Users\{username}\Desktop\FT2_logs.txt') as file:
                        for line in file:
                            ff.append(line)

                def copyx():
                    tt = []
                    with open(fr'C:\Users\{username}\Desktop\FT_logs.txt') as file:
                        for line in file:
                            tt.append(line.strip())

                    for f in ff:
                        print(f)
                        for a in tt:
                            shutil.copy(src=a, dst=f)

                def delete_logs():
                    os.remove(fr'C:\Users\{username}\Desktop\FT_logs.txt')
                    os.remove(fr'C:\Users\{username}\Desktop\FT2_logs.txt')

                file_copy()
                copyx()
                delete_logs()
                messagebox.showinfo(title=None,
                                    message="הקבצים הועברו בהצלחה, לפרטים בנוגע לשעות הלבנה, ניתן לפנות למשוב בית אל - "
                                            "0506235336")
                main_page()

            def files():

                root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                           filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
                path = f"C:/Users/{username}/Desktop/FT_logs.txt"
                if os.path.isfile(path) is True:
                    with open(rf'C:\Users\{username}\Desktop\FT_logs.txt', 'a+') as f:
                        f.write(root.filename + '\n')

                else:
                    open(rf"C:/Users/{username}/Desktop/FT_logs.txt", "a")
                    with open(rf'C:\Users\{username}\Desktop\FT_logs.txt', 'a+') as f:
                        f.write(root.filename + '\n')

            Label(text="אבן & צהלנט", font=("Impact", 35, "bold"), fg="black", bg="white").place(x=470, y=180)
            Button(cursor="hand2", text="חזור", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=600, y=475, width=100, height=40)
            Button(cursor="hand2", text="קבצים העלאה", bd=0, command=files, font=("Goudy old style", 15),
                   fg="black").place(x=470, y=300, width=200, height=100)
            Button(cursor="hand2", text="אישור", bd=0, command=prog, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

        def to_both():
            Frame(self.root, bg="white", ).place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.whoto.place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.name.place(x=470, y=310)

            def create_folder():
                directory_name = self.name.get()
                final = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}")
                if not final:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}")
                directory_whoto = self.whoto.get()
                final2 = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}")
                if not final2:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}")

                a = rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}"
                path = f"C:/Users/{username}/Desktop/FT2_logs.txt"
                if os.path.isfile(path) is True:
                    with open(rf'C:\Users\{username}\Desktop\FT2_logs.txt', 'a+') as f:
                        f.write(a)

                else:
                    open(rf"C:/Users/{username}/Desktop/FT2_logs.txt", "a")
                    with open(rf'C:\Users\{username}\Desktop\FT2_logs.txt', 'a+') as f:
                        f.write(a)
                both_t_page()

            Button(cursor="hand2", text="אישור", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

            Label(text="אבן & צהלנט", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=470, y=180)
            Button(cursor="hand2", text="חזור", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=630, y=475, width=100, height=40)
            Label(text=":השולח שם ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=280)

            Label(text=":הנמען שם ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=350)

        def to_even():
            Frame(self.root, bg="white", ).place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.whoto.place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.name.place(x=470, y=310)

            def create_folder():
                directory_name = self.name.get()
                final = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}")
                if not final:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}")
                directory_whoto = self.whoto.get()
                final2 = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}")
                if not final2:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}")

                a = rf"\\mnhazfs\nonword\halbanot\Both\{directory_name}\{directory_whoto}"
                path = f"C:/Users/{username}/Desktop/FT2_logs.txt"
                if os.path.isfile(path) is True:
                    with open(rf'C:\Users\{username}\Desktop\FT2_logs.txt', 'a+') as f:
                        f.write(a)

                else:
                    open(rf"C:/Users/{username}/Desktop/FT2_logs.txt", "a")
                    with open(rf'C:\Users\{username}\Desktop\FT2_logs.txt', 'a+') as f:
                        f.write(a)
                both_t_page()

            Button(cursor="hand2", text="אישור", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

            Label(text="אבן", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=530, y=180)
            Button(cursor="hand2", text="חזור", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=630, y=475, width=100, height=40)
            Label(text=":השולח שם ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=280)

            Label(text=":הנמען שם ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=350)

        def to_idf():
            Frame(self.root, bg="white", ).place(x=330, y=150, width=500, height=400)
            self.whoto = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.whoto.place(x=470, y=390)
            self.name = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.name.place(x=470, y=310)

            def create_folder():
                directory_name = self.name.get()
                final = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}")
                if not final:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}")
                directory_whoto = self.whoto.get()
                final2 = os.path.isdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}\{directory_whoto}")
                if not final2:
                    os.mkdir(rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}\{directory_whoto}")

                a = rf"\\mnhazfs\nonword\halbanot\IDF\{directory_name}\{directory_whoto}"
                path = f"C:/Users/{username}/Desktop/FT2_logs.txt"
                if os.path.isfile(path) is True:
                    with open(rf'C:\Users\{username}\Desktop\FT2_logs.txt', 'a+') as f:
                        f.write(a)

                else:
                    open(rf"C:/Users/{username}/Desktop/FT2_logs.txt", "a")
                    with open(rf'C:\Users\{username}\Desktop\FT2_logs.txt', 'a+') as f:
                        f.write(a)
                both_t_page()

            Button(cursor="hand2", text="אישור", bd=0, command=create_folder, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=450, y=475, width=100, height=40)

            Label(text="צהלנט", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=470, y=180)
            Button(cursor="hand2", text="חזור", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=630, y=475, width=100, height=40)
            Label(text=":השולח שם ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=280)

            Label(text=":הנמען שם ", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
                x=520, y=350)

        main_page()


root = Tk()

bg_pic = Image.open("idk.jpg")
resized = bg_pic.resize((1199, 850), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resized)
label_bgImage = Label(root, image=bg)
label_bgImage.place(x=0, y=0)
obj = Login(root)
root.mainloop()
