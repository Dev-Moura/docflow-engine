from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

class UserService:
    def __init__(
        self,
        repository: UserRepository
    ):
        self.repository = repository

    async def create_user(
        self,
        data: UserCreate
    ) -> User : 
        
        existing_user = (
            await self.repository.get_by_email(
                data.email
            )
        )
    
        if existing_user:
            raise ValueError(
                "Email already registered"
            )
        
        hashed_password = hash_password(
            data.password
        )

        user = User(
            name=data.nome,
            email=data.email,
            password_hash=hashed_password,
            
        )

        return await self.repository.create(user)