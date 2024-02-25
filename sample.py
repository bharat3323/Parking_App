import tkinter as tk
from tkinter import messagebox, Frame, PhotoImage, Button, Entry
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry

class SlotBookingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Slot Booking")
        self.geometry("1600x1600")
        self.config(bg="lightblue")

        # Add a label to the window
        self.label = tk.Label(self, text="Parking Area", font=("Arial", 50, "bold"), bg="white")
        self.label.pack(pady=20)

        # Add buttons for parking slots
        for i in range(10):
            button = tk.Button(self, text=f"parking NO {i+1}", command=self.book_slot, width=15, height=10)
            button.pack()
            button.place(x=30+150*(i%3), y=150+230*(i//3))

    def book_slot(self):
        messagebox.showinfo("Booking", "Slot booked successfully!")

class ParkingSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Parking System")
        self.geometry("1800x800")
        self.resizable(True, True)
        self.state('zoomed')

        self.create_login_screen()

    def create_login_screen(self):
        self.login_frame = Frame(self, width=1800, height=800)
        self.login_frame.pack(fill='both', expand=True)
        self.login_frame.place(x=0, y=0)

        self.login_bg_image = PhotoImage(file="myui/parking1.png", width=800, height=2000)
        self.login_bg_label = tk.Label(self.login_frame, image=self.login_bg_image, bg='white')
        self.login_bg_label.place(x=0, y=0)

        label2 = tk.Label(self.login_bg_label, text="Welcome to ", font=('Arial Black', 30), bg='white', fg='black',
                          justify='center')
        label2.place(x=250, y=20)

        label3 = tk.Label(self.login_bg_label, text="SmartPark", font=('Cooper Black', 30), bg='white', fg='#1260CC',
                          justify='center')
        label3.place(x=270, y=80)

        login_sub_frame = Frame(self.login_frame, width=500, height=1000, bg='#73A4FF')
        login_sub_frame.place(x=800, y=0)

        self.logo_image = PhotoImage(file="myui/logo2.png")
        self.logo_label = tk.Label(login_sub_frame, image=self.logo_image, bg='#73A4FF')
        self.logo_label.image = self.logo_image
        self.logo_label.place(x=150, y=0)

        heading = tk.Label(login_sub_frame, text="Login", fg='#ED9121', bg='#73A4FF',
                           font=('Cooper Black', 23, 'bold'))
        heading.place(x=200, y=200)

        label1 = tk.Label(login_sub_frame, text="Username", font=('ariel', 11), bg='#73A4FF', fg='black')
        label1.place(x=150, y=270)

        label2 = tk.Label(login_sub_frame, text="Password", font=('ariel', 11), bg='#73A4FF', fg='black')
        label2.place(x=150, y=330)

        self.username_entry = Entry(login_sub_frame, width=25, fg='black', border=0, bg="#ececec",
                                    font=('Microsoft YaHei UI Light', 11))
        self.username_entry.place(x=150, y=290)

        self.password_entry = Entry(login_sub_frame, width=25, fg='black', border=0, bg="#ececec",
                                    font=('Microsoft YaHei UI Light', 11), show="*")
        self.password_entry.place(x=150, y=350)

        self.loginbtn = PhotoImage(file="myui/login.png")
        btn1 = tk.Button(login_sub_frame, image=self.loginbtn, border=0, cursor='hand2', bg='#73A4FF',
                         command=self.login)
        btn1.place(x=150, y=400)

        btn2 = tk.Button(login_sub_frame, width=30, pady=7, text="Forgot Password?", font=('ariel', 11),
                         bg='#73A4FF', border=0, fg='blue', cursor='hand2')
        btn2.place(x=120, y=460)

        label4 = tk.Label(login_sub_frame, text="------------------   or   -----------------", bg='#73A4FF',
                          fg='black')
        label4.place(x=150, y=490)

        btn3 = tk.Button(login_sub_frame, image=self.loginbtn, border=0, cursor='hand2', bg='#73A4FF')
        btn3.place(x=150, y=520)

    def login(self):
        # Get username and password entered by the user
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Define a dictionary of predefined username-password pairs
        credentials = {
            "bharatbhandari036": "bharat123",
            "login": "123"
            # Add more username-password pairs as needed
        }

        # Check if the entered credentials match any of the predefined pairs
        if username in credentials and credentials[username] == password:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.login_frame.pack_forget()
            self.create_parking_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def create_parking_app(self):
        self.parking_app_frame = Frame(self, width=1800, height=800)
        self.parking_app_frame.pack(fill='both', expand=True)
        self.parking_app_frame.place(x=0, y=0)

        self.bg_frame = Frame(self.parking_app_frame, width=1000, height=800)
        self.bg_frame.pack(fill='both', expand=True)
        self.bg_frame.place(x=-80, y=0)

        original_image = Image.open(r"myui\bharat.png")  # Adjusted file path
        resized_image = original_image.resize((900, 800))
        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.background_label = tk.Label(self.bg_frame, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.info_frame = Frame(self.parking_app_frame, bg='#b5e2ff', width=700, height=800)
        self.info_frame.place(x=850, y=0)

        self.label1 = tk.Label(self.info_frame, text="Information page", width=20, height=1, bg='#b5e2ff',
                               font=('Helvetica', 35, 'italic'))
        self.label1.place(x=40, y=70)

        self.label2 = tk.Label(self.info_frame, text='Enter Vehicle Number:', font=('Arial', 20), bg='#b5e2ff',
                               fg='black')
        self.label2.place(x=20, y=190)

        self.label3 = tk.Label(self.info_frame, text='Enter Vehicle Model:', font=('Arial', 20), bg='#b5e2ff',
                               fg='black')
        self.label3.place(x=20, y=290)

        choices = ['Java', 'Python', 'C', 'C++', 'OS']
        self.label4 = tk.Label(self.info_frame, text='Select Batch:', font=('Arial', 20), bg='#b5e2ff', fg='black')
        self.label4.place(x=20, y=400)

        self.combo_box = ttk.Combobox(self.info_frame, values=choices, width=35, height=40)
        self.combo_box.place(x=300, y=400)

        self.label5 = tk.Label(self.info_frame, text='Select Date:', font=('Arial', 20), bg='#b5e2ff', fg='black')
        self.label5.place(x=20, y=500)

        self.label6 = tk.Label(self.info_frame, text='Select Time:', font=('Arial', 20), bg='#b5e2ff', fg='black')
        self.label6.place(x=20, y=600)

        self.entry1 = tk.Entry(self.info_frame, font=('Arial', 15))
        self.entry1.place(x=300, y=200)

        self.entry2 = tk.Entry(self.info_frame, font=('Arial', 15))
        self.entry2.place(x=300, y=295)

        self.entry4 = DateEntry(self.info_frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                                year=2024, font=('Arial', 15))
        self.entry4.place(x=300, y=500)

        self.entry5 = tk.Entry(self.info_frame, font=('Arial', 15))
        self.entry5.place(x=300, y=600)

        self.button = Button(self.info_frame, text='Go to slot booking', bg='cyan3',
                             font=('Arial', 15, 'italic'), bd=5, command=self.go_to_slot_booking)
        self.button.place(x=300, y=700)

    def go_to_slot_booking(self):
        self.parking_app_frame.pack_forget()
        slot_booking_app = SlotBookingApp()
        slot_booking_app.mainloop()


if __name__ == "__main__":
    app = ParkingSystem()
    app.mainloop()
