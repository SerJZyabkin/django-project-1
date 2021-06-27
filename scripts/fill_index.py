from django.db import models
import psycopg2

conn = psycopg2.connect(database="cabsbordb",  user="admin",  host="localhost",  password="admin")
cursor = conn.cursor()

cursor.execute("""DELETE FROM cab_sbor_backend_newsentry""")
conn.commit()

insert_query = """ INSERT INTO cab_sbor_backend_newsentry (name, icon, description)
                             VALUES (%s, %s, %s)"""
first = ('20 March 2021', 'scroll', '<p><sub>Окт<span style="font-size:26px">ябрь уж</span> наступил &mdash; уж роща отряхает Послед</sub>ни<u>е листы с нагих своих ветвей; Дохнул осенний хлад &mdash; дорога промерзает. Журча еще бежит за мельницу руч</u>ей, Но п<em>руд уже застыл; сосед мой поспешает В отъезжие поля с охотою своей, И страждут озими от бешеной забавы, И бу</em>дит л<sup>ай собак уснувши</sup>е<span style="font-size:18px"><span style="font-family:Courier New,Courier,monospace"> дубравы.</span></span></p>')
second = ('21 March 2021', 'cloud-sun', '<p>шифт этер чтобы между строчками было маленькое расстрояние</p>\r\n\r\n<p>Теперь моя пора: я не люблю весны; Скучна мне оттепель;<br />\r\nвонь, грязь &mdash; весной я болен; Кровь бродит; чувства, ум тоскою стеснены.<br />\r\nСуровою зимой я более доволен, Люблю ее снега; в присутствии луны<br />\r\nКак легкий бег саней с подругой быстр и волен, Когда под соболем, согрета и свежа,<br />\r\nОна вам руку жмет, пылая и дрожа!</p>')
third = ('22 March 2021', 'cloud-moon-rain', '\n            Как весело, обув железом острым ноги,\n            Скользить по зеркалу стоячих, ровных рек!\n            А зимних праздников блестящие тревоги?..\n            Но надо знать и честь; полгода снег да снег,\n            Ведь это наконец и жителю берлоги,\n            Медведю, надоест. Нельзя же целый век\n            Кататься нам в санях с Армидами младыми\n            Иль киснуть у печей за стеклами двойными.')


for record in [first, second, third]:
    cursor.execute(insert_query, record)
conn.commit()
conn.close()
