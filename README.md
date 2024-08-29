# USER CRUD USING UVICORN AND FASTAPI

This is the documentation of how to get the
best from this API

## Install

    Download the code from the git repository

## Run the app

    uvicorn main:app --reload

# REST API

The REST API to the crud app is described below.
Or access `/docs` on your browser to check the
interactive documentation provided by Swagger.

## Get list of Users

### Request

`GET /api/v1/users`

### Response

    HTTP/1.1 200 OK

    [
        {
            "id": "24d1e67d-9417-41f3-a7d0-cb1f00f3c22a",
            "first_name": "Matheus",
            "last_name": "Miranda",
            "middle_name": null,
            "gender": "male",
            "roles": [
            "user",
            "admin"
            ]
        },
        {
            "id": "a9341d54-dce3-4bd1-aba9-49c2dcbb24f1",
            "first_name": "Ana",
            "last_name": "Silva",
            "middle_name": null,
            "gender": "female",
            "roles": [
            "student"
            ]
        },
        {
            "id": "edc32623-5a2e-4a33-ada0-5669ddd7b372",
            "first_name": "Priscilla",
            "last_name": "Santana",
            "middle_name": null,
            "gender": "female",
            "roles": [
            "student"
            ]
        },
        {
            "id": "60d120eb-f4c4-4238-86bb-00ab913f53ca",
            "first_name": "Hadja",
            "last_name": "Costa",
            "middle_name": null,
            "gender": "female",
            "roles": [
            "student"
            ]
        }
    ]

## Create User

### Request

`POST /api/v1/users`

    {
        "first_name": "John",
        "last_name": "Wick",
        "gender": "male",
        "roles": [
        "admin"
        ]
    }

### Response

    HTTP/1.1 200 OK

    {
        "id": "7605a452-2efe-4a7f-8f05-dfbeced63282"
    }

## Delete User

### Request

`DELETE /api/v1/users/{user_id}`

### Response

    HTTP/1.1 200 OK

    {
        "message": "user deleted",
        "user": {
            "id": "66ad8513-bd6c-4cd5-b29a-f8dc0ad3a82c",
            "first_name": "Matheus",
            "last_name": "Miranda",
            "middle_name": null,
            "gender": "male",
            "roles": [
            "user",
            "admin"
            ]
        }
    }

## Delete User That Does Not Exist

### Request

`DELETE /api/v1/users/{invalid_user_id}`

### Response

    HTTP/1.1 404 Not Found

    {
        "detail": "user with id: 66ad8513-bd6c-4cd5-b29a-f8dc0ad3a82c does not exist"
    }

## Update User

### Request

`PUT /api/v1/users/{user_id}`

### Response

    HTTP/1.1 200 OK

    {
        "message": "user updated",
    }

## Update User That Does Not Exist

### Request

`PUT /api/v1/users/{invalid_user_id}`

### Response

    HTTP/1.1 404 Not Found

    {
        "detail": "user with id: 66ad8513-bd6c-4cd5-b29a-f8dc0ad3a82c does not exist"
    }
