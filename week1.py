import pandas as pd

customers = pd.read_csv("raw/olist_customers_dataset.csv")
geolocation = pd.read_csv("raw/olist_geolocation_dataset.csv")
items = pd.read_csv("raw/olist_order_items_dataset.csv")
payments = pd.read_csv("raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("raw/olist_order_reviews_dataset.csv")
orders = pd.read_csv("raw/olist_orders_dataset.csv")
products = pd.read_csv("raw/olist_products_dataset.csv")
sellers = pd.read_csv("raw/olist_sellers_dataset.csv")
translations = pd.read_csv("raw/product_category_name_translation.csv")


datasets = {
    "Customers": customers,
    "Geolocation": geolocation,
    "Order Items": items,
    "Payments": payments,
    "Reviews": reviews,
    "Orders": orders,
    "Products": products,
    "Sellers": sellers,
    "Translations": translations
}

for name, df in datasets.items():
    df.columns = df.columns.str.strip()

for name, df in datasets.items():
    print(f"\n=== {name} ===")
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print(f"Columns: {list(df.columns)}")


for name, df in datasets.items():
    missing = df.isnull().sum().sum()
    print(f"{name}: {missing} missing values")


print("\n=== Missing values per column ===")
for name, df in datasets.items():
    col_missing = df.isnull().sum()
    col_missing = col_missing[col_missing > 0]  # only show columns with missing values
    if len(col_missing) > 0:
        print(f"\n{name}:")
        print(col_missing)
print("REVIEWS==========")
reviews["review_comment_title"]  = reviews["review_comment_title"].fillna("No Comments")
reviews["review_comment_message"]  = reviews["review_comment_message"].fillna("No Comments")
print("ORDERS==========")
orders["order_approved_at"] = orders["order_approved_at"].fillna("Not Approved")
orders["order_delivered_carrier_date"] = orders["order_delivered_carrier_date"].fillna("Not Delivered")
orders["order_delivered_customer_date"] = orders["order_delivered_customer_date"].fillna("Not Delivered")
print("PRODUCTS==========")
products["product_category_name"] = products["product_category_name"].fillna("Unknown")
products["product_name_lenght"] = products["product_name_lenght"].fillna(0)
products["product_description_lenght"] = products["product_description_lenght"].fillna(0)
products["product_photos_qty"] = products["product_photos_qty"].fillna(0)


products["product_weight_g"] = products["product_weight_g"].fillna(products["product_weight_g"].median())
products["product_length_cm"] = products["product_length_cm"].fillna(products["product_length_cm"].median())
products["product_height_cm"] = products["product_height_cm"].fillna(products["product_height_cm"].median())
products["product_width_cm"] = products["product_width_cm"].fillna(products["product_width_cm"].median())

products["product_weight_g"] = products["product_weight_g"].astype(float)
products["product_length_cm"] = products["product_length_cm"].astype(float)
products["product_height_cm"] = products["product_height_cm"].astype(float)
products["product_width_cm"] = products["product_width_cm"].astype(float)

items["shipping_limit_date"] = pd.to_datetime(items["shipping_limit_date"])
reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"])
reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"])
orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"],errors= 'coerce')
orders["order_delivered_carrier_date"] =pd.to_datetime(orders["order_delivered_carrier_date"], errors= 'coerce')
orders["order_delivered_customer_date"] =pd.to_datetime(orders["order_delivered_customer_date"],errors= 'coerce')
orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"],errors= 'coerce')






customers.to_csv("cleaned_customers.csv", index=False)
geolocation.to_csv("cleaned_geolocation.csv", index=False)
items.to_csv("cleaned_items.csv", index=False)
payments.to_csv("cleaned_payments.csv", index=False)
reviews.to_csv("cleaned_reviews.csv", index=False)
orders.to_csv("cleaned_orders.csv", index=False)
products.to_csv("cleaned_products.csv", index=False)
sellers.to_csv("cleaned_sellers.csv", index=False)
translations.to_csv("cleaned_translations.csv", index=False)



print("week 1 done")


