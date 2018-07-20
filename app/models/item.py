# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util



class Item(Model):

    def __init__(self, name: str=None, id: str=None, similarity: float=None):  # noqa: E501
        """Item - a model defined in Swagger

        :param name: The name of this Item.  # noqa: E501
        :type name: str
        :param id: The id of this Item.  # noqa: E501
        :type id: str
        :param similarity: The similarity of this Item.  # noqa: E501
        :type similarity: float
        """
        self.swagger_types = {
            'name': str,
            'id': str,
            'similarity': float
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'similarity': 'similarity'
        }

        self._name = name
        self._id = id
        self._similarity = similarity

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Item of this Item.  # noqa: E501
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Item.


        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Item.


        :param name: The name of this Item.
        :type name: str
        """

        self._name = name

    @property
    def id(self) -> str:
        """Gets the id of this Item.


        :return: The id of this Item.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Item.


        :param id: The id of this Item.
        :type id: str
        """

        self._id = id

    @property
    def similarity(self) -> float:
        """Gets the similarity of this Item.


        :return: The similarity of this Item.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity: float):
        """Sets the similarity of this Item.


        :param similarity: The similarity of this Item.
        :type similarity: float
        """

        self._similarity = similarity
