from app.core.security import (
    create_acess_token,
    verify_password,
)

from app.repositories.user_repository import (
    UserRepository,
)

class AuthService:

    def __init__(
            self,
            repository: UserRepository
    ):
        
        self.repository = repository

    async def authenticate_user(
            self,
            email: str,
            password: str,
    ) -> str:
        
        user = await self.repository.get_by_email(
            email
        )

        if not user: 
            raise ValueError(
                "Invalid Credentials"
            )

        valid_password = verify_password(
            password,
            user.password_hash,
        )

        if not valid_password:
            raise ValueError(
                "Invalid Credentials"
            )
        
        acess_token = create_acess_token(
            subject=str(user.id)
        )

        return acess_token