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

from swagger_client.models.permission import Permission  # noqa: F401,E501


class AccessPermissionCreator(object):
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
        'access_info_id': 'str',
        'permission': 'Permission',
        'scope_id': 'str'
    }

    attribute_map = {
        'access_info_id': 'accessInfoId',
        'permission': 'permission',
        'scope_id': 'scopeId'
    }

    def __init__(self, access_info_id=None, permission=None, scope_id=None):  # noqa: E501
        """AccessPermissionCreator - a model defined in Swagger"""  # noqa: E501

        self._access_info_id = None
        self._permission = None
        self._scope_id = None
        self.discriminator = None

        if access_info_id is not None:
            self.access_info_id = access_info_id
        if permission is not None:
            self.permission = permission
        if scope_id is not None:
            self.scope_id = scope_id

    @property
    def access_info_id(self):
        """Gets the access_info_id of this AccessPermissionCreator.  # noqa: E501


        :return: The access_info_id of this AccessPermissionCreator.  # noqa: E501
        :rtype: str
        """
        return self._access_info_id

    @access_info_id.setter
    def access_info_id(self, access_info_id):
        """Sets the access_info_id of this AccessPermissionCreator.


        :param access_info_id: The access_info_id of this AccessPermissionCreator.  # noqa: E501
        :type: str
        """

        self._access_info_id = access_info_id

    @property
    def permission(self):
        """Gets the permission of this AccessPermissionCreator.  # noqa: E501


        :return: The permission of this AccessPermissionCreator.  # noqa: E501
        :rtype: Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this AccessPermissionCreator.


        :param permission: The permission of this AccessPermissionCreator.  # noqa: E501
        :type: Permission
        """

        self._permission = permission

    @property
    def scope_id(self):
        """Gets the scope_id of this AccessPermissionCreator.  # noqa: E501


        :return: The scope_id of this AccessPermissionCreator.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this AccessPermissionCreator.


        :param scope_id: The scope_id of this AccessPermissionCreator.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

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
        if issubclass(AccessPermissionCreator, dict):
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
        if not isinstance(other, AccessPermissionCreator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other