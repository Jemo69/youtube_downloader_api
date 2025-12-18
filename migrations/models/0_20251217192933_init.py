from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "video" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "url" VARCHAR(255) NOT NULL
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
    "eJztlVFr2zAUhf9K8FML3WizZC17SwNjG20K3VoGpRjFurFFZMmRrruWkv9eXdmJHCcNDR"
    "S20r3F5x5J93xIN49RrjlI+/FacNDRl85jpFgO7sdq4aATsaIIMgnIxtI775aWsUXDEnTi"
    "hEkLTuJgEyMKFFo5VZVSkqgTZxQqDVKpxKyEGHUKmIFxhZtbJwvF4R7s4rOYxhMBkq80Kj"
    "id7fUYHwqvfVf41RvptHGcaFnmKpiLB8y0WrqFQlJTUGAYAm2PpqT2qbs65iJR1WmwVC02"
    "1nCYsFJiI+4LGSRaET/XjfUBUzrlQ/eod9w7+fS5d+IsvpOlcjyv4oXs1UJPYPQrmvs6Q1"
    "Y5PMbADQW67dbQDTNmNrNbLmjhc0238S1gbeO3EALAcGleiWDO7mMJKsWMsPX7W3hdDy6H"
    "3waXe861T2m0u8jV9R7VpW5VI6gBYmnkLghr+zsHSE95Mm1cShLGLJn+YYbHaxXd1c9510"
    "t5N28rTLHU46GQlKAebQMwIsk2Db26snXqseD5P/be0Ni7A2OppR1ebWPJO3+5zdFHT2MH"
    "iLX9bQI8Ojx8AUDnehagr60CdCciVG9wFeKPnxejzRAbS1ogr5QLeMNFggcdKSze/ptYt1"
    "Ck1NR0bu1MNuHtnQ9+t7kOzy5OPQVtMTV+F7/B6d/+e5k/AXbSmZY="
)
