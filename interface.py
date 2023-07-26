from tkinter import messagebox
import mainFile
import tkinter as tk


def Evaluate_System():
    def check_input():
        if pathText.get() == '' or criteriontypeText.get() == '' or float(trainText.get()) == 0 or float(
                trainText.get()) < 0 or float(trainText.get()) > 0.99 or float(testText.get()) == 0 or float(
                testText.get()) < 0 or float(testText.get()) > 0.99:
            messagebox.showinfo("ERROR", "invalid Or Messing  Inputs")

        else:
            printopt = messagebox.askyesno("Confirmation", "Do you Save Tree Figur ?", )
            acc, cv10, cv5, cv3 = mainFile.main_function(pathText.get(), criteriontypeText.get(),
                                                         float(trainText.get()), float(testText.get()), printopt)

            root3 = tk.Tk()
            root3.geometry("500x400")
            root3.title("IDS")
            root3.resizable(False, False)
            root3.positionfrom()
            root3.config(bg="#D1D1D1")

            # widgets
            header_label3 = tk.Label(root3, text="IDS Using Decision Tree", fg="#FF0000", bg="#B8B8B8")
            acc_label = tk.Label(root3, text='Accuracy:' + str(acc)[:4] + '%', fg="#134991", bg="#D1D1D1")
            cv10_label = tk.Label(root3, text='Cross Validation(10):' + str(cv10)[:4], fg="#134991", bg="#D1D1D1")
            cv5_label = tk.Label(root3, text='Cross Validation(5):' + str(cv5)[:4], fg="#134991", bg="#D1D1D1")
            cv3_label = tk.Label(root3, text='Cross Validation(3):' + str(cv3)[:4], fg="#134991", bg="#D1D1D1")

            # config
            header_label3.config(font=("Georgia", 20))
            acc_label.config(font=("Georgia", 16))
            cv10_label.config(font=("Georgia", 16))
            cv5_label.config(font=("Georgia", 16))
            cv3_label.config(font=("Georgia", 16))
            # place
            header_label3.pack(anchor="center", pady=10, side='top')
            acc_label.pack(anchor="center", pady=20)
            cv10_label.pack(anchor="center", pady=20)
            cv5_label.pack(anchor="center", pady=20)
            cv3_label.pack(anchor="center", pady=20)
            root3.mainloop()

    root2 = tk.Tk()
    root2.geometry("600x600")
    root2.title("IDS")
    root2.resizable(False, False)
    root2.positionfrom()
    root2.config(bg="#D1D1D1")

    # widgets
    header_label2 = tk.Label(root2, text="IDS Using Decision Tree", fg="#FF0000", bg="#B8B8B8")
    header_label2.config(font=("Georgia", 20))
    header_label2.pack(anchor="center", pady=10)

    pathLabel = tk.Label(root2, text="Upload DataSet", fg="#134991", bg="#D1D1D1")
    pathLabel.config(font=("Georgia", 16))
    pathLabel.pack(anchor="center", pady=10)

    pathText = tk.Entry(root2)
    pathText.config(font=("Georgia", 14), bg="#B8B8B8")
    pathText.pack(anchor="center", pady=10)

    criteriontypeLabel = tk.Label(root2, text="Impurity Measure", fg="#134991", bg="#D1D1D1")
    criteriontypeLabel.config(font=("Georgia", 16))
    criteriontypeLabel.pack(anchor="center", pady=10)

    criteriontypeText = tk.Entry(root2)
    criteriontypeText.config(font=("Georgia", 14), bg="#B8B8B8")
    criteriontypeText.pack(anchor="center", pady=10)

    trainLabel = tk.Label(root2, text="Train Split Size", fg="#134991", bg="#D1D1D1")
    trainLabel.config(font=("Georgia", 16))
    trainLabel.pack(anchor="center", pady=10)

    trainText = tk.Entry(root2)
    trainText.config(font=("Georgia", 14), bg="#B8B8B8")
    trainText.pack(anchor="center", pady=10)

    testLabel = tk.Label(root2, text="Test Split Size", fg="#134991", bg="#D1D1D1")
    testLabel.config(font=("Georgia", 16))
    testLabel.pack(anchor="center", pady=10)

    testText = tk.Entry(root2)
    testText.config(font=("Georgia", 14), bg="#B8B8B8")
    testText.pack(anchor="center", pady=10)

    button2 = tk.Button(root2, text="Run",
                        command=check_input, bg="#D1D1D1", activebackground="#B8B8B8", fg="#1B8F3D")
    button2.config(font=("Georgia", 20))
    button2.pack(anchor="e", pady=30)

    root.destroy()
    root2.mainloop()


def Test_Individual_Sample():
    def check_input():
        if pathText.get() == '' or criteriontypeText.get() == '' or path2Text.get() == '':
            messagebox.showinfo("ERROR", "invalid Or Messing  Inputs")

        else:

            predections = mainFile.indvisual_scan(pathText.get(), criteriontypeText.get(), path2Text.get())

            root3 = tk.Tk()
            root3.geometry("450x200")
            root3.title("IDS")
            root3.resizable(False, True)
            root3.positionfrom()
            root3.config(bg="#D1D1D1")
            # widgets
            header_label3 = tk.Label(root3, text="IDS Using Decision Tree", fg="#FF0000", bg="#B8B8B8")
            prediction = ""
            for c, i in zip(range(len(predections)), predections):
                prediction += str(c + 1) + "-" + i + "\n"

            predections_label = tk.Label(root3, text='Decisions:\n' + prediction, fg="#134991", bg="#D1D1D1")

            # config
            header_label3.config(font=("Georgia", 20))
            predections_label.config(font=("Georgia", 16))

            # place
            header_label3.pack(anchor="center", pady=10, side='top')
            predections_label.pack(pady=20, anchor="nw")

            root3.mainloop()

    root2 = tk.Tk()
    root2.geometry("600x480")
    root2.title("IDS")
    root2.resizable(False, False)
    root2.positionfrom()

    header_label2 = tk.Label(root2, text="IDS Using Decision Tree", fg="#FF0000", bg="#B8B8B8")
    pathLabel = tk.Label(root2, text="Upload Training DataSet", fg="#134991", bg="#D1D1D1")
    pathText = tk.Entry(root2)
    criteriontypeLabel = tk.Label(root2, text="Impurity Measure ", fg="#134991", bg="#D1D1D1")
    criteriontypeText = tk.Entry(root2)
    path2Label = tk.Label(root2, text="Upload Testing DataSet", fg="#134991", bg="#D1D1D1")
    path2Text = tk.Entry(root2)
    button2 = tk.Button(root2, text="Run",
                        command=check_input, bg="#D1D1D1", activebackground="#B8B8B8", fg="#1B8F3D")

    # config
    root2.config(bg="#D1D1D1")
    header_label2.config(font=("Georgia", 20))
    pathLabel.config(font=("Georgia", 16))
    pathText.config(font=("Georgia", 14), bg="#B8B8B8")
    criteriontypeLabel.config(font=("Georgia", 16))
    criteriontypeText.config(font=("Georgia", 14), bg="#B8B8B8")

    path2Label.config(font=("Georgia", 16))
    path2Text.config(font=("Georgia", 14), bg="#B8B8B8")
    button2.config(font=("Georgia", 20))

    header_label2.pack(anchor="center", pady=10)
    pathLabel.pack(anchor="center", pady=10)
    pathText.pack(anchor="center", pady=10)
    criteriontypeLabel.pack(anchor="center", pady=10)
    criteriontypeText.pack(anchor="center", pady=10)

    path2Label.pack(anchor="center", pady=10)
    path2Text.pack(anchor="center", pady=10)

    button2.pack(anchor="e", pady=30)
    root.destroy()
    root2.mainloop()


root = tk.Tk()
root.geometry("500x350")
root.title("IDS")
root.config(bg="#D1D1D1")
root.resizable(False, False)
root.positionfrom()
header_label = tk.Label(root, text="IDS Using Decision Tree", fg="#FF0000", bg="#B8B8B8")
header_label.config(font=("Georgia", 20))
# widgets
button6 = tk.Button(root, text="Evaluate The System", command=Evaluate_System, bg="#D1D1D1", activebackground="#B8B8B8",
                    fg="#0D3162")
button7 = tk.Button(root, text="Test Individual Sample", command=Test_Individual_Sample, bg="#D1D1D1",
                    activebackground="#B8B8B8",
                    fg="#0D3162")

st_label = tk.Label(root, text="Abbas Ghasan Noury Jreou", fg="#134991", bg="#D1D1D1")
st_label.config(font=("Georgia", 14))
sp_label = tk.Label(root, text="Supervised by: Prof. Dr. Iman Salih Alshamery", fg="#134991", bg="#D1D1D1")
sp_label.config(font=("Georgia", 14))
button6.config(font=("Georgia", 14))
button7.config(font=("Georgia", 14))

# place of widgets
header_label.pack(pady=10, anchor="center", side="top")
button6.pack(pady=20, anchor="center")
button7.pack(pady=20, anchor="center")
sp_label.pack(anchor="center", pady=10, side="bottom")
st_label.pack(anchor="center", pady=10, side="bottom")
root.mainloop()
