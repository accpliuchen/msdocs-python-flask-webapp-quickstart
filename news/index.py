from flask import Blueprint, render_template

news_blueprint = Blueprint('news', __name__)

@news_blueprint.route("/news")
def index():
    return "Hello news!"