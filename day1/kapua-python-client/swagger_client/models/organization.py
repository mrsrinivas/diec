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


class Organization(object):
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
        'country': 'str',
        'person_name': 'str',
        'email': 'str',
        'phone_number': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'zip_post_code': 'str',
        'city': 'str',
        'state_province_county': 'str',
        'name': 'str'
    }

    attribute_map = {
        'country': 'country',
        'person_name': 'personName',
        'email': 'email',
        'phone_number': 'phoneNumber',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'zip_post_code': 'zipPostCode',
        'city': 'city',
        'state_province_county': 'stateProvinceCounty',
        'name': 'name'
    }

    def __init__(self, country=None, person_name=None, email=None, phone_number=None, address_line1=None, address_line2=None, zip_post_code=None, city=None, state_province_county=None, name=None):  # noqa: E501
        """Organization - a model defined in Swagger"""  # noqa: E501

        self._country = None
        self._person_name = None
        self._email = None
        self._phone_number = None
        self._address_line1 = None
        self._address_line2 = None
        self._zip_post_code = None
        self._city = None
        self._state_province_county = None
        self._name = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if person_name is not None:
            self.person_name = person_name
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if zip_post_code is not None:
            self.zip_post_code = zip_post_code
        if city is not None:
            self.city = city
        if state_province_county is not None:
            self.state_province_county = state_province_county
        if name is not None:
            self.name = name

    @property
    def country(self):
        """Gets the country of this Organization.  # noqa: E501


        :return: The country of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Organization.


        :param country: The country of this Organization.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def person_name(self):
        """Gets the person_name of this Organization.  # noqa: E501


        :return: The person_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._person_name

    @person_name.setter
    def person_name(self, person_name):
        """Sets the person_name of this Organization.


        :param person_name: The person_name of this Organization.  # noqa: E501
        :type: str
        """

        self._person_name = person_name

    @property
    def email(self):
        """Gets the email of this Organization.  # noqa: E501


        :return: The email of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Organization.


        :param email: The email of this Organization.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """Gets the phone_number of this Organization.  # noqa: E501


        :return: The phone_number of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Organization.


        :param phone_number: The phone_number of this Organization.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def address_line1(self):
        """Gets the address_line1 of this Organization.  # noqa: E501


        :return: The address_line1 of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Organization.


        :param address_line1: The address_line1 of this Organization.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Organization.  # noqa: E501


        :return: The address_line2 of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Organization.


        :param address_line2: The address_line2 of this Organization.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def zip_post_code(self):
        """Gets the zip_post_code of this Organization.  # noqa: E501


        :return: The zip_post_code of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._zip_post_code

    @zip_post_code.setter
    def zip_post_code(self, zip_post_code):
        """Sets the zip_post_code of this Organization.


        :param zip_post_code: The zip_post_code of this Organization.  # noqa: E501
        :type: str
        """

        self._zip_post_code = zip_post_code

    @property
    def city(self):
        """Gets the city of this Organization.  # noqa: E501


        :return: The city of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Organization.


        :param city: The city of this Organization.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_province_county(self):
        """Gets the state_province_county of this Organization.  # noqa: E501


        :return: The state_province_county of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._state_province_county

    @state_province_county.setter
    def state_province_county(self, state_province_county):
        """Sets the state_province_county of this Organization.


        :param state_province_county: The state_province_county of this Organization.  # noqa: E501
        :type: str
        """

        self._state_province_county = state_province_county

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501


        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.  # noqa: E501
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
        if issubclass(Organization, dict):
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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other