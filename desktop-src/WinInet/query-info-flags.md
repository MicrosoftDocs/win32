---
title: Query Info Flags (Wininet.h)
description: The following lists contain the attributes and modifiers used by HttpQueryInfo and QueryInfo.
ms.assetid: b1613193-ae03-411e-bf05-de42f471cd8c
topic_type:
- apiref
api_name:
- HTTP_QUERY_ACCEPT
- HTTP_QUERY_ACCEPT_CHARSET
- HTTP_QUERY_ACCEPT_ENCODING
- HTTP_QUERY_ACCEPT_LANGUAGE
- HTTP_QUERY_ACCEPT_RANGES
- HTTP_QUERY_AGE
- HTTP_QUERY_ALLOW
- HTTP_QUERY_AUTHORIZATION
- HTTP_QUERY_CACHE_CONTROL
- HTTP_QUERY_CONNECTION
- HTTP_QUERY_CONTENT_BASE
- HTTP_QUERY_CONTENT_DESCRIPTION
- HTTP_QUERY_CONTENT_DISPOSITION
- HTTP_QUERY_CONTENT_ENCODING
- HTTP_QUERY_CONTENT_ID
- HTTP_QUERY_CONTENT_LANGUAGE
- HTTP_QUERY_CONTENT_LENGTH
- HTTP_QUERY_CONTENT_LOCATION
- HTTP_QUERY_CONTENT_MD5
- HTTP_QUERY_CONTENT_RANGE
- HTTP_QUERY_CONTENT_TRANSFER_ENCODING
- HTTP_QUERY_CONTENT_TYPE
- HTTP_QUERY_COOKIE
- HTTP_QUERY_COST
- HTTP_QUERY_CUSTOM
- HTTP_QUERY_DATE
- HTTP_QUERY_DERIVED_FROM
- HTTP_QUERY_ECHO_HEADERS
- HTTP_QUERY_ECHO_HEADERS_CRLF
- HTTP_QUERY_ECHO_REPLY
- HTTP_QUERY_ECHO_REQUEST
- HTTP_QUERY_ETAG
- HTTP_QUERY_EXPECT
- HTTP_QUERY_EXPIRES
- HTTP_QUERY_FORWARDED
- HTTP_QUERY_FROM
- HTTP_QUERY_HOST
- HTTP_QUERY_IF_MATCH
- HTTP_QUERY_IF_MODIFIED_SINCE
- HTTP_QUERY_IF_NONE_MATCH
- HTTP_QUERY_IF_RANGE
- HTTP_QUERY_IF_UNMODIFIED_SINCE
- HTTP_QUERY_LAST_MODIFIED
- HTTP_QUERY_LINK
- HTTP_QUERY_LOCATION
- HTTP_QUERY_MAX
- HTTP_QUERY_MAX_FORWARDS
- HTTP_QUERY_MESSAGE_ID
- HTTP_QUERY_MIME_VERSION
- HTTP_QUERY_ORIG_URI
- HTTP_QUERY_PRAGMA
- HTTP_QUERY_PROXY_AUTHENTICATE
- HTTP_QUERY_PROXY_AUTHORIZATION
- HTTP_QUERY_PROXY_CONNECTION
- HTTP_QUERY_PUBLIC
- HTTP_QUERY_RANGE
- HTTP_QUERY_RAW_HEADERS
- HTTP_QUERY_RAW_HEADERS_CRLF
- HTTP_QUERY_REFERER
- HTTP_QUERY_REFRESH
- HTTP_QUERY_REQUEST_METHOD
- HTTP_QUERY_RETRY_AFTER
- HTTP_QUERY_SERVER
- HTTP_QUERY_SET_COOKIE
- HTTP_QUERY_STATUS_CODE
- HTTP_QUERY_STATUS_TEXT
- HTTP_QUERY_TITLE
- HTTP_QUERY_TRANSFER_ENCODING
- HTTP_QUERY_UNLESS_MODIFIED_SINCE
- HTTP_QUERY_UPGRADE
- HTTP_QUERY_URI
- HTTP_QUERY_USER_AGENT
- HTTP_QUERY_VARY
- HTTP_QUERY_VERSION
- HTTP_QUERY_VIA
- HTTP_QUERY_WARNING
- HTTP_QUERY_WWW_AUTHENTICATE
- HTTP_QUERY_X_CONTENT_TYPE_OPTIONS
- HTTP_QUERY_P3P
- HTTP_QUERY_X_P2P_PEERDIST
- HTTP_QUERY_TRANSLATE
- HTTP_QUERY_X_UA_COMPATIBLE
- HTTP_QUERY_DEFAULT_STYLE
- HTTP_QUERY_X_FRAME_OPTIONS
- HTTP_QUERY_X_XSS_PROTECTION
- HTTP_QUERY_FLAG_COALESCE
- HTTP_QUERY_FLAG_NUMBER
- HTTP_QUERY_FLAG_REQUEST_HEADERS
- HTTP_QUERY_FLAG_SYSTEMTIME
api_location:
- Wininet.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Query Info Flags (Wininet.h)

The following lists contain the attributes and modifiers used by [**HttpQueryInfo**](/windows/desktop/api/Wininet/nf-wininet-httpqueryinfoa) and [**QueryInfo**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms774972(v=vs.85)).

The attribute flags are used by [**HttpQueryInfo**](/windows/desktop/api/Wininet/nf-wininet-httpqueryinfoa) (or [**QueryInfo**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms774972(v=vs.85))) to indicate what data to retrieve. Most of the attribute flags map directly to a specific HTTP header. There are also some special flags, such as [HTTP\_QUERY\_RAW\_HEADERS](/windows), that are not related to a specific header.

<dl> <dt>

<span id="HTTP_QUERY_ACCEPT"></span><span id="http_query_accept"></span>**HTTP\_QUERY\_ACCEPT**
</dt> <dd> <dl> <dt>

24
</dt> <dt>



Retrieves the acceptable media types for the response.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ACCEPT_CHARSET"></span><span id="http_query_accept_charset"></span>**HTTP\_QUERY\_ACCEPT\_CHARSET**
</dt> <dd> <dl> <dt>

25
</dt> <dt>



Retrieves the acceptable character sets for the response.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ACCEPT_ENCODING"></span><span id="http_query_accept_encoding"></span>**HTTP\_QUERY\_ACCEPT\_ENCODING**
</dt> <dd> <dl> <dt>

26
</dt> <dt>



Retrieves the acceptable content-coding values for the response.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ACCEPT_LANGUAGE"></span><span id="http_query_accept_language"></span>**HTTP\_QUERY\_ACCEPT\_LANGUAGE**
</dt> <dd> <dl> <dt>

27
</dt> <dt>



Retrieves the acceptable natural languages for the response.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ACCEPT_RANGES"></span><span id="http_query_accept_ranges"></span>**HTTP\_QUERY\_ACCEPT\_RANGES**
</dt> <dd> <dl> <dt>

42
</dt> <dt>



Retrieves the types of range requests that are accepted for a resource.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_AGE"></span><span id="http_query_age"></span>**HTTP\_QUERY\_AGE**
</dt> <dd> <dl> <dt>

48
</dt> <dt>



Retrieves the Age response-header field, which contains the sender's estimate of the amount of time since the response was generated at the origin server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ALLOW"></span><span id="http_query_allow"></span>**HTTP\_QUERY\_ALLOW**
</dt> <dd> <dl> <dt>

7
</dt> <dt>



Receives the HTTP verbs supported by the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_AUTHORIZATION"></span><span id="http_query_authorization"></span>**HTTP\_QUERY\_AUTHORIZATION**
</dt> <dd> <dl> <dt>

28
</dt> <dt>



Retrieves the authorization credentials used for a request.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CACHE_CONTROL"></span><span id="http_query_cache_control"></span>**HTTP\_QUERY\_CACHE\_CONTROL**
</dt> <dd> <dl> <dt>

49
</dt> <dt>



Retrieves the cache control directives.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONNECTION"></span><span id="http_query_connection"></span>**HTTP\_QUERY\_CONNECTION**
</dt> <dd> <dl> <dt>

23
</dt> <dt>



Retrieves any options that are specified for a particular connection and must not be communicated by proxies over further connections.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_BASE"></span><span id="http_query_content_base"></span>**HTTP\_QUERY\_CONTENT\_BASE**
</dt> <dd> <dl> <dt>

50
</dt> <dt>



Retrieves the base URI (Uniform Resource Identifier) for resolving relative URLs within the entity.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_DESCRIPTION"></span><span id="http_query_content_description"></span>**HTTP\_QUERY\_CONTENT\_DESCRIPTION**
</dt> <dd> <dl> <dt>

4
</dt> <dt>



Obsolete. Maintained for legacy application compatibility only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_DISPOSITION"></span><span id="http_query_content_disposition"></span>**HTTP\_QUERY\_CONTENT\_DISPOSITION**
</dt> <dd> <dl> <dt>

47
</dt> <dt>



Obsolete. Maintained for legacy application compatibility only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_ENCODING"></span><span id="http_query_content_encoding"></span>**HTTP\_QUERY\_CONTENT\_ENCODING**
</dt> <dd> <dl> <dt>

29
</dt> <dt>



Retrieves any additional content codings that have been applied to the entire resource.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_ID"></span><span id="http_query_content_id"></span>**HTTP\_QUERY\_CONTENT\_ID**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



Retrieves the content identification.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_LANGUAGE"></span><span id="http_query_content_language"></span>**HTTP\_QUERY\_CONTENT\_LANGUAGE**
</dt> <dd> <dl> <dt>

6
</dt> <dt>



Retrieves the language that the content is in.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_LENGTH"></span><span id="http_query_content_length"></span>**HTTP\_QUERY\_CONTENT\_LENGTH**
</dt> <dd> <dl> <dt>

5
</dt> <dt>



Retrieves the size of the resource, in bytes.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_LOCATION"></span><span id="http_query_content_location"></span>**HTTP\_QUERY\_CONTENT\_LOCATION**
</dt> <dd> <dl> <dt>

51
</dt> <dt>



Retrieves the resource location for the entity enclosed in the message.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_MD5"></span><span id="http_query_content_md5"></span>**HTTP\_QUERY\_CONTENT\_MD5**
</dt> <dd> <dl> <dt>

52
</dt> <dt>



Retrieves an MD5 digest of the entity-body for the purpose of providing an end-to-end message integrity check (MIC) for the entity-body. For more information, see RFC1864, The Content-MD5 Header Field, at [https://ftp.isi.edu/in-notes/rfc1864.txt](https://tools.ietf.org/html/rfc1864).


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_RANGE"></span><span id="http_query_content_range"></span>**HTTP\_QUERY\_CONTENT\_RANGE**
</dt> <dd> <dl> <dt>

53
</dt> <dt>



Retrieves the location in the full entity-body where the partial entity-body should be inserted and the total size of the full entity-body.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_TRANSFER_ENCODING"></span><span id="http_query_content_transfer_encoding"></span>**HTTP\_QUERY\_CONTENT\_TRANSFER\_ENCODING**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Receives the additional content coding that has been applied to the resource.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CONTENT_TYPE"></span><span id="http_query_content_type"></span>**HTTP\_QUERY\_CONTENT\_TYPE**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Receives the content type of the resource (such as text/html).


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_COOKIE"></span><span id="http_query_cookie"></span>**HTTP\_QUERY\_COOKIE**
</dt> <dd> <dl> <dt>

44
</dt> <dt>



Retrieves any cookies associated with the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_COST"></span><span id="http_query_cost"></span>**HTTP\_QUERY\_COST**
</dt> <dd> <dl> <dt>

15
</dt> <dt>



No longer supported.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_CUSTOM"></span><span id="http_query_custom"></span>**HTTP\_QUERY\_CUSTOM**
</dt> <dd> <dl> <dt>

65535
</dt> <dt>



Causes [**HttpQueryInfo**](/windows/desktop/api/Wininet/nf-wininet-httpqueryinfoa) to search for the header name specified in *lpvBuffer* and store the header data in *lpvBuffer*.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_DATE"></span><span id="http_query_date"></span>**HTTP\_QUERY\_DATE**
</dt> <dd> <dl> <dt>

9
</dt> <dt>



Receives the date and time at which the message was originated.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_DERIVED_FROM"></span><span id="http_query_derived_from"></span>**HTTP\_QUERY\_DERIVED\_FROM**
</dt> <dd> <dl> <dt>

14
</dt> <dt>



No longer supported.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ECHO_HEADERS"></span><span id="http_query_echo_headers"></span>**HTTP\_QUERY\_ECHO\_HEADERS**
</dt> <dd> <dl> <dt>

73
</dt> <dt>



Not currently implemented.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ECHO_HEADERS_CRLF"></span><span id="http_query_echo_headers_crlf"></span>**HTTP\_QUERY\_ECHO\_HEADERS\_CRLF**
</dt> <dd> <dl> <dt>

74
</dt> <dt>



Not currently implemented.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ECHO_REPLY"></span><span id="http_query_echo_reply"></span>**HTTP\_QUERY\_ECHO\_REPLY**
</dt> <dd> <dl> <dt>

72
</dt> <dt>



Not currently implemented.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ECHO_REQUEST"></span><span id="http_query_echo_request"></span>**HTTP\_QUERY\_ECHO\_REQUEST**
</dt> <dd> <dl> <dt>

71
</dt> <dt>



Not currently implemented.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ETAG"></span><span id="http_query_etag"></span>**HTTP\_QUERY\_ETAG**
</dt> <dd> <dl> <dt>

54
</dt> <dt>



Retrieves the entity tag for the associated entity.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_EXPECT"></span><span id="http_query_expect"></span>**HTTP\_QUERY\_EXPECT**
</dt> <dd> <dl> <dt>

68
</dt> <dt>



Retrieves the Expect header, which indicates whether the client application should expect 100 series responses.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_EXPIRES"></span><span id="http_query_expires"></span>**HTTP\_QUERY\_EXPIRES**
</dt> <dd> <dl> <dt>

10
</dt> <dt>



Receives the date and time after which the resource should be considered outdated.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_FORWARDED"></span><span id="http_query_forwarded"></span>**HTTP\_QUERY\_FORWARDED**
</dt> <dd> <dl> <dt>

30
</dt> <dt>



Obsolete. Maintained for legacy application compatibility only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_FROM"></span><span id="http_query_from"></span>**HTTP\_QUERY\_FROM**
</dt> <dd> <dl> <dt>

31
</dt> <dt>



Retrieves the email address for the human user who controls the requesting user agent if the From header is given.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_HOST"></span><span id="http_query_host"></span>**HTTP\_QUERY\_HOST**
</dt> <dd> <dl> <dt>

55
</dt> <dt>



Retrieves the Internet host and port number of the resource being requested.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_IF_MATCH"></span><span id="http_query_if_match"></span>**HTTP\_QUERY\_IF\_MATCH**
</dt> <dd> <dl> <dt>

56
</dt> <dt>



Retrieves the contents of the If-Match request-header field.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_IF_MODIFIED_SINCE"></span><span id="http_query_if_modified_since"></span>**HTTP\_QUERY\_IF\_MODIFIED\_SINCE**
</dt> <dd> <dl> <dt>

32
</dt> <dt>



Retrieves the contents of the If-Modified-Since header.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_IF_NONE_MATCH"></span><span id="http_query_if_none_match"></span>**HTTP\_QUERY\_IF\_NONE\_MATCH**
</dt> <dd> <dl> <dt>

57
</dt> <dt>



Retrieves the contents of the If-None-Match request-header field.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_IF_RANGE"></span><span id="http_query_if_range"></span>**HTTP\_QUERY\_IF\_RANGE**
</dt> <dd> <dl> <dt>

58
</dt> <dt>



Retrieves the contents of the If-Range request-header field. This header enables the client application to verify that the entity related to a partial copy of the entity in the client application cache has not been updated. If the entity has not been updated, send the parts that the client application is missing. If the entity has been updated, send the entire updated entity.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_IF_UNMODIFIED_SINCE"></span><span id="http_query_if_unmodified_since"></span>**HTTP\_QUERY\_IF\_UNMODIFIED\_SINCE**
</dt> <dd> <dl> <dt>

59
</dt> <dt>



Retrieves the contents of the If-Unmodified-Since request-header field.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_LAST_MODIFIED"></span><span id="http_query_last_modified"></span>**HTTP\_QUERY\_LAST\_MODIFIED**
</dt> <dd> <dl> <dt>

11
</dt> <dt>



Receives the date and time at which the server believes the resource was last modified.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_LINK"></span><span id="http_query_link"></span>**HTTP\_QUERY\_LINK**
</dt> <dd> <dl> <dt>

16
</dt> <dt>



Obsolete. Maintained for legacy application compatibility only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_LOCATION"></span><span id="http_query_location"></span>**HTTP\_QUERY\_LOCATION**
</dt> <dd> <dl> <dt>

33
</dt> <dt>



Retrieves the absolute Uniform Resource Identifier (URI) used in a Location response-header.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_MAX"></span><span id="http_query_max"></span>**HTTP\_QUERY\_MAX**
</dt> <dd> <dl> <dt>

78
</dt> <dt>



Not a query flag. Indicates the maximum value of an HTTP\_QUERY\_\* value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_MAX_FORWARDS"></span><span id="http_query_max_forwards"></span>**HTTP\_QUERY\_MAX\_FORWARDS**
</dt> <dd> <dl> <dt>

60
</dt> <dt>



Retrieves the number of proxies or gateways that can forward the request to the next inbound server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_MESSAGE_ID"></span><span id="http_query_message_id"></span>**HTTP\_QUERY\_MESSAGE\_ID**
</dt> <dd> <dl> <dt>

12
</dt> <dt>



No longer supported.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_MIME_VERSION"></span><span id="http_query_mime_version"></span>**HTTP\_QUERY\_MIME\_VERSION**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Receives the version of the MIME protocol that was used to construct the message.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_ORIG_URI"></span><span id="http_query_orig_uri"></span>**HTTP\_QUERY\_ORIG\_URI**
</dt> <dd> <dl> <dt>

34
</dt> <dt>



Obsolete. Maintained for legacy application compatibility only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_PRAGMA"></span><span id="http_query_pragma"></span>**HTTP\_QUERY\_PRAGMA**
</dt> <dd> <dl> <dt>

17
</dt> <dt>



Receives the implementation-specific directives that might apply to any recipient along the request/response chain.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_PROXY_AUTHENTICATE"></span><span id="http_query_proxy_authenticate"></span>**HTTP\_QUERY\_PROXY\_AUTHENTICATE**
</dt> <dd> <dl> <dt>

41
</dt> <dt>



Retrieves the authentication scheme and realm returned by the proxy.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_PROXY_AUTHORIZATION"></span><span id="http_query_proxy_authorization"></span>**HTTP\_QUERY\_PROXY\_AUTHORIZATION**
</dt> <dd> <dl> <dt>

61
</dt> <dt>



Retrieves the header that is used to identify the user to a proxy that requires authentication. This header can only be retrieved before the request is sent to the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_PROXY_CONNECTION"></span><span id="http_query_proxy_connection"></span>**HTTP\_QUERY\_PROXY\_CONNECTION**
</dt> <dd> <dl> <dt>

69
</dt> <dt>



Retrieves the Proxy-Connection header.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_PUBLIC"></span><span id="http_query_public"></span>**HTTP\_QUERY\_PUBLIC**
</dt> <dd> <dl> <dt>

8
</dt> <dt>



Receives methods available at this server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_RANGE"></span><span id="http_query_range"></span>**HTTP\_QUERY\_RANGE**
</dt> <dd> <dl> <dt>

62
</dt> <dt>



Retrieves the byte range of an entity.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_RAW_HEADERS"></span><span id="http_query_raw_headers"></span>**HTTP\_QUERY\_RAW\_HEADERS**
</dt> <dd> <dl> <dt>

21
</dt> <dt>



Receives all the headers returned by the server. Each header is terminated by "\\0". An additional "\\0" terminates the list of headers.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_RAW_HEADERS_CRLF"></span><span id="http_query_raw_headers_crlf"></span>**HTTP\_QUERY\_RAW\_HEADERS\_CRLF**
</dt> <dd> <dl> <dt>

22
</dt> <dt>



Receives all the headers returned by the server. Each header is separated by a carriage return/line feed (CR/LF) sequence.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_REFERER"></span><span id="http_query_referer"></span>**HTTP\_QUERY\_REFERER**
</dt> <dd> <dl> <dt>

35
</dt> <dt>



Receives the Uniform Resource Identifier (URI) of the resource where the requested URI was obtained.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_REFRESH"></span><span id="http_query_refresh"></span>**HTTP\_QUERY\_REFRESH**
</dt> <dd> <dl> <dt>

46
</dt> <dt>



Obsolete. Maintained for legacy application compatibility only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_REQUEST_METHOD"></span><span id="http_query_request_method"></span>**HTTP\_QUERY\_REQUEST\_METHOD**
</dt> <dd> <dl> <dt>

45
</dt> <dt>



Receives the HTTP verb that is being used in the request, typically GET or POST.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_RETRY_AFTER"></span><span id="http_query_retry_after"></span>**HTTP\_QUERY\_RETRY\_AFTER**
</dt> <dd> <dl> <dt>

36
</dt> <dt>



Retrieves the amount of time the service is expected to be unavailable.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_SERVER"></span><span id="http_query_server"></span>**HTTP\_QUERY\_SERVER**
</dt> <dd> <dl> <dt>

37
</dt> <dt>



Retrieves data about the software used by the origin server to handle the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_SET_COOKIE"></span><span id="http_query_set_cookie"></span>**HTTP\_QUERY\_SET\_COOKIE**
</dt> <dd> <dl> <dt>

43
</dt> <dt>



Receives the value of the cookie set for the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_STATUS_CODE"></span><span id="http_query_status_code"></span>**HTTP\_QUERY\_STATUS\_CODE**
</dt> <dd> <dl> <dt>

19
</dt> <dt>



Receives the status code returned by the server. For more information and a list of possible values, see [**HTTP Status Codes**](http-status-codes.md).


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_STATUS_TEXT"></span><span id="http_query_status_text"></span>**HTTP\_QUERY\_STATUS\_TEXT**
</dt> <dd> <dl> <dt>

20
</dt> <dt>



Receives any additional text returned by the server on the response line.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_TITLE"></span><span id="http_query_title"></span>**HTTP\_QUERY\_TITLE**
</dt> <dd> <dl> <dt>

38
</dt> <dt>



Obsolete. Maintained for legacy application compatibility only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_TRANSFER_ENCODING"></span><span id="http_query_transfer_encoding"></span>**HTTP\_QUERY\_TRANSFER\_ENCODING**
</dt> <dd> <dl> <dt>

63
</dt> <dt>



Retrieves the type of transformation that has been applied to the message body so it can be safely transferred between the sender and recipient.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_UNLESS_MODIFIED_SINCE"></span><span id="http_query_unless_modified_since"></span>**HTTP\_QUERY\_UNLESS\_MODIFIED\_SINCE**
</dt> <dd> <dl> <dt>

70
</dt> <dt>



Retrieves the Unless-Modified-Since header.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_UPGRADE"></span><span id="http_query_upgrade"></span>**HTTP\_QUERY\_UPGRADE**
</dt> <dd> <dl> <dt>

64
</dt> <dt>



Retrieves the additional communication protocols that are supported by the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_URI"></span><span id="http_query_uri"></span>**HTTP\_QUERY\_URI**
</dt> <dd> <dl> <dt>

13
</dt> <dt>



Receives some or all of the Uniform Resource Identifiers (URIs) by which the Request-URI resource can be identified.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_USER_AGENT"></span><span id="http_query_user_agent"></span>**HTTP\_QUERY\_USER\_AGENT**
</dt> <dd> <dl> <dt>

39
</dt> <dt>



Retrieves data about the user agent that made the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_VARY"></span><span id="http_query_vary"></span>**HTTP\_QUERY\_VARY**
</dt> <dd> <dl> <dt>

65
</dt> <dt>



Retrieves the header that indicates that the entity was selected from a number of available representations of the response using server-driven negotiation.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_VERSION"></span><span id="http_query_version"></span>**HTTP\_QUERY\_VERSION**
</dt> <dd> <dl> <dt>

18
</dt> <dt>



Receives the last response code returned by the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_VIA"></span><span id="http_query_via"></span>**HTTP\_QUERY\_VIA**
</dt> <dd> <dl> <dt>

66
</dt> <dt>



Retrieves the intermediate protocols and recipients between the user agent and the server on requests, and between the origin server and the client on responses.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_WARNING"></span><span id="http_query_warning"></span>**HTTP\_QUERY\_WARNING**
</dt> <dd> <dl> <dt>

67
</dt> <dt>



Retrieves additional data about the status of a response that might not be reflected by the response status code.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_WWW_AUTHENTICATE"></span><span id="http_query_www_authenticate"></span>**HTTP\_QUERY\_WWW\_AUTHENTICATE**
</dt> <dd> <dl> <dt>

40
</dt> <dt>



Retrieves the authentication scheme and realm returned by the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_X_CONTENT_TYPE_OPTIONS"></span><span id="http_query_x_content_type_options"></span>**HTTP\_QUERY\_X\_CONTENT\_TYPE\_OPTIONS**
</dt> <dd> <dl> <dt>

79
</dt> <dt>



Retrieves the X-Content-Type-Options header value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_P3P"></span><span id="http_query_p3p"></span>**HTTP\_QUERY\_P3P**
</dt> <dd> <dl> <dt>

80
</dt> <dt>



Retrieves the P3P header value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_X_P2P_PEERDIST"></span><span id="http_query_x_p2p_peerdist"></span>**HTTP\_QUERY\_X\_P2P\_PEERDIST**
</dt> <dd> <dl> <dt>

81
</dt> <dt>



Retrieves the X-P2P-PeerDist header value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_TRANSLATE"></span><span id="http_query_translate"></span>**HTTP\_QUERY\_TRANSLATE**
</dt> <dd> <dl> <dt>

82
</dt> <dt>



Retrieves the translate header value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_X_UA_COMPATIBLE"></span><span id="http_query_x_ua_compatible"></span>**HTTP\_QUERY\_X\_UA\_COMPATIBLE**
</dt> <dd> <dl> <dt>

83
</dt> <dt>



Retrieves the X-UA-Compatible header value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_DEFAULT_STYLE"></span><span id="http_query_default_style"></span>**HTTP\_QUERY\_DEFAULT\_STYLE**
</dt> <dd> <dl> <dt>

84
</dt> <dt>



Retrieves the Default-Style header value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_X_FRAME_OPTIONS"></span><span id="http_query_x_frame_options"></span>**HTTP\_QUERY\_X\_FRAME\_OPTIONS**
</dt> <dd> <dl> <dt>

85
</dt> <dt>



Retrieves the X-Frame-Options header value.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_X_XSS_PROTECTION"></span><span id="http_query_x_xss_protection"></span>**HTTP\_QUERY\_X\_XSS\_PROTECTION**
</dt> <dd> <dl> <dt>

86
</dt> <dt>



Retrieves the X-XSS-Protection header value.


</dt> </dl> </dd> </dl>

The modifier flags are used in conjunction with an attribute flag to modify the request. Modifier flags either modify the format of the data returned or indicate where [**HttpQueryInfo**](/windows/desktop/api/Wininet/nf-wininet-httpqueryinfoa) (or [**QueryInfo**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms774972(v=vs.85))) should search for the data.

<dl> <dt>

<span id="HTTP_QUERY_FLAG_COALESCE"></span><span id="http_query_flag_coalesce"></span>**HTTP\_QUERY\_FLAG\_COALESCE**
</dt> <dd> <dl> <dt>

0x10000000
</dt> <dt>



Not implemented.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_FLAG_NUMBER"></span><span id="http_query_flag_number"></span>**HTTP\_QUERY\_FLAG\_NUMBER**
</dt> <dd> <dl> <dt>

0x20000000
</dt> <dt>



Returns the data as a 32-bit number for headers whose value is a number, such as the status code.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_FLAG_REQUEST_HEADERS"></span><span id="http_query_flag_request_headers"></span>**HTTP\_QUERY\_FLAG\_REQUEST\_HEADERS**
</dt> <dd> <dl> <dt>

0x80000000
</dt> <dt>



Queries request headers only.


</dt> </dl> </dd> <dt>

<span id="HTTP_QUERY_FLAG_SYSTEMTIME"></span><span id="http_query_flag_systemtime"></span>**HTTP\_QUERY\_FLAG\_SYSTEMTIME**
</dt> <dd> <dl> <dt>

0x40000000
</dt> <dt>



Returns the header value as a [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure, which does not require the application to parse the data. Use for headers whose value is a date/time string, such as "Last-Modified-Time".


</dt> </dl> </dd> </dl>

## Remarks

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wininet.h</dt> </dl> |



 

