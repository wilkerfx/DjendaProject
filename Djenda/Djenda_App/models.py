from django.db import models


class Empresa(models.Model):
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.empresa

    class Meta:
        ordering = ['empresa']


class Departamento(models.Model):
    empresa = models.ManyToManyField(Empresa)
    departamento = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.departamento


class Contactos(models.Model):
    nome = models.CharField(max_length=200)
    funcao = models.CharField(max_length=300)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=10)
    email = models.EmailField()
    telemovel = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % self.nome

    class Meta:
        ordering = ['nome']
