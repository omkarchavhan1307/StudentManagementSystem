from pydantic import BaseModel, Field
from typing import Annotated , Optional


class updateStruct(BaseModel):
    name:Annotated[Optional[str], Field(title="Enter your name " , default=None)]
    age:Annotated[Optional[int], Field(title="Enter your age " , default=None)]