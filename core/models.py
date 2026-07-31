from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    image = models.ImageField(
        upload_to="projects/",
        verbose_name="Project Image"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Project Title"
    )

    short_description = models.TextField(
        verbose_name="Short Description",
        blank=True,
        default=""
    )

    description = models.TextField(
        verbose_name="Description"
    )

    website = models.URLField(
        blank=True,
        null=True,
        verbose_name="Website URL"
    )

    project_date = models.DateField(
        verbose_name="Project Date"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title