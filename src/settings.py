# database.py or similar config file
TORTOISE_ORM = {
    "connections": {
        "default": "sqlite:////home/jemo/projects/youtube_downloader_api/db.sqlite3"
    },  # Or your PostgreSQL URL
    "apps": {
        "models": {
            "models": ["src.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
