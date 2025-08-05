
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BinCreate(BaseModel):
    title: Optional[str] = Field(None, description="Optional paste title")
    slug: Optional[str] = None
    content: str = Field(..., min_length=1, description="The body of the bin")
    language: str = Field("plaintext", description="Syntax highlight language")
    wrap_text: bool = Field(False, description="Wrap long lines")
    burn_after_read: bool = Field(False, description="Delete after one view")
    expiry_choice: Optional[str] = Field("24h", description="One of '1h','24h','7d','31d'")

class BinView(BaseModel):
    slug: str
    title: Optional[str]
    content: str
    language: str
    wrap_text: bool
    burn_after_read: bool
    expires_at: datetime
    created_at: datetime

class UserMetaView(BaseModel):
    paste_slug: str
    ip_address: str
    user_agent: str
    timestamp: datetime
