from flask import Flask, make_response, request, jsonify
import json, io
import random
from PIL import Image, ImageDraw, ImageFont
from faker import Faker

app = Flask(__name__)


def get_posts():
    with open("posts.json", "r", encoding="utf-8") as file:
        posts = json.load(file)
    return posts["posts"]


def get_jobs():
    with open("jobs.json", "r", encoding="utf-8") as file:
        jobs = json.load(file)
    return jobs["jobs"]


def get_users():
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    return users["users"]


def get_comments():
    with open("comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
    return comments["comments"]


@app.route("/api", methods=["POST", "GET"])
def api_home():
    return jsonify({"status": "ok", "message": "Welcome to the Fakeinfo API"})


@app.route("/api/v1", methods=["POST", "GET"])
def api_v1_home():
    return jsonify({"status": "ok", "message": "Welcome to the Fakeinfo API"})


@app.route(
    "/api/v1/posts", methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"]
)
def get_all_posts():
    try:
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get posts, use a GET request rather.",
                    }
                ),
                400,
            )
        return jsonify(
            {
                "status": "ok",
                "posts": get_posts(),
            }
        )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/posts/paginate",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"],
)
def paginate_posts():
    try:
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get posts, use a GET request rather.",
                    }
                ),
                400,
            )
        posts = get_posts()
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_data = posts[start_index:end_index]
        return jsonify(
            {
                "posts": paginated_data,
                "total": len(paginated_data),
                "status": "ok",
            },
        )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/post/<int:id>",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE", "HEAD"],
)
def handler_single_post(id):
    try:
        if request.method == "PUT" or request.method == "PATCH":
            return jsonify(
                {
                    "status": "ok",
                    "message": "Post updated successfully",
                }
            )

        elif request.method == "GET":
            posts = get_posts()
            length = len(posts)
            if id <= length:
                single_post = posts[id]
                return jsonify(
                    {
                        "status": "ok",
                        "post": single_post,
                    }
                )
            else:
                return jsonify(
                    {
                        "status": "failed",
                        "message": "The post you are trying to get does not exist",
                    }
                )
        else:
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get posts, use a GET request rather.",
                    }
                ),
                400,
            )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/comments", methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"]
)
def get_all_comments():
    try:
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get comments, use a GET request rather.",
                    }
                ),
                400,
            )
        return jsonify(
            {
                "status": "ok",
                "comments": get_comments(),
            }
        )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/comments/paginate",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"],
)
def paginate_comments():
    try:
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get comments, use a GET request rather.",
                    }
                ),
                400,
            )
        posts = get_comments()
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_data = posts[start_index:end_index]
        return jsonify(
            {
                "posts": paginated_data,
                "total": len(paginated_data),
                "status": "ok",
            },
        )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/comment/<int:id>",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE", "HEAD"],
)
def handler_single_comment(id):
    try:
        if request.method == "PUT" or request.method == "PATCH":
            return jsonify(
                {
                    "status": "ok",
                    "message": "Post updated successfully",
                }
            )

        elif request.method == "GET":
            comments = get_comments()
            length = len(comments)
            if id <= length:
                single_comment = comments[id]
                return jsonify(
                    {
                        "status": "ok",
                        "post": single_comment,
                    }
                )
            else:
                return jsonify(
                    {
                        "status": "failed",
                        "message": "The comment you are trying to get does not exist",
                    }
                )
        else:
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get comments, use a GET request rather.",
                    }
                ),
                400,
            )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/users", methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"]
)
def get_all_users():
    try:
        users = get_users()
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get users, use a GET request rather.",
                    }
                ),
                400,
            )
        return jsonify(
            {
                "status": "ok",
                "users": users,
                "total": len(users),
            },
        )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/users/paginate",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"],
)
def paginate_users():
    try:
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get users, use a GET request rather.",
                    }
                ),
                400,
            )
        users = get_users()
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_data = users[start_index:end_index]
        return jsonify(
            {
                "users": paginated_data,
                "total": len(paginated_data),
                "status": "ok",
            },
        )

    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/user/<int:id>",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE", "HEAD"],
)
def handler_single_user(id):
    try:
        if request.method == "PUT" or request.method == "PATCH":
            return jsonify(
                {
                    "status": "ok",
                    "message": "Post updated successfully",
                }
            )

        elif request.method == "GET":
            users = get_users()
            length = len(users)
            if id <= length:
                single_user = users[id]
                return jsonify(
                    {
                        "status": "ok",
                        "user": single_user,
                    }
                )
            else:
                return jsonify(
                    {
                        "status": "failed",
                        "message": "The user you are trying to get does not exist",
                    }
                )
        else:
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get users, use a GET request rather.",
                    }
                ),
                400,
            )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route("/api/v1/jobs", methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"])
def get_all_jobs():
    try:
        jobs = get_jobs()
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get jobs, use a GET request rather.",
                    }
                ),
                400,
            )
        return jsonify(
            {
                "status": "ok",
                "jobs": jobs,
                "total": len(jobs),
            },
        )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/jobs/paginate",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE"],
)
def paginate_jobs():
    try:
        if request.method != "GET":
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get jobs, use a GET request rather.",
                    }
                ),
                400,
            )
        jobs = get_jobs()
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_data = jobs[start_index:end_index]
        return jsonify(
            {
                "jobs": paginated_data,
                "total": len(paginated_data),
                "status": "ok",
            },
        )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route(
    "/api/v1/job/<int:id>",
    methods=["POST", "GET", "PUT", "PATCH", "OPTIONS", "DELETE", "HEAD"],
)
def handler_single_job(id):
    try:
        if request.method == "PUT" or request.method == "PATCH":
            return jsonify(
                {
                    "status": "ok",
                    "message": "Job updated successfully",
                }
            )

        elif request.method == "GET":
            jobs = get_jobs()
            length = len(jobs)
            if id <= length:
                single_job = jobs[id]
                return jsonify(
                    {
                        "status": "ok",
                        "job": single_job,
                    }
                )
            else:
                return jsonify(
                    {
                        "status": "failed",
                        "message": "The job you are trying to get does not exist",
                    }
                )
        else:
            return (
                jsonify(
                    {
                        "status": "failed",
                        "message": "To get jobs, use a GET request rather.",
                    }
                ),
                400,
            )
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


@app.route("/api/v1/imageplaceholder")
def generate_image_placeholder():
    try:
        width = int(request.args.get("width", 400))
        height = int(request.args.get("height", 200))
        text = f"{width} x {height}"

        # Create a blank white image
        image = Image.new("RGB", (width, height), "#e4e4e4")
        draw = ImageDraw.Draw(image)

        # Add optional text to the image
        if text:
            # Determine the font size based on the image dimensions
            font_size = min(width, height) // 5
            font = ImageFont.truetype("arial.ttf", font_size)

            # Calculate the text bounding box
            text_bbox = draw.textbbox((0, 0), text, font=font)

            # Calculate the text position at the center of the image
            text_position = ((width - text_bbox[2]) // 2, (height - text_bbox[3]) // 2)

            # Draw the text on the image
            draw.text(text_position, text, font=font, fill="black")

        # Save the image to a BytesIO buffer
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        # Create a response with the image data
        response = make_response(buffer.getvalue())
        response.headers["Content-Type"] = "image/png"

        return response
    except:
        return jsonify(
            {
                "status": "failed",
                "message": "Something happened and request could not process",
            }
        )


if __name__ == "__main__":
    app.run(debug=1)
