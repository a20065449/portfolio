from django import forms
from django.forms import ModelForm
from .models import Cadeira, Pessoa, Linguagem, TrabalhoFC, Blog, Projeto, Educacao

SEMESTRE= [
    ('1', '1'),
    ('2', '2'),
    ('Anual', 'Anual'),
    ]

ANOS= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ]

ECTS= [
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('20', '20'),
    ]

RANKING= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ]

Lista = []
Professor = Pessoa.objects.all()
for prof in Professor:
    lista = (prof, prof)


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': 50,
                'class': 'form field text fn'}),
            'ano': forms.Select(choices=ANOS, attrs={
                'style': 'width: 10%',
                'class': 'field select'}),
            'semestre': forms.Select(choices=SEMESTRE, attrs={
                'style': 'width: 10%',
                'class': 'field select'}),
            'ects': forms.Select(choices=ECTS, attrs={
                'style': 'width: 15%',
                'class': 'field select medium'}),
            'ranking': forms.Select(choices=RANKING, attrs={
                'style': 'width: 15%',
                'class': 'field select medium'}),
            'prof_teorica': forms.Select(choices=Lista, attrs={
                'style': 'width: 25%',
                'class': 'field select medium'}),
            'prof_pratica': forms.SelectMultiple(choices=Professor, attrs={
                'style': 'width: 25%',
                'class': 'field select small'}),
            'link': forms.TextInput(attrs={
                'size': 'width: 70%',
                'class': 'form field text fn'}),
            'descricao': forms.Textarea(attrs={
                'cols': 180,
                'rows': 3,
                'class': 'form field text fn'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome da Cadeira',
            'ano': 'Ano',
            'semestre': 'Semestre',
            'ects': 'ECTS',
            'ranking': 'Ranking',
            'prof_teorica': 'Professor da Teórica',
            'prof_pratica': 'Professor da Prática',
            'link': 'Link da Cadeira',
            'descricao': 'Descrição'
        }


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': 100,
                'style': 'width: 100%; padding-left: 10px;'}),
            'descricao': forms.Textarea(attrs={
                'cols': 300,
                'rows': 3,
                'style': 'width: 100%; padding: 10px;'}),
            'participantes': forms.SelectMultiple(attrs={
                'style': 'width: 100%; padding-left: 10px;'}),
            'ano': forms.TextInput(attrs={
                'size': 4,
                'maxlength': 4,
                'style': 'width: 50%; padding-left: 10px;'}),
            'link_github': forms.TextInput(attrs={
                'size': 100,
                'style': 'width: 100%; padding-left: 10px;'}),
            'link_youtube': forms.TextInput(attrs={
                'size': 100,
                'style': 'width: 100%; padding-left: 10px;'}),
            'email': forms.TextInput(attrs={
                'style': 'width: 100%; padding-left: 10px;'}),
            'tecnologias': forms.SelectMultiple(attrs={
                'style': 'width: 100%; padding-left: 10px;'}),
            'cadeira': forms.Select(attrs={
                'style': 'width: 100%; padding-left: 10px;'}),
        }


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': 100,
              }),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome da Pessoa',
        }

class LinguagemForm(ModelForm):
    class Meta:
        model = Linguagem
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': 100,
            }),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome da Linguagem',
        }

class TrabalhoFCForm(ModelForm):
    class Meta:
        model = TrabalhoFC
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': 100,
            }),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome da Linguagem',
        }

class ProjetoFCForm(ModelForm):
    class Meta:
        model = TrabalhoFC
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': 100,
            }),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome do TFC',
        }


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={
                'size': 50,
                'class': 'form field text fn'}),
            'autor': forms.TextInput(attrs={
                'size': 50,
                'class': 'form field text fn'}),
            'link': forms.TextInput(attrs={
                'size': 'width: 70%',
                'class': 'form field text fn'}),
            'descricao': forms.Textarea(attrs={
                'cols': 180,
                'rows': 3,
                'class': 'form field textarea fn'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'data': 'Data',
            'autor': 'Autor',
            'link': 'Link do Post',
            'descricao': 'Descrição'
        }


class EducacaoForm(ModelForm):
    class Meta:
        model = Educacao
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': 100,
                'style': 'width: 100%; padding-left: 10px;'}),
            'ano_Inicio': forms.TextInput(attrs={
                'size': 4,
                'maxlength': 4,
                'style': 'width: 50%; padding-left: 10px;'}),
            'ano_Fim': forms.TextInput(attrs={
                'size': 4,
                'maxlength': 4,
                'style': 'width: 50%; padding-left: 10px;'}),
            'grau': forms.TextInput(attrs={
                'size': 100,
                'style': 'width: 100%; padding-left: 10px;'}),
            'curso': forms.TextInput(attrs={
                'size': 100,
                'style': 'width: 100%; padding-left: 10px;'}),
            'qualificacao': forms.TextInput(attrs={
                'style': 'width: 100%; padding-left: 10px;'}),
            'classificacao': forms.SelectMultiple(attrs={
                'style': 'width: 100%; padding-left: 10px;'}),
        }