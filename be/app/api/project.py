
import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required
from app.helpers.paging import Page, PaginationParams, paginate
from app.models.project import Project
from app.schemas.base import DataResponse
from app.schemas.project import ProjectCreateRequest, ProjectDetailResponse, ProjectUpdateRequest
from app.services.project import ProjectService


logger = logging.getLogger()
router = APIRouter()

@router.post("", dependencies=[Depends(login_required)], response_model=DataResponse[ProjectDetailResponse])
def create(user_data: ProjectCreateRequest, project_service: ProjectService = Depends()) -> Any:
    """
    API Create Project
    """
    try:
        new_project = project_service.create_project(user_data)
        return DataResponse().success_response(data=new_project)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{project_id}", dependencies=[Depends(login_required)], response_model=DataResponse[ProjectDetailResponse])
def detail(project_id: int, project_service: ProjectService = Depends()) -> Any:
    """
    API Get Project Detail
    """
    try:
        project = project_service.get_project(project_id)
        return DataResponse().success_response(data=project)
    except Exception as e:
        raise CustomException(http_code=404, code='404', message=str(e))
    
@router.get("/users/{user_id}", dependencies=[Depends(login_required)], response_model=Page[ProjectDetailResponse])
def get(user_id: int, params: PaginationParams = Depends(), project_service : ProjectService = Depends()) -> Any:
    """
    API Get list of Projects
    """
    try:
        result = project_service.get_projects_by_user(user_id, params)
        return result 
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    
@router.get("", response_model=Page[ProjectDetailResponse])
def get_all(params: PaginationParams = Depends(), project_service: ProjectService = Depends()) -> Any:
    """
    API Get all Projects
    """
    try:
        projects = project_service.get_all_projects(params)
        return projects
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    
@router.put("/{project_id}", dependencies=[Depends(login_required)], response_model=DataResponse[ProjectDetailResponse])
def update(project_id: int, project_data: ProjectUpdateRequest, project_service: ProjectService = Depends()) -> Any:
    """
    API Update Project
    """
    try:
        updated_project = project_service.update(project_id, project_data)
        return DataResponse().success_response(data=updated_project)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))