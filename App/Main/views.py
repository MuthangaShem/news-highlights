from flask import render_template, request, redirect
from . import main
from ..requests import get_sources, get_articles


@main.route('/')
def index():
    """Function that returns index page and different news sources, view page source"""
    title = 'Home- Welcome News Highlights Website'

    # Getting the news sources
    news_sources = get_sources('sources')
    return render_template('index.html', title=title, sources=news_sources)


@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    Function that returns a source page and its data, view page source
    '''
    title = f"{source_id} page"
    articles = get_articles(source_id)
    return render_template('articles.html', title=title, articles=articles)
