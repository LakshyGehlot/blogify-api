from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.db.session import get_session
from .services import AuthServices
from .schema import CreateUser, User, SignIn
from src.utils import genrate_token, decode_token, verify_password

auth_serivces = AuthServices()

auth_router = APIRouter()

@auth_router.post("/signup", response_model=User)
async def register(user_data: CreateUser, session: AsyncSession = Depends(get_session)):
    if await auth_serivces.user_exists(user_data.email, session):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    
    user = await auth_serivces.create_user(user_data, session)
    return user

@auth_router.post("/signin")
async def signin(credentials: SignIn, session: AsyncSession = Depends(get_session)):
    user = await auth_serivces.get_user_by_email(credentials.email, session)
    if (user is None) or (not verify_password(credentials.password, user.password_hash)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect email or password")
    
    user_data = {"email": user.email, "uid": str(user.uid)}
    acess_token = genrate_token(user_data)
    refresh_token = genrate_token(user_data, refresh=True, expiry=21600)
    return JSONResponse(content={"acess-token": acess_token, "refresh-token": refresh_token, **user_data})