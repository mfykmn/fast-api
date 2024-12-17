from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    title: str = Field(..., description="タイトル", example="アンパンマンと山の人")
    category: str = Field(..., description="カテゴリ", example="絵本")
    publish_year: int = Field(default=None, description="出版年", example=2024)
    price: float = Field(default=None, gt=0, le=5000, description="価格", example=2500)


class BookResponseSchema(BookSchema):
    id: int
    