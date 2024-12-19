from fastapi import APIRouter
import asyncio
import httpx

router = APIRouter(tags=["Addresses"], prefix="/addresses")

@router.get("/")
async def get_address():
    zip_codes = [
        "0600000", # 北海道
        "1000001", # 東京
        "9000000", # 沖縄
    ]
    return await asyncio.gather(*(fetch_address(zip_code) for zip_code in zip_codes))

async def fetch_address(zip_code: str):
    async with httpx.AsyncClient() as client:
        url = "https://zipcloud.ibsnet.co.jp/api/search"
        param = {"zipcode": zip_code}
        response = await client.get(url, params=param)
        return response.json()
