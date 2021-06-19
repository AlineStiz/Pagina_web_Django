from django.db import models
from stdimage.models import StdImageField

class Base (models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    ICONE_CHOICES = (
        ('bi bi-briefcase', 'Maleta'),
        ('bi bi-card-checklist', 'Checklist'),
        ('bi bi-binoculars', 'Binoculos'),
        ('bi bi-brightness-high', 'Sol'),
    )
    produto = models.CharField('Produto', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=25, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.produto


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.CharField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'thumbs': {'width': 480, 'height': 500, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    linkedin = models.CharField('LinkedIn', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Galeria(Base):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to='galeria', variations=
                                                     {'thumbs': {'width': 350, 'height': 700, 'crop': True}})

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'

    def __str__(self):
        return self.nome

