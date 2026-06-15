from fastapi import APIRouter

# 创建一个新的APIRouter实例
router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/categories")
async def get_news_categories(skip: int = 0, limit: int = 100):
    return{
        "code": 200,
        "message": "成功获取新闻分类",
        "data":"新闻分类列表"
    }