import tkinter as tk


class GUI:

    def __init__(self):

        self.adjective = None
        self.person_in_room = None
        self.noun_one = None
        self.noun_two = None
        self.person_in_room_text = None
        self.noun_one_text = None
        self.noun_two_text = None

        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Madlib")

        self.label_frame = tk.Frame(self.root)
        self.label_frame.columnconfigure(0, weight=1)

        self.label_one = tk.Label(self.label_frame, text="Enter an adjective:", font=("Sans Serif", 16))
        self.label_one.grid(row=0, column=0)

        self.adjective_text = tk.Text(self.label_frame, height=1, width=15, font=("Sans Serif", 12))
        self.adjective_text.grid(row=0, column=1)

        self.label_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Sans Serif", 12), command=self.submit_adjective)
        self.submit_button.pack(padx=5, pady=5)

        self.root.mainloop()

    def submit_adjective(self):
        self.adjective = self.adjective_text.get('1.0', tk.END)

        self.label_frame.destroy()
        self.submit_button.destroy()

        self.label_frame = tk.Frame(self.root)
        self.label_frame.columnconfigure(0, weight=1)

        self.label_one = tk.Label(self.label_frame, text="Enter a person in the room:", font=("Sans Serif", 14))
        self.label_one.grid(row=0, column=0)

        self.person_in_room_text = tk.Text(self.label_frame, height=1, width=10, font=("Sans Serif", 12))
        self.person_in_room_text.grid(row=0, column=1)

        self.label_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Sans Serif", 12), command=self.submit_person_in_room)
        self.submit_button.pack(padx=5, pady=5)

    def submit_person_in_room(self):
        self.person_in_room = self.person_in_room_text.get('1.0', tk.END)

        self.label_frame.destroy()
        self.submit_button.destroy()

        self.label_frame = tk.Frame(self.root)
        self.label_frame.columnconfigure(0, weight=1)

        self.label_one = tk.Label(self.label_frame, text="Enter a noun:", font=("Sans Serif", 16))
        self.label_one.grid(row=0, column=0)

        self.noun_one_text = tk.Text(self.label_frame, height=1, width=10, font=("Sans Serif", 12))
        self.noun_one_text.grid(row=0, column=1)

        self.label_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Sans Serif", 12), command=self.submit_noun_one)
        self.submit_button.pack(padx=5, pady=5)

    def submit_noun_one(self):
        self.noun_one = self.noun_one_text.get('1.0', tk.END)

        self.label_frame.destroy()
        self.submit_button.destroy()

        self.label_frame = tk.Frame(self.root)
        self.label_frame.columnconfigure(0, weight=1)

        self.label_one = tk.Label(self.label_frame, text="Enter another noun:", font=("Sans Serif", 16))
        self.label_one.grid(row=0, column=0)

        self.noun_two_text = tk.Text(self.label_frame, height=1, width=10, font=("Sans Serif", 12))
        self.noun_two_text.grid(row=0, column=1)

        self.label_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Sans Serif", 12),
                                       command=self.submit_final_entry)
        self.submit_button.pack(padx=5, pady=5)

    def submit_final_entry(self):
        self.noun_two = self.noun_two_text.get('1.0', tk.END)

        self.label_frame.destroy()
        self.submit_button.destroy()

        madlib_text = "This Thanksgiving, I'm thankful for all the " + self.adjective + \
                      " things in my life. Even though I complain about how " + self.person_in_room + \
                      " is always getting on my nerves, or how my " + self.noun_one + \
                      " homework is boring, or how I hate cleaning my " + self.noun_two + "."

        final_label = tk.Label(self.root, text=madlib_text, font=("Sans Serif", 18))
        final_label.pack(padx=10, pady=10)
