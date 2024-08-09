import os

from googleapiclient.errors import HttpError

from config.config import sheet_id
from src.models.model import requestModel, exist_user
from src.gSheetsSet import get_sheet

SPREADSHEET_ID = sheet_id

class google_sheets:
    @classmethod
    async def check_user(cls, data: requestModel) -> exist_user:
        try:
            sheet = get_sheet().spreadsheets()
            user_dict = data.model_dump()
            l = user_dict["group_number"]
            range_ = f"{l}!A:AH"
            
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
            values = result.get("values", [])
            flag = 0
            if not values:
                return {"ok": False, "login": user_dict["login"], "num_in_list": -1}
            else:
                match_found = 0
                for row in values:
                    try:
                        # Номер по списку (первый столбец)
                        num = row[0]
                        # Ник GitHub (последний столбец, 32-й в этом примере)
                        github_nick = row[33]
                        

                        # Проверка совпадения номера лабораторной и ника GitHub
                        if github_nick == user_dict["login"]:
                            print(f"Совпадение найдено: Номер по списку: {num} GitHub: {github_nick}")
                            match_found = 1
                            return {"ok": True, "login": github_nick, "num_in_list": num}  # Прекращаем поиск после первого совпадения
                    except IndexError:
                        print("Некорректная строка, пропускаем...")

                if not match_found:
                    return {"ok": False, "login": user_dict["login"], "num_in_list": -2}
                    
              
            # Добавить проверку наличия идентификатора (тг, дискорд), если нужна
            
        except HttpError as error:
            print(error)
            
    
    @classmethod
    async def exists_list(cls, group_num: str) -> int:
        try:
            service = get_sheet()
            
            spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
            sheets = spreadsheet.get("sheets", [])
            
            for sheet in sheets:
                if sheet["properties"]["title"] == group_num:
                    return 1
            
        except HttpError as error:
            print(error)

        return 0