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

from swagger_client.models.role_permission import RolePermission  # noqa: F401,E501


class RolePermissionListResult(object):
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
        'items': 'list[RolePermission]',
        'limit_exceeded': 'bool',
        'first_item': 'RolePermission',
        'empty': 'bool',
        'size': 'int'
    }

    attribute_map = {
        'items': 'items',
        'limit_exceeded': 'limitExceeded',
        'first_item': 'firstItem',
        'empty': 'empty',
        'size': 'size'
    }

    def __init__(self, items=None, limit_exceeded=None, first_item=None, empty=None, size=None):  # noqa: E501
        """RolePermissionListResult - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._limit_exceeded = None
        self._first_item = None
        self._empty = None
        self._size = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if limit_exceeded is not None:
            self.limit_exceeded = limit_exceeded
        if first_item is not None:
            self.first_item = first_item
        if empty is not None:
            self.empty = empty
        if size is not None:
            self.size = size

    @property
    def items(self):
        """Gets the items of this RolePermissionListResult.  # noqa: E501


        :return: The items of this RolePermissionListResult.  # noqa: E501
        :rtype: list[RolePermission]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this RolePermissionListResult.


        :param items: The items of this RolePermissionListResult.  # noqa: E501
        :type: list[RolePermission]
        """

        self._items = items

    @property
    def limit_exceeded(self):
        """Gets the limit_exceeded of this RolePermissionListResult.  # noqa: E501


        :return: The limit_exceeded of this RolePermissionListResult.  # noqa: E501
        :rtype: bool
        """
        return self._limit_exceeded

    @limit_exceeded.setter
    def limit_exceeded(self, limit_exceeded):
        """Sets the limit_exceeded of this RolePermissionListResult.


        :param limit_exceeded: The limit_exceeded of this RolePermissionListResult.  # noqa: E501
        :type: bool
        """

        self._limit_exceeded = limit_exceeded

    @property
    def first_item(self):
        """Gets the first_item of this RolePermissionListResult.  # noqa: E501


        :return: The first_item of this RolePermissionListResult.  # noqa: E501
        :rtype: RolePermission
        """
        return self._first_item

    @first_item.setter
    def first_item(self, first_item):
        """Sets the first_item of this RolePermissionListResult.


        :param first_item: The first_item of this RolePermissionListResult.  # noqa: E501
        :type: RolePermission
        """

        self._first_item = first_item

    @property
    def empty(self):
        """Gets the empty of this RolePermissionListResult.  # noqa: E501


        :return: The empty of this RolePermissionListResult.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this RolePermissionListResult.


        :param empty: The empty of this RolePermissionListResult.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def size(self):
        """Gets the size of this RolePermissionListResult.  # noqa: E501


        :return: The size of this RolePermissionListResult.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RolePermissionListResult.


        :param size: The size of this RolePermissionListResult.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if issubclass(RolePermissionListResult, dict):
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
        if not isinstance(other, RolePermissionListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
