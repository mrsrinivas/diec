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

from swagger_client.models.kapua_data_channel import KapuaDataChannel  # noqa: F401,E501
from swagger_client.models.kapua_id import KapuaId  # noqa: F401,E501
from swagger_client.models.kapua_payload import KapuaPayload  # noqa: F401,E501
from swagger_client.models.kapua_position import KapuaPosition  # noqa: F401,E501
from swagger_client.models.storable_id import StorableId  # noqa: F401,E501


class DatastoreMessage(object):
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
        'scope_id': 'str',
        'timestamp': 'datetime',
        'id': 'str',
        'payload': 'KapuaPayload',
        'client_id': 'str',
        'device_id': 'KapuaId',
        'received_on': 'datetime',
        'sent_on': 'datetime',
        'captured_on': 'datetime',
        'channel': 'KapuaDataChannel',
        'datastore_id': 'StorableId'
    }

    attribute_map = {
        'position': 'position',
        'scope_id': 'scopeId',
        'timestamp': 'timestamp',
        'id': 'id',
        'payload': 'payload',
        'client_id': 'clientId',
        'device_id': 'deviceId',
        'received_on': 'receivedOn',
        'sent_on': 'sentOn',
        'captured_on': 'capturedOn',
        'channel': 'channel',
        'datastore_id': 'datastoreId'
    }

    def __init__(self, position=None, scope_id=None, timestamp=None, id=None, payload=None, client_id=None, device_id=None, received_on=None, sent_on=None, captured_on=None, channel=None, datastore_id=None):  # noqa: E501
        """DatastoreMessage - a model defined in Swagger"""  # noqa: E501

        self._position = None
        self._scope_id = None
        self._timestamp = None
        self._id = None
        self._payload = None
        self._client_id = None
        self._device_id = None
        self._received_on = None
        self._sent_on = None
        self._captured_on = None
        self._channel = None
        self._datastore_id = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if scope_id is not None:
            self.scope_id = scope_id
        if timestamp is not None:
            self.timestamp = timestamp
        if id is not None:
            self.id = id
        if payload is not None:
            self.payload = payload
        if client_id is not None:
            self.client_id = client_id
        if device_id is not None:
            self.device_id = device_id
        if received_on is not None:
            self.received_on = received_on
        if sent_on is not None:
            self.sent_on = sent_on
        if captured_on is not None:
            self.captured_on = captured_on
        if channel is not None:
            self.channel = channel
        if datastore_id is not None:
            self.datastore_id = datastore_id

    @property
    def position(self):
        """Gets the position of this DatastoreMessage.  # noqa: E501


        :return: The position of this DatastoreMessage.  # noqa: E501
        :rtype: KapuaPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DatastoreMessage.


        :param position: The position of this DatastoreMessage.  # noqa: E501
        :type: KapuaPosition
        """

        self._position = position

    @property
    def scope_id(self):
        """Gets the scope_id of this DatastoreMessage.  # noqa: E501


        :return: The scope_id of this DatastoreMessage.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this DatastoreMessage.


        :param scope_id: The scope_id of this DatastoreMessage.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def timestamp(self):
        """Gets the timestamp of this DatastoreMessage.  # noqa: E501


        :return: The timestamp of this DatastoreMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DatastoreMessage.


        :param timestamp: The timestamp of this DatastoreMessage.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this DatastoreMessage.  # noqa: E501


        :return: The id of this DatastoreMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatastoreMessage.


        :param id: The id of this DatastoreMessage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def payload(self):
        """Gets the payload of this DatastoreMessage.  # noqa: E501


        :return: The payload of this DatastoreMessage.  # noqa: E501
        :rtype: KapuaPayload
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this DatastoreMessage.


        :param payload: The payload of this DatastoreMessage.  # noqa: E501
        :type: KapuaPayload
        """

        self._payload = payload

    @property
    def client_id(self):
        """Gets the client_id of this DatastoreMessage.  # noqa: E501


        :return: The client_id of this DatastoreMessage.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this DatastoreMessage.


        :param client_id: The client_id of this DatastoreMessage.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def device_id(self):
        """Gets the device_id of this DatastoreMessage.  # noqa: E501


        :return: The device_id of this DatastoreMessage.  # noqa: E501
        :rtype: KapuaId
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DatastoreMessage.


        :param device_id: The device_id of this DatastoreMessage.  # noqa: E501
        :type: KapuaId
        """

        self._device_id = device_id

    @property
    def received_on(self):
        """Gets the received_on of this DatastoreMessage.  # noqa: E501


        :return: The received_on of this DatastoreMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._received_on

    @received_on.setter
    def received_on(self, received_on):
        """Sets the received_on of this DatastoreMessage.


        :param received_on: The received_on of this DatastoreMessage.  # noqa: E501
        :type: datetime
        """

        self._received_on = received_on

    @property
    def sent_on(self):
        """Gets the sent_on of this DatastoreMessage.  # noqa: E501


        :return: The sent_on of this DatastoreMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._sent_on

    @sent_on.setter
    def sent_on(self, sent_on):
        """Sets the sent_on of this DatastoreMessage.


        :param sent_on: The sent_on of this DatastoreMessage.  # noqa: E501
        :type: datetime
        """

        self._sent_on = sent_on

    @property
    def captured_on(self):
        """Gets the captured_on of this DatastoreMessage.  # noqa: E501


        :return: The captured_on of this DatastoreMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._captured_on

    @captured_on.setter
    def captured_on(self, captured_on):
        """Sets the captured_on of this DatastoreMessage.


        :param captured_on: The captured_on of this DatastoreMessage.  # noqa: E501
        :type: datetime
        """

        self._captured_on = captured_on

    @property
    def channel(self):
        """Gets the channel of this DatastoreMessage.  # noqa: E501


        :return: The channel of this DatastoreMessage.  # noqa: E501
        :rtype: KapuaDataChannel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this DatastoreMessage.


        :param channel: The channel of this DatastoreMessage.  # noqa: E501
        :type: KapuaDataChannel
        """

        self._channel = channel

    @property
    def datastore_id(self):
        """Gets the datastore_id of this DatastoreMessage.  # noqa: E501


        :return: The datastore_id of this DatastoreMessage.  # noqa: E501
        :rtype: StorableId
        """
        return self._datastore_id

    @datastore_id.setter
    def datastore_id(self, datastore_id):
        """Sets the datastore_id of this DatastoreMessage.


        :param datastore_id: The datastore_id of this DatastoreMessage.  # noqa: E501
        :type: StorableId
        """

        self._datastore_id = datastore_id

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
        if issubclass(DatastoreMessage, dict):
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
        if not isinstance(other, DatastoreMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
