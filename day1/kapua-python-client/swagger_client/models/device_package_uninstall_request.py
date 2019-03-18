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


class DevicePackageUninstallRequest(object):
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
        'version': 'str',
        'reboot': 'bool',
        'reboot_delay': 'int',
        'name': 'str'
    }

    attribute_map = {
        'version': 'version',
        'reboot': 'reboot',
        'reboot_delay': 'rebootDelay',
        'name': 'name'
    }

    def __init__(self, version=None, reboot=None, reboot_delay=None, name=None):  # noqa: E501
        """DevicePackageUninstallRequest - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._reboot = None
        self._reboot_delay = None
        self._name = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if reboot is not None:
            self.reboot = reboot
        if reboot_delay is not None:
            self.reboot_delay = reboot_delay
        if name is not None:
            self.name = name

    @property
    def version(self):
        """Gets the version of this DevicePackageUninstallRequest.  # noqa: E501


        :return: The version of this DevicePackageUninstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DevicePackageUninstallRequest.


        :param version: The version of this DevicePackageUninstallRequest.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def reboot(self):
        """Gets the reboot of this DevicePackageUninstallRequest.  # noqa: E501


        :return: The reboot of this DevicePackageUninstallRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        """Sets the reboot of this DevicePackageUninstallRequest.


        :param reboot: The reboot of this DevicePackageUninstallRequest.  # noqa: E501
        :type: bool
        """

        self._reboot = reboot

    @property
    def reboot_delay(self):
        """Gets the reboot_delay of this DevicePackageUninstallRequest.  # noqa: E501


        :return: The reboot_delay of this DevicePackageUninstallRequest.  # noqa: E501
        :rtype: int
        """
        return self._reboot_delay

    @reboot_delay.setter
    def reboot_delay(self, reboot_delay):
        """Sets the reboot_delay of this DevicePackageUninstallRequest.


        :param reboot_delay: The reboot_delay of this DevicePackageUninstallRequest.  # noqa: E501
        :type: int
        """

        self._reboot_delay = reboot_delay

    @property
    def name(self):
        """Gets the name of this DevicePackageUninstallRequest.  # noqa: E501


        :return: The name of this DevicePackageUninstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DevicePackageUninstallRequest.


        :param name: The name of this DevicePackageUninstallRequest.  # noqa: E501
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
        if issubclass(DevicePackageUninstallRequest, dict):
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
        if not isinstance(other, DevicePackageUninstallRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other