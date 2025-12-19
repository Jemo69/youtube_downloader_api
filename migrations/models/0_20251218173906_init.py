from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "video" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "url" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmG1P2zAQx79KlVdMYgg6nrR3oRTRMdoJCptAKHITN7Vw7GA7lAr1u892HpzHjkpsKl"
    "Ne0f7vLr772fFdebUC6kHMd244ZNbXzqtFQADlh4K+3bFAGBpVCQJMsHaMUo8JFwy4QmpT"
    "gDmUkge5y1AoECVSJRHGSqSudETEN1JE0FMEHUF9KGY6j/sHKSPiwRfI06/hozNFEHuFNJ"
    "Gn1ta6Ixah1gZEnGlHtdrEcSmOAmKcw4WYUZJ5IyKU6kMCGRBQPV6wSKWvskuqTCuKMzUu"
    "cYq5GA9OQYRFrtw3MnApUfxkNlwX6KtVPnf39o/2j78c7h9LF51Jphwt4/JM7XGgJjAcW0"
    "ttBwLEHhqj4ab/Vsj1ZoDVo0v9S/BkymV4KapV9FLB4DNH5p34BeDFwZD4YqagHRysoHVr"
    "X/XO7ast6fVJVUPlMY7P9jAxdWObQmoQwgAgvA7DLKCFmEEMAedzymre4maO+ZgWZYbSZV"
    "CV7ABRhXkqLQIFsB5oMbKE1EtCd9IPGwpY1uCNCF4kd/EKvuPBZf96bF/+UJUEnD9hjcge"
    "95Wlq9VFSd06LG1F9pDOz8H4vKO+du5Gw74mSLnwmV7R+I3vLJUTiAR1CJ07wMu1jVRNwS"
    "xVw5s+5q5uJUyA+zgHzHMKFnMCnpEHKa/u/kkSd3ZxBTHQZKv7nDT8W/WMzdziZXpuUzXd"
    "asWGdmkTraop6AZlBRDg66zV2mqlAo+aySgD1TwaPWcu7Wz0gWYjgQReazjKAtpulEGM2F"
    "qzUeLeAmzb+f/YzgtvhvzB7Kx1N+ci/nxBb8j+vcMdXZmBigyrAM8og8gnF3ChOQ5kRoC4"
    "dTdz6b8bm8evadaRMgPzrNnnj4YsTxYFRXzT2tc9+7RvLZvnxr85NdmQIXdWNzYllpVzEz"
    "A+7eC0YS/lqsHpGTKe/Lh4a9/PhbS9PwOpXo01ICbuHxPg3u7uGwBKr0aA2lYanigRkNRM"
    "Tt+uR8OGqcmElEDeEFngvYdcsd3BiIuHzcS6gqKqujAdpfC2Lu1fZa6976OT8tijHnBS15"
    "L/ZXtZ/gbobeK6"
)
