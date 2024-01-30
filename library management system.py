import tkinter as tk
from tkinter import messagebox

class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("400x400")
        self.master.config(bg='#708090')

        self.books = []
        self.lend_list = []

        # Labels
        self.login_label = tk.Label(self.master, text="Library Management System", font=("Helvetica", 16), bg='#708090', fg='white')
        self.login_label.pack()
        self.username_label = tk.Label(self.master, text="Username", font=("Helvetica", 12), bg='#708090', fg='white')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack()
        self.password_label = tk.Label(self.master, text="Password", font=("Helvetica", 12), bg='#708090', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 12), show="*")
        self.password_entry.pack()

        # Login
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Helvetica", 12))
        self.login_button.pack()

        # Register
        self.register_button = tk.Button(self.master, text="Register", command=self.register, font=("Helvetica", 12))
        self.register_button.pack()

        self.username = ""
        self.password = ""
        self.librarians = []

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for librarian in self.librarians:
            if self.username == librarian[0] and self.password == librarian[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.library_management_screen()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.librarians.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    def library_management_screen(self):
        # add books
        self.add_book_label = tk.Label(self.master, text="Add Book", font=("Helvetica", 16), bg='#708090', fg='white')
        self.add_book_label.pack()
        self.add_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.add_book_entry.pack()
        self.add_book_button = tk.Button(self.master, text="Add Book", command=self.add_book, font=("Helvetica", 12))
        self.add_book_button.pack()
        # remove books
        self.remove_book_label = tk.Label(self.master, text="Remove Book", font=("Helvetica", 16), bg='#708090', fg='white')
        self.remove_book_label.pack()
        self.remove_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.remove_book_entry.pack()
        self.remove_book_button = tk.Button(self.master, text="Remove Book", command=self.remove_book, font=("Helvetica", 12))
        self.remove_book_button.pack()
        # issue books
        self.issue_book_label = tk.Label(self.master, text="Issue Book", font=("Helvetica", 16), bg='#708090', fg='white')
        self.issue_book_label.pack()
        self.issue_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.issue_book_entry.pack()
        self.issue_book_button = tk.Button(self.master, text="Issue Book", command=self.issue_book, font=("Helvetica", 12))
        self.issue_book_button.pack()
        # return book
        self.return_book_label = tk.Label(self.master, text="Return Book", font=("Helvetica", 16), bg='#708090', fg='white')
        self.return_book_label.pack()
        self.return_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.return_book_entry.pack()
        self.return_book_button = tk.Button(self.master, text="Return Book", command=self.return_book, font=("Helvetica", 12))
        self.return_book_button.pack()
         # Search Books
        self.search_label = tk.Label(self.master, text="Search Books", font=("Helvetica", 16), bg='#708090', fg='white')
        self.search_label.pack()
        self.search_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.search_entry.pack()
        self.search_button = tk.Button(self.master, text="Search", command=self.search_books, font=("Helvetica", 12))
        self.search_button.pack()
        self.search_result_label = tk.Label(self.master, text="", font=("Helvetica", 12), bg='#708090', fg='white')
        self.search_result_label.pack()
        # view book
        self.view_books_button = tk.Button(self.master, text="View Books", command=self.view_books, font=("Helvetica", 12))
        self.view_books_button.pack()
        

    def add_book(self):
        book = self.add_book_entry.get()
        self.books.append(book)
        messagebox.showinfo("Success", "Book added successfully")
        self.add_book_entry.delete(0, tk.END)

    def remove_book(self):
        book = self.remove_book_entry.get()
        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Success", "Book removed successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.remove_book_entry.delete(0, tk.END)

    def issue_book(self):
        book = self.issue_book_entry.get()
        if book in self.books:
            self.lend_list.append(book)
            self.books.remove(book)
            messagebox.showinfo("Success", "Book issued successfully")
        else:
            messagebox.showerror("Error", "Book not found")
        self.issue_book_entry.delete(0, tk.END)
    def return_book(self):
        returned_book = self.return_book_entry.get()
        if returned_book in self.lend_list:
            self.books.append(returned_book)
            self.lend_list.remove(returned_book)
            messagebox.showinfo("Success", "Book returned successfully")
        else:
            messagebox.showerror("Error", "Book not found in the lend list")
        self.return_book_entry.delete(0, tk.END)
    def search_books(self):
        query = self.search_entry.get().lower()
        search_result = [book for book in self.books if query in book.lower()]
        if search_result:
            result_message = "\n".join(search_result)
            self.search_result_label.config(text=f"Search Result:\n{result_message}")
        else:
            self.search_result_label.config(text="No matching books found")


    def view_books(self):
        message = "\n".join(self.books)
        messagebox.showinfo("Books", message)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()