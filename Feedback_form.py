from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Feedback:
    def __init__(self, master):
        master.title('AppMillers Online Courses')
        master.geometry("480x500")
        master.configure(background='#ECECEC')
        master.resizable(False, False)

        # Define styles
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#ECECEC', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))
        self.style.configure('TButton', font=('Arial', 11), padding=5)
        self.style.configure('TFrame', background='#ECECEC')

        # Header frame (Logo + Title + Description)
        self.header_frame = ttk.Frame(master)
        self.header_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Add a logo image
        try:
            self.logo = PhotoImage(file="appmillers_logo.gif")
            ttk.Label(self.header_frame, image=self.logo).grid(row=0, column=0, rowspan=2, padx=(0, 20))
        except TclError:
            ttk.Label(self.header_frame, text="LOGO", font=('Arial', 20, 'bold'), background="#ECECEC", foreground="gray").grid(row=0, column=0, rowspan=2, padx=(0, 20))

        # Title and description
        ttk.Label(self.header_frame, text="Thanks for joining us!", style='Header.TLabel').grid(row=0, column=1, sticky='w')
        ttk.Label(self.header_frame, wraplength=350, text='We are glad you chose AppMillers for your online study. '
                                                          'Please tell us what you thought about our online courses.').grid(row=1, column=1, sticky='w')

        # Content frame (Name, Email, Comments)
        self.content_frame = ttk.Frame(master)
        self.content_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Name and Email fields (side by side)
        ttk.Label(self.content_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky='sw')
        ttk.Label(self.content_frame, text="Email:").grid(row=0, column=1, padx=5, pady=5, sticky='sw')
        self.name_entry = ttk.Entry(self.content_frame, width=25)
        self.name_entry.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.email_entry = ttk.Entry(self.content_frame, width=25)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Comments field
        ttk.Label(self.content_frame, text="Comments:").grid(row=2, column=0, columnspan=2, padx=5, pady=(10, 5), sticky='sw')
        self.comment_text = Text(self.content_frame, width=58, height=10, font=('Arial', 10), relief="solid")
        self.comment_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        # Buttons frame
        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(row=2, column=0, pady=20)

        self.submit_button = ttk.Button(self.button_frame, text='Submit', command=self.submit)
        self.submit_button.grid(row=0, column=0, padx=10)

        self.clear_button = ttk.Button(self.button_frame, text='Clear', command=self.clear)
        self.clear_button.grid(row=0, column=1, padx=10)

    def clear(self):
        """Clear all input fields."""
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.comment_text.delete(1.0, 'end')

    def submit(self):
        """Handle submission of the form."""
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        comment = self.comment_text.get("1.0", "end").strip()

        # Check if all fields are filled
        if not name or not email or not comment:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields before submitting.")
            return

        # Display the feedback in the console (or save to a file/database)
        print("Feedback Submitted:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Comment: {comment}")

        # Show a confirmation message
        messagebox.showinfo(title="Feedback Submitted", message="Thank you for your feedback!")
        self.clear()


def main():
    main_window = Tk()
    Feedback(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
