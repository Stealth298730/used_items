import asyncio
from fastapi import FastAPI,HTTPException,status,Depends
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn


from app.routes.users import users_route
from app.routes.products import products_route
from app.db.base import create_db

app = FastAPI()
app.include_router(users_route)
app.include_router(products_route)
#app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(TrustedHostMiddleware,["127.0.0.1","127.0.0.2"])
app.add_middleware(GZipMiddleware,minimum_size = 1000)

if __name__ == "__main__":
    #asyncio.run(create_db())
    uvicorn.run("main:app",reload=True)