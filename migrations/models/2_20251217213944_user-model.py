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
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";"""


MODELS_STATE = (
    "eJztll1v2jAUhv8K4opJXdUy+qHdUcZUpgFTS7upVRWZxAQLx05tpxRV/Pf6OB8OIURF2r"
    "RWyhXhPe+Jz3mS+PilGXAPU3l4I7Fofm28NBkKsL7Y0A8aTRSGVgVBoSk1xih1TKUSyFVa"
    "myEqsZY8LF1BQkU40yqLKAWRu9pImG+liJHHCDuK+1jNTR33D1omzMPPWKZ/w4UzI5h6G2"
    "USD9Y2uqNWodEGTH03Rlht6ricRgGz5nCl5pxlbsIUqD5mWCCF4fZKRFA+VJd0mXYUV2ot"
    "cYm5HA/PUERVrt03MnA5A366Gmka9GGVz+3jzlnn/Mtp51xbTCWZcraO27O9x4mGwGjSXJ"
    "s4Uih2GIyWm/ndItebI1GOLvUX4OmSi/BSVFX0UsHis6/MX+IXoGeHYuarOUA7Oamgddu9"
    "6l12r1ra9Qm64fo1jt/tURJqxzFAahHiABG6D8MsoYaYQQyRlEsuSr7i3RzzOTXKDKUrML"
    "TsILUN85uOKBLgcqCbmQWkXpJ6mF68U8C6B2/M6CrZiyv4TgbD/vWkO/wFnQRSPlKDqDvp"
    "Q6Rt1FVBbZ0WHkV2k8bvweSyAX8bd+NR3xDkUvnCrGh9k7sm1IQixR3Glw7ycmMjVVMwax"
    "h4s0Vu6wZhitzFEgnP2YrwNt/l3Q4F7aCoIIZ881gALpSZjP9b4mFedi6IA5UHg6fMUp8M"
    "PtDJQBFF9zoaZAn1XpxBjMReJ4PEXgOsh1k9zP7ZMOtiQdx52TRLIpXjDFlPPc8+0Dx7wk"
    "JCSXtsx7mUekvOQMKnsQfExP4xAR4fHb0BoHbtBGhihZnGmcKsZKD9uB6Pdgwzm1IAecN0"
    "g/cecdVBgxKpHt4n1gqK0PXG0ErhtYbdP0WuvZ/ji+I0ghtcaMb/dbysXwFz8cPP"
)
