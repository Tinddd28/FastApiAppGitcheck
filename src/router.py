from fastapi import APIRouter, Depends
from typing import Annotated

from src.models.model import requestModel, check_tests, exist_user
from src.gSheets import google_sheets

router = APIRouter(
    prefix="/methods",
    tags=["tests"]
)

@router.get("/get")
async def check_user_exists(request: Annotated[requestModel, Depends()]) -> exist_user:
    list_ = await google_sheets.exists_list(request.group_number)
    print(list_)
    if (list_):
        data = await google_sheets.check_user(request)
    
        if list_ != "График":
            return {"ok": False, "login": request.login, "num_in_list": 0, "user_id": request.user_id, "group_number": request.group_number, "status": "В графике нет студентов!"}
        if int(data["num_in_list"]) > 0:
            return {"ok": True, "login": request.login, "num_in_list": int(data["num_in_list"]), "user_id": request.user_id, "group_number": request.group_number, "status": "Good!"}
        elif int(data["num_in_list"]) == -1:
            return {"ok": False, "login": request.login, "num_in_list": 0, "user_id": request.user_id, "group_number": request.group_number, "status": "Таблица пуста!"}
        elif int(data["num_in_list"]) == -2:
            return {"ok": False, "login": request.login, "num_in_list": 0, "user_id": request.user_id, "group_number":  request.group_number, "status": "Нет студента с таким аккаунтом GitHub!"}
        
    else:
        return {"ok": False, "login": request.login, "num_in_list": 0, "user_id": request.user_id, "group_number": request.group_number, "status": "Такой группы нет!"}