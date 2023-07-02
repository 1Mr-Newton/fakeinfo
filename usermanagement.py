from concurrent.futures import ThreadPoolExecutor
import json
from faker import Faker
from gender_guesser.detector import Detector
import bcrypt
from datetime import datetime, timedelta
from random import randint
from time import perf_counter
import requests

fake = Faker()
gender_detector = Detector()

t0 = perf_counter()


def get_img_url(g):
    g = "man" if g == "male" else "woman"
    url = f"https://source.unsplash.com/random/500x500/?{g}"

    r = requests.head(url)
    return r.headers.get("location")


def generate_username(first_name, last_name, maiden_name):
    first_name = first_name.lower().replace(" ", "")
    last_name = last_name.lower().replace(" ", "")
    maiden_name = maiden_name.lower().replace(" ", "")

    if maiden_name:
        username = (
            first_name[0] + last_name[: randint(3, 5)] + maiden_name[: randint(2, 5)]
        )
    else:
        username = first_name[0] + last_name[: randint(5, 8)]

    return username


def generate_birth_date(age):
    today = datetime.now()
    birth_date = today - timedelta(days=age * 365)
    return birth_date.strftime("%Y-%m-%d")


def generate_user(i):
    password = fake.password()
    fn = fake.first_name()
    ln = fake.last_name()
    mdn = fake.last_name()
    age = fake.random_int(min=18, max=80)
    dob = generate_birth_date(age)
    key = bcrypt.gensalt().decode("utf-8")
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"), key.encode("utf-8")
    ).decode("utf-8")
    username = generate_username(fn, ln, mdn)
    gender = gender_detector.get_gender(fn)

    user = {
        "id": i + 1,
        "firstName": fn,
        "lastName": ln,
        "maidenName": mdn,
        "age": age,
        "gender": gender if gender != "unknown" else "something else",
        "email": fake.email(),
        "phone": fake.phone_number(),
        "username": username,
        "password": password,
        "passwordkey": key,
        "passwordhash": hashed_password,
        "birthDate": dob,
        "image": get_img_url(gender if gender != "unknown" else "man"),
        "bloodGroup": fake.random_element(
            elements=("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        ),
        "height": fake.random_int(min=150, max=200),
        "weight": fake.random_int(min=150, max=200),
        "eyeColor": fake.random_element(elements=("Blue", "Green", "Brown")),
        "hair": {
            "color": fake.color_name(),
            "type": fake.random_element(elements=("Straight", "Curly", "Wavy")),
        },
        "domain": fake.domain_name(),
        "ip": fake.ipv4(),
        "address": {
            "address": fake.street_address(),
            "city": fake.city(),
            "coordinates": {
                "lat": float(fake.latitude()),
                "lng": float(fake.longitude()),
            },
            "postalCode": fake.zipcode(),
            "state": fake.state(),
        },
        "macAddress": fake.mac_address(),
        "university": fake.company(),
        "bank": {
            "cardExpire": fake.credit_card_expire(),
            "cardNumber": fake.credit_card_number(),
            "cardType": fake.credit_card_provider(),
            "currency": fake.currency_name(),
            "iban": fake.iban(),
        },
        "company": {
            "address": {
                "address": fake.street_address(),
                "city": fake.city(),
                "coordinates": {
                    "lat": float(fake.latitude()),
                    "lng": float(fake.longitude()),
                },
                "postalCode": fake.zipcode(),
                "state": fake.state(),
            },
            "department": fake.job(),
            "title": fake.job(),
        },
        "ein": fake.ein(),
        "ssn": fake.ssn(),
    }

    return user


def generate_users(n):
    with ThreadPoolExecutor() as executor:
        users = list(executor.map(generate_user, range(n)))
    return users


def users(n):
    us = generate_users(n)
    results = {
        "users": us,
        "total": n,
    }
    return json.dumps(results)


# with open("users.json", "w") as f:
#     f.write(users(1000))
# print(perf_counter() - t0)
