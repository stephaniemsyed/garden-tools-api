from fastapi import Depends, FastAPI

from app.dependencies import get_token_header
from app.routers.internal import admin
from app.routers import users, items

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    print("hit root")
    return {"message": "Hello Bigger Applications!"}


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "Hello Bigger Applications!"}
