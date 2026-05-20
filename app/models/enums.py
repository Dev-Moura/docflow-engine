from enum import Enum

class DocumentStatus(str, Enum):

    PENDING = "PENDING"

    IN_REVIEW = "IN_REVIEW"

    APPROVED = "APPROVED"

    REJECTED = "REJECTED"

