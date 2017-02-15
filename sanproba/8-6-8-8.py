# def city_country(city, country):
#     a = print(city.title() + ', ' + country.title())
#     return a
# city_country('москва', 'россия')
# city_country(city='киев', country='украина')
# city_country('ростов', country='россия')


def make_album(name_art, name_alb, dor='10'):
    a = {'артист': name_art, 'альбом': name_alb, 'дорожек': dor, }
    return a


cc = []
while True:
    n_art = input('Введите имя музыканта Если хотите выйти, нажмите n')
    if n_art != 'n':
        n_art_a = n_art
    else:
        break
    n_alb = input('Введите название альбома Если хотите выйти, нажмите n')
    if n_alb != 'n':
        n_alba = n_alb
    else:
        break
    do = input('Введите количество дорожек. Если хотите выйти, нажмите n. Если дорожки по умолчанию,то d')
    if do == 'n':
        break
    elif do == 'd':
        bb = make_album(n_art_a, n_alba)
    else:
        ddd = do
        bb = make_album(n_art_a, n_alba, ddd)
    # Запускаем функцию с аргументами, введенными в инпут, возвращается словарь.
    # значение возвращенного словаря присваиваем переменной bb
    # должно получиться типа bb = {'артист': Пугачева, 'альбом': 'красавчик',
    cc.append(bb)
    dd = input('Нажми n для выхода')
    if dd == 'n':
        break
    else:
        continue
for ii in cc:
    print(ii)
