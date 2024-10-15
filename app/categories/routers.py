from fastapi import APIRouter
from app.categories.dao import CategoriesDAO
from app.categories.schemas import SCategories

router = APIRouter(prefix='/categories', tags=['Категории'])

@router.get('/all')
async def get_categories():
    return await CategoriesDAO.qty_products_in_categories()

@router.get('/{id}')
async def get_categories(id: int):
    return await CategoriesDAO.qty_products_in_category(model_id = id)

@router.post('/add')
async def add_products(data: SCategories):
    await CategoriesDAO.add_data(id=data.id,
                               name=data.name,)
                               
    return 'Категория успешно добавлена'
