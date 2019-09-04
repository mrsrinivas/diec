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

from swagger_client.models.storable_id import StorableId  # noqa: F401,E501


class ChannelInfo(object):
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
        'scope_id': 'str',
        'id': 'StorableId',
        'client_id': 'str',
        'first_message_id': 'StorableId',
        'first_message_on': 'datetime',
        'last_message_id': 'StorableId',
        'last_message_on': 'datetime',
        'name': 'str'
    }

    attribute_map = {
        'scope_id': 'scopeId',
        'id': 'id',
        'client_id': 'clientId',
        'first_message_id': 'firstMessageId',
        'first_message_on': 'firstMessageOn',
        'last_message_id': 'lastMessageId',
        'last_message_on': 'lastMessageOn',
        'name': 'name'
    }

    def __init__(self, scope_id=None, id=None, client_id=None, first_message_id=None, first_message_on=None, last_message_id=None, last_message_on=None, name=None):  # noqa: E501
        """ChannelInfo - a model defined in Swagger"""  # noqa: E501

        self._scope_id = None
        self._id = None
        self._client_id = None
        self._first_message_id = None
        self._first_message_on = None
        self._last_message_id = None
        self._last_message_on = None
        self._name = None
        self.discriminator = None

        if scope_id is not None:
            self.scope_id = scope_id
        if id is not None:
            self.id = id
        if client_id is not None:
            self.client_id = client_id
        if first_message_id is not None:
            self.first_message_id = first_message_id
        if first_message_on is not None:
            self.first_message_on = first_message_on
        if last_message_id is not None:
            self.last_message_id = last_message_id
        if last_message_on is not None:
            self.last_message_on = last_message_on
        if name is not None:
            self.name = name

    @property
    def scope_id(self):
        """Gets the scope_id of this ChannelInfo.  # noqa: E501


        :return: The scope_id of this ChannelInfo.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this ChannelInfo.


        :param scope_id: The scope_id of this ChannelInfo.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def id(self):
        """Gets the id of this ChannelInfo.  # noqa: E501


        :return: The id of this ChannelInfo.  # noqa: E501
        :rtype: StorableId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChannelInfo.


        :param id: The id of this ChannelInfo.  # noqa: E501
        :type: StorableId
        """

        self._id = id

    @property
    def client_id(self):
        """Gets the client_id of this ChannelInfo.  # noqa: E501


        :return: The client_id of this ChannelInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ChannelInfo.


        :param client_id: The client_id of this ChannelInfo.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def first_message_id(self):
        """Gets the first_message_id of this ChannelInfo.  # noqa: E501


        :return: The first_message_id of this ChannelInfo.  # noqa: E501
        :rtype: StorableId
        """
        return self._first_message_id

    @first_message_id.setter
    def first_message_id(self, first_message_id):
        """Sets the first_message_id of this ChannelInfo.


        :param first_message_id: The first_message_id of this ChannelInfo.  # noqa: E501
        :type: StorableId
        """

        self._first_message_id = first_message_id

    @property
    def first_message_on(self):
        """Gets the first_message_on of this ChannelInfo.  # noqa: E501


        :return: The first_message_on of this ChannelInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._first_message_on

    @first_message_on.setter
    def first_message_on(self, first_message_on):
        """Sets the first_message_on of this ChannelInfo.


        :param first_message_on: The first_message_on of this ChannelInfo.  # noqa: E501
        :type: datetime
        """

        self._first_message_on = first_message_on

    @property
    def last_message_id(self):
        """Gets the last_message_id of this ChannelInfo.  # noqa: E501


        :return: The last_message_id of this ChannelInfo.  # noqa: E501
        :rtype: StorableId
        """
        return self._last_message_id

    @last_message_id.setter
    def last_message_id(self, last_message_id):
        """Sets the last_message_id of this ChannelInfo.


        :param last_message_id: The last_message_id of this ChannelInfo.  # noqa: E501
        :type: StorableId
        """

        self._last_message_id = last_message_id

    @property
    def last_message_on(self):
        """Gets the last_message_on of this ChannelInfo.  # noqa: E501


        :return: The last_message_on of this ChannelInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_message_on

    @last_message_on.setter
    def last_message_on(self, last_message_on):
        """Sets the last_message_on of this ChannelInfo.


        :param last_message_on: The last_message_on of this ChannelInfo.  # noqa: E501
        :type: datetime
        """

        self._last_message_on = last_message_on

    @property
    def name(self):
        """Gets the name of this ChannelInfo.  # noqa: E501


        :return: The name of this ChannelInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChannelInfo.


        :param name: The name of this ChannelInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(ChannelInfo, dict):
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
        if not isinstance(other, ChannelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
