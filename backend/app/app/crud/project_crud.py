
from app.models.project_model import Project

from app.models.user_model import User
from app.schemas.project_schema import IProjectCreate, IProjectUpdate
from app.crud.base_crud import CRUDBase
from sqlmodel import select
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession


class CRUDProject(CRUDBase[Project, IProjectCreate, IProjectUpdate]):
    
    async def get_project_by_id(
        self, *, id: str, db_session: AsyncSession | None = None
    ) -> Project:
        db_session = db_session or super().get_db().session
        project = await db_session.execute(select(Project).where(Project.id == id))
        return project.scalar_one_or_none()
    
    
    async def add_user_to_project(self, *, user: User, project_id: UUID) -> Project:
        db_session = super().get_db().session
        project = await super().get(id=project_id)
        project.users.append(user)
        db_session.add(project)
        await db_session.commit()
        await db_session.refresh(project)
        return project
    
    async def delete_user_from_project(self, *, user: User, project_id: UUID) -> Project:
        db_session = super().get_db().session
        project = await super().get(id=project_id)

        if user not in project.users:
            return None
        
        project.users.remove(user)
        db_session.add(project)
        await db_session.commit()
        await db_session.refresh(project)
        return project

    async def add_users_to_project(
        self,
        *,
        users: list[User],
        project_id: UUID,
        db_session: AsyncSession | None = None,
    ) -> Project:
        db_session = db_session or super().get_db().session
        project = await super().get(id=project_id, db_session=db_session)
        project.users.extend(users)
        db_session.add(project)
        await db_session.commit()
        await db_session.refresh(project)
        return project


project = CRUDProject(Project)
