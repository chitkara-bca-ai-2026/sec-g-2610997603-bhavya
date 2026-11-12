print("=" * 55)
print("              DATA CONVERSION UTILITY")
print("=" * 55)

product_name = input("Enter Product Name : ")
price = float(input("Enter Price       : "))
quantity = int(input("Enter Quantity    : "))


total_price = price * quantity


amount_str = str(total_price)

print("\n" + "-" * 55)
print("              TYPE CASTING SUMMARY")
print("-" * 55)

print("Variable       Value       Python Type")
print("-" * 55)

print("product_name   ", product_name, "    ", type(product_name))
print("price          ", price, "    ", type(price))
print("quantity       ", quantity, "          ", type(quantity))
print("total_price    ", total_price, "    ", type(total_price))
print("amount_str     ", amount_str, "    ", type(amount_str))

print("-" * 55)
print("                 TAX INVOICE")
print("-" * 55)

print("Product Name : ", product_name)
print("Price per Unit : Rs.", price)
print("Quantity      : ", quantity)
print("-" * 55)
print("Invoice Total : Rs.", total_price)

print("=" * 55)