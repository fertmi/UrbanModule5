from time import sleep


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = ''
        self.current_age = ''

    def log_in(self, nickname, password):
        if len(self.users) > 0:
            for i in range(0, len(self.users)):
                if nickname in self.users[i][0]:
                    if self.users[i][1]==hash(password):
                        self.current_user = self.users[i][0]
                        self.current_age = self.users[i][2]
                        print(f'Пользователь {self.current_user} вошёл в UrTube')
                    else:
                        print(f'Неверный пароль пользователя {self.users[i][0]}')


    def register(self, nickname, password, age):
        in_users = False
        if len(self.users) > 0:
            for i in range(0,len(self.users)):
                if nickname in self.users[i][0]:
                    print(f"Пользователь {nickname} уже существует")
                    in_users = True
                    break
        if not in_users:
            self.users.append([nickname, hash(password), age])
            self.current_user = nickname
            self.current_age = age

    def log_out(self):
        print(f'Пользователь {self.current_user} вышел из UrTube')
        self.current_user = ''

    def add(self, *args):
        for x in range(0,len(args)):
            self.videos.append(args[x])
        return self.videos

    def get_videos(self, world_video):
        world_video = [x.title for x in self.videos if ', '.join(x.title.upper().split()).find(world_video.upper())!=-1]
        return world_video

    def watch_video(self, name_video):
        if self.current_user == '':
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in range(0,len(self.videos)):
                if name_video in self.videos[i].title:
                        if not self.videos[i].adult_mode or (self.videos[i].adult_mode and self.current_age>=18):
                            print(f'Просмотр фильма "{self.videos[i].title}":', end=' ')
                            for j in range(self.videos[i].time_now, self.videos[i].duration):
                                sleep(1)
                                print(j+1, end=' ')
                            print('Конец фильма')
                            if j != self.videos[i].duration-1:
                                self.videos[i].time_now = j
                        else:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

#Основная программа
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

ur.log_out()

ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года')