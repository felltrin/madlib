import tkinter as tk


class GUI:

    def __init__(self):

        self.adjective = None
        self.person_in_room = None
        self.noun_one = None
        self.noun_two = None
        self.noun_three = None

        self.root = tk.Tk()
        self.root.geometry("350x350")
        self.root.title("Madlib")

        self.label_frame = tk.Frame(self.root)
        self.label_frame.columnconfigure(0, weight=1)

        self.label = tk.Label(self.label_frame, text="Enter an adjective:", font=("Sans Serif", 16))
        self.label.grid(row=0, column=0)

        self.text = tk.Text(self.label_frame, height=1, width=15, font=("Sans Serif", 12))
        self.text.grid(row=0, column=1)

        self.label_frame.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Sans Serif", 12), command=self.submit_adjective)
        self.submit_button.pack(padx=5, pady=5)

        self.root.mainloop()

    def submit_adjective(self):
        self.adjective = self.text.get('1.0', tk.END)
        self.adjective = self.adjective.strip()

        self.text.delete("1.0", "end")

        self.label["text"] = "Enter a person in the room:"
        self.label["font"] = ("Sans Serif", 14)
        self.submit_button.config(command=self.submit_person_in_room)

    def submit_person_in_room(self):
        self.person_in_room = self.text.get('1.0', tk.END)
        self.person_in_room = self.person_in_room.strip()

        self.text.delete('1.0', "end")

        self.label["text"] = "Enter a noun:"
        self.label["font"] = ("Sans Serif", 16)
        self.submit_button.config(command=self.submit_noun_one)

    def submit_noun_one(self):
        self.noun_one = self.text.get('1.0', tk.END)
        self.noun_one = self.noun_one.strip()

        self.text.delete('1.0', "end")

        self.label["text"] = "Enter another noun:"
        self.label["font"] = ("Sans Serif", 16)
        self.submit_button.config(command=self.submit_noun_two)

    def submit_noun_two(self):
        self.noun_two = self.text.get('1.0', tk.END)
        self.noun_two = self.noun_two.strip()

        self.text.delete('1.0', "end")

        self.label["text"] = "Enter one more noun:"
        self.label["font"] = ("Sans Serif", 16)
        self.submit_button.config(command=self.submit_final_entry)

    def submit_final_entry(self):
        self.noun_three = self.text.get('1.0', tk.END)
        self.noun_three = self.noun_three.strip()

        self.label_frame.destroy()
        self.submit_button.destroy()

        madlib_text = "This Thanksgiving, I'm thankful for all the " + self.adjective + \
                      " things in my life. Even though I complain about how " + self.person_in_room + \
                      " is always getting on my nerves, or how my " + self.noun_one + \
                      " homework is boring, or how I hate cleaning my " + self.noun_two + ", I know I am " \
                      "a very lucky " + self.noun_three + "."

        final_label = tk.Label(self.root, text=madlib_text, font=("Sans Serif", 16), wraplength=300)
        final_label.pack(padx=10, pady=10)
