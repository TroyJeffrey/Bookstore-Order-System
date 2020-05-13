# Troy Amegashie
# Advanced Programming Techniques
# Final Project
# Book Order System
# 05.07.2020


import sqlite3
from sqlite3 import Error


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn


connection = create_connection("../assignment-13/Assignment13.db")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_customer_table = """
CREATE TABLE IF NOT EXISTS customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first TEXT NOT NULL,
  last TEXT NOT NULL,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip INTEGER NOT NULL
);
"""
execute_query(connection,create_customer_table)

create_book_table = """
CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    ISBN TEXT NOT NULL  ,
    edition TEXT NOT NULL,
    price TEXT NOT NULL,
    publisher TEXT NOT NULL
);
    """
execute_query(connection,create_book_table)

create_order_table = """
CREATE TABLE IF NOT EXISTS Order_t (
    number INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    total TEXT NOT NULL,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);
    """
execute_query(connection,create_order_table)

create_orderlineitem_table = """
CREATE TABLE IF NOT EXISTS order_line_item (
    order_number INTEGER,  
    book_id INTEGER,
    Quantity TEXT NOT NULL, 
    PRIMARY KEY (order_number, book_id)
    FOREIGN KEY (order_number) REFERENCES Order_t (number),
    FOREIGN KEY (book_id) REFERENCES book (book_id)
);
"""
execute_query(connection,create_orderlineitem_table)


Menu = 0
while Menu != 5:
    print('\nWelcome to your Book Order Database System \n Select a table to continue')
    print('1.Customers table')
    print('2.Books table')
    print('3.Orders table')
    print('4.Order line item')
    print('5.Exit Program')
    Menu = int(input("\n>"))
    if Menu == 1:
        customer_menu = 0
        while customer_menu != 5:
            print("\nHere is your Customer Menu. What would you like to do?")
            print("1. Add a new customer")
            print("2. Modify an existing customer")
            print("3. Print a list of all customers")
            print("4. Delete a customer")
            print("5. Return to Main Menu")
            customer_choice = int(input("\n>"))

            if customer_choice == 1:
                # String holds the query to add data to the table
                print("Please enter the details for the customer you want to add:")
                first_name = input("First name : \n>")
                last_name = input("Last name : \n>")
                street_address = input("street address : \n>")
                city = input("city : \n>")
                state = input("state : \n>")
                zip_code = input("zip code : \n>")

                create_customer = f"""
                        INSERT INTO
                          customer(first, last, address, city, state, zip)
                        VALUES
                          ('{first_name}', '{last_name}', '{street_address}', '{city}', '{state}', '{zip_code}')
                           """
                execute_query(connection, create_customer)

                print(f"\n{first_name} {last_name} has been added to the Customer table")

            elif customer_choice == 2:
                print("Please enter the details for the customer you want to modify.")
                modify = input("Field to be modified (first, last, address, city, state, zip) : \n>")
                value = input("What specific value are you modifying? (ex. Smith) : \n>")
                modified = input(f"What are you changing '{value}' to? : \n>")

                update_customer = f"""
                        UPDATE
                          customer
                        SET
                          {modify} = '{modified}'
                        WHERE
                          {modify} = '{value}'
                        """
                execute_query(connection, update_customer)

                print(f"\n'{value}' has been modified to '{modified}' successfully.")

            elif customer_choice == 3:
                print("Here is the list of all your customers in your Customer Table.\n")
                select_customers = "SELECT * from customer"
                people = execute_read_query(connection, select_customers)

                for person in people:
                    print(person)

            elif customer_choice == 4:
                print("Please enter the details of the customer you would like to delete.")
                delete_last = input("last name : \n>")
                delete_first = input("first name : \n>")

                delete_customer = f'''
                        DELETE 
                          customer
                        WHERE
                          last = '{delete_last}',
                          first = '{delete_first}'
                        '''
                execute_query(connection, delete_customer)
                print(f"{delete_first} {delete_last} has been deleted from the customer table.")

    elif Menu == 2:
        book_menu = 0
        while book_menu != 5:
            print("Here is your Book Menu. What would you like to do?")
            print("1. Add a new book")
            print("2. Modify an existing book")
            print("3. Print a list of all books")
            print("4. Delete a book")
            print("5. Return to Main Menu")
            book_choice = int(input("\n>"))

            if book_choice == 1:
                print("Please enter the details for the book you want to add:")
                title = input("Title : \n>")
                author = input("Author : \n>")
                isbn = int(input("isbn : \n>"))
                edition = int(input("Edition : \n>"))
                price = int(input("Price : \n>"))
                publisher = input("Publisher : \n>")

                create_book = f"""
                               INSERT INTO
                                 book(title, author, isbn, edition, price, publisher)
                               VALUES
                                 ('{title}', '{author}', '{isbn}', '{edition}', '{price}', '{publisher}')
                                  """
                execute_query(connection, create_book)

                print(f"{title} by {author} has been added to the Book table")

            elif book_choice == 2:
                print("Please enter the details for the book you want to modify.")
                modify = input("Field to be modified : \n>")
                value = input("What specific value are you modifying? (ex. Smith) : \n>")
                modified = input(f"What are you changing '{value}' to? : \n>")

                update_book = f"""
                               UPDATE
                                 book
                               SET
                                 {modify} = '{value}'
                               WHERE
                                 {modify} = '{modified}'
                               """
                execute_query(connection, update_book)
                print("Book has been modified successfully.")

            elif book_choice == 3:
                print("Here is the list of all your book in your Book Table.\n")
                select_books = "SELECT * from customer"
                book = execute_read_query(connection, select_books)

                for book in book:
                    print(book)

            elif book_choice == 4:
                print("Please enter the details of the book you would like to delete.")
                delete_book = input("Title : \n>")

                delete_customer = f'''
                               DELETE 
                                 customer
                               WHERE
                                 title = '{delete_book}'
                               '''
                execute_query(connection, delete_customer)
                print(f"{delete_book}  has been deleted from the customer table.")

    elif Menu == 3:
        print("Here is your Orders Table Menu. What would you like to do?")
        print("1.Add order")
        print("2.print order")
        order_choice = int(input("\n>"))
        if order_choice == 1:
            print("Enter the details of the Order:")
            date = input("What is the order date?")
            total = input("What is the total number of orders?")
            customer_id = int(input("Enter the customer id of the customer making the order."))

            create_order = f"""
            INSERT INTO
                 Order_t (date, total, customer_id)
            VALUES
                ('{date}', '{total}','{customer_id} );
            """

            execute_query(connection, create_order)

        elif order_choice == 2:
            select_orders = "SELECT * FROM Order_t"
            orders_books = execute_read_query(connection, select_orders)

            for book in orders_books:
                print(book)

    elif Menu == 4:
        print("Here is your Order line Item Menu. What would you like to do?")
        print("1.Add item")
        print("2.Print Order line items")
        order_line_choice = int(input())
        if order_line_choice == 1:
            print("Please enter the details of the item")
            order_number = int(input("What is the Order number?"))
            Book_id = int(input("What is the book id ?"))
            quantity = input("What is the order quantity of that item")

            create_item = f"""
            INSERT INTO 
                    order_line_item (order_number, book_id, Quantity)
            VALUES
                    ('{order_number}','{Book_id}','{quantity}');
            """
            execute_query(connection,create_item)
        if order_line_choice == 2:
            select_item = "SELECT * FROM order_line_item"
            item = execute_read_query(connection,select_item)

            for i in item:
                print(i)


