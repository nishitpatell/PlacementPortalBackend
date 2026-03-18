
import uuid
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    domains = Column(ARRAY(String), nullable=False)
    website = Column(String, nullable=True)
    hr_email = Column(String, nullable=True)