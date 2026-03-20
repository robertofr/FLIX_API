from django.db import models

# List of Nationalities Choices

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR','Brasil'),
    ('UK', 'Reino Unido'),
    ('FR', 'França'),
    ('DE', 'Alemanha'),
    ('IT', 'Itália'),
    ('JP', 'Japão'),
    ('IN', 'Índia'),
    ('CN', 'China'),
    ('ES', 'Espanha'),
)

class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name