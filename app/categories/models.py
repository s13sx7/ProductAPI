from app.database import Base, int_pk, str_uniq
from sqlalchemy.orm import Mapped


class Categories(Base):
    __tablename__ = "products_categories"
    
    id: Mapped[int_pk]
    name:Mapped[str_uniq]