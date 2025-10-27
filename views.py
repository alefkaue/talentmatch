from django.shortcuts import render, redirect
from django.contrib.auth import logout

# NOVA VIEW: Para a landing page
def landing_page(request):
    return render(request, 'landing.html')

# Views já existentes
def dashboard_candidato(request):
    return render(request, 'dashboard_candidato.html')

def perfil_candidato(request):
    return render(request, 'perfil_candidato.html')

def explorar_vagas(request):
    return render(request, 'explorar_vagas.html')

def candidaturas_vagas(request):
    return render(request, 'candidaturas_vagas.html')

def caixa_mensagens(request):
    return render(request, 'mensagens.html')

def chat_ia(request):
    return render(request, 'chat_ia.html')

def cursos(request):
    return render(request, 'cursos.html')

def conf(request):
    return render(request, 'conf.html')

def cadastrar_vaga(request):
    # Esta página parece ser de "aplicar para vaga", não "cadastrar vaga de emprego"
    # O nome da view está mantido como você criou.
    return render(request, 'cadastrar_vaga.html')

def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')

def dashboard_empresa(request):
    return render(request, 'dashboard_empresa.html')

def detalhe_vaga(request, id):
    # O ID é passado, mas não usado no template estático.
    # Em um projeto real, você usaria o ID para buscar a vaga no banco.
    context = {'vaga_id': id}
    return render(request, 'detalhe_vaga.html', context)

def progre_cursos(request):
    return render(request, 'progre_cursos.html')

def login_view(request):
    # Adicione sua lógica de login aqui
    # Se o usuário já estiver logado, talvez redirecionar para o dashboard?
    # if request.user.is_authenticated:
    #     return redirect('dashboard_candidato')
    return render(request, 'login.html')

# ✅ Logout
def logout_view(request):
    if request.method == "POST":
        logout(request)
        # Redireciona para a página de login após o logout
        return redirect("login")
    # Mostra a página de confirmação de logout
    return render(request, "sair.html")
