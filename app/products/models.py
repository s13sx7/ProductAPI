from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, int_pk,str_uniq


class Products(Base):
    __tablename__ = "products"
    
    id: Mapped[int_pk]
    name: Mapped[str_uniq]
    qty: Mapped[int] = mapped_column(nullable=False)
    category: Mapped[int] = mapped_column(ForeignKey('products_categories.id'))
    cost: Mapped[int]  = mapped_column(nullable=False)
