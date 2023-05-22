# Flat 10
def flat_10(subtotal):
    Total = subtotal - 10
    return Total

# Bulk 5
def bulk_5(subtotal):
    Total = subtotal * 95/100
    return Total
# Bulk 10
def bulk_10(subtotal):
    Total = subtotal * 90/100
    return Total
# Tiered 50
def tiered_50(quantity_A,quantity_B,quantity_C):
    tiered_A = 0
    tiered_B = 0
    tiered_C = 0
    if quantity_A> 15:
        tiered_A = 15*20 + (quantity_A-15) * 20 * (50/100)
    else:
        tiered_A = quantity_A * 20 
    if tiered_B> 15:
        tiered_B = 15*40 + (quantity_B-15) * 40 * (50/100)
    else:
        tiered_B = quantity_B * 40 
    if quantity_C> 15:
        tiered_C = 15*50 + (quantity_C-15) * 50 * (50/100)
    else:
        tiered_C= quantity_C * 50 
    total = tiered_A + tiered_B + tiered_C
    return total