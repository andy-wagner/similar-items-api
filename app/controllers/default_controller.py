import connexion
from app.models.item_set import ItemSet
from app.models.result_item_set import ResultItemSet
from app.models.item import Item
from app.models.build_info import BuildInfo
import json
import os
from app.controllers.nlp import stem_tokens, normalize, cosine_sim
from sklearn.feature_extraction.text import TfidfVectorizer
import logging

logger = logging.getLogger(__name__)


def build_info_get():
    """Returns the build info
    :rtype: BuildInfo
    """
    try:
        filename = os.path.join(
            os.path.dirname(__file__), 'resource', 'buildInfo.json')
        with open(filename) as f:
            config = json.load(f)
            build_info = BuildInfo(config['name'], config['version'])
    except Exception as e:
        logger.warning(e)
    return build_info


def similar_get(id, body):
    """Returns the set of items ordered by similarity, compared to the given query item
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes
    :rtype: ResultItemSet
    """
    try:
        vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
        if connexion.request.is_json:
            data = {}
            input_item = Item(id=id, name='', similarity=0)
            results = []
            item_set = ItemSet.from_dict(connexion.request.get_json())
            for i in item_set.data:
                if i.id != id:
                    data[i.id] = i.name
                else:
                    input_item.name = i.name
            for item in data:
                results.append(
                    (Item(id=item, name=data[item], similarity=cosine_sim(input_item.name, data[item], vectorizer))))
            item_set.data = sorted(results, key=lambda it: (it.similarity), reverse=True)
    except Exception as e:
        logger.warning(e, connexion.request)

    return item_set
