#  Jesse Terblanche

#  Importing tkinter library
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#  To create the root, add a title to it and customize it
root = tk.Tk()
root.title("Ticket Sales")
root.geometry("400x600")
root.resizable(0, 0)
root.config(bg="#aeb6bf")


#  class for all objects and functionality
class ClsTicketSales:
    def __init__(self, master):
        #  2 frames to keep different sections of the program
        frame1 = Frame(master, width=350, height=350, bg="#5d6d7e")
        frame1.place(x=25, y=20)
        frame2 = Frame(master, width=350, height=200, bg="#5d6d7e")
        frame2.place(x=25, y=380)
        
        #  Label and entry field for cellphone number
        self.cellLabel = Label(frame1, text="Enter cell number", bg="#5d6d7e")
        self.cellLabel.place(x=10, y=20)
        self.cellnumber = Entry(frame1, bg="#d6dbdf")
        self.cellnumber.place(x=150, y=20)

        #  prices for types of tickets
        self.stprice = 40.00
        self.mtprice = 75.00
        self.thprice = 100.00

        #  select box for type of ticket
        self.options = ["Soccer", "Movie", "Theater"]
        self.option = StringVar(root)
        self.option.set("Select")
        self.selectlabel = Label(frame1, text="Select Category", bg="#5d6d7e")
        self.selectlabel.place(x=10, y=65)
        self.select = OptionMenu(frame1, self.option, *self.options)
        self.select.place(x=150, y=60)
        
        #  Spinbox for selecting number of tickets
        self.nrticketslabel = Label(frame1, text="Select number of tickets", bg="#5d6d7e")
        self.nrticketslabel.place(x=10, y=120)
        self.nrTickets = Spinbox(frame1, width=8, from_=0, to=100, bg="#d6dbdf")
        self.nrTickets.place(x=180, y=120)

        #  button to calculate total and display info about purchase
        self.calculatebtn = Button(frame1, text="Calculate Ticket", command=self.calcprepayment)
        self.calculatebtn.place(x=10, y=200)

        #  button to clear all fields
        self.clearbtn = Button(frame1, text="Clear All", command=self.clear)
        self.clearbtn.place(x=230, y=200)

        #  field for purchase info to be displayed in
        self.line1 = Label(frame2, text="~~~~~~~~~~~~~~~~~~~~~~~~~~", bg="#5d6d7e", fg="#aeb6bf")
        self.line1.place(x=30, y=20)
        self.line2 = Label(frame2, text=" ", bg="#5d6d7e")
        self.line2.place(x=30, y=50)
        self.line3 = Label(frame2, text=" ", bg="#5d6d7e")
        self.line3.place(x=30, y=90)
        self.line4 = Label(frame2, text=" ", bg="#5d6d7e")
        self.line4.place(x=30, y=130)
        self.line5 = Label(frame2, text="~~~~~~~~~~~~~~~~~~~~~~~~~~", bg="#5d6d7e", fg="#aeb6bf")
        self.line5.place(x=30, y=160)

    #  method for calculation of total and errortrapping if invalid input is given
    def calcprepayment(self):
        #  if valid inputs are given, conditionals to display purchase info based on selected option
        try:
            if self.option.get() == "Soccer":
                cellphone = int(self.cellnumber.get())
                soccerpr = float(self.stprice)
                tickets = float(self.nrTickets.get())
                total = soccerpr * tickets
                vat = (total * 14/100)
                result = total + vat
                self.line2.config(text="Amount payable: R" + str(result))
                self.line3.config(text="Reservation for " + self.option.get() + " for " + str(self.nrTickets.get()))
                self.line4.config(text="Was done by " + str(cellphone))
            elif self.option.get() == "Movie":
                cellphone = int(self.cellnumber.get())
                moviepr = float(self.mtprice)
                tickets = float(self.nrTickets.get())
                total = moviepr * tickets
                vat = (total * 14 / 100)
                result = total + vat
                self.line2.config(text="Amount payable: R" + str(result))
                self.line3.config(text="Reservation for " + self.option.get() + " for " + str(self.nrTickets.get()))
                self.line4.config(text="Was done by " + str(cellphone))
            elif self.option.get() == "Theater":
                cellphone = int(self.cellnumber.get())
                theaterpr = float(self.thprice)
                tickets = float(self.nrTickets.get())
                total = theaterpr * tickets
                vat = (total * 14 / 100)
                result = total + vat
                self.line2.config(text="Amount payable: R" + str(result))
                self.line3.config(text="Reservation for " + self.option.get() + " for " + str(self.nrTickets.get()))
                self.line4.config(text="Was done by " + str(cellphone))

        #  if invalid input is given, error messagebox shows
        except ValueError:
            messagebox.showerror("error", "Invalid input. Please try again.")
            self.cellnumber.delete(0, END)
            self.nrTickets.delete(0, END)
            self.line2.config(text="")
            self.line3.config(text="")
            self.line4.config(text="")

    #  method to clear fields
    def clear(self):
        self.cellnumber.delete(0, END)
        self.option.set("Select")
        self.nrTickets.delete(0, END)
        self.line2.config(text="")
        self.line3.config(text="")
        self.line4.config(text="")


#  puts objects on screen
c = ClsTicketSales(root)
root.mainloop()
