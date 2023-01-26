from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    created = models.DateField('Create', auto_now_add=True)
    modified = models.DateField('Update', auto_now_add=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    service = models.CharField('Service', max_length=100)
    stats = models.TextField('Stats', max_length=200)
    icon = models.CharField('Icon', max_length=13, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self) -> str:
        return self.service


class Position(Base):
    position = models.CharField('Position', max_length=100)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
    
    def __str__(self) -> str:
        return self.position


class Employee(Base):
    name = models.CharField('Name', max_length=100)
    position = models.ForeignKey(
                        'core.Position', verbose_name='Position',
                        on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=230)
    image = StdImageField('Image', upload_to='team',variations={'thumb':{
                        'width': 480,
                        'height': 480, 
                        'crop':True}})
    facebook = models.CharField('Facebook', max_length=150, default='#')
    twitter = models.CharField('Twitter', max_length=150, default='#')
    instagram = models.CharField('Instagram', max_length=150, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self) -> str:
        return self.name
