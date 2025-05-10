from django.db import models

# Create your models here.
class skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    year = models.PositiveIntegerField()
    skills = models.ManyToManyField(skill, related_name='projects')
    img = models.ImageField(upload_to='./static/img/', blank=False, null=False)
    web_link = models.URLField(blank=False, null=False)
    
    def __str__(self):
        return f"{self.name} - ({self.year})"

class timelineEntry(models.Model):
    class Meta:
        verbose_name = "Timeline entry"
        verbose_name_plural = "Timeline entries"
    
    ENTRY_TYPE_CHOICES = [
        ('experience', 'Experience'),
        ('education', 'Education'),
    ]

    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPE_CHOICES)
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    skills = models.ManyToManyField(skill, related_name='timeline_entries')

    def __str__(self):
        return f"{self.entry_type.capitalize()}: {self.title} at {self.name}"
