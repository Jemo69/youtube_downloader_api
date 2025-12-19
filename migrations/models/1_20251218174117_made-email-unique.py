from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX "uid_user_email_1b4f1c" ON "user" ("email");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_user_email_1b4f1c";"""


MODELS_STATE = (
    "eJztmG1P2zAQx79KlVdMYgg6YGjvQimiY7QTFDaBUOQmbmrh2MF2KBXqd5/txHlORyWYyp"
    "RXbf++i+9+frhLX6yAehDznWsOmfWt82IREED5paBvdywQhpmqBAEmWBtGxmLCBQOukNoU"
    "YA6l5EHuMhQKRIlUSYSxEqkrDRHxMyki6DGCjqA+FDMdx929lBHx4DPk5mf44EwRxF4hTO"
    "SpubXuiEWotQERp9pQzTZxXIqjgGTG4ULMKEmtERFK9SGBDAioHi9YpMJX0SVZmoziSDOT"
    "OMScjwenIMIil+4rGbiUKH4yGq4T9NUsn7t7+1/3j74c7h9JEx1JqnxdxulluceOmsBwbC"
    "31OBAgttAYM276s0KuNwOsHp2xL8GTIZfhGVSr6Bkhw5dtmTfiF4BnB0Pii5mCdnCwgtaN"
    "fdk7sy+3pNUnlQ2V2zje28NkqBuPKaQZQhgAhNdhmDq8DcR334LvjzAEnM8pqznDzRTzPu"
    "1uTFG6DKqUHSCqME/kiEABrAda9Cwh9RLXHfNlQwHLHLwRwYvkGKzgOx5c9K/G9sVPlUnA"
    "+SPWiOxxX410tbooqVuHpaVIH9L5NRifddTPzu1o2NcEKRc+0zNmduNbS8UEIkEdQucO8H"
    "In1qgGzFKVu+lD7uJWwgS4D3PAPKcwku2AJ+RByqurf5z4nZ5fQgw02eo6J+X+Rj1jM5d4"
    "afatUc1SKza0S5toVYeCblBWAAG+jlrNrWYq8Kjpi1JQzY3RU2rSdkYfqDMSSOC1WqPUoa"
    "1GKcSIrdUZJeYtwLac/4/lvHAy5Ouys9bdnPP4+wW9Iev3Bnd0pQcqMqwCPKUMIp+cw4Xm"
    "OJARAeLW3cyl/zY2j19TryNlBuZpsc9vDZmeTAqK+Ka1r3r2Sd9aNveN79k12ZAhd1bXNi"
    "UjK/smkNm0jdOGHcpVjdMTZDx5uXht3c+5tLU/BamOxhoQE/OPCXBvd/cVAKVVI0A9Vmqe"
    "KBGQ1HRO369Gw4auKXMpgbwmMsE7D7liu4MRF/ebiXUFRZV1oTsy8LYu7N9lrr0fo+Ny26"
    "MecFxXkv9leVn+AUMG4iQ="
)
