import random
import string

# Список улиц и городов
cities = ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Новосибирск', 'Казань', 'Саратов', 'Волжск', 'Вологда', 'Пенза']
streets = ['Ул. Пушкина', 'Ул. Гоголя', 'Ул. Ленина', 'Ул. Советская', 'Ул. Кирова']

# Создаем пустой список для хранения данных
data_list = []
apartment = []
dacha = []
sarai = []
dom = []

# Генерируем и записываем 1000 записей
for _ in range(10000):
    area = round(random.uniform(10, 150), 2)
    price = random.randint(400000, 20000000)
    city = random.choice(cities)
    address = city + ', ' + random.choice(streets) + ', Д. ' + str(random.randint(1, 100)) + ', Кв.' + str(random.randint(1, 200))
    material = random.choice(['Кирпич', 'Панель', 'Дерево', 'Монолит', 'Шлакоблок'])
    # Добавляем данные в список
    data_list.append(f"{area},{price},'{address}','{material}','Квартира'")

for _ in range(10000):
    area = round(random.uniform(10, 150), 2)
    price = random.randint(400000, 20000000)
    city = random.choice(cities)
    address = city + ', ' + random.choice(streets) + ', Д. ' + str(random.randint(1, 100))
    material = random.choice(['Кирпич', 'Панель', 'Дерево', 'Монолит', 'Шлакоблок'])
    # Добавляем данные в список
    data_list.append(f"{area},{price},'{address}','{material}','Дача'")

for _ in range(10000):
    area = round(random.uniform(10, 150), 2)
    price = random.randint(2000000, 200000000)
    city = random.choice(cities)
    address = city + ', ' + random.choice(streets) + ', Д. ' + str(random.randint(1, 100))
    material = random.choice(['Кирпич', 'Панель', 'Дерево', 'Монолит', 'Шлакоблок'])
    # Добавляем данные в список
    data_list.append(f"{area},{price},'{address}','{material}','Дом'")

for _ in range(10000):
    area = round(random.uniform(10, 150), 2)
    price = random.randint(400000, 20000000)
    city = random.choice(cities)
    address = city + ', ' + random.choice(streets) + ', ' + str(random.randint(1, 100))
    material = random.choice(['Кирпич', 'Панель', 'Дерево', 'Монолит', 'Шлакоблок'])
    # Добавляем данные в список
    data_list.append(f"{area},{price},'{address}','{material}','Гараж'")

current_number = 1
random.shuffle(data_list)

with open('data.txt', 'w', encoding='windows-1251') as file:
    for i, line in enumerate(data_list):
        file.write(line + '\n')

            # Если строка содержит 'Квартира', то записываем номер строки и случайное число от 1 до 15
        if 'Квартира' in line:
            random_number = random.randint(1, 15)
            apartment.append(f"{i+1},{random_number}")
        if 'Гараж' in line:
            random_si = random.choice(["Да","Нет"])
            random_si2 = random.choice(["Да","Нет"])
            sarai.append(f"{i+1},{random_si},{random_si2}")
        if 'Дом' in line:
            random_number = random.randint(1, 15)
            random_ch2 = random.choice(["Многоэтажный","Культурный объект","Блоковый дом"])
            random_ch3 = random.choice(["Да","Нет","Требуется ремонт"])
            dom.append(f"{i+1},{random_number},{random_ch2},{random_ch3}")
        if 'Дача' in line:
            random_ch1 = random.choice(["Да","Нет","Требуется ремонт"])
            random_ch2 = random.choice(["Да","Нет","Требуется ремонт"])
            random_ch3 = random.choice(["Да","Нет"])
            dacha.append(f"{i+1},{random_ch1},{random_ch2},{random_ch3}")

with open('dom.txt', 'w') as file:
    for i, line in enumerate(dom):
            # Записываем данные в файл
        file.write(line + '\n')

with open('dacha.txt', 'w') as file:
    for i, line in enumerate(dacha):
            # Записываем данные в файл
        file.write(line + '\n')
with open('apartment.txt', 'w') as file:
    for i, line in enumerate(apartment):
            # Записываем данные в файл
        file.write(line + '\n')
with open('sarai.txt', 'w') as file:
    for i, line in enumerate(sarai):
        file.write(line + '\n')

ooo = ['ООО', 'ОАО', 'АОО', 'ОНН', 'АОР']
a1 = ['Шумные','Новые','Тихие','Грязные', 'Милые','Уютные','Сказочные','Райские','Нормальные','Обычные']
a2=['дома','домики', 'домины', 'домищи', 'хибары','лачуги', 'шарашки','человейники','коттеджи']

with open('Realtor.txt', 'w') as file:
    for i in range(15000):
        check =  random.choice(ooo)
        check1 = random.choice(a1)
        check2 = random.choice(a2)
        line = f"{i+1},{check} {check1} {check2}"
        file.write(line + '\n')

def generate_phone_number():
    # Генерируем случайный код региона
    region_code = random.randint(1, 999)
    region_code_str = str(region_code).zfill(3)

    # Генерируем случайные цифры для номера
    phone_number = ''.join(random.choices(string.digits, k=7))

    # Собираем номер в формате +7 (код региона) номер
    phone = f"+7{region_code_str}{phone_number}"

    return phone

# Генерация случайного email с доменом .ru
def generate_email():
    username_length = random.randint(5, 10)  # Длина имени пользователя
    username = ''.join(random.choices(string.ascii_lowercase, k=username_length))

    domain = ".ru"

    email = f"{username}@example{domain}"  # Пример домена

    return email


with open('Client.txt', 'w') as file:
    for i in range(20000):
        phone = generate_phone_number()
        email = generate_email()
        line = f"{i+1},{phone},{email}"
        file.write(line + '\n')





print("Генерация, перемешивание и запись данных завершены.")