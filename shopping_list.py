shopping_list = [
    {"item": "Notebook", "price": 150, "purchased": False},
    {"item": "Pen", "price": 30, "purchased": True},
    {"item": "USB Drive", "price": 900, "purchased": False}
]

still_need = [x["item"] for x in shopping_list if x["purchased"] == False]

remaining_cost = sum([x["price"] for x in shopping_list if x["purchased"] == False])

print("Still need to buy:", still_need)
print("Remaining cost:", remaining_cost)