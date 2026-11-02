
try:
    with open("productData.txt", "a+") as f1:
        f1.seek(0)
        data = f1.read()

       
        #f1.write("Product_name\tPrice\tQty   \tAmount\n")

        pname = input("Enter product name  = ")
        price = float(input("Enter product price = "))
        Qty = int(input("Enter product Qty   = "))

        Ta = price * Qty
        Amount = Ta

        f1.write(f"{pname}      \t{price}  \t{Qty}     \t{Amount}\n")

    print("Data saved successfully!")

except Exception as e:
    print("Error:", e)
