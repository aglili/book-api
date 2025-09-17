from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String, nullable=True)
    published_year = Column(Integer, nullable=True)
    price = Column(Float, nullable=True)
    
    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"