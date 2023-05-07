import re

from pydantic import BaseModel, EmailStr, Field, validator
from pydantic.schema import date


class UserModel(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    surname: str = Field(min_length=3, max_length=20)
    email: EmailStr
    phone: str = Field(max_length=16)
    birthday: date
    additional_info: str

    @validator('phone')
    def validate_phone_number(phone: str) -> str:
        pattern = r'^\+38\d{3}-\d{3}-\d{2}-\d{2}$'
        if not re.match(pattern, phone):
            raise ValueError(
                'The number is entered incorrectly, please check the correctness of the input.'
                'The number must be in the format +380ХХ-XXX-XX-ХХ')
        return phone


class UserResponse(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=20)
    surname: str = Field(min_length=3, max_length=20)
    email: EmailStr
    phone: str = Field(max_length=16)
    birthday: date
    additional_info: str

    @validator('phone')
    def validate_phone_number(phone: str) -> str:
        pattern = r'^\+38\d{3}-\d{3}-\d{2}-\d{2}$'
        if not re.match(pattern, phone):
            raise ValueError(
                'The number is entered incorrectly, please check the correctness of the input.'
                'The number must be in the format +380ХХ-XXX-XX-ХХ')
        return phone
