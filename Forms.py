from tkinter import messagebox

import mainFile
import tkinter as tk


def start_project():
    def check_input():
        if pathText.get() == '' or criteriontypeText.get() == '' or float(trainText.get()) == 0 or float(
                trainText.get()) < 0 or float(trainText.get()) > 0.99 or float(testText.get()) == 0 or float(
                testText.get()) < 0 or float(testText.get()) > 0.99:
            messagebox.showinfo("ERROR", "invalid Inputs")
        else:
            acc, cv10, cv5, cv3 = mainFile.main_function(pathText.get(), criteriontypeText.get(),
                                                         float(trainText.get()), float(testText.get()))


            root3 = tk.Tk()
            root3.geometry("700x600")
            root3.title("IDS")
            root3.resizable(False, False)
            root3.positionfrom("user")
            root3.config(bg="#536B78")


            # widgets
            header_label3 = tk.Label(root3, text="IDS Using Machine Learning", fg="#CEE5F2", bg="#536B78")

            acc_label = tk.Label(root3, text='Accuracy:' + str(acc) + '%', fg="#CEE5F2", bg="#536B78")
            cv10_label = tk.Label(root3, text='Cross Validation(10):' + str(cv10), fg="#CEE5F2", bg="#536B78")
            cv5_label = tk.Label(root3, text='Cross Validation(5):' + str(cv5), fg="#CEE5F2", bg="#536B78")
            cv3_label = tk.Label(root3, text='Cross Validation(3):' + str(cv3), fg="#CEE5F2", bg="#536B78")

            # config
            header_label3.config(font=("Century Gothic (Body)", 20))
            acc_label.config(font=("Century Gothic (Body)", 16))
            cv10_label.config(font=("Century Gothic (Body)", 16))
            cv5_label.config(font=("Century Gothic (Body)", 16))
            cv3_label.config(font=("Century Gothic (Body)", 16))
            # place
            header_label3.pack(anchor="center", pady=10, side='top')
            acc_label.pack(anchor="center", pady=20)
            cv10_label.pack(anchor="center", pady=20)
            cv5_label.pack(anchor="center", pady=20)
            cv3_label.pack(anchor="center", pady=20)
            root3.mainloop()

    root2 = tk.Tk()
    root2.geometry("700x600")
    root2.title("IDS")
    root2.resizable(False, False)
    root2.positionfrom("user")

    # widgets
    header_label2 = tk.Label(root2, text="IDS Using Machine Learning", fg="#CEE5F2", bg="#536B78")
    pathLabel = tk.Label(root2, text="Enter Path Of DataSet :", fg="#CEE5F2", bg="#536B78")
    pathText = tk.Entry(root2)
    criteriontypeLabel = tk.Label(root2, text="Enter Criterion Type :", fg="#CEE5F2", bg="#536B78")
    criteriontypeText = tk.Entry(root2)
    trainLabel = tk.Label(root2, text="Enter Train Size :", fg="#CEE5F2", bg="#536B78")
    trainText = tk.Entry(root2)
    testLabel = tk.Label(root2, text="Enter Test Size :", fg="#CEE5F2", bg="#536B78")
    testText = tk.Entry(root2)
    button2 = tk.Button(root2, text="Run",
                        command=check_input, bg="#536B78", activebackground="#536B78")

    # config
    root2.config(bg="#536B78")
    header_label2.config(font=("Century Gothic (Body)", 20))
    pathLabel.config(font=("Century Gothic (Body)", 16))
    pathText.config(font=("Century Gothic (Body)", 16))
    criteriontypeLabel.config(font=("Century Gothic (Body)", 16))
    criteriontypeText.config(font=("Century Gothic (Body)", 16))
    trainLabel.config(font=("Century Gothic (Body)", 16))
    trainText.config(font=("Century Gothic (Body)", 16))
    testLabel.config(font=("Century Gothic (Body)", 16))
    testText.config(font=("Century Gothic (Body)", 16))
    button2.config(font=("Century Gothic (Body)", 24))

    # remove first form
    root.destroy()
    # place
    header_label2.pack(anchor="center", pady=10)
    pathLabel.pack(anchor="w", pady=10)
    pathText.pack(anchor="w", pady=10)
    criteriontypeLabel.pack(anchor="w", pady=10)
    criteriontypeText.pack(anchor="w", pady=10)
    trainLabel.pack(anchor="w", pady=10)
    trainText.pack(anchor="w", pady=10)
    testLabel.pack(anchor="w", pady=10)
    testText.pack(anchor="w", pady=10)
    button2.pack(anchor="center", pady=30)

    root2.mainloop()


root = tk.Tk()
root.geometry("700x600")
root.title("IDS")
root.config(bg="#536B78")
root.resizable(False, False)
root.positionfrom("user")
header_label = tk.Label(root, text="IDS Using Machine Learning", fg="#CEE5F2", bg="#536B78")
header_label.config(font=("Century Gothic (Body)", 20))

# widgets
button = tk.Button(root, text="Start", command=start_project, bg="#536B78", activebackground="#536B78")
button.config(font=("Century Gothic (Body)", 24))
st_label = tk.Label(root, text="Created by: Abbas Ghasan Noury Jreou", fg="#CEE5F2", bg="#536B78")
st_label.config(font=("Century Gothic (Body)", 14))
sp_label = tk.Label(root, text="Supervised by: Prof. Dr. Iman Salih Sakban", fg="#CEE5F2", bg="#536B78")
sp_label.config(font=("Century Gothic (Body)", 14))

# place of widgets
header_label.pack(pady=10, anchor="center", side="top")
button.pack(pady=70, anchor="center", side="top")
sp_label.pack(anchor="w", pady=10, side="bottom")
st_label.pack(anchor="w", pady=10, side="bottom")

root.mainloop()
