import tkinter as tk
from tkinter import messagebox
import mysql.connector

def submit_data():
    name = entry_name.get()
    gender = entry_gender.get()
    title = entry_title.get()
    year_of_title = entry_year.get()
    salary = entry_salary.get()
    city = entry_city.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Divyanshu@123*",
            database="sports"
        )
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO chessgmform (Name, Gender, Title, Year_of_Title, Salary, City)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (name, gender, title, int(year_of_title), float(salary), city)
        cursor.execute(insert_query, data)
        connection.commit()

        messagebox.showinfo("Success", "Data inserted successfully.")
        clear_fields()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database Error: {err}")
    finally:
        cursor.close()
        connection.close()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_city.delete(0, tk.END)

# GUI using tkinter
root = tk.Tk()
root.title("Chess GM Registration Form")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Gender").grid(row=1, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=1, column=1)

tk.Label(root, text="Title").grid(row=2, column=0)
entry_title = tk.Entry(root)
entry_title.grid(row=2, column=1)

tk.Label(root, text="Year of Title").grid(row=3, column=0)
entry_year = tk.Entry(root)
entry_year.grid(row=3, column=1)

tk.Label(root, text="Salary").grid(row=4, column=0)
entry_salary = tk.Entry(root)
entry_salary.grid(row=4, column=1)

tk.Label(root, text="City").grid(row=5, column=0)
entry_city = tk.Entry(root)
entry_city.grid(row=5, column=1)

submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.grid(row=6, column=1, pady=10)

root.mainloop()
