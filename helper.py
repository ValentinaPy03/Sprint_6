from faker import Faker
import random

def generate_order_data():
    faker = Faker('ru_RU')
    name = faker.first_name()
    last_name = faker.last_name()
    address = f'{faker.street_name()}, {random.randint(1, 200)}'
    phone = f'89{random.randint(111111111, 999999999)}'
    return name, last_name, address, phone

