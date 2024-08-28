# USER CRUD USING UVICORN AND FASTAPI

This is the documentation of how to get the
best from this API

## Install

    Download the code from the git repository

## Run the app

    Uvicorn main:app --reload

# REST API

The REST API to the crud app is described below.

## Get list of Users

### Request

`GET /api/v1/users`

### Response

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

`POST /`

### Response

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
