from datetime import datetime
from mongoengine.errors import ValidationError
from models import AddressBook, Email, Phone
import connect


def create_user(user_name: str, address: str = None, phone: str = None, email: str = None, birthday: datetime = None):
    try:
        field_phone = Phone(data=phone)
        field_email = Email(data=email)
        AddressBook(name=user_name, address=address, birthday=birthday, phone=[field_phone], email=[field_email]).save()
        print(f'User {user_name} had been created')
    except ValidationError:
        print('User not create, try again')


def search_user(user_name: str):
    users = AddressBook.objects(name__iregex=f'{user_name}')
    for user in users:
        phone = [phone.data for phone in user.phone]
        email = [email.data for email in user.email]
        print(f'User: {user.name}', *phone, *email)


def add_phone(user_name: str, phone: str):
    new_phone = Phone(data=phone)
    users = AddressBook.objects(name__iregex=f'{user_name}')
    for user in users:
        old_phone = []
        for el in user.phone:
            old_phone.append(el)
        user.update(phone=[*old_phone, new_phone])
        print(f'Phone {phone} has been add for {user.name} user')


if __name__ == '__main__':
    create_user('Mongo Team', email='test@')  # invalid email
    create_user('Test User', email='tetet@test.com')
    create_user('Test Person', email='new@test.com', phone='099932321')
    search_user('Test')
    add_phone('Test', '3333')
