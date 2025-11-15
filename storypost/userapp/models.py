from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()   # MongoDB ObjectId
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    class Meta:
        db_table = "user_collection"   # Explicitly link to your collection

    def __str__(self):
        return self.name
