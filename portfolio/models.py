from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    email = models.EmailField(default="")

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=10)
    ects = models.IntegerField()
    ranking = models.IntegerField()
    prof_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    prof_pratica = models.ManyToManyField(Pessoa, related_name='cadeiras', default=1)
    link = models.CharField(max_length=500, default="")
    descricao = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=10)
    ano_criacao = models.IntegerField()
    criador = models.CharField(max_length=50)
    logotipo = models.ImageField(upload_to='media/', blank=True)
    link = models.CharField(max_length=500)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Projeto(models.Model):

    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    ano = models.IntegerField()
    logotipo = models.ImageField(upload_to='media/', blank=True)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE, default=1)
    participantes = models.ManyToManyField(Pessoa, related_name='pessoas', default=1)
    email = models.EmailField()
    link_github = models.CharField(max_length=500, default="")
    link_youtube = models.CharField(max_length=500, default="")
    tecnologias = models.ManyToManyField(Linguagem, related_name='tecnologias', default=1)

    def __str__(self):
        return self.nome


class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True)

####################################################################
# QUIZZ
####################################################################
class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()


    def __str__(self):
        return self.nome

class Questionario(models.Model):
    pergunta = models.CharField(max_length=200, null=True)
    opcao1 = models.CharField(max_length=200, null=True)
    opcao2 = models.CharField(max_length=200, null=True)
    opcao3 = models.CharField(max_length=200, null=True)
    opcao4 = models.CharField(max_length=200, null=True)
    resposta = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.pergunta
####################################################################

class TrabalhoFC(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    orientadores = models.ManyToManyField(Pessoa, related_name='orientadores')
    titulo = models.CharField(max_length=100)
    resumo = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/', blank=True)
    link_github = models.CharField(max_length=500)
    link_youtube = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/', blank=True)
    link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.titulo


class Educacao(models.Model):
    nome = models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    ano_Inicio = models.IntegerField()
    ano_Fim = models.IntegerField()
    grau = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    qualificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome