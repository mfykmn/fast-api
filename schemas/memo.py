from pydantic import BaseModel, Field

class InsertAndUpdateMemoSchema(BaseModel):
    title: str = Field(..., description="タイトル", example="明日のアジェンダ")
    description: str = Field(..., description="説明", example="プロジェクトの進捗状況")

class MemoResponseSchema(InsertAndUpdateMemoSchema):
    memo_id: int

class ResponseSchema(BaseModel):
    message: str = Field(..., description="タイトル", example="明日のアジェンダ")
