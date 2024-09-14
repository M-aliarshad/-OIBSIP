import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Create a database connection
def create_connection():
    conn = sqlite3.connect('bmi_data.db')
    return conn

# Create a table for storing BMI data
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                      (id INTEGER PRIMARY KEY, weight REAL, height REAL, bmi REAL)''')
    conn.commit()
    conn.close()

def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
        
        save_to_db(weight, height, bmi)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def save_to_db(weight, height, bmi):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bmi_records (weight, height, bmi) VALUES (?, ?, ?)", (weight, height, bmi))
    conn.commit()
    conn.close()
    
def view_history():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bmi_records")
    records = cursor.fetchall()
    conn.close()
    
    if records:
        weights, heights, bmis = zip(*[(r[1], r[2], r[3]) for r in records])
        plt.plot(bmis, label='BMI Trend')
        plt.xlabel('Record Number')
        plt.ylabel('BMI')
        plt.title('BMI Trend Over Time')
        plt.legend()
        plt.show()
    else:
        messagebox.showinfo("History", "No records found.")

# Create the main window
root = tk.Tk()
root.title("Ali's BMI Calculator")
root.geometry("300x300")

create_table()

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text= "Calculate", command=calculate )

calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

history_button = tk.Button(root, text="View History", command=view_history)
history_button.pack()

root.mainloop()