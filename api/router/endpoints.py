from fastapi import APIRouter

router = APIRouter()

@router.get("/{country}")
def pais(country):
    return {
        "Pais" : country
    }