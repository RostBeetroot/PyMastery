def tax_count():
    purchase_amount = float(input("Enter your purchase amount: "))

    federal_tax = 0.05
    federal_tax = purchase_amount * federal_tax

    regional_tax = 0.025
    regional_tax = purchase_amount * regional_tax

    total_tax = federal_tax + regional_tax

    total_sale_amount = purchase_amount + total_tax

    print(f"Purchase amount: ${purchase_amount:.2f}")
    print(f"Federal tax: ${federal_tax:.2f}")
    print(f"Regional tax: ${regional_tax:.2f}")
    print(f"Total tax: ${total_tax:.2f}")
    print(f"Total sale amount: ${total_sale_amount:.2f}")


tax_count()
