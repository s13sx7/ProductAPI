from pydantic import BaseModel

class SProducts(BaseModel):
    id: int | None
    name: str | None
    qty: int | None
    category: int | None
    cost: int| None
    
    class Config:
        from_atribute = True

class SProductsId(BaseModel):
    id:int
    
    class Config:
        from_atribute = True
        
class SProductsUpdate(BaseModel):
    qty: int
    cost: int
    
    class Config:
        from_atribute = True