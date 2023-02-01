import random
user = input(' Введите дейстия :')
combinations = ['Камень','Ножницы','Бумага']
pc_game = random.choice(combinations)

def game(u,p):
    start = True
    while start:
        start = False
    if user == pc_game:
        print(f'вы оба выбрали{user} и бот выбрал{user}')
    elif user == 'Камень':
        if pc_game == 'Ножницы':
            print(f'Камень разбивает бумагу! Вы победили--> (Ваш выброр{user}бот выбрал{pc_game}) ')
    elif user == 'Бумага':
        if pc_game == 'Ножницы':

            print(f'Ножницы режут бумагу!Бот победил---> (Ваш выбор {user}бот выбрал{pc_game} )')
    elif user == 'Бумага':
        if pc_game == 'Камень':
            print(f'Бумага обваарчивает камень! Победил---->(Ваш выбор {user}вы выбрали {pc_game}')



a = game(u=user,p=pc_game)
print()


