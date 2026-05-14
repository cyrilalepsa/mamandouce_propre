"""
Routes de développement de l'embryon pour MamanDouce - Version Réaliste (Sans Emergent)
"""
from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(tags=["embryo"])

# Base de données des semaines - Pointant vers nos images locales
# Les images devront être placées dans : backend/static/assets/embryo/
WEEKLY_DATA = {
    1: {
        "title": "Le début de l'aventure",
        "size": "0.1 mm",
        "fruit": "un grain de sable",
        "dev": "L'œuf fécondé descend vers l'utérus pour la nidation."
    },
    # On pourra compléter les 40 semaines ici avec N2
}

@router.get("/embryo/week/{week}")
async def get_embryo_info(week: int):
    if week < 1 or week > 41:
        raise HTTPException(status_code=400, detail="Semaine invalide")
    
    # On récupère les infos de base ou on les calcule
    data = WEEKLY_DATA.get(week, {"title": f"Semaine {week}", "size": "N/A", "fruit": "N/A", "dev": "Développement en cours..."})
    
    return {
        "week": week,
        "title": data["title"],
        "embryo_size": data["size"],
        "fruit_comparison": data["fruit"],
        "development": data["dev"],
        # C'EST ICI QUE LA MAGIE OPÈRE : Lien local uniquement
        "image_url": f"/static/assets/embryo/week{week}.png"
    }