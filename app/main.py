from fastapi import FastAPI
from app.categories.routers import router as router_categories
from app.products.routers import router as router_products


app = FastAPI()
app.include_router(router_categories)
app.include_router(router_products)