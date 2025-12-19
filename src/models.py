from tortoise import fields, models


class Video(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="videos" , null=False)
    title = fields.CharField(max_length=255)
    url = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255 , unique=True)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

class Playlist(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="playlists" , null=False)
    title = fields.CharField(max_length=255)
    url = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
