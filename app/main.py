from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.categories.routers import router as router_categories
from app.products.routers import router as router_products


app = FastAPI()
app.include_router(router_categories)
app.include_router(router_products)

origins = [
    "http://localhost:8080"
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['GET', 'POST','PUT','PATCH','DELETE'],
                   allow_headers=['*'])