
from pydantic import BaseModel

class Settings(BaseModel):
    CONST1 = 10
    CONST2 = 20

settings = Settings()