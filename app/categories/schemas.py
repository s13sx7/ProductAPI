from pydantic import BaseModel

class SCategories(BaseModel):
    
    id: int
    name:str
    
    class Config:
        from_atribute = True