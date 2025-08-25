from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    quantity: int
    description: str

class ItemCreate(ItemBase):
    pass

# NEW: for updating an item (PUT)
class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
