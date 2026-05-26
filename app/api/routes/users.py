from fastapi import(
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependecies import get_db

from app.repositories.user_repository import (
    UserRepository,
)

from app.schemas.user import (
    UserCreate,
    UserResponse,
)

from app.services.user_service import (
    UserService,
)

from app.core.dependencies import (
    get_current_user,
)

from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)

async def create_user(
    data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    respository = UserRepository(db)
    service = UserService(respository)

    try:
        user  = await service.create_user(data)
        return UserResponse.model_validate(user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

@router.get(
    "/me",
    response_model=UserResponse,
)

async def get_me(
    current_user: User = Depends(
        get_current_user
    ),
):
    return UserResponse.model_validate(
        current_user
    )