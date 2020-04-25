print ("""
Working.
@muuT3ra$$uu b2
#FuckAll.Everything. 
by Tripl_color vk.com/Tripl_color""")

import vk_requests
import time

id = 1                             # Вставь сюда свой айди ( id = 472165736 )
pst =  35                          # Вставь сюда айди поста ( pst = 1 )
t = 5                              # Время перед постами
c = 3                              # сколько нужно сделать
wall = 0                           # если хочешь флуд человеку на стене  (поставь 2 если хочешь чтоб был флуд или 0 если не хочешь )
comments = 2                       # если хочешь флуд человеку в коменты по постами (поставь 2 если хочешь чтоб был флуд или 0 если не хочешь )
tokencom = "токен для коментов сюда" # Введи сюда токен группы от которой можно оставлять коментарии
tokenwall = "токен для стены сюда давай" # Введи сюда токен страницы в вк


#ПЕРЕМЕННЫЕ КОТОРЫЕ ТРОГАТЬ НЕЛЬЗЯ!11
a = 0



msg = "@muuT3ra$$uu b3 , #FuckAll.Everything. by Tripl_color vk.com/Tripl_color" # Сообщение в коментариях
if comments > 1:
 while a < c:
  api = vk_requests.create_api(service_token=tokencom)  # Введи сюда токен группы от которой можно оставлять коментарии
  a +=1
  print(a),print(api.wall.createComment(owner_id= id, post_id= pst, message= msg))
  time.sleep(t)

if wall > 1:
 while a < c:
  api = vk_requests.create_api(service_token=tokenwall)
  a +=1
  print(a),print(api.wall.post(owner_id= id, message= msg))
  time.sleep(t)
