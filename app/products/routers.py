from typing import Annotated, List, Optional
from fastapi import APIRouter, Query
from app.products.dao import ProductsDAO
from app.products.schemas import SProducts, SProductsUpdate, SProductsId
from app.products.filter import filt

router = APIRouter(prefix='/products', tags=['Продукты'])

@router.get('/all')
async def get_all_producrs()-> List[SProducts]:
    return await ProductsDAO.fild_all()

@router.post('/add')
async def add_products(data: SProducts):
    await ProductsDAO.add_data(id=data.id,
                               name=data.name,
                               qty= data.qty,
                               category=data.category, 
                               cost= data.cost )
    return{'message':'Товар успешно добавлен'}

@router.patch('/update')
async def update_products(valid_data: SProductsId, data: SProductsUpdate):
    await ProductsDAO.update_data(id=valid_data.id, qty=data.qty, cost = data.cost,)
    return{'message':'Товар обновлен'}
    
@router.delete('/delete')
async def delet_product(data: SProductsId):
    await ProductsDAO.delete_data_by_id(model_id=data.id)
    return {'message':'Товар удален'}

@router.get('/filter_search')
async def filter_search(name: Optional[str] = Query(None),
                        category: Optional[int] = Query(None),
                        min_qty:Optional[int] = Query(None),
                        max_qty:Optional[int] = Query(None), 
                        min_cost:Optional[int] = Query(None), 
                        max_cost:Optional[int] = Query(None)):

        result = await ProductsDAO.filter_by(name=name,
                                     category=category,
                                     min_qty=min_qty,
                                     max_qty=max_qty,
                                     min_cost=min_cost,
                                     max_cost=max_cost)
        
        if result:
            return result
        return {'message': 'Нет совпадений'}
    
@router.get('/{id}')
async def get_prod_by_id(id: int):
    result = await ProductsDAO.find_one_or_none(id=id)
    if result != None:
        return result
    return {'message':'Товар не существует'}