from requests import Response
from pytest_voluptuous import S

from utils.base_session import reqres_session
import schemas.schemas as schema


def test_post_create_user_schema():
    name = "yuri"
    job = "engineer"

    result: Response = reqres_session().post(
        url="/api/users",
        json={"name": name, "job": job, "id": "1024"}
    )

    print(result.text)

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(schema.create_user_schema)


def test_put_update_user_schema():
    name = "yuri"
    job = "superhuman"

    result: Response = reqres_session().put(
        url="/api/users/2",
        json={"name": name, "job": job}
    )

    print(result.text)

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(schema.update_user_schema)


def test_get_list_user():
    userid = "1024"

    result: Response = reqres_session().get(
        url="/api/users/2",
        json={"id": userid}
    )

    print(result.text)

    assert result.json()['data']['email'] == 'janet.weaver@reqres.in'


def test_post_register_user():
    email = "lindsay.ferguson@reqres.in"
    password = "Hm#&!@(YHK34"

    result: Response = reqres_session().post(
        url="/api/register",
        json={
            "email": email,
            "password": password
        }
    )

    print(result.text)

    assert result.status_code == 200
    assert result.json() == S(schema.post_register_user_schema)
    assert result.json()["id"] == 8
    assert isinstance(result.json()["id"], int)
    assert result.json()["token"] == "QpwL5tke4Pnpja7X8"
    assert isinstance(result.json()["token"], str)


def test_delete_user():
    result: Response = reqres_session().delete(
        url="/api/users/2"
    )
    print(result.text)
    assert result.status_code == 204
