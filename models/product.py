from sqlalchemy import Column, DateTime, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models.category import Category


Base = declarative_base()

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship(
        Category,
        backref=backref('products',
                        uselist=True,
                        cascade='delete, all')
    )

    def __str__(self):
        return f"{self.name}{self.title}{self.price}"

class Services(Base): # Определяем класс Услуги
    __tablename__ = 'services' # Задаем название таблицы Услуги

    id = Column(Integer, primary_key=True) # Задаем идентификатор
    name = Column(String, index=True) # Название услуги
    title = Column(String) # Название того кто оказывает услугу
    price = Column(Float) # Стоимость услуги
    quantity = Column(Integer) # Количество предоставляемых услуг
    is_active = Column(Boolean) # Предоставляется ли услуга
    date_start = Column(DateTime) # Дата начала предоставления услуги
    data_stop = Column(DateTime) # Дата окончания предоставления услуги
    category_id = Column(Integer, ForeignKey('category.id')) # Устанавливаем связь
    # с внешней таблицей Category по полю id

    category = relationship( # Здесь устанавливается связь один ко многим
        Category, # внешняя таблица Category с которой мы связаны через ForeignKey
        backref = backref( # обратная ссылка на таблицу services
            'services', # название таблицы
            uselist=True, # применить каскадное удаление ко всем найденным отношениям
            cascade='delete, all' # все товары связанные с данной категорией удалить
            # то есть если удаляется категория удаляются все записи об услугах
        )

    )
    def __str__(self):
        return f"{self.name}{self.title}{self.price}" #