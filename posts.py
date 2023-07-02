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


def get_thumbnail_url():
    g = choice(["nature", "farm", "animal", "ai", "technology"])
    url = f"https://source.unsplash.com/random/500x300/?{g}"

    r = requests.head(url)
    return r.headers.get("location")


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
    post = {
        "post_id": n,
        "title": fake.sentence(nb_words=randint(6, 14)),
        "body": fake.paragraph(nb_sentences=randint(4, 12)),
        "thumbnail_url": get_thumbnail_url(),
        "created_at": str(fake.date_time_this_year()),
        "author_id": randint(1, 100),
        "author": fake.name(),
        "likes": fake.random_int(min=0, max=100),
        "comments": [],
    }

    with concurrent.futures.ThreadPoolExecutor() as executor:
        comment_futures = [
            executor.submit(
                create_comment,
                i + 1,
                post["post_id"],
                randint(1, 1000),
                profile_pic,
                username,
            )
            for i in range(randint(0, 5))
        ]
        for future in concurrent.futures.as_completed(comment_futures):
            post["comments"].append(future.result())

    return post


def create_comment(id, post_id, commenter_id, profile_pic, username):
    comment = {
        "id": id,
        "message": fake.sentence(nb_words=randint(6, 14)),
        "post_id": post_id,
        "commenter_id": commenter_id,
        "profile_pic": profile_pic,
        "username": username,
    }
    return comment


def create_posts(n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        post_futures = [executor.submit(create_post, i) for i in range(n)]
        posts = [
            future.result() for future in concurrent.futures.as_completed(post_futures)
        ]

    return posts


with open("posts.json", "w") as f:
    json.dump(create_posts(1000), f)
print(perf_counter() - t0)
