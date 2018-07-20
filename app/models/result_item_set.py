# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime

from typing import List, Dict

from app.models.base_model_ import Model
from app.models.item import Item
from app import util


class ResultItemSet(Model):

    def __init__(self, result: Item=None, similar: List[Item]=None, count: int=None):  # noqa: E501
        """ResultItemSet - a model defined in Swagger

        :param result: The result of this ResultItemSet.  # noqa: E501
        :type result: Item
        :param similar: The similar of this ResultItemSet.  # noqa: E501
        :type similar: List[Item]
        :param count: The count of this ResultItemSet.  # noqa: E501
        :type count: int
        """
        self.swagger_types = {
            'result': Item,
            'similar': List[Item],
            'count': int
        }

        self.attribute_map = {
            'result': 'result',
            'similar': 'similar',
            'count': 'count'
        }

        self._result = result
        self._similar = similar
        self._count = count

    @classmethod
    def from_dict(cls, dikt) -> 'ResultItemSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResultItemSet of this ResultItemSet.  # noqa: E501
        :rtype: ResultItemSet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self) -> Item:
        """Gets the result of this ResultItemSet.


        :return: The result of this ResultItemSet.
        :rtype: Item
        """
        return self._result

    @result.setter
    def result(self, result: Item):
        """Sets the result of this ResultItemSet.


        :param result: The result of this ResultItemSet.
        :type result: Item
        """

        self._result = result

    @property
    def similar(self) -> List[Item]:
        """Gets the similar of this ResultItemSet.


        :return: The similar of this ResultItemSet.
        :rtype: List[Item]
        """
        return self._similar

    @similar.setter
    def similar(self, similar: List[Item]):
        """Sets the similar of this ResultItemSet.


        :param similar: The similar of this ResultItemSet.
        :type similar: List[Item]
        """

        self._similar = similar

    @property
    def count(self) -> int:
        """Gets the count of this ResultItemSet.


        :return: The count of this ResultItemSet.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this ResultItemSet.


        :param count: The count of this ResultItemSet.
        :type count: int
        """

        self._count = count
