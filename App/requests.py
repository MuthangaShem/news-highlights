import urlib2.request
import json
from .models import Sources, Articles

# Getting the API KEY
api_key = None

# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources(source):
    """
    Retrieve news sources list from the News api
    """

    get_sources_url = base_url.format(source, api_key)

    with urlib2.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    """Process the results list and transforms them into a list of objects
    Args: sources_list: A list of dictionaries that contains news sources details
    Returns:
    sources_results: a list of news sources objects"""

    sources_results = []  # a list of news sources objects

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        source_object = Sources(id, name, description, url, category)
        sources_results.append(source_object)

    return sources_results


def get_articles(id):
    '''
    Function to get a source and it's articles
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        id, api_key)

    with urlib2.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results



