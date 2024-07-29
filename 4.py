# LibraryManager.py

def create_sample_books():
  
  books = {
    "9780134695814": {
      "title": "Operating System Concepts",
      "author": "Abraham Silberschatz, Peter Baer Galvin",
      "publisher": "John Wiley & Sons",
      "volume": 10,
      "year": 2020,
    },
    "9780321937004": {
      "title": "Introduction to Algorithms",
      "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
      "publisher": "MIT Press",
      "volume": 4,
      "year": 2022,
    },
   
  }
  return books


def add_book(library, book_details):

  isbn = book_details["ISBN"]
  if isbn in library:
    print(f"Book with ISBN {isbn} already exists!")
  else:
    library[isbn] = book_details
    print(f"Book with ISBN {isbn} added successfully!")


def remove_book(library, isbn):

  if isbn in library:
    del library[isbn]
    print(f"Book with ISBN {isbn} removed successfully!")
  else:
    print(f"Book with ISBN {isbn} not found!")


def get_book_details(library, isbn):

  if isbn in library:
    book = library[isbn]
    print(f"\nTitle: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Publisher: {book['publisher']}")
    print(f"Volume: {book['volume']}")
    print(f"Year: {book['year']}")
  else:
    print(f"Book with ISBN {isbn} not found!")


def search_books(library, search_term):

  results = []
  for isbn, book in library.items():
    if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower():
      results.append(isbn)
  if results:
    print(f"\nFound books matching '{search_term}':")
    for isbn in results:
      print(f"- ISBN: {isbn}")
  else:
    print(f"No books found matching '{search_term}'")


def list_books(library):

  if library:
    print("\nList of all books:")
    for isbn, _ in library.items():
      print(f"- ISBN: {isbn}")
  else:
    print("Library is currently empty!")


def update_book_details(library, isbn, update_data):

  if isbn in library:
    book = library[isbn]
    for key, value in update_data.items():
      book[key] = value
    print(f"Book with ISBN {isbn} updated successfully!")
  else:
    print(f"Book with ISBN {isbn} not found!")


def is_available(library, isbn):

  return isbn in library



library = create_sample_books()


new_book = {
  "ISBN": "9780134801753",
  "title": "Machine Learning: An Introduction",
  "author": "Ethem Alpaydin",
  "publisher": "MIT Press",
  "volume": 4,
  "year": 20
}
