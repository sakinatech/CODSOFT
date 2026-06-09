import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("450x400")
        
        # Dictionary to store contacts (Name: Phone)
        self.contacts = {}

        # --- Left Side: Input Fields & Buttons ---
        input_frame = tk.LabelFrame(root, text="Manage Contact", padx=10, pady=10)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(input_frame, width=20)
        self.name_entry.grid(row=1, column=0, pady=5)

        tk.Label(input_frame, text="Phone:").grid(row=2, column=0, sticky="w")
        self.phone_entry = tk.Entry(input_frame, width=20)
        self.phone_entry.grid(row=3, column=0, pady=5)

        tk.Button(input_frame, text="Add Contact", width=16, command=self.add_contact).grid(row=4, column=0, pady=5)
        tk.Button(input_frame, text="Delete Contact", width=16, bg="#ffcccb", command=self.delete_contact).grid(row=5, column=0, pady=5)
        tk.Button(input_frame, text="Clear Fields", width=16, command=self.clear_entries).grid(row=6, column=0, pady=5)

        # --- Right Side: Contact List Display ---
        list_frame = tk.LabelFrame(root, text="Contact List", padx=10, pady=10)
        list_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.contact_listbox = tk.Listbox(list_frame, width=25, height=15)
        self.contact_listbox.grid(row=0, column=0)
        self.contact_listbox.bind('<<ListboxSelect>>', self.load_selected_contact)

        # Configure weights for proper resizing
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Both Name and Phone fields are required!")
            return

        # Add or update contact in the memory dictionary
        self.contacts[name] = phone
        self.update_listbox()
        self.clear_entries()
        messagebox.showinfo("Success", f"Contact '{name}' saved successfully.")

    def delete_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            selected_text = self.contact_listbox.get(selected_index)
            name = selected_text.split(" - ")[0] # Extract name from display format

            del self.contacts[name]
            self.update_listbox()
            self.clear_entries()
            messagebox.showinfo("Deleted", f"Contact '{name}' removed.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a contact from the list to delete.")

    def load_selected_contact(self, event):
        # Fill input boxes when a user clicks on an item in the list
        try:
            selected_index = self.contact_listbox.curselection()[0]
            selected_text = self.contact_listbox.get(selected_index)
            name, phone = selected_text.split(" - ")
            
            self.clear_entries()
            self.name_entry.insert(0, name)
            self.phone_entry.insert(0, phone)
        except IndexError:
            pass

    def update_listbox(self):
        # Refresh the displayed listbox with updated dictionary data
        self.contact_listbox.delete(0, tk.END)
        for name, phone in sorted(self.contacts.items()):
            self.contact_listbox.insert(tk.END, f"{name} - {phone}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
