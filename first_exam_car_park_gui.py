#first_exam_car_park_gui.py

import tkinter as tk
from tkinter import messagebox
from first_exam_car_park_functions import FirstExamCarPark

class FirstExamCarParkGUI:
    def __init__(self, root):
        self.this_car_park = FirstExamCarPark()
        self.root = root
        self.root.title("FIRSTEXAMCARPARK SIMULATOR")

        # Labels for input entry fields
        self.instruction_welcome = tk.Label(root, text="WELCOME TO FIRST EXAM CAR PARK", padx=10, pady=10)
        self.instruction_welcome.grid(row=0, column=1, padx=10,pady=10)

        self.instruction_entry_and_exit = tk.Label(root, text="Car Registration Number format--AB12 CDE", padx=10, pady=5)
        self.instruction_entry_and_exit.grid(row=0, column=0, padx=10,pady=5)

        self.car_reg_label = tk.Label(root, text="Car Registration Number:", padx=10, pady=5)
        self.car_reg_label.grid(row=1, column=0, padx=10, pady=10)

        self.car_reg_label = tk.Label(root, text="Car Registration Number:", padx=10, pady=5)
        self.car_reg_label.grid(row=2, column=0, padx=10, pady=10)

        self.ticket_label = tk.Label(root, text="Ticket Number:", padx=10, pady=5)
        self.ticket_label.grid(row=3, column=0, padx=10, pady=10)

        # Entry field for car registration number
        self.car_reg_entry1 = tk.Entry(root, width=30)
        self.car_reg_entry1.grid(row=1, column=1, padx=10, pady=10)

        # Button for entering the car park
        self.enter_button = tk.Button(root, text="Enter the Car Park", command=self.EnterCarPark, bg="#4CAF50", fg="black", padx=10, pady=5, relief=tk.GROOVE)
        self.enter_button.grid(row=1, column=3, columnspan=9, padx=10, pady=10)

        # Entry field for car registration number
        self.car_reg_entry2 = tk.Entry(root, width=30)
        self.car_reg_entry2.grid(row=2, column=1, padx=10, pady=10)

        # Button for exiting the car park
        self.exit_button = tk.Button(root, text="Exit the Car Park", command=self.ExitCarPark, bg="#FF5733", fg="black", padx=10, pady=5, relief=tk.GROOVE)
        self.exit_button.grid(row=2, column=3, padx=10, pady=10)

        # Entry field for search value
        self.checkValue = tk.Entry(root, width=30)
        self.checkValue.grid(row=3, column=1, padx=10, pady=10)

        # Button for searching parking records by ticket number
        self.searchButton = tk.Button(root, text="Query Parking Record", command=self.Query_Parking_Record_by_TicketNumber, bg="#8e44ad", fg="black", padx=10, pady=5, relief=tk.GROOVE)
        self.searchButton.grid(row=3, column=3, padx=10, pady=10)

        # Button for displaying available parking spaces
        self.available_spaces_button = tk.Button(root, text="View Available Parking Spaces", command=self.ViewAvailableParkingSpaces, bg="#3498db", fg="black", padx=10, pady=5, relief=tk.GROOVE)
        self.available_spaces_button.grid(row=4, column=3, padx=10, pady=10)

        # Button for exiting the program
        self.quitGui_button = tk.Button(root, text="Exit Program", command=self.quitGui, bg="#c0392b", fg="black", padx=10, pady=5, relief=tk.GROOVE)
        self.quitGui_button.grid(row=5, column=3, padx=10, pady=10)

        self.instruction_quit = tk.Label(root, text="We hope to see you again soon.", padx=10, pady=10)
        self.instruction_quit.grid(row=5, column=1, padx=10,pady=10)


    def EnterCarPark(self):
        reg_number = self.car_reg_entry1.get()
        
        if not reg_number:
            messagebox.showerror("Error", "Car registration number cannot be empty.")
            return

        result = self.this_car_park.Enter_the_Car_Park(reg_number)
        messagebox.showinfo("Result", result)
        # self.updateOutputScreen()

    def ExitCarPark(self):
        reg_number = self.car_reg_entry2.get()
        
        if not reg_number:
            messagebox.showerror("Error", "Car registration number cannot be empty.")
            return

        result = self.this_car_park.Exit_the_Car_Park(reg_number)
        messagebox.showinfo("Result", result)
        # self.updateOutputScreen()

    def ViewAvailableParkingSpaces(self):
        available_spaces = self.this_car_park.AvailableParkingSpace()
        messagebox.showinfo("Available Spaces", f"Available Parking Spaces: {len(available_spaces)}")

    def Query_Parking_Record_by_TicketNumber(self):
        value = self.checkValue.get()
        result = self.this_car_park.Query_Parking_Record_by_TicketNumber(value)
        messagebox.showinfo("Query Parking Record", f"Parking Records for Ticket Number {value}:\n{result}")
        # self.updateOutputScreen()

    def quitGui(self):
        self.this_car_park.UpdateParkDetails() 
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FirstExamCarParkGUI(root)
    root.mainloop()   
