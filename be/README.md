## FASTAPI TEMPLATE

## Installation

**Cách 1:**

```
// Clone project & run
$ git clone https://github.com/kasik01/app-manager.git
$ cd be
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ alembic upgrade head // create db before this (docker run -d --name my_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5433:5432 postgres:15)
$ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Cách 2:**

- Clone Project
- Run docker-compose

```
$ git clone https://github.com/kasik01/app-manager.git
$ cd be
$ docker-compose up --build -d
```

## Cấu trúc project

```
.
├── alembic
│   ├── versions    // thư mục chứa file migrations
│   └── env.py
├── app
│   ├── api         // các file api được đặt trong này
│   ├── core        // chứa file config load các biến env & function tạo/verify JWT access-token
│   ├── db          // file cấu hình make DB session
│   ├── helpers     // các function hỗ trợ như login_manager, paging
│   ├── models      // Database model, tích hợp với alembic để auto generate migration
│   ├── schemas     // Pydantic Schema
│   ├── services    // Chứa logic CRUD giao tiếp với DB
│   └── main.py     // cấu hình chính của toàn bộ project
├── tests
│   ├── api         // chứa các file test cho từng api
│   ├── faker       // chứa file cấu hình faker để tái sử dụng
│   ├── .env        // config DB test
│   └── conftest.py // cấu hình chung của pytest
├── .gitignore
├── alembic.ini
├── docker-compose.yaml
├── Dockerfile
├── env.example
├── logging.ini     // cấu hình logging
├── postgresql.conf // file cấu hình postgresql, sử dụng khi run docker-compose
├── pytest.ini      // file setup cho pytest
├── README.md
└── requirements.txt    // file chứa các thư viện để cài đặt qua pip install
```

## Migration

Dùng Alembic để thực hiện các thay đổi của table:

```
$ alembic revision --autogenerate   # Create migration versions
$ alembic upgrade head   # Upgrade to last version migration
```
