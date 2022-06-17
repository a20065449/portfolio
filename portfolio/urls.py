from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('cadeira/<int:cadeira_id>', views.cadeira_page_view, name='cadeira'),
    path('nova_cadeira/', views.nova_cadeira_page_view, name='nova_cadeira'),
    path('edita_cadeira/<int:cadeira_id>', views.edita_cadeira_page_view, name='edita_cadeira'),
    path('apaga_cadeira/<int:cadeira_id>', views.apaga_cadeira_page_view, name='apaga_cadeira'),
    path('lista_pessoas', views.lista_pessoas_page_view, name='lista_pessoas'),
    path('pessoa/<int:pessoa_id>', views.pessoa_page_view, name='pessoa'),
    path('nova_pessoa/', views.nova_pessoa_page_view, name='nova_pessoa'),
    path('edita_pessoa/<int:pessoa_id>', views.edita_pessoa_page_view, name='edita_pessoa'),
    path('apaga_pessoa/<int:pessoa_id>', views.apaga_pessoa_page_view, name='apaga_pessoa'),
    path('lista_projetos', views.lista_projetos_page_view, name='lista_projetos'),
    path('projeto/<int:projeto_id>', views.projeto_page_view, name='projeto'),
    path('novo_projeto/', views.novo_projeto_page_view, name='novo_projeto'),
    path('edita_projeto/<int:projeto_id>', views.edita_projeto_page_view, name='edita_projeto'),
    path('apaga_projeto/<int:projeto_id>', views.apaga_projeto_page_view, name='apaga_projeto'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('tecnologias', views.tecnologias_page_view, name='tecnologias'),
    path('lista_linguagens', views.lista_linguagens_page_view, name='lista_linguagens'),
    path('linguagem/<int:linguagem_id>', views.linguagem_page_view, name='linguagem'),
    path('nova_linguagem/', views.nova_linguagem_page_view, name='nova_linguagem'),
    path('edita_linguagem/<int:linguagem_id>', views.edita_linguagem_page_view, name='edita_linguagem'),
    path('apaga_linguagem/<int:linguagem_id>', views.apaga_linguagem_page_view, name='apaga_linguagem'),
    path('blog', views.blog_page_view, name='blog'),
    path('novopost/', views.novopost_page_view, name='novopost'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('api', views.api_page_view, name='api'),
    path('video', views.video_page_view, name='video'),
    path('laboratorios', views.laboratorios_page_view, name='laboratorios'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user', views.user_view, name='user'),
    path('hobbie', views.hobbie_page_view, name='hobbie'),
    path('tfc/<int:tfc_id>', views.tfc_page_view, name='tfc'),
    path('lista_tfc', views.lista_tfc_page_view, name='lista_tfc'),
    path('novo_tfc/', views.novo_tfc_page_view, name='novo_tfc'),
    path('edita_tfc/<int:tfc_id>', views.edita_tfc_page_view, name='edita_tfc'),
    path('apaga_tfc/<int:tfc_id>', views.apaga_tfc_page_view, name='apaga_tfc'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
