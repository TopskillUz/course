from app.models import Profession
from crud.base_crud import CRUDBase


class ProfessionCRUD(CRUDBase):
    pass


ProfessionCRUD = ProfessionCRUD(Profession)
