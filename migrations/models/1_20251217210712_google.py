from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "video" ADD "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "video" DROP COLUMN "created_at";"""


MODELS_STATE = (
    "eJztlW1P2zAQx79KlFedxBB05UF7F7pOdFrbCTI2gVDkxm5q1bFLcgEq1O+Oz3lwmz6ISp"
    "MGUt8l//ufffeL43txY0WZSA9vOGXK/eq8uJLETD8sBw4cl0ynVkYByFAY52NlGaaQkBC0"
    "OCIiZVqiLA0TPgWupFZlJgSKKtRGLiMrZZI/ZCwAFTEYs0QH7u61zCVlzywtX6eTYMSZoE"
    "uFcop7Gz2A2dRoXQnfjRF3GwahElksrXk6g7GSlZtLQDVikiUEGC4PSYblY3VFm2VHeaXW"
    "kpe4kEPZiGQCFtp9I4NQSeSnq0lNgxHu8rl53DprnX85bZ1ri6mkUs7meXu29zzREOj77t"
    "zECZDcYTBabsBBL7eCrj0myXp2VUINny66jq+EtY1fKViA9tD8I4IxeQ4EkxGMEdvJyRZe"
    "N95V+9K7amjXJ+xG6YOcH+9+EWrmMYRqIWaJ2AVhYd8DrACGCcOWAwKrHL/pCPCYrWe5nF"
    "lDSovUw/LhnQLWPdCBFLPi+tjC1+/2Ote+1/uFncRp+iAMIs/vYKRp1FlNbZzWPkW1iPOn"
    "6186+OrcDvodQ1ClECVmR+vzb12siWSgAqmeAkIXbrpSLcHM8Y4eTRZuGxSGJJw8kYQGKx"
    "HVVJu8q6G4GdcVIklkPgvCxTKLmeWxhIfjddOsiGwdZ8R69vPsA82zR5akWNIO1/FCyv5K"
    "rkDir7EDxML+MQEeHx29AaB2bQRoYrWZpiQwuWag/bge9DcMM5tSA/lb6gbvKA/hwBE8hf"
    "v3iXULRex6aWiV8Bo972+da/vn4KI+jXCBC834v46X+SsWtDD2"
)
