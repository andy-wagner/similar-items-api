# coding: utf-8

from __future__ import absolute_import

from flask import json
from app.models.item_set import ItemSet
from app.models.item import Item
from app.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_build_info_get(self):
        """Test case for build_info_get

        Returns the build info
        """
        response = self.client.open(
            '/',
            method='GET')

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_similar_get(self):
        """Test case for similar_get

        Returns the set of items ordered by similarity, compared to the given item
        """
        body = ItemSet(data=[Item(id='1',name="car bmw"), Item(id='2',name='car')])
        response = self.client.open(
            '/similar/{id}'.format(id='1'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
