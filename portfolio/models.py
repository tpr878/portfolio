from django.db import models


class PortfolioItem(models.Model):
    """Model representing portfolio items like education, experience, projects, etc."""
    
    CATEGORY_CHOICES = [
        ('profile', 'Profile'),
        ('education', 'Education'),
        ('experience', 'Experience'),
        ('project', 'Project'),
        ('publication', 'Publication'),
        ('skill', 'Skill'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, db_index=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, help_text="HTML allowed")
    date_start = models.CharField(max_length=50, blank=True)
    date_end = models.CharField(max_length=50, blank=True)
    technologies = models.CharField(max_length=500, blank=True, help_text="Comma-separated")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', '-date_start']
    
    def __str__(self):
        return f"{self.get_category_display()}: {self.title}"
    
    def get_tech_list(self):
        """Return technologies as a list."""
        if self.technologies:
            return [t.strip() for t in self.technologies.split(',')]
        return []
