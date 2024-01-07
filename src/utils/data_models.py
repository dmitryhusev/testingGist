from pydantic import BaseModel, constr, field_validator
import pytest


class Gist(BaseModel):
    # Class for gist response data validation

    id_: constr(min_length=1)
    url: constr(min_length=1)
    file_name: dict
    description: str

    @field_validator('file_name')
    def check_file_name_field(cls, v):
        if isinstance(v, dict) and len(v) > 0:
            return v
        else:
            pytest.fail(f'file_name field is invalid: {v}')
