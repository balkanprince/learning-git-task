# -*- coding: utf-8 -*- 
shopping_list = {
    "Piekarnia": ["chleb", "pączek", "bułki"],
    "Warzywniak": ["marchew", "seler", "rukola"]
}

print("Lista zakupów")
for shop, items in shopping_list.items():
    formatted_shop = shop.capitalize()
    formatted_items = [item.capitalize() for item in items]
    print(f"Idę do {formatted_shop}, kupuję tu następujące rzeczy: {formatted_items}.")
    total_items = sum(len(items) for items in shopping_list.values())
    print(f"W sumie kupuję {total_items} produktów.")
    total_items = sum(len(items) for items in shopping_list.values())
print(f"W sumie kupuję {total_items} produktów.")
