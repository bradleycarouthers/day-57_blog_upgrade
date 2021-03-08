from flask import Flask, render_template
from post import Post
import requests

# Put each post object in list
all_posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    # Replace pertinent fields in index will post information from post objects list
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    # This page gets displayed when clicked on from home page
    # Create an empty var and pull relavent info depending on id number of post
    request_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            # Empty var is filled if its id matches the index number
            request_post = blog_post
    return render_template("post.html", post=request_post)


if __name__ == "__main__":
    app.run(debug=True)
