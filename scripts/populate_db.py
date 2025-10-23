import random
from app.db import Product, SessionLocal, init_db

init_db()
session = SessionLocal()

names = ["کرم آبرسان", "شامپو تقویت‌کننده", "ماسک مو", "رژ لب", "ادکلن مردانه", "اسپری بدن",
         "کرم ضدآفتاب", "سرم صورت", "تونر پاک‌کننده", "صابون گیاهی"]

for i in range(1, 101):
    name = random.choice(names)
    desc = f"{name} مدل {i} با فرمول خاص برای مراقبت پوست و مو."
    price = round(random.uniform(50, 3000), 2)
    session.add(Product(name=name, description=desc, price=price))

session.commit()
session.close()
print("Database population completed!")
