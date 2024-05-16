import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import defaultdict
import os

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        # Variables for user input
        self.weight = tk.DoubleVar()
        self.height = tk.DoubleVar()
        self.bmi_result = tk.StringVar()

        # Create user interface elements
        tk.Label(master, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(master, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(master, textvariable=self.weight).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(master, textvariable=self.height).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(master, text="Calculate BMI", command=self.calculate_bmi).grid(row=2, columnspan=2)

        # Display BMI result
        tk.Label(master, text="BMI Result:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(master, textvariable=self.bmi_result).grid(row=3, column=1, padx=10, pady=10)

        # Buttons for data storage and analysis
        tk.Button(master, text="Save Data", command=self.save_data).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(master, text="View History", command=self.view_history).grid(row=4, column=1, padx=10, pady=10)

        # Initialize data storage
        self.data_file = "bmi_data.txt"
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w'):
                pass
        self.data = defaultdict(list)
        self.load_data()

    def calculate_bmi(self):
        weight = self.weight.get()
        height = self.height.get()
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive numbers.")
            return
        bmi = weight / (height ** 2)
        self.bmi_result.set(f"{bmi:.2f}")

    def save_data(self):
        weight = self.weight.get()
        height = self.height.get()
        bmi = float(self.bmi_result.get())
        self.data["Weight"].append(weight)
        self.data["Height"].append(height)
        self.data["BMI"].append(bmi)
        with open(self.data_file, 'a') as file:
            file.write(f"{weight},{height},{bmi}\n")
        messagebox.showinfo("Data Saved", "BMI data saved successfully.")

    def view_history(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data["BMI"], marker='o', linestyle='-')
        plt.title("BMI History")
        plt.xlabel("Measurement")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.show()

    def load_data(self):
        with open(self.data_file, 'r') as file:
            for line in file:
                weight, height, bmi = map(float, line.strip().split(','))
                self.data["Weight"].append(weight)
                self.data["Height"].append(height)
                self.data["BMI"].append(bmi)

def main():
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
