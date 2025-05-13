# API Documentation Maker

## Project Overview
This project is designed to store API documentation efficiently. It provides tools to manage, generate, and maintain documentation for APIs in a structured and user-friendly manner.

## Features
- **API Documentation Storage**: Store and organize API documentation.
- **Readme Generator**: Automatically generate README files for your projects.
- **FastAPI Integration**: Built using FastAPI for high performance and ease of use.
- **Alembic for Migrations**: Manage database migrations seamlessly.

## Project Structure
```
backend/
    alembic.ini
    main.py
    requirements.txt
    alembicmigration/
        env.py
        README
        script.py.mako
        versions/
            11039e592f55_create_user_table.py
    apis/
        base.py
        v1/
            route_auth.py
    config/
        hashing.py
    database/
        base_class.py
        base.py
        config.py
        session.py
    models/
        user.py
    repository/
        auth/
            auth.py
vvirtualenv/
    pyvenv.cfg
    bin/
    include/
    lib/
```

## How to Run
1. **Set up the virtual environment**:
   ```bash
   source vvirtualenv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn backend.main:app --reload
   ```

## How to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Create a pull request.

## License
This project is licensed under the MIT License.
