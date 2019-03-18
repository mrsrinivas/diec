# coding: utf-8

"""
    Eclipse Kapua REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DomainsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def domain_count(self, scope_id, body, **kwargs):  # noqa: E501
        """Counts the Domains  # noqa: E501

        Counts the Domains with the given DomainQuery parameter returning the number of matching Domains  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_count(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to count results (required)
        :param DomainQuery body: The DomainQuery to use to filter count results (required)
        :return: CountResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_count_with_http_info(scope_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_count_with_http_info(scope_id, body, **kwargs)  # noqa: E501
            return data

    def domain_count_with_http_info(self, scope_id, body, **kwargs):  # noqa: E501
        """Counts the Domains  # noqa: E501

        Counts the Domains with the given DomainQuery parameter returning the number of matching Domains  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_count_with_http_info(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to count results (required)
        :param DomainQuery body: The DomainQuery to use to filter count results (required)
        :return: CountResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `domain_count`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `domain_count`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/domains/_count', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_find(self, scope_id, domain_id, **kwargs):  # noqa: E501
        """Get a Domain  # noqa: E501

        Returns the Domain specified by the \"domainId\" path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_find(scope_id, domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId of the requested Domain. (required)
        :param str domain_id: The id of the requested Domain (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_find_with_http_info(scope_id, domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_find_with_http_info(scope_id, domain_id, **kwargs)  # noqa: E501
            return data

    def domain_find_with_http_info(self, scope_id, domain_id, **kwargs):  # noqa: E501
        """Get a Domain  # noqa: E501

        Returns the Domain specified by the \"domainId\" path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_find_with_http_info(scope_id, domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId of the requested Domain. (required)
        :param str domain_id: The id of the requested Domain (required)
        :return: Domain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_find" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `domain_find`")  # noqa: E501
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `domain_find`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/domains/{domainId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Domain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_query(self, scope_id, body, **kwargs):  # noqa: E501
        """Queries the Domains  # noqa: E501

        Queries the Domains with the given DomainQuery parameter returning all matching Domains  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_query(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param DomainQuery body: The DomainQuery to use to filter results. (required)
        :return: DomainListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_query_with_http_info(scope_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_query_with_http_info(scope_id, body, **kwargs)  # noqa: E501
            return data

    def domain_query_with_http_info(self, scope_id, body, **kwargs):  # noqa: E501
        """Queries the Domains  # noqa: E501

        Queries the Domains with the given DomainQuery parameter returning all matching Domains  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_query_with_http_info(scope_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param DomainQuery body: The DomainQuery to use to filter results. (required)
        :return: DomainListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `domain_query`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `domain_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/domains/_query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_simple_query(self, scope_id, **kwargs):  # noqa: E501
        """Gets the Domain list in the scope  # noqa: E501

        Returns the list of all the domains associated to the current selected scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_simple_query(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str name: The domain name to filter results.
        :param int offset: The result set offset.
        :param int limit: The result set limit.
        :return: DomainListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_simple_query_with_http_info(scope_id, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_simple_query_with_http_info(scope_id, **kwargs)  # noqa: E501
            return data

    def domain_simple_query_with_http_info(self, scope_id, **kwargs):  # noqa: E501
        """Gets the Domain list in the scope  # noqa: E501

        Returns the list of all the domains associated to the current selected scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_simple_query_with_http_info(scope_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope_id: The ScopeId in which to search results. (required)
        :param str name: The domain name to filter results.
        :param int offset: The result set offset.
        :param int limit: The result set limit.
        :return: DomainListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope_id', 'name', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_simple_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scope_id' is set
        if ('scope_id' not in params or
                params['scope_id'] is None):
            raise ValueError("Missing the required parameter `scope_id` when calling `domain_simple_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope_id' in params:
            path_params['scopeId'] = params['scope_id']  # noqa: E501

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['kapuaAccessToken']  # noqa: E501

        return self.api_client.call_api(
            '/{scopeId}/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)