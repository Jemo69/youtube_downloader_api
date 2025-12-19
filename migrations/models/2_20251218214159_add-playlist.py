from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "playlist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "url" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "playlist";"""


MODELS_STATE = (
    "eJztmFtP2zAUx79KlScmMQQdN+0tlCI6RougsAmEIjdxUwvHDrZDqVC/+2zn2txGN9halK"
    "e25+Kc84sv//rF8KgDMd+6wGCGERfG19aLQYAH5ZeCb7NlAN9PPcogwAjrYD8bNeKCAVuN"
    "NgaYQ2lyILcZ8gWiRFpJgLEyUlsGIuKmpoCgxwBagrpQTCCTjrt7aUbEgc+Qxz/9B2uMIH"
    "YWykWOera2W2Lma1uPiBMdqJ42smyKA4+kwf5MTChJohHR5buQQAYEVMMLFqjyVXVRp3FH"
    "YaVpSFhiJseBYxBgkWn3lQxsShQ/WQ3XDbrqKZ/bO7sHu4df9ncPZYiuJLEczMP20t7DRE"
    "2gPzTm2g8ECCM0xpSbQEIOV0DXmQBWzi5JyOGTRefxxbDq+MWGFGA6ad6IoAeeLQyJKyYK"
    "295eDa8b87Jzal5uyKhPqhsqJ3I4w/uRqx36FNQUYsDwMgij8AZgAtBmULVsAVHkeCw9An"
    "mwnOViZg6pE6VuxV9WFLDswRkQPIu2jxq+w95592ponl+oTjzOH7FGZA67ytPW1lnOurGf"
    "exXJIK0fveFpS/1s3Q76XU2QcuEy/cQ0bnhrqJpAIKhF6NQCTmani60xmMWVwSGzltqbMx"
    "m/36BX5P29wR6tDrbxQ+kWrYgUAZ5QBpFLzuBMc+zJigCxy3bm6CS/joZZPX7zeA7E1nRy"
    "MTBNDvvs1JDtyaagCHda86pjHncNDXEE7IcpYI61QFN5aJvmLEls0eW1vbwFEODq/lUXqu"
    "Ys2BLpFAOvlk3xm20k06otxzrJpD+XOO7j+Oa8TxBCD6ClJFOS8DYQ330Kvj9CH3A+paxk"
    "DVdTzOY0s7FRnx9RfRaEVLUoyCym6P6CFyfAUZR6cnYJMdBwKyVW9rJk9V50lcxaWAtPyI"
    "H0LzHcqDHWjMF7CsSQR4lCTEBVS8SnJKTRiGukEZtrteZa7f8DbITNBxI2zbXaH+zRzbXa"
    "2l6rmZAhe1ImmyJPrW4CaUwjnFZsUdYJpyfIePTn4rXnfialOfsTkGppLAExCl9PgDvb26"
    "8AKKMqAWpfTjxRIiApUU7frgb9CtWUpuRAXhPZ4J2DbLHZUjcE96uJtYai6npBHcXwNs7N"
    "n3mune+Do7zsUQMclR3J//J4mf8CntoyBg=="
)
