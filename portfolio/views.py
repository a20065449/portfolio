from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CadeiraForm, PessoaForm, LinguagemForm, BlogForm, TrabalhoFCForm, ProjetoForm
from .models import Cadeira, Pessoa, Linguagem, PontuacaoQuizz, TrabalhoFC, Blog, Projeto, Educacao, Questionario
import datetime
# imports para imprimir grafico
import matplotlib.pyplot as plt
import io
import urllib
import base64
import matplotlib
matplotlib.use('Agg')

# Create your views here.
def hobbies():
	hobbie = {
		'fazer BTT',
		'andar de Mota',
		'estar em casa', 'visitar Serras',
		'ir à praia', 'estar com os meus filhos',
		'ouvir musica',
		'ir à praia'
		}
	return hobbie

def com_sociais():
	sociais = {
		'Boa estrutura de comunicação',
		'Capacidade de adaptação a ambientes multiculturais',
		'Fácil integração e interacção entre colegas de trabalho',
		'Sentido de responsabilidade',
	}
	return sociais

def com_organizacao():
	organizacao = {
		'Capacidade para trabalhar em equipa',
		'Franca capacidade de liderança e organização',
		'Fácil adaptação a novos projectos',
		'Atitude positiva',
		'Resiliência e resolução de problemas',
		'Delegar tarefas',
	}
	return organizacao

def com_programacao():
	programacao = {
		'HTML', 'JAVA', 'PHP', 'ASP', 'JSP', 'JavaScript',
		'C', 'CSS', 'PASCAL', 'VBASIC', 'PROLOG', 'MYSQL',
		'JTFM (Plataforma do BBVA'}
	return programacao

def com_informaticas():
	informatica = {
		'Instalação e Configuração de Hardware',
		'Domínio do software Microsoft Office (Word, Excel, PowerPoint e Access)',
		'Facilidade na navegação Web',
	}
	return informatica

def com_software():
	software = {'Photoshop', 'Paint Shop Pro', 'Corel Draw', }
	return software


def home_page_view(request):
	agora = datetime.datetime.now()
	local = 'Nazaré'
	context = {
		'hora': agora.hour,
		'local': local,
		'hobbies': hobbies(),
	}
	return render(request, 'portfolio/home.html', context)

def user_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('portfolio:login'))
	return render(request, 'portfolio/user.html')

def login_view(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('portfolio:user'))
		else:
			return render(request, 'portfolio/login.html', {'message': "Credênciais inválidas."})

	return render(request, 'portfolio/login.html')

def logout_view(request):
	logout(request)
	return render(request, 'portfolio/logout.html', {'message': "Desconectado."})

def laboratorios_page_view(request):

	labs = [{
		'nome': 'Laboratório 1', 'descricao': "Conhecer a Internet com a minha primeira página Web.", 'link': "https://a20065449-pw-lab2.herokuapp.com/lab1/index.html"},
		{'nome': 'Laboratório 2', 'descricao': "Explorando o HTML com o meu primeiro website.", 'link': "https://a20065449-pw-lab2.herokuapp.com/lab2/index.html"},
		{'nome': 'Laboratório 3', 'descricao': "Website com Quizz e seletores CSS.", 'link': "https://a20065449-pw-lab2.herokuapp.com/lab3/index.html"},
		{'nome': 'Laboratório 4', 'descricao': "SPA com layout responsivo baseado em Flexbox e Grid.", 'link': "https://a20065449-pw-lab2.herokuapp.com/lab4/index.html"},
		{'nome': 'Laboratório 5', 'descricao': "SPA aplicando princípios de web design.", 'link': "https://a20065449-pw-lab2.herokuapp.com/lab5/index.html"},
	]
	return render(request, 'portfolio/laboratorios.html', {'labs': labs})

def contacto_page_view(request):
	return render(request, 'portfolio/contacto.html')


def formacao_page_view(request):
	escolas = Educacao.objects.all()
	return render(request, 'portfolio/formacao.html', {'escolas': escolas})


def competencias_page_view(request):
	context = {
		'sociais': com_sociais(),
		'organizacao': com_organizacao(),
		'informaticas': com_informaticas(),
		'programacao': com_programacao(),
		'software': com_software(),
	}
	return render(request, 'portfolio/competencias.html', context)

def apresentacao_page_view(request):
	return render(request, 'portfolio/apresentacao.html')

# Cadeiras
def licenciatura_page_view(request):
	cadeira = Cadeira.objects.all().order_by('ano', 'semestre')
	return render(request, 'portfolio/licenciatura.html', {'cadeiras': cadeira})

def cadeira_page_view(request, cadeira_id):
	cadeira = Cadeira.objects.get(id=cadeira_id)
	form = CadeiraForm(request.POST, instance=cadeira)
	prof_praticas = cadeira.prof_pratica.all()

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:home'))

	context = {'cadeira': cadeira, 'prof_praticas': prof_praticas}
	return render(request, 'portfolio/cadeira.html', context)

@login_required
def nova_cadeira_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('portfolio:login'))
	form = CadeiraForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:licenciatura'))
	context = {'form': form}

	return render(request, 'portfolio/novaCadeira.html', context)

@login_required
def edita_cadeira_page_view(request, cadeira_id):
	cadeira = Cadeira.objects.get(id=cadeira_id)
	form = CadeiraForm(request.POST or None, instance=cadeira)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:licenciatura'))

	context = {'form': form, 'cadeira_id': cadeira_id}

	return render(request, 'portfolio/editaCadeira.html', context)

@login_required
def apaga_cadeira_page_view(request, cadeira_id):
	Cadeira.objects.get(id=cadeira_id).delete()
	return HttpResponseRedirect(reverse('portfolio:licenciatura'))
# Fim Cadeiras

# PESSOAS
def lista_pessoas_page_view(request):
	pessoas = Pessoa.objects.all().order_by('nome')

	#f = open('/Users/Admin/Dropbox/Roberto/Lusofona/Programação WEB/pw-labs-RobertoLuzindro-a20065449/lab8/portfolio/professores.txt',encoding='utf-8')
	#lista_professores = f.readlines()
	#f.close()

	#for professor in lista_professores:
	#	r = Pessoa(nome=professor, link="", email="")
	#	r.save()
	return render(request, 'portfolio/lista_pessoas.html', {'pessoas': pessoas})

def pessoa_page_view(request, pessoa_id):
	pessoa = Pessoa.objects.get(id=pessoa_id)
	form = PessoaForm(request.POST, instance=pessoa)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_pessoas'))

	context = {'pessoa': pessoa}
	return render(request, 'portfolio/pessoa.html', context)

@login_required
def nova_pessoa_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('portfolio:login'))
	form = PessoaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:user'))
	context = {'form': form}
	return render(request, 'portfolio/novaPessoa.html', context)

@login_required
def edita_pessoa_page_view(request, pessoa_id):
	pessoa = Pessoa.objects.get(id=pessoa_id)
	form = PessoaForm(request.POST or None, instance=pessoa)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_pessoas'))

	context = {'form': form, 'pessoa_id': pessoa_id}

	return render(request, 'portfolio/editaPessoa.html', context)

@login_required
def apaga_pessoa_page_view(request, pessoa_id):
	Pessoa.objects.get(id=pessoa_id).delete()
	return HttpResponseRedirect(reverse('portfolio:user'))

#FIM PESSOAS

# PROJETOS
def lista_projetos_page_view(request):
	projetos = Projeto.objects.all()
	return render(request, 'portfolio/lista_projetos.html', {'projetos': projetos})

def projeto_page_view(request, projeto_id):
	projeto = Projeto.objects.get(id=projeto_id)
	form = ProjetoForm(request.POST, instance=projeto)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_projetos'))

	context = {'projeto': projeto}
	return render(request, 'portfolio/projeto.html', context)

@login_required
def novo_projeto_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('portfolio:login'))
	form = ProjetoForm(request.POST or None)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_projetos'))
	context = {'form': form}

	return render(request, 'portfolio/novoProjeto.html', context)

@login_required
def edita_projeto_page_view(request, projeto_id):
	projeto = Projeto.objects.get(id=projeto_id)
	form = ProjetoForm(request.POST or None, instance=projeto)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_projetos'))

	context = {'form': form, 'projeto_id': projeto_id}
	return render(request, 'portfolio/editaProjeto.html', context)

@login_required
def apaga_projeto_page_view(request, projeto_id):
	Projeto.objects.get(id=projeto_id).delete()
	return HttpResponseRedirect(reverse('portfolio:lista_projetos'))
# FIM PROJETOS

# LINGUAGENS
def lista_linguagens_page_view(request):
	linguagem = Linguagem.objects.all()
	return render(request, 'portfolio/lista_linguagens.html', {'linguagens': linguagem})

def linguagem_page_view(request, linguagem_id):
	linguagem = Linguagem.objects.get(id=linguagem_id)
	form = LinguagemForm(request.POST, instance=linguagem)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_linguagens'))

	context = {'linguagem': linguagem}
	return render(request, 'portfolio/linguagem.html', context)

def nova_linguagem_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('portfolio:login'))
	form = LinguagemForm()
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_linguagens'))

	context = {'form': form}
	return render(request, 'portfolio/novaLinguagem.html', context)

@login_required
def edita_linguagem_page_view(request, linguagem_id):
	linguagem = Linguagem.objects.get(id=linguagem_id)
	form = LinguagemForm(request.POST, instance=linguagem)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_linguagens'))

	context = {'form': form, 'linguagem_id': linguagem_id}
	return render(request, 'portfolio/editaLinguagem.html', context)

@login_required
def apaga_linguagem_page_view(request, linguagem_id):
	Linguagem.objects.get(id=linguagem_id).delete()
	return HttpResponseRedirect(reverse('portfolio:lista_linguagens'))

# FIM LINGUAGENS

# TFC
def lista_tfc_page_view(request):
	lista_tfc = TrabalhoFC.objects.all()
	return render(request, 'portfolio/lista_tfc.html', {'lista_tfc': lista_tfc})

def tfc_page_view(request, tfc_id):
	trabalho = TrabalhoFC.objects.get(id=tfc_id)
	form = TrabalhoFCForm(request.POST, instance=trabalho)
	orientadores = trabalho.orientadores.all()

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_tfc'))

	context = {
		'tfc': trabalho,
		'orientadores': orientadores
	}
	return render(request, 'portfolio/tfc.html', context)

@login_required
def novo_tfc_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('portfolio:login'))
	form = TrabalhoFCForm()
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_tfc'))
	context = {'form': form}

	return render(request, 'portfolio/novoTFC.html', context)

@login_required
def edita_tfc_page_view(request, tfc_id):
	tfc = TrabalhoFC.objects.get(id=tfc_id)
	form = TrabalhoFCForm(request.POST, instance=tfc)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:lista_tfc'))

	context = {'form': form, 'tfc': tfc}
	return render(request, 'portfolio/editaTfc.html', context)

@login_required
def apaga_tfc_page_view(request, tfc_id):
	TrabalhoFC.objects.get(id=tfc_id).delete()
	return HttpResponseRedirect(reverse('portfolio:lista_tfc'))
# FIM TFC


def tecnologias_page_view(request):
	topicos = ['HTML', 'CSS', 'Python', 'Django', 'Heroku', 'JavaScript']

	return render(request, 'portfolio/tecnologias.html', {'topicos': topicos})

def front_end_page_view(request):
	topicos = ['HTML', 'CSS', 'Python', 'Django', 'Heroku', 'JavaScript']

	context = {
		'topicos': topicos,
	}
	return render(request, 'portfolio/tecnologias.html', context)

# BLOG
def blog_page_view(request):
	lista = Blog.objects.all()
	blog = lista.order_by('data').reverse()
	return render(request, 'portfolio/blog.html', {'mensagens': blog})

def novopost_page_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('portfolio:login'))
	form = BlogForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('portfolio:blog'))
	context = {'form': form}

	return render(request, 'portfolio/novoPost.html', context)


def hobbie_page_view(request):
	context = {
		'hobbies': hobbies(),
	}
	return render(request, 'portfolio/hobbies.html', context)


def quiz_page_view(request):
	if request.method == 'POST':
		nome = request.POST['nome']
		perguntas = Questionario.objects.all()
		resultado = 0
		errado = 0
		certo = 0
		total = 0
		for q in perguntas:
			total += 1
			if q.resposta == request.POST.get(q.pergunta):
				resultado += 1
				certo += 1
			else:
				errado += 1
		percentagem = resultado / (total * 10) * 100
		print(resultado)
		r = PontuacaoQuizz(nome=nome, pontuacao=resultado)
		r.save()
		context = {
			'nome': nome,
			'percentagem': percentagem,
			'data': cria_grafico()
		}
		return render(request, 'portfolio/quizz.html', context)
	else:
		perguntas = Questionario.objects.all()
		pontuacao = PontuacaoQuizz.objects.all()
		context = {
			'perguntas': perguntas,
			'pontuacao': pontuacao,
			'data': cria_grafico()
		}
		return render(request, 'portfolio/quiz.html', context)


def quizz_page_view(request):
	perguntas = Questionario.objects.all()
	pontuacao = PontuacaoQuizz.objects.all()
	context = {
		'perguntas': perguntas,
		'pontuacao': pontuacao,
		'data': cria_grafico()
	}
	return render(request, 'portfolio/quizz.html', context)


def api_page_view(request):
	api = Questionario.objects.all()
	return render(request, 'portfolio/quiz.html', {'perguntas': api})


def cria_grafico():

	font = {'family': 'serif',
			'color': 'darkred',
			'weight': 'normal',
			'size': 12,
			}

	quiz = PontuacaoQuizz.objects.all().order_by('pontuacao')
	nomes = [nomes.nome for nomes in quiz]
	pontos = [pontos.pontuacao for pontos in quiz]

	plt.barh(nomes, pontos)
	plt.xlabel("Pontos", fontdict=font)
	plt.ylabel("Nomes", fontdict=font)
	plt.title('Gráfico de Pontuação', fontdict=font)
	plt.subplots_adjust(left=0.25)
	plt.autoscale()

	fig = plt.gcf()
	plt.close()
	buf = io.BytesIO()
	fig.savefig(buf, format='png')

	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri = urllib.parse.quote(string)

	return uri