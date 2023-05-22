from coupon_code import *

product_A = int(input("Please enter the number of 'Product A' required: "))
product_B = int(input("Please enter the number of 'Product B' required: "))
product_C = int(input("Please enter the number of 'Product C' required: "))
gift_check = input("Purchase this as a gift? (Y/N)")
total_quantity = product_A + product_B + product_C
subtotal = product_A * 20 + product_B * 40 + product_C *50

# Price of the products
if product_A != 0:
    print("Price of Product A for",product_A,"item(s) = ",product_A * 20)
if product_B != 0:
    print("Price of Product B for",product_B,"item(s) = ",product_B * 40)
if product_C != 0:
    print("Price of Product C for",product_C,"item(s) = ",product_C * 50)

# To print the subtotal amount
print ("Subtotal = ", subtotal)

# Coupon Code
if subtotal > 200:
    if (total_quantity>10) & (total_quantity<=20):
        print("bulk_5 coupon code applied")
        total = bulk_5(subtotal)
    elif (total_quantity>20) & (total_quantity<=30):
        print("bulk_10 coupon code applied")
        total = bulk_10(subtotal)
    elif (total_quantity>30) & (product_A>15) or (product_B>15) or (product_C>15):
        print("tiered_50 coupon code applied")
        total = tiered_50(product_A,product_B,product_C)
    else:
        print("flat_10 coupon code applied")
        total = flat_10(subtotal)
else:
    total = subtotal
    print ("No eligibile coupons found")

# Print Discount amount
print("Discounted amount :",subtotal - total)

# Gift Wrap
if (gift_check == 'Y') or (gift_check == 'y'):
    gift_wrap_fee = total_quantity
else:
    gift_wrap_fee = 0

print("Gift wrap fee: ",gift_wrap_fee)

# Shipping Fee
if total_quantity > 0:
    units = total_quantity // 10
    if total_quantity % 10 !=0 :
        units += 1
    shipping_charge = units * 5

print ("Shipping Charges :",shipping_charge)

# Total Amount
TotalAmount= total+gift_wrap_fee+shipping_charge
print ("Total amount :",TotalAmount)

print("Thank you for shopping with us")