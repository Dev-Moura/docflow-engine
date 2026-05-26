from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependecies import get_db

from app.repositories.user_repository import (
    UserRepository,    
)

from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)

from app.services.auth_service import (
    AuthService,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/login",
    response_model=TokenResponse,
)

async def login (
    data: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    repository = UserRepository(db)

    service = AuthService(repository)

    try:
        
        acess_token = (
            await service.authenticate_user(
                email=data.email,
                password=data.password,
         )
        
        )    

        return TokenResponse(
            acess_token=acess_token,
        )
    

    except ValueError:
    
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
)
