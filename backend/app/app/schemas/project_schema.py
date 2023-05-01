from datetime import datetime
from app.models.project_model import ProjectBase
from app.utils.partial import optional
from uuid import UUID
from .user_schema import IUserReadWithoutGroups


class IProjectCreate(ProjectBase):
    
    project_users: list[UUID] | None = []

    def __init__(self, **data):
        super().__init__(**data)
        start_date = self.start_date.replace(tzinfo=None)
        self.start_date = datetime(start_date.year, start_date.month, start_date.day)
        end_date = self.end_date.replace(tzinfo=None)
        self.end_date = datetime(end_date.year, end_date.month, end_date.day)
    

class IProjectRead(ProjectBase):
    id: UUID

class IProjectReadWithUsers(ProjectBase):
    id: UUID
    users: list[IUserReadWithoutGroups] | None = []


@optional
class IProjectUpdate(ProjectBase):
    
    def __init__(self, **data):
        super().__init__(**data)
    


# class IGroupCreate(GroupBase):
#     pass


# class IGroupRead(GroupBase):
#     id: UUID


# class IGroupReadWithUsers(GroupBase):
#     id: UUID
#     users: list[IUserReadWithoutGroups] | None = []


# # All these fields are optional
# @optional
# class IGroupUpdate(GroupBase):
#     pass
