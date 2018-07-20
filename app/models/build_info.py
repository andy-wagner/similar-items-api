# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util


class BuildInfo(Model):

    def __init__(self, name: str=None, version: str=None):
        """BuildInfo - a model defined in Swagger

        :param name: The name of this BuildInfo.
        :type name: str
        :param version: The version of this BuildInfo.
        :type version: str
        """
        self.swagger_types = {
            'name': str,
            'version': str
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version'
        }

        self._name = name
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'BuildInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BuildInfo of this BuildInfo.
        :rtype: BuildInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this BuildInfo.


        :return: The name of this BuildInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BuildInfo.


        :param name: The name of this BuildInfo.
        :type name: str
        """

        self._name = name

    @property
    def version(self) -> str:
        """Gets the version of this BuildInfo.


        :return: The version of this BuildInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this BuildInfo.


        :param version: The version of this BuildInfo.
        :type version: str
        """

        self._version = version
