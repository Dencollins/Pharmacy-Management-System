from tkinter import *
import tkinter
import mysql.connector
from ttkbootstrap import Style
import customtkinter as custom
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import PhotoImage
import ttkbootstrap as bootstrap
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from tkinter import ttk

custom.set_appearance_mode("light")
custom.set_default_color_theme("blue")


# newpage
def button_function():
    first_page.destroy()

    root = bootstrap.Window(themename="yeti")
    root.title = "BENORA DASHBOARD"
    root.state("zoomed")  # Maximize the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    colors = root.style.colors

    # Create a function to open different sections in frame2
    def open_section(section_func):
        # Clear the current content of frame2
        for widget in frame2.winfo_children():
            widget.destroy()
        # Call the provided section function to populate frame2
        section_func()

    # fuctions
    def open_dashboard():
        frame3 = bootstrap.Frame(frame2, bootstyle="dark")
        frame3.pack(fill="both", expand=True, padx=10, pady=10)

        # Create a Text widget to display the text
        text = """                                                                                                                               !! ABOUT BENORA CHEMIST !!
        
            Nestled within the scenic landscapes of Narok County, Kenya, stands a pillar of healthcare excellence—Benora Chemist. For over two illustrious decades, Benora Chemist has transcended its mere existence as a pharmacy, evolving into a revered institution, an integral part of the region's healthcare tapestry, and an indispensable guardian of community wellness.

            Founded over 20 years ago, Benora Chemist embarked on a journey rooted in a profound commitment to serve. It commenced its humble inception with a fervent mission to provide essential medications and healthcare supplies, catering to the diverse needs of the local populace. Through the passage of time, it blossomed into a sanctuary of health, a beacon of hope, and a trusted sanctuary for countless individuals and families across Narok County.

            The very essence of Benora Chemist lies not only in its longevity but in the immeasurable impact it has imprinted upon the community. It has transformed into an enduring cornerstone, etching its narrative into the collective consciousness of Narok County's inhabitants.

            The chemist's legacy spans beyond the mere dispensing of medications. It has cultivated a culture of care, compassion, and trust, forging enduring relationships with patrons who regard it not just as a commercial entity but as an ally in their well-being journey. Families have relied upon its unwavering presence during times of health challenges, finding solace in the expertise and empathy dispensed along with the pharmaceuticals.

            Benora Chemist's significance radiates beyond the physical realm of its establishment. It symbolizes dedication and reliability, a testament to resilience amid the dynamic landscape of healthcare. Its walls resonate with stories of triumphs, healing, and the embodiment of community spirit.

            Through the years, the chemist has evolved, embracing innovation, and adapting to the evolving needs of a burgeoning community. It stands as a testament to resilience, navigating through healthcare revolutions, epidemics, and societal changes, steadfast in its commitment to serve with excellence.

            Moreover, the impact of Benora Chemist extends beyond the peripheries of healthcare provision. It has actively participated in community health initiatives, offering educational programs, health screenings, and outreach services, amplifying its role as a catalyst for well-being enhancement.

            The Chemist's ethos reverberates in every interaction, echoing the virtues of reliability and care. Its team, composed of dedicated healthcare professionals, exudes empathy and expertise, instilling confidence and assurance in every consultation, cementing its status as a trusted confidant in health-related matters.

            Furthermore, Benora Chemist's commitment to quality service is unrivaled. It has diligently curated a spectrum of essential medications, health supplies, and professional guidance, ensuring accessibility and efficacy in every prescription filled.

            In essence, Benora Chemist's legacy is not just about bricks and mortar but about the profound impact it has made in the lives of Narok County's inhabitants. It signifies perseverance, compassion, and a relentless pursuit of wellness. It stands tall, not just as a pharmacy but as an enduring testament to the unwavering spirit of healthcare excellence.
            
                                                                                                                                    !! WELCOME !!"""

        text_widget = tkinter.Text(
            frame3, wrap=tkinter.WORD, height=20, width=80, padx=10, pady=10
        )
        text_widget.insert(tkinter.END, text)
        text_widget.config(state=tkinter.DISABLED)  # Make the Text widget read-only
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

    def open_invoice():
        frame_invoice = bootstrap.Frame(frame2, bootstyle="dark")
        frame_invoice.pack(fill="both", expand=True, padx=10, pady=10)

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select["Med_id"])
            e2.insert(0, select["Medicine"])
            e3.insert(0, select["Company"])
            e4.insert(0, select["Quantity"])
            e5.insert(0, select["Price"])

        def Add():
            iMed_id = e1.get()
            iMedicine = e2.get()
            iCompany = e3.get()
            # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()
            if quantity_value:
                try:
                    iQuantity = int(quantity_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
                # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()

            # Validate and convert Quantity (e4) to integer
            price_value = e5.get()
            if price_value:
                try:
                    iPrice = int(price_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
            price_value = e5.get()
            iTotal_Price = iQuantity * iPrice

            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "INSERT INTO invoice_table (Med_id,Medicine,Company,Quantity,Price,Total_Price) VALUES (%s, %s, %s, %s, %s,%s)"
                val = (
                    iMed_id,
                    iMedicine,
                    iCompany,
                    iQuantity,
                    iPrice,
                    iTotal_Price,
                )
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Data inserted successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
                show()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            iMed_id = e1.get()
            iMedicine = e2.get()
            iCompany = e3.get()

            # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()
            if quantity_value:
                try:
                    iQuantity = int(quantity_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
                # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()

            # Validate and convert Quantity (e4) to integer
            price_value = e4.get()
            if price_value:
                try:
                    iPrice = int(price_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
            price_value = e4.get()
            iTotal_Price = iQuantity * iPrice

            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "Update invoice_table set Medicine= %s,Company= %s,Quantity= %s ,Price= %s,Total_Price= %s where Med_id= %s"
                val = (
                    iMedicine,
                    iCompany,
                    iQuantity,
                    iPrice,
                    iTotal_Price,
                    iMed_id,
                )
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            iMed_id = e1.get()
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "delete from invoice_table where Med_id = %s"
                val = (iMed_id,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Deleted successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            mycursor.execute(
                "SELECT Med_id,Medicine,Company,Quantity,Price,Total_Price FROM invoice_table"
            )
            records = mycursor.fetchall()
            print(records)
            for i, (
                id,
                hashMedicine,
                hashCompany,
                hashQuantity,
                hashPrice,
                hashTotal_Price,
            ) in enumerate(records, start=1):
                listBox.insert(
                    "",
                    "end",
                    values=(
                        id,
                        hashMedicine,
                        hashCompany,
                        hashQuantity,
                        hashPrice,
                        hashTotal_Price,
                    ),
                )

        global e1
        global e2
        global e3
        global e4
        global e5
        global iTotal_Price

        tkinter.Label(frame_invoice, text="Med_id", width=15, anchor="w").place(
            x=20, y=10
        )
        Label(frame_invoice, text="Medicine", width=15, anchor="w").place(x=20, y=50)
        Label(frame_invoice, text="Company", width=15, anchor="w").place(x=20, y=90)
        Label(frame_invoice, text="Quantity", width=15, anchor="w").place(x=20, y=130)
        Label(frame_invoice, text="Price", width=15, anchor="w").place(x=20, y=170)

        e1 = Entry(frame_invoice)
        e1.place(x=150, y=10, width=480)
        e2 = Entry(frame_invoice)
        e2.place(x=150, y=50, width=480)
        e3 = Entry(frame_invoice)
        e3.place(x=150, y=90, width=480)
        e4 = Entry(frame_invoice)
        e4.place(x=150, y=130, width=480)
        e5 = Entry(frame_invoice)
        e5.place(x=150, y=170, width=480)

        Button(frame_invoice, text="Add", command=Add, height=1, width=20).place(
            x=20, y=210
        )
        Button(frame_invoice, text="update", command=update, height=1, width=20).place(
            x=180, y=210
        )
        Button(frame_invoice, text="Delete", command=delete, height=1, width=20).place(
            x=340, y=210
        )
        cols = (
            "Med_id",
            "Medicine",
            "Company",
            "Quantity",
            "Price",
            "Total_Price",
        )
        listBox = ttk.Treeview(
            frame_invoice,
            columns=cols,
            show="headings",
            height=24,
            style="Custom.Treeview",
        )
        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=4)
            listBox.place(x=20, y=300, width=1200)
        show()
        listBox.bind("<Double-Button-1>", GetValue)

    def open_sales():
        frame_sales = bootstrap.Frame(frame2, bootstyle="dark")
        frame_sales.pack(fill="both", expand=True, padx=10, pady=10)

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)

            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select["Medicine_id"])
            e2.insert(0, select["Medicine_Name"])
            e3.insert(0, select["Patients_No"])
            e4.insert(0, select["Quantity"])
            e5.insert(0, select["Price"])

        def Add():
            iMed_id = e1.get()
            iMedicine = e2.get()
            iNumber = e3.get()
            # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()
            if quantity_value:
                try:
                    iQuantity = int(quantity_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
                # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()

            # Validate and convert Quantity (e4) to integer
            price_value = e5.get()
            if price_value:
                try:
                    iPrice = int(price_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
            price_value = e5.get()
            iTotal_Price = iQuantity * iPrice

            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "INSERT INTO sales_table (Medicine_id,Medicine_Name,Patients_No,Quantity,Price,Total_Price) VALUES (%s, %s, %s, %s, %s,%s)"
                val = (
                    iMed_id,
                    iMedicine,
                    iNumber,
                    iQuantity,
                    iPrice,
                    iTotal_Price,
                )
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Data inserted successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
                show()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            iMed_id = e1.get()
            iMedicine = e2.get()
            iNumber = e3.get()

            # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()
            if quantity_value:
                try:
                    iQuantity = int(quantity_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
                # Validate and convert Quantity (e4) to integer
            quantity_value = e4.get()

            # Validate and convert Quantity (e4) to integer
            price_value = e5.get()
            if price_value:
                try:
                    iPrice = int(price_value)
                except ValueError:
                    # Handle the case where the input is not a valid integer
                    messagebox.showerror("Error", "Quantity should be a valid number")
                    return  # Stop further execution of this function
            else:
                # Handle the case where the input is an empty string
                messagebox.showerror("Error", "Quantity cannot be empty")
                return  # Stop further execution of this function
            price_value = e5.get()
            iTotal_Price = iQuantity * iPrice

            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "Update sales_table set Medicine_Name= %s,Patients_No= %s,Quantity= %s ,Price= %s,Total_Price= %s where Medicine_id= %s"
                val = (
                    iMedicine,
                    iNumber,
                    iQuantity,
                    iPrice,
                    iTotal_Price,
                    iMed_id,
                )
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            iMed_id = e1.get()
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "delete from sales_table where Medicine_id = %s"
                val = (iMed_id,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Deleted successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            mycursor.execute(
                "SELECT Medicine_id,Medicine_Name,Patients_No,Quantity,Price,Total_Price FROM sales_table"
            )
            records = mycursor.fetchall()
            print(records)
            for i, (
                id,
                hashMedicine,
                hashNumber,
                hashQuantity,
                hashPrice,
                hashTotal_Price,
            ) in enumerate(records, start=1):
                listBox.insert(
                    "",
                    "end",
                    values=(
                        id,
                        hashMedicine,
                        hashNumber,
                        hashQuantity,
                        hashPrice,
                        hashTotal_Price,
                    ),
                )

        global e1
        global e2
        global e3
        global e4
        global e5
        global iTotal_Price

        tkinter.Label(frame_sales, text="Medicine_id", width=15, anchor="w").place(
            x=20, y=10
        )
        Label(frame_sales, text="Medicine_Name", width=15, anchor="w").place(x=20, y=50)
        Label(frame_sales, text="Patients_No", width=15, anchor="w").place(x=20, y=90)
        Label(frame_sales, text="Quantity", width=15, anchor="w").place(x=20, y=130)
        Label(frame_sales, text="Price", width=15, anchor="w").place(x=20, y=170)

        e1 = Entry(frame_sales)
        e1.place(x=150, y=10, width=480)
        e2 = Entry(frame_sales)
        e2.place(x=150, y=50, width=480)
        e3 = Entry(frame_sales)
        e3.place(x=150, y=90, width=480)
        e4 = Entry(frame_sales)
        e4.place(x=150, y=130, width=480)
        e5 = Entry(frame_sales)
        e5.place(x=150, y=170, width=480)

        Button(frame_sales, text="Add", command=Add, height=1, width=20).place(
            x=20, y=210
        )
        Button(frame_sales, text="update", command=update, height=1, width=20).place(
            x=180, y=210
        )
        Button(frame_sales, text="Delete", command=delete, height=1, width=20).place(
            x=340, y=210
        )
        cols = (
            "Medicine_id",
            "Medicine_Name",
            "Patients_No",
            "Quantity",
            "Price",
            "Total_Price",
        )
        listBox = ttk.Treeview(
            frame_sales,
            columns=cols,
            show="headings",
            height=24,
            style="Custom.Treeview",
        )
        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=4)
            listBox.place(x=20, y=300, width=1200)
        show()
        listBox.bind("<Double-Button-1>", GetValue)

    def open_pharmacist():
        frame_pharm = bootstrap.Frame(frame2, bootstyle="dark")
        frame_pharm.pack(fill="both", expand=True, padx=10, pady=10)

        def GetValue(event):
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            row_id = listBox.selection()[0]
            select = listBox.set(row_id)
            e1.insert(0, select["Pharm_id"])
            e2.insert(0, select["Pharmacist_Name"])
            e3.insert(0, select["Contact_Number"])
            e4.insert(0, select["E_mail_Address"])

        def Add():
            PharmId = e1.get()
            PharmacistName = e2.get()
            ContactNumber = e3.get()
            EmailAddress = e4.get()
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "INSERT INTO  pharmacist_table (Pharm_id,Pharmacist_Name,Contact_Number,E_mail_Address) VALUES (%s, %s, %s, %s)"
                val = (PharmId, PharmacistName, ContactNumber, EmailAddress)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo(
                    "information", "Pharmacist inserted successfully..."
                )
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def update():
            PharmId = e1.get()
            PharmacistName = e2.get()
            ContactNumber = e3.get()
            EmailAddress = e4.get()
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "Update  pharmacist_table set Pharmacist_Name= %s,Contact_Number= %s,E_mail_Address= %s where Pharm_id= %s"
                val = (PharmacistName, ContactNumber, EmailAddress, PharmId)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def delete():
            PharmId = e1.get()
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "delete from pharmacist_table where Pharm_id = %s"
                val = (PharmId,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastPharm_id = mycursor.lastrowid
                messagebox.showinfo("information", "Record Deleted successfully...")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e1.focus_set()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

        def show():
            mysqldb = mysql.connector.connect(
                host="localhost",
                port="3307",
                user="root",
                password="Dencollins175",
                database="pharmacist",
            )
            mycursor = mysqldb.cursor()
            mycursor.execute(
                "SELECT Pharm_id,Pharmacist_Name,Contact_Number,E_mail_Address FROM pharmacist_table"
            )
            records = mycursor.fetchall()
            print(records)
            for i, (
                id,
                Pharmacist,
                Contact,
                E_mail,
            ) in enumerate(records, start=1):
                listBox.insert(
                    "",
                    "end",
                    values=(id, Pharmacist, Contact, E_mail),
                )

        global e1
        global e2
        global e3
        global e4

        tkinter.Label(frame_pharm, text="Pharm ID", width=15, anchor="w").place(
            x=20, y=10
        )
        Label(frame_pharm, text="Name", width=15, anchor="w").place(x=20, y=50)
        Label(frame_pharm, text="Contact No", width=15, anchor="w").place(x=20, y=90)
        Label(frame_pharm, text="E-mail", width=15, anchor="w").place(x=20, y=130)
        e1 = Entry(frame_pharm)
        e1.place(x=150, y=10, width=480)
        e2 = Entry(frame_pharm)
        e2.place(x=150, y=50, width=480)
        e3 = Entry(frame_pharm)
        e3.place(x=150, y=90, width=480)
        e4 = Entry(frame_pharm)
        e4.place(x=150, y=130, width=480)
        Button(frame_pharm, text="Add", command=Add, height=1, width=20).place(
            x=20, y=170
        )
        Button(frame_pharm, text="update", command=update, height=1, width=20).place(
            x=180, y=170
        )
        Button(frame_pharm, text="Delete", command=delete, height=1, width=20).place(
            x=340, y=170
        )
        cols = ("Pharm_id", "Pharmacist_Name", "Contact_Number", "E_mail_Address")
        listBox = ttk.Treeview(
            frame_pharm,
            columns=cols,
            show="headings",
            height=25,
            style="Custom.Treeview",
        )
        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=4)
            listBox.place(x=20, y=220, width=1200)
        show()
        listBox.bind("<Double-Button-1>", GetValue)

    def open_medicine():
        coldata = [
            {"text": "Medicine", "stretch": True},
            "Quantity",
            {"text": "Price", "stretch": False},
        ]

        rowdata = [
            ("Aspirin", "100 tablets", "KES 500.00"),
            ("Ibuprofen", "100 tablets", "KES 250.00"),
            ("Amoxicillin", "100 capsules", "KES 1,000.00"),
            ("Omeprazole", "100 tablets", "KES 400.00"),
            ("Lisinopril", "100 tablets", "KES 750.00"),
            ("Atorvastatin", "100 tablets", "KES 600.00"),
            ("Acetaminophen", "100 tablets", "KES 350.00"),
            ("Ciprofloxacin", "100 tablets", "KES 800.00"),
            ("Simvastatin", "100 tablets", "KES 900.00"),
            ("Prednisone", "100 tablets", "KES 1,200.00"),
            ("Metformin", "100 tablets", "KES 550.00"),
            ("Losartan", "100 tablets", "KES 650.00"),
            ("Azithromycin", "100 capsules", "KES 1,100.00"),
            ("Doxycycline", "100 tablets", "KES 600.00"),
            ("Hydrochlorothiazide", "100 tablets", "KES 450.00"),
            ("Sertraline", "100 tablets", "KES 700.00"),
            ("Metoprolol", "100 tablets", "KES 750.00"),
            ("Albuterol", "100 tablets", "KES 850.00"),
            ("Fluoxetine", "100 tablets", "KES 500.00"),
            ("Gabapentin", "100 tablets", "KES 950.00"),
            ("Amlodipine", "100 tablets", "KES 1,050.00"),
            ("Levothyroxine", "100 tablets", "KES 650.00"),
            ("Amoxicillin/Clavulanate", "100 tablets", "KES 1,450.00"),
            ("Montelukast", "100 tablets", "KES 1,150.00"),
            ("Cephalexin", "100 tablets", "KES 1,350.00"),
            ("Tramadol", "100 tablets", "KES 1,250.00"),
            ("Losartan/Hydrochlorothiazide", "100 tablets", "KES 1,550.00"),
            ("Tadalafil", "100 tablets", "KES 1,600.00"),
            ("Fluticasone", "100 tablets", "KES 800.00"),
            ("Prednisolone", "100 tablets", "KES 550.00"),
            ("Warfarin", "100 tablets", "KES 700.00"),
            ("Clopidogrel", "100 tablets", "KES 1,000.00"),
            ("Methotrexate", "100 tablets", "KES 900.00"),
            ("Sildenafil", "100 tablets", "KES 650.00"),
            ("Meloxicam", "100 tablets", "KES 1,100.00"),
            ("Atenolol", "100 tablets", "KES 750.00"),
            ("Citalopram", "100 tablets", "KES 600.00"),
            ("Fluconazole", "100 tablets", "KES 400.00"),
            ("Esomeprazole", "100 tablets", "KES 900.00"),
            ("Fluvoxamine", "100 tablets", "KES 800.00"),
            ("Naproxen", "100 tablets", "KES 500.00"),
            ("Lorazepam", "100 tablets", "KES 700.00"),
            ("Ranitidine", "100 tablets", "KES 550.00"),
            ("Duloxetine", "100 tablets", "KES 1,050.00"),
            ("Cetirizine", "100 tablets", "KES 650.00"),
            ("Metronidazole", "100 tablets", "KES 450.00"),
            ("Venlafaxine", "100 tablets", "KES 700.00"),
            ("Diazepam", "100 tablets", "KES 600.00"),
            ("Fluocinonide", "100 tablets", "KES 400.00"),
            ("Clobetasol", "100 tablets", "KES 750.00"),
            ("Hydrocortisone", "100 tablets", "KES 650.00"),
            ("Nystatin", "100 tablets", "KES 500.00"),
            ("Ketoconazole", "100 tablets", "KES 800.00"),
            ("Mometasone", "100 tablets", "KES 950.00"),
            ("Mupirocin", "100 tablets", "KES 500.00"),
            ("Benzoyl Peroxide", "100 tablets", "KES 350.00"),
            ("Tretinoin", "100 tablets", "KES 650.00"),
            ("Econazole", "100 capsules", "KES 1,100.00"),
            ("Latanoprost", "100 tablets", "KES 600.00"),
            ("Methazolamide", "100 tablets", "KES 450.00"),
            ("Dorzolamide", "100 tablets", "KES 700.00"),
            ("Cyclopentolate", "100 tablets", "KES 750.00"),
            ("Homatropine", "100 tablets", "KES 850.00"),
            ("Dipivefrin", "100 tablets", "KES 500.00"),
            ("Ketorolac", "100 tablets", "KES 950.00"),
            ("Diclofenac", "100 tablets", "KES 1,050.00"),
            ("Oxycodone", "100 tablets", "KES 650.00"),
            ("Hydrocodone", "100 tablets", "KES 1,450.00"),
            ("Codeine", "100 tablets", "KES 1,150.00"),
            ("Morphine", "100 tablets", "KES 1,350.00"),
            ("Fentanyl", "100 tablets", "KES 1,250.00"),
            ("Tramadol", "100 tablets", "KES 1,550.00"),
            ("Pregabalin", "100 tablets", "KES 1,600.00"),
            ("Gabapentin", "100 tablets", "KES 800.00"),
            ("Mirtazapine", "100 tablets", "KES 550.00"),
            ("Trazodone", "100 tablets", "KES 700.00"),
            ("Lorazepam", "100 tablets", "KES 1,000.00"),
            ("Clonazepam", "100 tablets", "KES 900.00"),
            ("Alprazolam", "100 tablets", "KES 650.00"),
            ("Diazepam", "100 tablets", "KES 1,100.00"),
            ("Zolpidem", "100 tablets", "KES 750.00"),
            ("Eszopiclone", "100 tablets", "KES 600.00"),
            ("Temazepam", "100 tablets", "KES 400.00"),
            ("Estazolam", "100 tablets", "KES 900.00"),
            ("Triazolam", "100 tablets", "KES 800.00"),
            ("Zaleplon", "100 tablets", "KES 500.00"),
            ("Modafinil", "100 tablets", "KES 700.00"),
            ("Armodafinil", "100 tablets", "KES 550.00"),
            ("Methylphenidate", "100 tablets", "KES 1,050.00"),
            ("Amphetamine", "100 tablets", "KES 850.00"),
            ("Dextroamphetamine", "100 tablets", "KES 450.00"),
            ("Atomoxetine", "100 tablets", "KES 700.00"),
            ("Bupropion", "100 tablets", "KES 500.00"),
            ("Venlafaxine", "100 tablets", "KES 750.00"),
            ("Duloxetine", "100 tablets", "KES 1,350.00"),
            ("Trazodone", "100 tablets", "KES 1,050.00"),
            ("Mirtazapine", "100 tablets", "KES 650.00"),
            ("Paroxetine", "100 tablets", "KES 500.00"),
            ("Fluoxetine", "100 tablets", "KES 800.00"),
            ("Sertraline", "100 tablets", "KES 750.00"),
            ("Citalopram", "100 tablets", "KES 450.00"),
        ]
        dt = Tableview(
            master=frame2,
            coldata=coldata,
            rowdata=rowdata,
            paginated=False,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None),
        )
        dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    frame1 = bootstrap.Frame(root, bootstyle="dark", width=220)
    frame1.pack(side="left", fill="y", expand=False, padx=1, pady=1)

    admin = ImageTk.PhotoImage(Image.open("LoginSystem\Adminlogo.jpg"))
    admin_label = Label(master=frame1, image=admin, width=260, height=220)
    admin_label.pack(padx=10, pady=10, fill="both")

    # Define buttons with their corresponding section functions
    button_data = [
        ("Dashboard", open_dashboard),
        ("Invoice", open_invoice),
        ("Sales", open_sales),
        ("Pharmacist", open_pharmacist),
        ("Medicine", open_medicine),
    ]

    # Create and pack the buttons in frame1
    buttons = []
    for text, section_func in button_data:
        button = bootstrap.Button(
            frame1,
            text=text,
            bootstyle="dark",
            command=lambda func=section_func: open_section(func),
        )
        button.pack(fill="x", pady=10)
        buttons.append(button)

    frame2 = bootstrap.Frame(root, bootstyle="light")
    frame2.pack(side="right", fill="both", expand=True, padx=1, pady=1)

    open_dashboard()
    root.mainloop()


# Function to check login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    # Replace these with actual credentials validation
    if username == "benora" and password == "1234":
        messagebox.showinfo("welcome!", "Login successful")
        button_function()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
first_page = custom.CTk()
first_page.title("Benora Pharmacy Login")
first_page.geometry("600X440")
# back ground image
bg_image = ImageTk.PhotoImage(Image.open("LoginSystem\loginBg.jpg"))
bg_label = Label(master=first_page, image=bg_image)
bg_label.pack()

frame = custom.CTkFrame(master=bg_label, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Create and place labels and entry widgets
username_label = custom.CTkLabel(
    master=frame, text="Enter Username:", font=("Century Gothic", 20)
)
username_label.place(x=50, y=45)
username_entry = custom.CTkEntry(master=frame, width=220, placeholder_text="username")
username_entry.place(x=50, y=110)

password_label = custom.CTkLabel(
    master=frame, text="Password:", font=("Century Gothic", 20)
)
password_label.place(x=50, y=165)
password_entry = custom.CTkEntry(
    master=frame, width=220, placeholder_text="password", show="*"
)  # Show '*' instead of the actual characters
password_entry.place(x=50, y=200)

# Create and place the login button
login_button = custom.CTkButton(
    master=frame, width=220, text="Login", corner_radius=6, command=login
)
login_button.place(x=50, y=240)


# Start the tkinter event loop
first_page.mainloop()
