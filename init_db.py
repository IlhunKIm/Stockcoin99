import openpyxl
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Stockcoin99

wb = openpyxl.load_workbook("C:/Users/kimv7/OneDrive/바탕 화면/Sparta Coding Club/pjc_01/Stockcoin99/applist.xlsx")
wb_sheet = wb.active

for row in wb_sheet:
    type = row[2].value
    if type is not None:
        company = row[3].value
        app_name = row[4].value
        image_url = row[5].value
        google_url = row[6].value
        doc = {
            'type': type, #코인, 증권 타입
            'company': company, #회사명
            'app_name': app_name, #어플리케이션명
            'image_url': image_url, #이미지 경로
            'google_url': google_url #구글 플레이스토어 경로
        }
        print(doc)
        db.applist.insert_one(doc)

wb.close()