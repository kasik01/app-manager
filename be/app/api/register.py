from typing import Any

from fastapi import APIRouter, Depends

from app.helpers.exception_handler import CustomException
from app.schemas.base import DataResponse
from app.schemas.user import UserItemResponse, UserRegisterRequest
from app.services.user import UserService

router = APIRouter()

@router.post('', response_model=DataResponse[UserItemResponse])
def register(register_data: UserRegisterRequest, user_service: UserService = Depends()) -> Any:
    try:
        register_user = user_service.register_user(register_data)
        return DataResponse().success_response(data=register_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
