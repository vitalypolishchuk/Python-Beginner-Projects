# ******************************************
# category = Account('Category') -> to create a category
# category.deposit(amount,'description') -> to deposit the money
# category.withdraw(amount,'description') -> to withdraw the money
# category.transfer(amount,'description') -> to transfer the money to the other category
# print(category) -> to check the history of the operations
# ******************************************

import budget

food = budget.Account("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = budget.Account("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Account("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)