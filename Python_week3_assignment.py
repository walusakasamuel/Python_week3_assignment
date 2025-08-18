#1. A function calculate_discount(price, discount_percent) calculates the final price after applying a discount.
#The original price (price) and the discount percentage (discount_percent) are the parameters
#If the discount is 20% or higher, the discount is applied; otherwise,it returns the original price.

def calculate_discount(price, discount_percent):
  """
  The function calculates the final price after applying a discount.

  Args:
    Price: original price before discount
    Discount_%: The discount percentage.

  Returns:
    The final price after applying the discount, or the original price if
    no discount was applied.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# 2. Prompt the user for input
try:
  original_price = float(input("Enter the original price of the item: "))
  discount_percentage = float(input("Enter the discount percentage: "))

  # Final price calculations.
  final_price = calculate_discount(original_price, discount_percentage)
  
  #print the results.
  if final_price != original_price:
    print(f"Final price after discount: ${final_price:.2f}")
  else:
    print(f"No discount applied. Original price: ${original_price:.2f}")

except ValueError:
  print("Invalid input. Please enter valid numbers only.")