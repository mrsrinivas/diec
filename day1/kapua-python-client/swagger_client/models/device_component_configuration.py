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

from swagger_client.models.kapua_tocd import KapuaTocd  # noqa: F401,E501


class DeviceComponentConfiguration(object):
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
        'id': 'str',
        'definition': 'KapuaTocd',
        'name': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'definition': 'definition',
        'name': 'name',
        'properties': 'properties'
    }

    def __init__(self, id=None, definition=None, name=None, properties=None):  # noqa: E501
        """DeviceComponentConfiguration - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._definition = None
        self._name = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if definition is not None:
            self.definition = definition
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this DeviceComponentConfiguration.  # noqa: E501


        :return: The id of this DeviceComponentConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceComponentConfiguration.


        :param id: The id of this DeviceComponentConfiguration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def definition(self):
        """Gets the definition of this DeviceComponentConfiguration.  # noqa: E501


        :return: The definition of this DeviceComponentConfiguration.  # noqa: E501
        :rtype: KapuaTocd
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this DeviceComponentConfiguration.


        :param definition: The definition of this DeviceComponentConfiguration.  # noqa: E501
        :type: KapuaTocd
        """

        self._definition = definition

    @property
    def name(self):
        """Gets the name of this DeviceComponentConfiguration.  # noqa: E501


        :return: The name of this DeviceComponentConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceComponentConfiguration.


        :param name: The name of this DeviceComponentConfiguration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this DeviceComponentConfiguration.  # noqa: E501


        :return: The properties of this DeviceComponentConfiguration.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DeviceComponentConfiguration.


        :param properties: The properties of this DeviceComponentConfiguration.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

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
        if issubclass(DeviceComponentConfiguration, dict):
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
        if not isinstance(other, DeviceComponentConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other