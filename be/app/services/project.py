from typing import Any
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db

from app.helpers.paging import PaginationParams, paginate
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreateRequest, ProjectUpdateRequest


class ProjectService(object):
    __instance = None

    def __init__(self) -> None:
        pass

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod   
    def create_project(data: ProjectCreateRequest):
        """
        Create a new project.
        """
        if data.user_id is None:
            raise Exception("User ID is required")

        exist_user = db.session.query(User).filter(User.id == data.user_id).first()
        if not exist_user:
            raise Exception("User does not exist")

        new_project = Project(
            user_id=data.user_id,
            name=data.name,
            is_active=data.is_active,
            description=data.description,
            url=data.url
        )
        db.session.add(new_project) 
        db.session.commit()
        return new_project
    
    @staticmethod
    def get_project(project_id: int):
        """
        Get a project by its ID.
        """
        project = db.session.query(Project).get(project_id)
        if project is None:
            raise Exception('Project not found')
        return project
       
    @staticmethod
    def get_projects_by_user(user_id: int, params: PaginationParams):
        """
        Get all projects by user_id with paging.
        """
        projects = db.session.query(Project).filter(Project.user_id == user_id)
        if not projects:
            raise Exception('No projects found for this user')
        
        result = paginate(model=Project, query=projects, params=params)

        return result
    
    @staticmethod
    def get_all_projects(params: PaginationParams):
        """
        Get all projects with paging.
        """
        _query = db.session.query(Project)
        projects = paginate(model=Project, query=_query, params=params)
        return projects
    
    @staticmethod
    def update(project_id: int, data: ProjectUpdateRequest):
        """
        Update a project.
        """
        project = db.session.query(Project).get(project_id)
        if project is None:
            raise Exception('Project not found')
        project.name = data.name if data.name is not None else project.name
        project.is_active = data.is_active if data.is_active is not None else project.is_active 
        project.description = data.description if data.description is not None else project.description
        project.url = data.url if data.url is not None else project.url

        db.session.commit()
        return project