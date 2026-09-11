product_value=float(input("Enter the product value: "))
if product_value<=100:
    discount=product_value*0.02
else:
    discount=product_value*0.10
final_value=product_value-discount
print(f"\nThe final value after discount is: ${final_value:.2f}")
print(f"You save: ${discount:.2f}")