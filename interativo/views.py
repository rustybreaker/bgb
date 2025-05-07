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
        {'foto': 'click1.JPEG', 'texto': 'Queria que me olhasse como olha pra comida... ❤️'},
        {'foto': 'juntos1.JPEG', 'texto': 'Nosso primeiro ano novo juntos de muitos meu amor... ✨'},
        {'foto': 'amigos1.jpg', 'texto': 'Não vejo a hora deles serem nossos padrinhos... 🍣'},
        {'foto': 'dogpool.jpg', 'texto': 'Nenipool — o que seria do mundo sem você? 🐶🦸‍♀️'},
        {'foto': 'cabelo.JPEG', 'texto': 'Poder cuidar de você é uma benção... 🧡'},
        {'foto': 'dirigindo.JPEG', 'texto': 'Eu valorizo cada ato que você faz por mim neni... 🚗'},
        {'foto': 'joao1.JPEG', 'texto': 'Em breve é o nosso pedindo tetê... 🍼'},
        {'foto': 'niet1.jpg', 'texto': 'Obrigado por cuidar tão bem do nosso filhinho... ❤️'},
        {'foto': 'doente1.JPG', 'texto': 'Na saúde e na doença... 💉'},
        {'foto': 'selfie2.JPEG', 'texto': 'No botox e na beleza! ✨'},
        {'foto': 'click2.JPEG', 'texto': 'Seu olhar me hipnotiza... 👀'},
        {'foto': 'click3.JPEG', 'texto': 'Se você soubesse o quanto te amo... 💫'},
        {'foto': 'click4.JPEG', 'texto': 'Ver você sorrindo é como ganhar na loteria... 😍'},
        {'foto': 'festa1.JPEG', 'texto': 'E por mais que eu não goste de tirar fotos 🎉'},
        {'foto': 'festa3.jpg', 'texto': '...sei que sempre teremos...'},
        {'foto': 'festa4.jpg', 'texto': 'outras oportunidades! 💃'},
        {'foto': 'festa5.JPEG', 'texto': 'Porque você é a mais linda 🍻'},
        {'foto': 'festa6.jpg', 'texto': 'a mais engraçada 🎓'},
        {'foto': 'festa7.JPG', 'texto': 'e a melhor namorada! 🍺'},
        {'foto': 'rest2.JPEG', 'texto': 'Te amo, minha comilona! 🍝'},
    ]
    return render(request, 'galeria.html', {'fotos_legendas': fotos_legendas})

