from db.db import engine, SessionLocal
from db.models import Base, Category, Book
from db.crud import create_category, create_book

Base.metadata.create_all(bind=engine)

db = SessionLocal()

cat1 = create_category(db, "Фантастика")
cat2 = create_category(db, "Программирование")

create_book(db, "Дюна", "Научная фантастика о пустынной планете", 599.99, "", cat1.id)
create_book(db, "Основание", "Классика научной фантастики", 499.99, "", cat1.id)
create_book(db, "Python для начинающих", "Изучаем Python с нуля", 899.99, "", cat2.id)
create_book(db, "Алгоритмы", "Структуры данных и алгоритмы", 1299.99, "", cat2.id)

print("База данных успешно заполнена!")
db.close()