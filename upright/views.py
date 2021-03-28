from django.shortcuts import render
from .models import NewsEntry, LinkEntry
# Create your views here.


def index(request):
    entry_1 = NewsEntry()
    entry_1.id = 0
    entry_1.description = '''
            Октябрь уж наступил — уж роща отряхает
            Последние листы с нагих своих ветвей;
            Дохнул осенний хлад — дорога промерзает.
            Журча еще бежит за мельницу ручей,
            Но пруд уже застыл; сосед мой поспешает
            В отъезжие поля с охотою своей,
            И страждут озими от бешеной забавы,
            И будит лай собак уснувшие дубравы.'''
    entry_1.name = '20 March 2021'
    entry_1.icon = "scroll"

    entry_2 = NewsEntry()
    entry_2.id = 1
    entry_2.description = '''
            Теперь моя пора: я не люблю весны;
            Скучна мне оттепель; вонь, грязь — весной я болен;
            Кровь бродит; чувства, ум тоскою стеснены.
            Суровою зимой я более доволен,
            Люблю ее снега; в присутствии луны
            Как легкий бег саней с подругой быстр и волен,
            Когда под соболем, согрета и свежа,
            Она вам руку жмет, пылая и дрожа!'''
    entry_2.name = '21 March 2021'
    entry_2.icon = "cloud-sun"
   # entry_2.icon = "dove"

    entry_3 = NewsEntry()
    entry_3.id = 2
    entry_3.description = '''
            Как весело, обув железом острым ноги,
            Скользить по зеркалу стоячих, ровных рек!
            А зимних праздников блестящие тревоги?..
            Но надо знать и честь; полгода снег да снег,
            Ведь это наконец и жителю берлоги,
            Медведю, надоест. Нельзя же целый век
            Кататься нам в санях с Армидами младыми
            Иль киснуть у печей за стеклами двойными.'''
    entry_3.name = '22 March 2021'
    entry_3.icon = "none"

    news_entries = [entry_1, entry_2, entry_3]

    
    
    link1 = LinkEntry()
    link1.name = 'Исходно тут'
    link1.description = 'Какие-то люди, и при нажатии открываются ссылки на твиттер и т.ж. но можно превратить и в предметы.'
    link1.extra_text = 'и делать ссылки на другие страницы'
    link1.image = 'about-01.jpg'
    
    link2 = LinkEntry()
    link2.name = 'Jenifer Soft'
    link2.description = 'This is a carousel for a list of 10 team members. Each member image hover has 3 social icons.'
    link2.extra_text = ''
    link2.image = 'about-02.jpg'
    
    link3 = LinkEntry()
    link3.name = 'Заголовок'
    link3.description = 'Развернутое описание'
    link3.extra_text = 'Фраза'
    link3.image = 'about-03.jpg'

    link4 = LinkEntry()
    link4.name = 'Заголовок 2'
    link4.description = 'Развернутое описание 1 '
    link4.extra_text = 'Фраза 1'
    link4.image = 'about-01.jpg'


    links_out = [link3, link4, link1, link2]

    return render(request, "index.html", {'news_entries': news_entries, 'links_out': links_out})