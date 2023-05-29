##::::::::::'###::::'########:::::'###::::::::::::::'#######::
##:::::::::'## ##::: ##.... ##:::'## ##::::::::::::'##.... ##:
##::::::::'##:. ##:: ##:::: ##::'##:. ##:::::::::::..::::: ##:
##:::::::'##:::. ##: ########::'##:::. ##:'#######::'#######::
##::::::: #########: ##.... ##: #########:........:'##::::::::
##::::::: ##.... ##: ##:::: ##: ##.... ##:::::::::: ##::::::::
########: ##:::: ##: ########:: ##:::: ##:::::::::: #########:
#Код на проверку пароля
a=input('Enter your password - ')
b=input('Enjter your password again - ')
if a==b:
    print('Correct')
else:
    print('not correct your password')
#Категория места у пассажира
ai=int(input('Напишите нмоер вашего места - '))
if ai % 2:
    print('место у окна')
elif ai % 10:
    print('место у прохода')
else:
    print('Одноместое место')
#Високостный год
year=int(input('напишите год - '))
if (year%4==0) and (year%100 !=0) or (year % 400==0):
    print('Да весокостный')
else:
    print('Не весокостный')
#Cмешивание цветов
print(
    "Введите два цвета чтобы узнать какой получится "
    "Варианты - красный синий желтый "
)
cvet_1=str(input("Введите первый цвет - "))
cvet_2=str(input("Введите второй цвет - "))
if cvet_1=='красный' and cvet_2=='синий':
    print('получится фиолетовый!')
elif cvet_1=="красный" and cvet_2=="желтый":
    print("Получится ораенжевый!")
elif cvet_1=="синий" and cvet_2=="желтый":
    print("получится зеленый!")
else:
    print("Не распознование цвета")
#n число
noe_chislo=input('Введите прделожение - ')
print(noe_chislo.replace(' ',''))
###::::::::::'###::::'########:::::'###::::::::::::::'#######::
##:::::::::'## ##::: ##.... ##:::'## ##::::::::::::'##.... ##:
##::::::::'##:. ##:: ##:::: ##::'##:. ##:::::::::::..::::: ##:
##:::::::'##:::. ##: ########::'##:::. ##:'#######::'#######::
##::::::: #########: ##.... ##: #########:........::...... ##:
##::::::: ##.... ##: ##:::: ##: ##.... ##::::::::::'##:::: ##:
########: ##:::: ##: ########:: ##:::: ##::::::::::. #######::
#........::..:::::..::........:::..:::::..::::::::::::.......:::
#3.4
def four():
    print("У вас есть 3 попытки чтобы правильно ответить")
    import random
    correct=0
    mistaces=0
    while mistaces < 3:
        a=random.randrange(1,100)
        b=random.randrange(1,100)
        answer= a + b
        otvet=('не правильно, првильный ответ =',answer)
        hi=input(f"{a} + {b} = ")
        if int(hi) == answer:
            correct += 1
            print('правильно!')
        else:
            mistaces += 1
            print('Не правильно! Правильный ответ -',answer)
    print(f'Игра окончена! Правильных ответов -', correct,'не правильных ответов -', mistaces)
#3.1
def one():
    noe_chislo=input("Введите предлоэение - ")
    print(noe_chislo.replace(' ',''))
    print(
        ' '.join([input("Введите слово - ") for i in range(int(input('Введите количество слов - ')))])
    )
#3.2
def trhee():
    print('Введите слова, чтобы закончить ввод слов напишите "stop"')
    while True:
        word = input('Введите слово - ')
        if word == "stop":
            print('Вы остановили процесс')
            break
        print(" ".join(word))
#3.3
def second():
    print('Чтобы закончить ввод слов напишите "stop"')
    while True:
        rare_words = str(input('Введите слово - '))
        if "ф" in rare_words.lower():
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово')
        if rare_words=="stop":
            break
    print('Вы закончили ввод слов')
##::::::::::'###::::'########:::::'###:::::::::::::'##::::::::
##:::::::::'## ##::: ##.... ##:::'## ##:::::::::::: ##:::'##::
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::: ##::: ##::
##:::::::'##:::. ##: ########::'##:::. ##:'#######: ##::: ##::
##::::::: #########: ##.... ##: #########:........: #########:
##::::::: ##.... ##: ##:::: ##: ##.... ##::::::::::...... ##::
########: ##:::: ##: ########:: ##:::: ##:::::::::::::::: ##::
#4.1
def p1():
    number = int(input("Введите число:"))
    b = number % 3
    if b == 0 and number != 0:
        print("Число делиться на 3")
    else:
        print("Число не делиться на 3")
#4.2
def p2():
    try:
        number = int(input("Введите число:"))
        b = 100 / number
    except ValueError:
        print("Пользователь ввёл не число")
    except ZeroDivisionError:
        print("Введено число 0")
    else:
        print("Деление числа 100 на введённное число", b)
#4.3
def p3():
    y = input("Введите дату: ")
    y = y.split('.')
    if int(y[0]) * int(y[1]) == int(y[2][2:4]):
        print("Магическая дата")
    else:
        print("Не магическая дата")
#4.4
def p4():
    a = input("Введите число: ")
    b = 0
    d = 0
    if len(a) % 2 == 0:
        for j in a[0:int(len(a) / 2)]:
            b = b + int(j)
        for j in a[int(len(a) / 2):int(len(a))+1]:
            d = d + int(j)
        if d == b:
            print("Это счастливый билет")
        else:
            print("Это не счастливый билет")
    else:
        print("Введено нечётное кол-во цифр")

##::::::::::'###::::'########:::::'###:::::::::::::'########:
##:::::::::'## ##::: ##.... ##:::'## ##:::::::::::: ##.....::
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::: ##:::::::
##:::::::'##:::. ##: ########::'##:::. ##:'#######: #######::
##::::::: #########: ##.... ##: #########:........:...... ##:
##::::::: ##.... ##: ##:::: ##: ##.... ##::::::::::'##::: ##:
########: ##:::: ##: ########:: ##:::: ##::::::::::. ######::
#5.1
def p1():
    import random
    b = int(input("Введите число: "))
    d = [random.randint(1,10)for i in range(5)]
    if b in d:
        print(("Поздравляю,вы угадали число!"))
    else:
        print("Нет такого числа!")
#5.2
def p2():
    b = []
    a = [1, 2, 4, 6, 5, 4, 1, 7, 2,8]
    for i in a:
        if a.count(i) > 1:
            b.append(i)
    print(*b)
#5.3
def p3():
    a = int(input("Введите сколько вы хотите выходных на неделе: "))
    d = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    for j in d:
        print("Ваши выходные дни: ", *d[-a:])
        print("Ваши рабочие дни: ", *d[:-a])
        break
5.4
def p4():
    import random
    md5 = ["Яриз", "Соболева", "Зимина", "Пархомец", "Кельштейн", "Кашицына", "Марченко", "Скрипилова", "Капустинский", "Заяц"]
    md8 = ["Степанова", "Иванов", "Сальников", "Данилов", "Мешков", "Маскалёв", "Запарожец", "Гридасова", "Иванов", "Семенченко"]
    a1 = []
    a2 = []
    a = []
    a1.append(random.sample(md5, 5))
    a2.append(random.sample(md8, 5))
    a.extend(*a1)
    a.extend(*a2)
    a = tuple(a)
    print("Исходный список: ", *md5)
    print("Исходный список: ", *md8)
    print('a', *a)
    print('b', len(a))
    print('d', *sorted(a))
    print('e', 'Иванов' in a)
    print('e', a.count('Иванов)'))
###::::::::::'###::::'########:::::'###:::::::::::::'#######::
##:::::::::'## ##::: ##.... ##:::'## ##::::::::::::'##.... ##:
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::: ##::::..::
##:::::::'##:::. ##: ########::'##:::. ##:'#######: ########::
##::::::: #########: ##.... ##: #########:........: ##.... ##:
##::::::: ##.... ##: ##:::: ##: ##.... ##:::::::::: ##:::: ##:
########: ##:::: ##: ########:: ##:::: ##::::::::::. #######::
def o():
    countrees_and_cities={
        'Russia' :'Moscow',
        'America':'Boston',
        'netherlands':'amsterdam'
    }
    #Выведите на экран все пары ключ-значение.
    #b)Выведите на экран столицу для определенной страны.
    #c)Отсортируйте и выведите на экран содержимое словаря в алфавитном порядке названий стран.
    print("A -",*countrees_and_cities.keys())
    print("B -",countrees_and_cities['America'])
    print("C -",*sorted(countrees_and_cities)) \
        #Эрудит
def s():
    spisok_ochkov = {
        'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5,
        'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1,
        'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5,
        'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8,
        'Я': 3
    }
    put = input("Игра Эрудит. Введите слово - ").upper()
    points = 0
    for letter in put:
        points += spisok_ochkov.get(letter, 0)
    print("Слово",put,"стоит",points,"очков.")
def t():
    students = {
        'Иванов': {'английский', 'немецкий', 'французский'},
        'Петров': {'английский', 'китайский', 'испанский'},
        'Сидоров': {'немецкий', 'испанский', 'итальянский'},
        'Смирнова': {'французский', 'китайский'}
    }
    languages=set()
    for student in students:
        languages.update(students[student])
    chinese_speakers = [student for student in students if 'китайский' in students[student]]
    print('Имена людей которые знают китайский -',", ".join(chinese_speakers))
    print("Все языки которые знают студенты -",*languages)
###::::::::::'###::::'########:::::'###:::::::::::::'########:
##:::::::::'## ##::: ##.... ##:::'## ##:::::::::::: ##..  ##:
##::::::::'##:. ##:: ##:::: ##::'##:. ##:::::::::::..:: ##:::
##:::::::'##:::. ##: ########::'##:::. ##:'#######:::: ##::::
##::::::: #########: ##.... ##: #########:........::: ##:::::
##::::::: ##.... ##: ##:::: ##: ##.... ##:::::::::::: ##:::::
########: ##:::: ##: ########:: ##:::: ##:::::::::::: ##:::::
#7.1
def o():
    from PIL import Image
    k=Image.open('LABA_7.jpg')
    k.show()

    print("format -", k.format)
    print("size -", k.size)
    print("mode -",k.mode)
#7.2
def s():
    from PIL import Image
    img = Image.open("LABA_7.jpg")
    new_size = (198, 426)
    new_img = img.resize(new_size)
    new_img.save("/Users/mak/Desktop/LABA_7.2/resized_image.jpg")
    new_img_second=img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img_second.save("/Users/mak/Desktop/LABA_7.2/transpose_image.jpg")
    new_img_three=img.transpose(Image.FLIP_TOP_BOTTOM)
    new_img_three.save("/Users/mak/Desktop/LABA_7.2/transpose_2_image.jpg")
#7.3
def f():
    from PIL import Image, ImageEnhance
    f=Image.open("1.jpg")
    contrast = 10.0
    enhancer = ImageEnhance.Contrast(f)
    f = enhancer.enhance(contrast)
    f.save("/Users/mak/Desktop/UIU/1.jpg")
    s=Image.open("2.jpg")
    contrast = 10.0
    enhancer = ImageEnhance.Contrast(s)
    s = enhancer.enhance(contrast)
    s.save("/Users/mak/Desktop/UIU/2.jpg")
    t=Image.open("3.jpg")
    contrast = 10.0
    enhancer = ImageEnhance.Contrast(t)
    t = enhancer.enhance(contrast)
    t.save("/Users/mak/Desktop/UIU/3.jpg")
    fo=Image.open("4.jpg")
    contrast = 10.0
    enhancer = ImageEnhance.Contrast(f)
    fo = enhancer.enhance(contrast)
    fo.save("/Users/mak/Desktop/UIU/4.jpg")
    fi=Image.open("5.jpg")
    contrast = 10.0
    enhancer = ImageEnhance.Contrast(fi)
    fi = enhancer.enhance(contrast)
    fi.save("/Users/mak/Desktop/UIU/5.jpg")
#7.4
def ff():
    from PIL import Image
    img_path = '/Users/mak/Desktop/UIU/LABA_7.jpg'
    watermark_path = '/Users/mak/Desktop/UIU/Unknown-2.png'
    img = Image.open(img_path).convert('RGB')
    watermark = Image.open(watermark_path).convert('RGBA')
    watermark = watermark.resize((350,233))
    img.paste(watermark, (1, 10), watermark)
    img.save('/Users/mak/Desktop/UIU/LABA_7.1.2.jpg')
##::::::::::'###::::'########:::::'###::::::::::::::'#######::
##:::::::::'## ##::: ##.... ##:::'## ##::::::::::::'##.... ##:
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::: ##:::: ##:
##:::::::'##:::. ##: ########::'##:::. ##:'#######:: #######::
##::::::: #########: ##.... ##: #########:........:'##.... ##:
##::::::: ##.... ##: ##:::: ##: ##.... ##:::::::::: ##:::: ##:
########: ##:::: ##: ########:: ##:::: ##::::::::::. #######::
#8.1
def o():
    from PIL import Image
    frod='/Users/mak/Desktop/UIU/Holidays/LABA_8.jpg'
    img=Image.open(frod)
    print("size -", img.size)
    box = (50, 50, 400, 200)
    new_img = img.crop(box)
    new_img.save("/Users/mak/Desktop/UIU/Holidays/LABA_8.2.jpg")
    new_img.show()
#8.2
def s():
    from PIL import Image
    holidays = {
        'День рождения': '/Users/mak/Desktop/UIU/Holidays/2.jpg',
        'Новый год': '/Users/mak/Desktop/UIU/Holidays/LABA_8.2.jpg',
        'С 8 марта': '/Users/mak/Desktop/UIU/Holidays/3.jpg'
    }
    holiday = input('Введите название праздника - ')
    if holiday in holidays:
        filename=holidays[holiday]
        img = Image.open(filename)
        img.show()
    else:
        print('К сожалению, мы не нашли открытку')
#8.3
def treee():
    from PIL import Image,ImageDraw, ImageFont

    frod='/Users/mak/Desktop/UIU/Holidays/LABA_8.jpg'
    img=Image.open(frod)
    draw = ImageDraw.Draw(img)
    # k = input('Введите текст, который вы хотите добавить в открытку -')
    font = ImageFont.truetype('arial.ttf', size=36)
    text_width, text_height = draw.textsize('Hello, world!', font=font)
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2
    draw.text((x, y), 'Hello, world!', font=font, fill=(255, 255, 255))
    img.save("/Users/mak/Desktop/UIU/Holidays/LABA_8.2.jpg")
    img.show()
def tre():
    from PIL import Image, ImageDraw, ImageFont

    image = Image.open("LABA_7.jpg")

    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, 100), "Hello World!\nПривет мир!", font=font, fill='black')

    image.save('new_img.jpg')
    image.show()
##::::::::::'###::::'########:::::'###::::::::::::::'#######::
##:::::::::'## ##::: ##.... ##:::'## ##::::::::::::'##.... ##:
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::: ##:::: ##:
##:::::::'##:::. ##: ########::'##:::. ##::::::::::: ########:
##::::::: #########: ##.... ##: #########:::::::::::...... ##:
##::::::: ##.... ##: ##:::: ##: ##.... ##::::::::::'##:::: ##:
########: ##:::: ##: ########:: ##:::: ##:'#######:. #######::
#9.1
def one():
    from PIL import Image, ImageFilter
    import os
    slovar = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    new_folder = "files_for_LABA_9"
    os.makedirs(new_folder, exist_ok=True)
    for name in slovar:
        img = Image.open(name)
        img = img.filter(ImageFilter.CONTOUR)
        saving = os.path.join(new_folder, "new_" + name)
        img.save(saving)
#9.2
def second():
    from PIL import Image,ImageFilter
    import os
    slovar = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    new_folder = "files_for_LABA_9"
    os.makedirs(new_folder,exist_ok=True)
    for name in slovar:
        if name.endswith('.jpg'):
            img = Image.open(name)
            img = img.filter(ImageFilter.CONTOUR)
            saving=os.path.join(new_folder,"new_"+name)
            img.save(saving)
            print(name)
def trree():
    import csv
    kk=0
    print("nedd to buy")
    with open("data.csv") as file:
        file = csv.reader(file)
        for i in file:
            name=1[0]
            kol=int(1[1])
            c=int(i[2])
            kk += kol *c
            print(name,"-",kol,"шт. за",c,"руб")
    print("Итоговая сумма: ", kk)
##::::::::::'###::::'########:::::'###::::::::::::::::'##:::::'#####:::
##:::::::::'## ##::: ##.... ##:::'## ##:::::::::::::'####::::'##.. ##::
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::::.. ##:::'##:::: ##:
##:::::::'##:::. ##: ########::'##:::. ##:'#######:::: ##::: ##:::: ##:
##::::::: #########: ##.... ##: #########:........:::: ##::: ##:::: ##:
##::::::: ##.... ##: ##:::: ##: ##.... ##::::::::::::: ##:::. ##:: ##::
########: ##:::: ##: ########:: ##:::: ##:::::::::::'######::. #####:::
def p101():
    import json
    with open('json', 'r',encoding='utf-8') as fl:
        a = json.load(fl)
    for i in a['products']:
        print('Название:', i['name'])
        print('Цена:', i['price'])
        print('Вес: ', i['weight'])
        if i['available']:
            print('В наличии')
        else:
            print('Нет в наличии')

def p102():
    import json
    with open('json', 'r', encoding='utf-8') as fl:
        a = json.load(fl)
    for i in a['products']:
        print('Название:', i['name'])
        print('Цена:', i['price'])
        print('Вес: ', i['weight'])
        if i['available']:
            print('В наличии')
        else:
            print('Нет в наличии')
    name = input('Введите название:')
    price = input('Введите цену:')
    weight = input('Введите вес:')
    available = input(str('В наличии, введите да или нет:'))
    print('Название:', name)
    print('Цена:', price)
    print('Вес: ', weight)
    print('В наличие или нет: ', available)

def p103():
    a = {}
    with open('en.txt',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            fdata = line.split('-')
            fdata[0] = fdata[0].lstrip().rstrip()
            for j in fdata[1].split(','):
                j = j.lstrip().rstrip()
                if j not in a:
                    a[j] = [fdata[0]]
                else:
                    a[j].append(fdata[0])
    sd = dict(sorted(a.items()))
    with open('ru-en.txt', 'w',encoding='utf-8') as f:
        for key, value in sd.items():
            f.write(key + ' - ' + ', '.join(value) + '\n')
            print(key +'-'+','.join(value))

##::::::::::'###::::'########:::::'###::::::::::::::::'##::::::'##:::
##:::::::::'## ##::: ##.... ##:::'## ##:::::::::::::'####::::'####:::
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::::.. ##::::.. ##:::
##:::::::'##:::. ##: ########::'##:::. ##:'#######:::: ##:::::: ##:::
##::::::: #########: ##.... ##: #########:........:::: ##:::::: ##:::
##::::::: ##.... ##: ##:::: ##: ##.... ##::::::::::::: ##:::::: ##:::
########: ##:::: ##: ########:: ##:::: ##:::::::::::'######::'######:
def p111():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')

    newrestaurant = restaurant('Название: Кавказ', 'Тип кухни: Кавказская кухня')
    print(newrestaurant.restaurant_name)
    print(newrestaurant.cuisine_type)
    newrestaurant.describe_restaurant()
    newrestaurant.open_restaurant()

def p112():
    class rest:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')

    restaurant1 = rest('Италия', 'Итальянская кухня')
    restaurant1.describe_restaurant()
    restaurant2 = rest('Карл и Фридрих', 'Немецкая кухня')
    restaurant2.describe_restaurant()
    restaurant3 = rest('Евразия', 'Европейская кухня')
    restaurant3.describe_restaurant()

def p113():
    class rest:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')
            print(f'Рейтинг ресторана: {self.rating}')

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')

        def rating_set(self, new_rating):
            self.rating = new_rating

        def raiting(self):
            print(f'Новый рейтинг:{self.rating}')

    newrest = rest('Евразия', 'Европейская кухня', 4)
    newrest.describe_restaurant()
    newrest.rating_set(input('Введите новый рейтинг:'))
    newrest.raiting()
##::::::::::'###::::'########:::::'###::::::::::::::::'##::::'#######::
##:::::::::'## ##::: ##.... ##:::'## ##:::::::::::::'####:::'##.... ##:
##::::::::'##:. ##:: ##:::: ##::'##:. ##::::::::::::.. ##:::..::::: ##:
##:::::::'##:::. ##: ########::'##:::. ##:'#######:::: ##::::'#######::
##::::::: #########: ##.... ##: #########:........:::: ##:::'##::::::::
##::::::: ##.... ##: ##:::: ##: ##.... ##::::::::::::: ##::: ##::::::::
########: ##:::: ##: ########:: ##:::: ##:::::::::::'######: #########:
def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Название:",self.restaurant_name, "Тип кухни:",self.cuisine_type)

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ice_flavors(self):
            print('Вкусы мороженого:')
            print(*self.flavors, sep='\n')

    s = IceCreamStand("Мороженка", 'кафе', ['ваниль', 'клубника', 'шоколад'])
    s.ice_flavors()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors, loc, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = loc
            self.time = time

        def ice_flavors(self):
            print('Виды мороженного: ')
            print(*self.flavors, sep='\n')

        def newflavor(self):
            self.flavors.append(input('Введите новый сорт: '))

        def delflavor(self):
            self.flavors.remove(input('Введите сорт, который хотите удалить: '))

        def poisk(self):
            if input('Какой вкус хотите найти? ') in self.flavors:
                print('В наличии')
            else:
                print('Нет в наличии')

    class na_palochke(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, loc, time, material):
            super().__init__(restaurant_name, cuisine_type, flavors, loc, time)
            self.material = material

        def palochka(self):
            print('Материал палочки:', self.material)

    s = IceCreamStand("Морожка", 'кафе', ['ваниль', 'клубника', 'шоколад'], 'ул. Садовая', '6:00-18:00')
    s.describe_restaurant()
    s.newflavor()
    s.ice_flavors()
    s.delflavor()
    s.ice_flavors()
    s.poisk()

    g = na_palochke("Морожка", 'кафе', ['ваниль', 'клубника'], 'Вознесенский пр.', '8:00-22:00', 'дерево')
    g.palochka()

def z3():
    import tkinter as tk
    class IceCreamStand:
        def __init__(self):
            self.names = ['Как раньше', 'Ekzo', 'Коровка из Кореновки', 'Свитлогорье', 'Даша', 'Золотая трубочка']
            self.types = ['Пломбир', 'Эскимо', 'Стаканчик', 'Пломбир', 'Брикет', 'Рожок']

        def get_names(self):
            return self.names

        def get_types(self):
            return self.types

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master
            master.title("Ice Cream Stand")

            self.ice_cream_stand = IceCreamStand()
            self.names_label = tk.Label(master, text='Название', font='Calibri 12 italic bold')
            self.names_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_names()))

            for name in self.ice_cream_stand.get_names():
                self.names_listbox.insert(tk.END, name)

            self.types_label = tk.Label(master, text='Вид', font='Calibri 12 italic bold')
            self.types_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_types()))

            for type in self.ice_cream_stand.get_types():
                self.types_listbox.insert(tk.END, type)

            self.names_label.grid(row=0, column=0)
            self.names_listbox.grid(row=1, column=0)
            self.types_label.grid(row=0, column=1)
            self.types_listbox.grid(row=1, column=1)

    root = tk.Tk()
    a = IceCreamStandGUI(root)
    root.mainloop()





