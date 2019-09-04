# coding: utf-8

"""
    Eclipse Kapua REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.kapua_id import KapuaId  # noqa: F401,E501
from swagger_client.models.sort_field import SortField  # noqa: F401,E501
from swagger_client.models.storable_predicate import StorablePredicate  # noqa: F401,E501


class MessageQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'limit': 'int',
        'scope_id': 'KapuaId',
        'fetch_attributes': 'list[str]',
        'predicate': 'StorablePredicate',
        'ask_total_count': 'bool',
        'fetch_style': 'str',
        'sort_fields': 'list[SortField]',
        'offset': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'scope_id': 'scopeId',
        'fetch_attributes': 'fetchAttributes',
        'predicate': 'predicate',
        'ask_total_count': 'askTotalCount',
        'fetch_style': 'fetchStyle',
        'sort_fields': 'sortFields',
        'offset': 'offset'
    }

    def __init__(self, limit=None, scope_id=None, fetch_attributes=None, predicate=None, ask_total_count=None, fetch_style=None, sort_fields=None, offset=None):  # noqa: E501
        """MessageQuery - a model defined in Swagger"""  # noqa: E501

        self._limit = None
        self._scope_id = None
        self._fetch_attributes = None
        self._predicate = None
        self._ask_total_count = None
        self._fetch_style = None
        self._sort_fields = None
        self._offset = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if scope_id is not None:
            self.scope_id = scope_id
        if fetch_attributes is not None:
            self.fetch_attributes = fetch_attributes
        if predicate is not None:
            self.predicate = predicate
        if ask_total_count is not None:
            self.ask_total_count = ask_total_count
        if fetch_style is not None:
            self.fetch_style = fetch_style
        if sort_fields is not None:
            self.sort_fields = sort_fields
        if offset is not None:
            self.offset = offset

    @property
    def limit(self):
        """Gets the limit of this MessageQuery.  # noqa: E501


        :return: The limit of this MessageQuery.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this MessageQuery.


        :param limit: The limit of this MessageQuery.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def scope_id(self):
        """Gets the scope_id of this MessageQuery.  # noqa: E501


        :return: The scope_id of this MessageQuery.  # noqa: E501
        :rtype: KapuaId
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this MessageQuery.


        :param scope_id: The scope_id of this MessageQuery.  # noqa: E501
        :type: KapuaId
        """

        self._scope_id = scope_id

    @property
    def fetch_attributes(self):
        """Gets the fetch_attributes of this MessageQuery.  # noqa: E501


        :return: The fetch_attributes of this MessageQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._fetch_attributes

    @fetch_attributes.setter
    def fetch_attributes(self, fetch_attributes):
        """Sets the fetch_attributes of this MessageQuery.


        :param fetch_attributes: The fetch_attributes of this MessageQuery.  # noqa: E501
        :type: list[str]
        """

        self._fetch_attributes = fetch_attributes

    @property
    def predicate(self):
        """Gets the predicate of this MessageQuery.  # noqa: E501


        :return: The predicate of this MessageQuery.  # noqa: E501
        :rtype: StorablePredicate
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this MessageQuery.


        :param predicate: The predicate of this MessageQuery.  # noqa: E501
        :type: StorablePredicate
        """

        self._predicate = predicate

    @property
    def ask_total_count(self):
        """Gets the ask_total_count of this MessageQuery.  # noqa: E501


        :return: The ask_total_count of this MessageQuery.  # noqa: E501
        :rtype: bool
        """
        return self._ask_total_count

    @ask_total_count.setter
    def ask_total_count(self, ask_total_count):
        """Sets the ask_total_count of this MessageQuery.


        :param ask_total_count: The ask_total_count of this MessageQuery.  # noqa: E501
        :type: bool
        """

        self._ask_total_count = ask_total_count

    @property
    def fetch_style(self):
        """Gets the fetch_style of this MessageQuery.  # noqa: E501


        :return: The fetch_style of this MessageQuery.  # noqa: E501
        :rtype: str
        """
        return self._fetch_style

    @fetch_style.setter
    def fetch_style(self, fetch_style):
        """Sets the fetch_style of this MessageQuery.


        :param fetch_style: The fetch_style of this MessageQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIELDS", "SOURCE_SELECT", "SOURCE_FULL"]  # noqa: E501
        if fetch_style not in allowed_values:
            raise ValueError(
                "Invalid value for `fetch_style` ({0}), must be one of {1}"  # noqa: E501
                .format(fetch_style, allowed_values)
            )

        self._fetch_style = fetch_style

    @property
    def sort_fields(self):
        """Gets the sort_fields of this MessageQuery.  # noqa: E501


        :return: The sort_fields of this MessageQuery.  # noqa: E501
        :rtype: list[SortField]
        """
        return self._sort_fields

    @sort_fields.setter
    def sort_fields(self, sort_fields):
        """Sets the sort_fields of this MessageQuery.


        :param sort_fields: The sort_fields of this MessageQuery.  # noqa: E501
        :type: list[SortField]
        """

        self._sort_fields = sort_fields

    @property
    def offset(self):
        """Gets the offset of this MessageQuery.  # noqa: E501


        :return: The offset of this MessageQuery.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this MessageQuery.


        :param offset: The offset of this MessageQuery.  # noqa: E501
        :type: int
        """

        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MessageQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MessageQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
