import pandas as pd
import random
from faker import Faker

fake = Faker('en_US')  # لو حابب نخليها 'ar_EG' ممكن نغيرها
Faker.seed(42)

# عدد الصفوف
num_rows = 20000

# القيم الثابتة المحتملة
transaction_types = ['Withdrawal', 'Deposit', 'Purchase']
customer_segments = ['VIP', 'Regular', 'New']
branches = ['Nasr City', 'Maadi', 'Zamalek', 'New Cairo', 'Heliopolis']
regions = ['Cairo', 'Alexandria', 'Giza', 'Assiut', 'Mansoura']

# إنشاء البيانات
data = []
for i in range(1, num_rows + 1):
    customer_id = fake.uuid4()
    transaction_id = f'TXN{i:05d}'
    transaction_type = random.choice(transaction_types)
    amount = round(random.uniform(50, 10000), 2)
    date = fake.date_between(start_date='-1y', end_date='today')
    branch = random.choice(branches)
    region = random.choice(regions)
    customer_segment = random.choice(customer_segments)

    data.append({
        'TransactionID': transaction_id,
        'CustomerID': customer_id,
        'TransactionType': transaction_type,
        'Amount': amount,
        'Date': date,
        'Branch': branch,
        'Region': region,
        'CustomerSegment': customer_segment
    })

# تحويلها لـ DataFrame وتصديرها
df = pd.DataFrame(data)
df.to_csv('financial_transactions.csv', index=False)

print("✅ File 'financial_transactions.csv' generated successfully.")



df = pd.read_csv(r"D:\Tech Courses\Projects\Projects_Files\financial_transactions.csv")
print(df)

df.info()

print(df.columns)

print(df.columns.tolist())

print(df.shape)

print(f"The Dataset Contains {df.shape[1]} Columns")

print(f"Dataset contains {df.shape[0]} Rows and {df.shape[1]} Columns")

print(df.describe())

print(df.isnull())

print(df.isnull().sum())

print(df.duplicated())

print(df.duplicated().sum())

df['Date'] = pd.to_datetime(df['Date'])

df.info()

df.to_csv("Financial_Transactions_Cleaned.csv")



































































