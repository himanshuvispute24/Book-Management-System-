"""Objective

Before starting Django, review Python fundamentals by
building a simple book management system.
This will help you practice organizing code and working with common Python features."""


#=============================================BOOK COLLECTION===========================================================


class BookCollection:
    def __init__(self):
        self.books = {}  # Dictionary to store books and their quantities

    def add_book(self, title, quantity):
        ##Add a book or update its quantity.
        if not title or quantity <= 0:
            print("Invalid input: Title cannot be empty, and quantity must be a positive number.")
            return

        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"Added {quantity} copies of '{title}'.")

    def remove_book(self, title, quantity):
        ##Remove a specified quantity of a book.
        if title not in self.books:
            print(f"Error: '{title}' not found in the collection.")
            return

        if quantity <= 0:
            print("Invalid input: Quantity to remove must be a positive number.")
            return

        if self.books[title] < quantity:
            print(f"Error: Cannot remove {quantity} copies of '{title}'. Only {self.books[title]} available.")
            return

        self.books[title] -= quantity
        if self.books[title] == 0:
            del self.books[title]
            print(f"Removed all copies of '{title}'. Book deleted from collection.")
        else:
            print(f"Removed {quantity} copies of '{title}'. {self.books[title]} copies remaining.")

    def view_collection(self):
        ##Display all books and their quantities.
        if not self.books:
            print("The book collection is empty.")
            return

        print("Book Collection:")
        for title, quantity in self.books.items():
            print(f"- '{title}': {quantity} copies")

    def get_total_books(self):
        ##Calculate and display the total number of books in the collection.
        total = sum(self.books.values())
        print(f"Total books in collection: {total}")
#===========================================MENU OPTION=============================================================

def display_menu():
    ##Display the menu options.
    print("\nBook Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. View Book Collection")
    print("4. Get Total Books")
    print("5. Exit")

#===========================================ENTER THE CHOICES=========================================================================
def main():
    book_collection = BookCollection()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the book title: ").strip()
            quantity = int(input("Enter the quantity to add: "))
            book_collection.add_book(title, quantity)

        elif choice == "2":
            title = input("Enter the book title: ").strip()
            quantity = int(input("Enter the quantity to remove: "))
            book_collection.remove_book(title, quantity)

        elif choice == "3":
            book_collection.view_collection()

        elif choice == "4":
            book_collection.get_total_books()

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
