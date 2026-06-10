# main.py

from database import *

# DISPLAY USER
def print_user(user):

    print("\n-----------------------------")
    print(f"ID       : {user['id']}")
    print(f"Name     : {user['name']}")
    print(f"Email    : {user['email']}")
    print("-----------------------------")


# DISPLAY PRODUCT
def print_product(product):

    print("\n-----------------------------")
    print(f"ID       : {product['id']}")
    print(f"Name     : {product['name']}")
    print(f"Category : {product['category']}")
    print(f"Price    : ₹{product['price']}")
    print(f"Stock    : {product['stock']}")
    print("-----------------------------")


# DISPLAY CART
def print_cart(item):

    print("\n-----------------------------")
    print(f"Cart ID      : {item['id']}")
    print(f"User Name    : {item['user_name']}")
    print(f"Product Name : {item['product_name']}")
    print(f"Quantity     : {item['quantity']}")
    print("-----------------------------")


# DISPLAY ORDER
def print_order(order):

    print("\n-----------------------------")
    print(f"Order ID     : {order['id']}")
    print(f"Customer     : {order['name']}")
    print(f"Amount       : ₹{order['total_amount']}")
    print(f"Order Date   : {order['order_date']}")
    print("-----------------------------")


# DISPLAY PAYMENT
def print_payment(payment):

    print("\n-----------------------------")
    print(f"Payment ID      : {payment['id']}")
    print(f"Order ID        : {payment['order_id']}")
    print(f"Payment Method  : {payment['payment_method']}")
    print(f"Payment Status  : {payment['payment_status']}")
    print("-----------------------------")


# MENU
def menu():

    print("\n===================================")
    print("     MINI E-COMMERCE BACKEND")
    print("===================================")

    print("1. Initialize Database")

    print("\n----- USER MANAGEMENT -----")
    print("2. Add User")
    print("3. View Users")
    print("4. Search User")
    print("5. Delete User")

    print("\n----- PRODUCT MANAGEMENT -----")
    print("6. Add Product")
    print("7. View Products")
    print("8. Search Product")
    print("9. Delete Product")

    print("\n----- CART MANAGEMENT -----")
    print("10. Add To Cart")
    print("11. View Cart")

    print("\n----- ORDER MANAGEMENT -----")
    print("12. Place Order")
    print("13. View Orders")

    print("\n----- PAYMENT MANAGEMENT -----")
    print("14. Add Payment")
    print("15. View Payments")

    print("\n16. Exit")

    print("===================================")


# MAIN FUNCTION
def main():

    while True:

        menu()

        choice = input("Enter your choice: ")

        # INITIALIZE DATABASE
        if choice == "1":

            initialize_db()

        # ADD USER
        elif choice == "2":

            name = input("Enter Name: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            add_user(name, email, password)

        # VIEW USERS
        elif choice == "3":

            users = view_users()

            for user in users:
                print_user(user)

        # SEARCH USER
        elif choice == "4":

            keyword = input("Enter keyword: ")

            results = search_user(keyword)

            for user in results:
                print_user(user)

        # DELETE USER
        elif choice == "5":

            user_id = input("Enter User ID: ")

            delete_user(user_id)

        # ADD PRODUCT
        elif choice == "6":

            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))

            add_product(name, category, price, stock)

        # VIEW PRODUCTS
        elif choice == "7":

            products = view_products()

            for product in products:
                print_product(product)

        # SEARCH PRODUCT
        elif choice == "8":

            keyword = input("Enter keyword: ")

            results = search_product(keyword)

            for product in results:
                print_product(product)

        # DELETE PRODUCT
        elif choice == "9":

            product_id = input("Enter Product ID: ")

            delete_product(product_id)

        # ADD TO CART
        elif choice == "10":

            user_id = int(input("Enter User ID: "))
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))

            add_to_cart(user_id, product_id, quantity)

        # VIEW CART
        elif choice == "11":

            items = view_cart()

            for item in items:
                print_cart(item)

        # PLACE ORDER
        elif choice == "12":

            user_id = int(input("Enter User ID: "))
            total_amount = float(input("Enter Total Amount: "))

            place_order(user_id, total_amount)

        # VIEW ORDERS
        elif choice == "13":

            orders = view_orders()

            for order in orders:
                print_order(order)

        # ADD PAYMENT
        elif choice == "14":

            order_id = int(input("Enter Order ID: "))
            payment_method = input("Enter Payment Method: ")
            payment_status = input("Enter Payment Status: ")

            add_payment(order_id, payment_method, payment_status)

        # VIEW PAYMENTS
        elif choice == "15":

            payments = view_payments()

            for payment in payments:
                print_payment(payment)

        # EXIT
        elif choice == "16":

            print("Goodbye 👋")
            break

        else:

            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()