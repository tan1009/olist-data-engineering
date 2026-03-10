import pandas as pd

# Load raw data
customers = pd.read_csv("raw/olist_customers_dataset.csv")
geolocation = pd.read_csv("raw/olist_geolocation_dataset.csv")
items = pd.read_csv("raw/olist_order_items_dataset.csv")
payments = pd.read_csv("raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("raw/olist_order_reviews_dataset.csv")
orders = pd.read_csv("raw/olist_orders_dataset.csv")
products = pd.read_csv("raw/olist_products_dataset.csv")
sellers = pd.read_csv("raw/olist_sellers_dataset.csv")
translations = pd.read_csv("raw/product_category_name_translation.csv")

# Create datasets dictionary
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
    missing = df.isnull().sum().sum()
    print(f"{name}: {missing} missing values")


reviews["review_comment_title"] = reviews["review_comment_title"].fillna("No Comments")
reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No Comments")

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


orders["order_approved_at"] = orders["order_approved_at"].fillna("2099-01-01 00:00:00")
orders["order_delivered_carrier_date"] = orders["order_delivered_carrier_date"].fillna("2099-01-01 00:00:00")
orders["order_delivered_customer_date"] = orders["order_delivered_customer_date"].fillna("2099-01-01 00:00:00")
orders["order_estimated_delivery_date"] = orders["order_estimated_delivery_date"].fillna("2099-01-01 00:00:00")
orders["order_estimated_delivery_date"] = orders["order_estimated_delivery_date"].fillna("2099-01-01")

items["shipping_limit_date"] = pd.to_datetime(items["shipping_limit_date"])
reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"])
reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"])
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"])
orders["order_delivered_carrier_date"] = pd.to_datetime(orders["order_delivered_carrier_date"])
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])
orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"])

print("\n=== Final Check ===")
for name, df in datasets.items():
    missing = df.isnull().sum().sum()
    print(f"{name}: {missing} missing values")

customers.to_csv("cleaned/cleaned_customers.csv", index=False)
geolocation.to_csv("cleaned/cleaned_geolocation.csv", index=False)
items.to_csv("cleaned/cleaned_items.csv", index=False)
payments.to_csv("cleaned/cleaned_payments.csv", index=False)
reviews.to_csv("cleaned/cleaned_reviews.csv", index=False)
orders.to_csv("cleaned/cleaned_orders.csv", index=False)
products.to_csv("cleaned/cleaned_products.csv", index=False)
sellers.to_csv("cleaned/cleaned_sellers.csv", index=False)
translations.to_csv("cleaned/cleaned_translations.csv", index=False)

print(orders.isnull().sum())


print("\n✅ Week 1 Complete! All cleaned files saved!")