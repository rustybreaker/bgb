from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

def menu(request):
    return render(request, 'menu.html')

def galeria(request):
    return render(request, 'galeria.html')  # ainda vamos criar esse template

def cartinha(request):
    return render(request, 'cartinha.html')

from django.shortcuts import render

from django.shortcuts import render

def galeria(request):
    fotos_legendas = [
        {'foto': 'click1.JPEG', 'texto': 'Queria que você me olhasse igual olha pra comida ❤️'},
        {'foto': 'juntos1.JPEG', 'texto': 'Nosso primeiro ano novo juntos de muitos! ✨'},
        {'foto': 'amigos1.jpg', 'texto': 'Aprendendo o nome das comidas japonesas com nossos futuros padrinhos rsrs 🍣'},
        {'foto': 'dogpool.jpg', 'texto': 'Nenipool — não sei o que seria do mundo sem você! 🐶🦸‍♀️'},
        {'foto': 'cabelo.JPEG', 'texto': 'Reclama do maridão... 🧡'},
        {'foto': 'dirigindo.JPEG', 'texto': 'Mulher no volante, perigo constante! brincs  rsrs 🚗'},
        {'foto': 'joao1.JPEG', 'texto': 'Em breve é o nosso pedindo tetê 🍼'},
        {'foto': 'niet1.jpg', 'texto': 'Obrigado por cuidar tão bem do meu filhinho ❤️'},
        {'foto': 'doente1.JPG', 'texto': 'Na saúde e na doença 💉'},
        {'foto': 'selfie2.JPEG', 'texto': 'Botox e beleza! ✨'},
        {'foto': 'click2.JPEG', 'texto': 'Compraria o pack que fosse... 👀'},
        {'foto': 'click3.JPEG', 'texto': 'Minha Abaporu que amo tanto... 💫'},
        {'foto': 'click4.JPEG', 'texto': 'Essa mina, ela é linda, ela faz coisas absurdas... 😍'},
        {'foto': 'festa1.JPEG', 'texto': '5º ano com a mais gata 🎉'},
        {'foto': 'festa3.jpg', 'texto': 'No meu role favorito!'},
        {'foto': 'festa4.jpg', 'texto': 'Ela sempre a mais linda, do lado do seu jogador 💃'},
        {'foto': 'festa5.JPEG', 'texto': 'Amo nossa habilidade de tirar fotos juntos 🍻'},
        {'foto': 'festa6.jpg', 'texto': '6º ano com a mais risonha 🎓'},
        {'foto': 'festa7.JPG', 'texto': 'Cervejada e minha felicidade! 🍺'},
        {'foto': 'rest2.JPEG', 'texto': 'Te entendiei? Dicupa, come uma batatinha! 🍝'},
    ]
    return render(request, 'galeria.html', {'fotos_legendas': fotos_legendas})

