from random import choice, randint
from faker import Faker
import json
from gender_guesser.detector import Detector
import requests
import concurrent.futures
from time import perf_counter

t0 = perf_counter()

fake = Faker()
gender_detector = Detector()


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


def get_img_url(g):
    g = "man" if g == "male" else "woman"
    url = f"https://source.unsplash.com/random/500x500/?{g}"

    r = requests.head(url)
    return r.headers.get("location")


def create_post(n):
    fn = fake.first_name()
    ln = fake.last_name()
    mdn = fake.last_name()
    gender = gender_detector.get_gender(fn)
    profile_pic = get_img_url(gender if gender != "unknown" else "man")
    username = generate_username(fn, ln, mdn)
    comment = {
        "id": n,
        "message": fake.sentence(nb_words=randint(4, 18)),
        "profile_pic": profile_pic,
        "created_at": str(fake.date_time_this_year()),
        "commenter_id": randint(1, 100),
        "username": username,
        "post_id": randint(1, 1000),
    }
    return comment


def create_comments(n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        post_futures = [executor.submit(create_post, i) for i in range(n)]
        posts = [
            future.result() for future in concurrent.futures.as_completed(post_futures)
        ]

    return posts


with open("comments.json", "w") as f:
    json.dump(create_comments(1000), f)
print(perf_counter() - t0)
