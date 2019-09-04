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

from swagger_client.models.kapua_position import KapuaPosition  # noqa: F401,E501


class DeviceEvent(object):
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
        'position': 'KapuaPosition',
        'response_code': 'str',
        'resource': 'str',
        'action': 'str',
        'device_id': 'str',
        'received_on': 'datetime',
        'sent_on': 'datetime',
        'event_message': 'str',
        'type': 'str',
        'scope_id': 'str',
        'id': 'str',
        'created_on': 'datetime',
        'created_by': 'str'
    }

    attribute_map = {
        'position': 'position',
        'response_code': 'responseCode',
        'resource': 'resource',
        'action': 'action',
        'device_id': 'deviceId',
        'received_on': 'receivedOn',
        'sent_on': 'sentOn',
        'event_message': 'eventMessage',
        'type': 'type',
        'scope_id': 'scopeId',
        'id': 'id',
        'created_on': 'createdOn',
        'created_by': 'createdBy'
    }

    def __init__(self, position=None, response_code=None, resource=None, action=None, device_id=None, received_on=None, sent_on=None, event_message=None, type=None, scope_id=None, id=None, created_on=None, created_by=None):  # noqa: E501
        """DeviceEvent - a model defined in Swagger"""  # noqa: E501

        self._position = None
        self._response_code = None
        self._resource = None
        self._action = None
        self._device_id = None
        self._received_on = None
        self._sent_on = None
        self._event_message = None
        self._type = None
        self._scope_id = None
        self._id = None
        self._created_on = None
        self._created_by = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if response_code is not None:
            self.response_code = response_code
        if resource is not None:
            self.resource = resource
        if action is not None:
            self.action = action
        if device_id is not None:
            self.device_id = device_id
        if received_on is not None:
            self.received_on = received_on
        if sent_on is not None:
            self.sent_on = sent_on
        if event_message is not None:
            self.event_message = event_message
        if type is not None:
            self.type = type
        if scope_id is not None:
            self.scope_id = scope_id
        if id is not None:
            self.id = id
        if created_on is not None:
            self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by

    @property
    def position(self):
        """Gets the position of this DeviceEvent.  # noqa: E501


        :return: The position of this DeviceEvent.  # noqa: E501
        :rtype: KapuaPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DeviceEvent.


        :param position: The position of this DeviceEvent.  # noqa: E501
        :type: KapuaPosition
        """

        self._position = position

    @property
    def response_code(self):
        """Gets the response_code of this DeviceEvent.  # noqa: E501


        :return: The response_code of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this DeviceEvent.


        :param response_code: The response_code of this DeviceEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCEPTED", "BAD_REQUEST", "NOT_FOUND", "INTERNAL_ERROR"]  # noqa: E501
        if response_code not in allowed_values:
            raise ValueError(
                "Invalid value for `response_code` ({0}), must be one of {1}"  # noqa: E501
                .format(response_code, allowed_values)
            )

        self._response_code = response_code

    @property
    def resource(self):
        """Gets the resource of this DeviceEvent.  # noqa: E501


        :return: The resource of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this DeviceEvent.


        :param resource: The resource of this DeviceEvent.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def action(self):
        """Gets the action of this DeviceEvent.  # noqa: E501


        :return: The action of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DeviceEvent.


        :param action: The action of this DeviceEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["READ", "CREATE", "WRITE", "DELETE", "OPTIONS", "EXECUTE"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def device_id(self):
        """Gets the device_id of this DeviceEvent.  # noqa: E501


        :return: The device_id of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceEvent.


        :param device_id: The device_id of this DeviceEvent.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def received_on(self):
        """Gets the received_on of this DeviceEvent.  # noqa: E501


        :return: The received_on of this DeviceEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._received_on

    @received_on.setter
    def received_on(self, received_on):
        """Sets the received_on of this DeviceEvent.


        :param received_on: The received_on of this DeviceEvent.  # noqa: E501
        :type: datetime
        """

        self._received_on = received_on

    @property
    def sent_on(self):
        """Gets the sent_on of this DeviceEvent.  # noqa: E501


        :return: The sent_on of this DeviceEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._sent_on

    @sent_on.setter
    def sent_on(self, sent_on):
        """Sets the sent_on of this DeviceEvent.


        :param sent_on: The sent_on of this DeviceEvent.  # noqa: E501
        :type: datetime
        """

        self._sent_on = sent_on

    @property
    def event_message(self):
        """Gets the event_message of this DeviceEvent.  # noqa: E501


        :return: The event_message of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_message

    @event_message.setter
    def event_message(self, event_message):
        """Sets the event_message of this DeviceEvent.


        :param event_message: The event_message of this DeviceEvent.  # noqa: E501
        :type: str
        """

        self._event_message = event_message

    @property
    def type(self):
        """Gets the type of this DeviceEvent.  # noqa: E501


        :return: The type of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceEvent.


        :param type: The type of this DeviceEvent.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def scope_id(self):
        """Gets the scope_id of this DeviceEvent.  # noqa: E501


        :return: The scope_id of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this DeviceEvent.


        :param scope_id: The scope_id of this DeviceEvent.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def id(self):
        """Gets the id of this DeviceEvent.  # noqa: E501


        :return: The id of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceEvent.


        :param id: The id of this DeviceEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this DeviceEvent.  # noqa: E501


        :return: The created_on of this DeviceEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceEvent.


        :param created_on: The created_on of this DeviceEvent.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this DeviceEvent.  # noqa: E501


        :return: The created_by of this DeviceEvent.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DeviceEvent.


        :param created_by: The created_by of this DeviceEvent.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
        if issubclass(DeviceEvent, dict):
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
        if not isinstance(other, DeviceEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
