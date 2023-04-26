from app.models.project_model import ProjectBase
from app.utils.partial import optional
from uuid import UUID
from .user_schema import IUserReadWithoutGroups


class IProjectCreate(ProjectBase):
    pass


class IProjectRead(ProjectBase):
    id: UUID

class IProjectReadWithUsers(ProjectBase):
    id: UUID
    users: list[IUserReadWithoutGroups] | None = []


@optional
class IProjectUpdate(ProjectBase):
    pass


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
