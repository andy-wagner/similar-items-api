# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime

from typing import List, Dict

from app.models.base_model_ import Model
from app.models.item import Item
from app import util


class ItemSet(Model):

    def __init__(self, data: List[Item]=None):  # noqa: E501
        """ItemSet - a model defined in Swagger

        :param data: The data of this ItemSet.  # noqa: E501
        :type data: List[Item]
        """
        self.swagger_types = {
            'data': List[Item]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ItemSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ItemSet of this ItemSet.  # noqa: E501
        :rtype: ItemSet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[Item]:
        """Gets the data of this ItemSet.


        :return: The data of this ItemSet.
        :rtype: List[Item]
        """
        return self._data

    @data.setter
    def data(self, data: List[Item]):
        """Sets the data of this ItemSet.


        :param data: The data of this ItemSet.
        :type data: List[Item]
        """

        self._data = data