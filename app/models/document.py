from sqlalchemy import String 
from sqlalchemy import ForeignKey
from sqlalchemy import Enum as SqlEnum

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from app.models.enums import DocumentStatus

class Document(BaseModel):

    __tablename__ = "documents"

    title: Mapped[str] = mapped_column(
        String[255],
        nullable=False
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    status: Mapped[DocumentStatus] = mapped_column(
        SqlEnum(DocumentStatus),
        default=DocumentStatus.PENDING    
    )

    owner_id = mapped_column(
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="documents"
    )