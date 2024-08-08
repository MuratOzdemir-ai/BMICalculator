from tkinter import *
from tkinter import messagebox

def get_height():
    height = float(ENTRY2.get())
    return height

def get_weight():
    weight = float(ENTRY1.get())
    return weight

def calculate_bmi(a=""):
    print(a)
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)

    except ValueError:
        messagebox.showinfo("Result", "Enter a valid number!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Obesity(Class I)!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Obesity(Class II)!!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Extreme Obesity!!!"
            messagebox.showinfo("Result", res)


if __name__ == '__main__':
    My = Tk()
    My.bind("<Return>", calculate_bmi)
    My.geometry("375x375")
    My.configure(background="#DEB887")
    My.title("BMI Calculator")
    My.resizable(width=False, height=False)
    LABEL = Label(My, bg="#DEB887", text="BMI CALCULATOR", font=("Helvetica", 15, "bold"), pady=10)
    LABEL.place(x=100, y=0)
    LABEL1 = Label(My, bg="#DEB887", text="Enter Weight (kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABEL1.place(x=55, y=60)
    ENTRY1 = Entry(My, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABEL2 = Label(My, bg="#DEB887", text="Enter Height (cm):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABEL2.place(x=55, y=121)
    ENTRY2 = Entry(My, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bg="#F8F8FF", bd=12, text="BMI", padx=33, pady=20, command=calculate_bmi,
                    font=("Helvetica", 18, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)

    My.mainloop()

