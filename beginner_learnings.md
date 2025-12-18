# Beginner Learnings from YouTube Downloader API Setup

This document summarizes key concepts and lessons a beginner can learn from setting up and troubleshooting a YouTube downloader API using FastAPI, Tortoise ORM, and Aerich.

## 1. Project Structure and Dependencies
- **Python Project Setup**: Use `uv` for dependency management (e.g., `uv init`, `uv add`, `uv sync`).
- **Virtual Environments**: Always use virtual environments to isolate dependencies (handled by `uv run`).
- **Dependencies**: Key libraries include FastAPI for the API, Tortoise ORM for database interactions, Aerich for migrations, and Pyright for linting.

## 2. FastAPI Basics
- **App Creation**: Initialize with `app = FastAPI()`.
- **Routers**: Include routers with `app.include_router(router, prefix="/endpoint")` for modular endpoints.
- **CORS Middleware**: Add `CORSMiddleware` to handle cross-origin requests, especially for frontend integration.
- **Running the App**: Use `uv run fastapi dev` for development with auto-reload.

## 3. Tortoise ORM for Database Models
- **Model Definition**: Create models by inheriting from `models.Model`, defining fields like `fields.CharField`, `fields.IntField`.
- **Auto-Fields**: Tortoise automatically adds `created_at` and `updated_at` timestamps to models.
- **Configuration**: Use a config dict (`TORTOISE_ORM`) with connections, apps, and models paths.
- **Integration with FastAPI**: Use `register_tortoise` with `generate_schemas=True` to auto-create tables on startup.

## 4. Database Migrations with Aerich
- **Initialization**: Run `aerich init-db` to set up migrations and generate initial schema.
- **Commands**:
  - `aerich migrate --name <description>`: Generate a migration file for model changes.
  - `aerich upgrade`: Apply migrations to update the database.
  - `aerich history`: View migration history.
- **Common Issues**: Ensure models are correctly defined before migrating; Aerich detects changes and generates SQL.

## 5. Linting and Type Checking with Pyright
- **Configuration**: Create `pyrightconfig.json` to specify include paths, extra paths for imports, and Python version.
- **Resolving Imports**: Use `"extraPaths": ["src"]` to help Pyright find modules in subdirectories.
- **Common Errors**: Import resolution issues often stem from path problems; verify with `uv run pyright`.

## 6. Troubleshooting Common Errors
- **AttributeError in Tortoise**: Often due to incompatible versions (e.g., downgrade `aiosqlite` if needed).
- **ConfigurationError**: Avoid passing conflicting params to `register_tortoise` (e.g., don't mix `config` and `db_url` redundantly).
- **Table Not Found**: Ensure `generate_schemas=True` or run migrations; check database paths (relative vs. absolute).
- **Missing Columns**: Add auto-fields explicitly if Aerich doesn't detect them; regenerate migrations for model changes.
- **Import Errors**: Use relative imports or configure linters; ensure scripts run from the correct directory.

## 7. Best Practices
- **Version Pinning**: Pin dependencies in `pyproject.toml` to avoid compatibility issues.
- **Database Paths**: Use absolute paths for production; relative paths can cause issues if run from different directories.
- **Error Handling**: Add try-except blocks in endpoints for robustness (e.g., invalid URLs, download failures).
- **Security**: Never log or expose secrets; validate inputs to prevent issues.
- **Documentation**: Use FastAPI's auto-docs at `/docs` for API testing.

## 8. Tools and Commands Summary
- `uv run fastapi dev src/main.py`: Start development server.
- `uv run aerich init-db`: Initialize migrations.
- `uv run aerich migrate --name "add fields"`: Create migration.
- `uv run aerich upgrade`: Apply migrations.
- `uv run pyright src/`: Lint code.
- `sqlite3 db.sqlite3 ".tables"`: Inspect database tables.

By following this setup and troubleshooting process, beginners learn about full-stack Python development, database management, and debugging real-world issues.