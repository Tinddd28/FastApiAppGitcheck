from typing import Optional
from pydantic import BaseModel


class requestModel(BaseModel):
    user_id: int
    group_number: str
    login: str
    
    
class check_tests(requestModel):
    ok: bool = True
    num: int
    user_id: int
    login: str
    number_of_lab: int
    status: str
    
    
class exist_user(requestModel):
    ok: bool = True
    #user_id: int
    login: str
    num_in_list: int
    status: str
    