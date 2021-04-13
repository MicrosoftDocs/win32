---
description: These attributes and modifiers are used by WinHttpQueryHeaders.
ms.assetid: c26dac1d-9a75-440a-a0ef-a2029f138f3b
title: Query Info Flags (Winhttp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Query Info Flags (Winhttp.h)

These attributes and modifiers are used by [**WinHttpQueryHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryheaders).

The attribute flags are used by [**WinHttpQueryHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryheaders) to indicate what information to retrieve. Most of the attribute flags map directly to a specific HTTP header. There are also some special flags, such as WINHTTP\_QUERY\_RAW\_HEADERS, that are not related to a specific header.

<dl> <dt>

<span id="WINHTTP_QUERY_ACCEPT"></span><span id="winhttp_query_accept"></span>**WINHTTP\_QUERY\_ACCEPT**
</dt> <dd> <dl> <dt>



Retrieves the acceptable media types for the response.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_ACCEPT_CHARSET"></span><span id="winhttp_query_accept_charset"></span>**WINHTTP\_QUERY\_ACCEPT\_CHARSET**
</dt> <dd> <dl> <dt>



Retrieves the acceptable character sets for the response.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_ACCEPT_ENCODING"></span><span id="winhttp_query_accept_encoding"></span>**WINHTTP\_QUERY\_ACCEPT\_ENCODING**
</dt> <dd> <dl> <dt>



Retrieves the acceptable content-coding values for the response.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_ACCEPT_LANGUAGE"></span><span id="winhttp_query_accept_language"></span>**WINHTTP\_QUERY\_ACCEPT\_LANGUAGE**
</dt> <dd> <dl> <dt>



Retrieves the acceptable natural languages for the response.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_ACCEPT_RANGES"></span><span id="winhttp_query_accept_ranges"></span>**WINHTTP\_QUERY\_ACCEPT\_RANGES**
</dt> <dd> <dl> <dt>



Retrieves the types of range requests that are accepted for a resource.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_AGE"></span><span id="winhttp_query_age"></span>**WINHTTP\_QUERY\_AGE**
</dt> <dd> <dl> <dt>



Retrieves the Age response-header field, which contains the sender's estimate of the amount of time since the response was generated at the originating server.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_ALLOW"></span><span id="winhttp_query_allow"></span>**WINHTTP\_QUERY\_ALLOW**
</dt> <dd> <dl> <dt>



Receives the [*HTTP verbs*](glossary.md) supported by the server.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_AUTHENTICATION_INFO"></span><span id="winhttp_query_authentication_info"></span>**WINHTTP\_QUERY\_AUTHENTICATION\_INFO**
</dt> <dd> <dl> <dt>



Retrieves the Authentication-Info header.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_AUTHORIZATION"></span><span id="winhttp_query_authorization"></span>**WINHTTP\_QUERY\_AUTHORIZATION**
</dt> <dd> <dl> <dt>



Retrieves the authorization credentials used for a request.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CACHE_CONTROL"></span><span id="winhttp_query_cache_control"></span>**WINHTTP\_QUERY\_CACHE\_CONTROL**
</dt> <dd> <dl> <dt>



Retrieves the cache control directives.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONNECTION"></span><span id="winhttp_query_connection"></span>**WINHTTP\_QUERY\_CONNECTION**
</dt> <dd> <dl> <dt>



Retrieves any options that are specified for a particular connection and must not be communicated by proxies over further connections.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_BASE"></span><span id="winhttp_query_content_base"></span>**WINHTTP\_QUERY\_CONTENT\_BASE**
</dt> <dd> <dl> <dt>



Retrieves the base Uniform Resource Identifier (URI) to resolve relative URLs within the entity.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_DESCRIPTION"></span><span id="winhttp_query_content_description"></span>**WINHTTP\_QUERY\_CONTENT\_DESCRIPTION**
</dt> <dd> <dl> <dt>



Obsolete. Maintained for legacy application compatibility.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_DISPOSITION"></span><span id="winhttp_query_content_disposition"></span>**WINHTTP\_QUERY\_CONTENT\_DISPOSITION**
</dt> <dd> <dl> <dt>



Obsolete. Maintained for legacy application compatibility.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_ENCODING"></span><span id="winhttp_query_content_encoding"></span>**WINHTTP\_QUERY\_CONTENT\_ENCODING**
</dt> <dd> <dl> <dt>



Retrieves additional content coding that has been applied to the entire resource.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_ID"></span><span id="winhttp_query_content_id"></span>**WINHTTP\_QUERY\_CONTENT\_ID**
</dt> <dd> <dl> <dt>



Retrieves the content identification.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_LANGUAGE"></span><span id="winhttp_query_content_language"></span>**WINHTTP\_QUERY\_CONTENT\_LANGUAGE**
</dt> <dd> <dl> <dt>



Retrieves the language that the content is written in.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_LENGTH"></span><span id="winhttp_query_content_length"></span>**WINHTTP\_QUERY\_CONTENT\_LENGTH**
</dt> <dd> <dl> <dt>



Retrieves the size of the resource, in bytes.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_LOCATION"></span><span id="winhttp_query_content_location"></span>**WINHTTP\_QUERY\_CONTENT\_LOCATION**
</dt> <dd> <dl> <dt>



Retrieves the resource location for the entity enclosed in the message.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_MD5"></span><span id="winhttp_query_content_md5"></span>**WINHTTP\_QUERY\_CONTENT\_MD5**
</dt> <dd> <dl> <dt>



Retrieves an MD5 digest of the entity body for the purpose of providing an end-to-end message integrity check for the entity body. For more information, see [RFC 1864](https://www.ietf.org/rfc/rfc1864.txt).


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_RANGE"></span><span id="winhttp_query_content_range"></span>**WINHTTP\_QUERY\_CONTENT\_RANGE**
</dt> <dd> <dl> <dt>



Retrieves the location in the full entity body where the partial entity body should be inserted and the total size of the full entity body.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_TRANSFER_ENCODING"></span><span id="winhttp_query_content_transfer_encoding"></span>**WINHTTP\_QUERY\_CONTENT\_TRANSFER\_ENCODING**
</dt> <dd> <dl> <dt>



Retrieves an encoding transformation applicable to an entity-body. It may already have been applied, may need to be applied, or may be optionally applicable.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CONTENT_TYPE"></span><span id="winhttp_query_content_type"></span>**WINHTTP\_QUERY\_CONTENT\_TYPE**
</dt> <dd> <dl> <dt>



Receives the content type of the resource, such as text or html.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_COOKIE"></span><span id="winhttp_query_cookie"></span>**WINHTTP\_QUERY\_COOKIE**
</dt> <dd> <dl> <dt>



Retrieves any cookies associated with the request.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_COST"></span><span id="winhttp_query_cost"></span>**WINHTTP\_QUERY\_COST**
</dt> <dd> <dl> <dt>



Not supported.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_CUSTOM"></span><span id="winhttp_query_custom"></span>**WINHTTP\_QUERY\_CUSTOM**
</dt> <dd> <dl> <dt>



Causes [**WinHttpQueryHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryheaders) to search for the header name specified in the *pwszName* parameter and store the header information in *lpBuffer*. An application can use **WINHTTP\_OPTION\_RECEIVE\_RESPONSE\_TIMEOUT** to limit the maximum time this query waits for all headers to be received.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_DATE"></span><span id="winhttp_query_date"></span>**WINHTTP\_QUERY\_DATE**
</dt> <dd> <dl> <dt>



Receives the date and time at which the message was originated.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_DERIVED_FROM"></span><span id="winhttp_query_derived_from"></span>**WINHTTP\_QUERY\_DERIVED\_FROM**
</dt> <dd> <dl> <dt>



Not supported.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_ETAG"></span><span id="winhttp_query_etag"></span>**WINHTTP\_QUERY\_ETAG**
</dt> <dd> <dl> <dt>



Retrieves the entity tag for the associated entity.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_EXPECT"></span><span id="winhttp_query_expect"></span>**WINHTTP\_QUERY\_EXPECT**
</dt> <dd> <dl> <dt>



Retrieves the Expect header, which indicates whether the client application should expect 100 series responses.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_EXPIRES"></span><span id="winhttp_query_expires"></span>**WINHTTP\_QUERY\_EXPIRES**
</dt> <dd> <dl> <dt>



Receives the date and time after which the resource should be considered outdated.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_FORWARDED"></span><span id="winhttp_query_forwarded"></span>**WINHTTP\_QUERY\_FORWARDED**
</dt> <dd> <dl> <dt>



Obsolete. Maintained for legacy application compatibility.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_FROM"></span><span id="winhttp_query_from"></span>**WINHTTP\_QUERY\_FROM**
</dt> <dd> <dl> <dt>



Retrieves the e-mail address for the user who controls the requesting [*user agent*](glossary.md) if the From header is given.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_HOST"></span><span id="winhttp_query_host"></span>**WINHTTP\_QUERY\_HOST**
</dt> <dd> <dl> <dt>



Retrieves the Internet host and port number of the resource being requested.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_IF_MATCH"></span><span id="winhttp_query_if_match"></span>**WINHTTP\_QUERY\_IF\_MATCH**
</dt> <dd> <dl> <dt>



Retrieves the contents of the If-Match request-header field.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_IF_MODIFIED_SINCE"></span><span id="winhttp_query_if_modified_since"></span>**WINHTTP\_QUERY\_IF\_MODIFIED\_SINCE**
</dt> <dd> <dl> <dt>



Retrieves the contents of the If-Modified-Since header.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_IF_NONE_MATCH"></span><span id="winhttp_query_if_none_match"></span>**WINHTTP\_QUERY\_IF\_NONE\_MATCH**
</dt> <dd> <dl> <dt>



Retrieves the contents of the If-None-Match request-header field.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_IF_RANGE"></span><span id="winhttp_query_if_range"></span>**WINHTTP\_QUERY\_IF\_RANGE**
</dt> <dd> <dl> <dt>



Retrieves the contents of the If-Range request-header field. This header allows the client application to check if the entity related to a partial copy of the entity in the client application's cache has not been updated. If the entity has not been updated, send the parts that the client application is missing. If the entity has been updated, send the entire updated entity.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_IF_UNMODIFIED_SINCE"></span><span id="winhttp_query_if_unmodified_since"></span>**WINHTTP\_QUERY\_IF\_UNMODIFIED\_SINCE**
</dt> <dd> <dl> <dt>



Retrieves the contents of the If-Unmodified-Since request-header field.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_LINK"></span><span id="winhttp_query_link"></span>**WINHTTP\_QUERY\_LINK**
</dt> <dd> <dl> <dt>



Obsolete. Maintained for legacy application compatibility.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_LAST_MODIFIED"></span><span id="winhttp_query_last_modified"></span>**WINHTTP\_QUERY\_LAST\_MODIFIED**
</dt> <dd> <dl> <dt>



Receives the date and time at which the resource was last modified. The date and time are determined by the server.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_LOCATION"></span><span id="winhttp_query_location"></span>**WINHTTP\_QUERY\_LOCATION**
</dt> <dd> <dl> <dt>



Retrieves the absolute URI used in a Location response-header.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_MAX"></span><span id="winhttp_query_max"></span>**WINHTTP\_QUERY\_MAX**
</dt> <dd> <dl> <dt>



Indicates the maximum value of a WINHTTP\_QUERY\_\* value. Not a query flag.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_MAX_FORWARDS"></span><span id="winhttp_query_max_forwards"></span>**WINHTTP\_QUERY\_MAX\_FORWARDS**
</dt> <dd> <dl> <dt>



Retrieves the number of proxies or gateways that can forward the request to the next inbound server.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_MESSAGE_ID"></span><span id="winhttp_query_message_id"></span>**WINHTTP\_QUERY\_MESSAGE\_ID**
</dt> <dd> <dl> <dt>



Not supported.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_MIME_VERSION"></span><span id="winhttp_query_mime_version"></span>**WINHTTP\_QUERY\_MIME\_VERSION**
</dt> <dd> <dl> <dt>



Receives the version of the Multipurpose Internet Mail Extensions (MIME) protocol that was used to construct the message.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_ORIG_URI"></span><span id="winhttp_query_orig_uri"></span>**WINHTTP\_QUERY\_ORIG\_URI**
</dt> <dd> <dl> <dt>



Obsolete. Maintained for legacy application compatibility.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_PRAGMA"></span><span id="winhttp_query_pragma"></span>**WINHTTP\_QUERY\_PRAGMA**
</dt> <dd> <dl> <dt>



Receives the implementation-specific directives that might apply to any recipient along the request/response chain.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_PROXY_AUTHENTICATE"></span><span id="winhttp_query_proxy_authenticate"></span>**WINHTTP\_QUERY\_PROXY\_AUTHENTICATE**
</dt> <dd> <dl> <dt>



Retrieves the authentication scheme and realm returned by the proxy.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_PROXY_AUTHORIZATION"></span><span id="winhttp_query_proxy_authorization"></span>**WINHTTP\_QUERY\_PROXY\_AUTHORIZATION**
</dt> <dd> <dl> <dt>



Retrieves the header that is used to identify the user to a proxy that requires authentication. This header can only be retrieved before the request is sent to the server.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_PROXY_CONNECTION"></span><span id="winhttp_query_proxy_connection"></span>**WINHTTP\_QUERY\_PROXY\_CONNECTION**
</dt> <dd> <dl> <dt>



Retrieves the Proxy-Connection header.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_PROXY_SUPPORT"></span><span id="winhttp_query_proxy_support"></span>**WINHTTP\_QUERY\_PROXY\_SUPPORT**
</dt> <dd> <dl> <dt>



Retrieves the Proxy-Support header.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_PUBLIC"></span><span id="winhttp_query_public"></span>**WINHTTP\_QUERY\_PUBLIC**
</dt> <dd> <dl> <dt>



Receives HTTP verbs available at this server.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_RANGE"></span><span id="winhttp_query_range"></span>**WINHTTP\_QUERY\_RANGE**
</dt> <dd> <dl> <dt>



Retrieves the byte range of an entity.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_RAW_HEADERS"></span><span id="winhttp_query_raw_headers"></span>**WINHTTP\_QUERY\_RAW\_HEADERS**
</dt> <dd> <dl> <dt>



Receives all the headers returned by the server. Each header is terminated by "\\0". An additional "\\0" terminates the list of headers.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_RAW_HEADERS_CRLF"></span><span id="winhttp_query_raw_headers_crlf"></span>**WINHTTP\_QUERY\_RAW\_HEADERS\_CRLF**
</dt> <dd> <dl> <dt>



Receives all the headers returned by the server. Each header is separated by a carriage return/line feed (CR/LF) sequence.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_REFERER"></span><span id="winhttp_query_referer"></span>**WINHTTP\_QUERY\_REFERER**
</dt> <dd> <dl> <dt>



Receives the URI of the resource where the requested URI was obtained.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_REFRESH"></span><span id="winhttp_query_refresh"></span>**WINHTTP\_QUERY\_REFRESH**
</dt> <dd> <dl> <dt>



Obsolete. Maintained for legacy application compatibility.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_REQUEST_METHOD"></span><span id="winhttp_query_request_method"></span>**WINHTTP\_QUERY\_REQUEST\_METHOD**
</dt> <dd> <dl> <dt>



Receives the HTTP verb that is being used in the request, typically GET or POST.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_RETRY_AFTER"></span><span id="winhttp_query_retry_after"></span>**WINHTTP\_QUERY\_RETRY\_AFTER**
</dt> <dd> <dl> <dt>



Retrieves the amount of time the service is expected to be unavailable.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_SERVER"></span><span id="winhttp_query_server"></span>**WINHTTP\_QUERY\_SERVER**
</dt> <dd> <dl> <dt>



Retrieves information about the software used by the originating server to handle the request.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_SET_COOKIE"></span><span id="winhttp_query_set_cookie"></span>**WINHTTP\_QUERY\_SET\_COOKIE**
</dt> <dd> <dl> <dt>



Receives the value of the cookie set for the request.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_STATUS_CODE"></span><span id="winhttp_query_status_code"></span>**WINHTTP\_QUERY\_STATUS\_CODE**
</dt> <dd> <dl> <dt>



Receives the status code returned by the server. For a list of possible values, see [**HTTP Status Codes**](http-status-codes.md).


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_STATUS_TEXT"></span><span id="winhttp_query_status_text"></span>**WINHTTP\_QUERY\_STATUS\_TEXT**
</dt> <dd> <dl> <dt>



Receives additional text returned by the server on the response line.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_TITLE"></span><span id="winhttp_query_title"></span>**WINHTTP\_QUERY\_TITLE**
</dt> <dd> <dl> <dt>



Obsolete. Maintained for legacy application compatibility.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_TRANSFER_ENCODING"></span><span id="winhttp_query_transfer_encoding"></span>**WINHTTP\_QUERY\_TRANSFER\_ENCODING**
</dt> <dd> <dl> <dt>



Retrieves the type of transformation that has been applied to the message body so it can be safely transferred between the sender and recipient.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_UNLESS_MODIFIED_SINCE"></span><span id="winhttp_query_unless_modified_since"></span>**WINHTTP\_QUERY\_UNLESS\_MODIFIED\_SINCE**
</dt> <dd> <dl> <dt>



Retrieves the Unless-Modified-Since header.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_UPGRADE"></span><span id="winhttp_query_upgrade"></span>**WINHTTP\_QUERY\_UPGRADE**
</dt> <dd> <dl> <dt>



Retrieves the additional communication protocols that are supported by the server.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_URI"></span><span id="winhttp_query_uri"></span>**WINHTTP\_QUERY\_URI**
</dt> <dd> <dl> <dt>



Receives some or all of the URI by which the Request-URI resource can be identified.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_USER_AGENT"></span><span id="winhttp_query_user_agent"></span>**WINHTTP\_QUERY\_USER\_AGENT**
</dt> <dd> <dl> <dt>



Retrieves information about the user agent that made the request.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_VARY"></span><span id="winhttp_query_vary"></span>**WINHTTP\_QUERY\_VARY**
</dt> <dd> <dl> <dt>



Retrieves the header that indicates that the entity was selected from a number of available representations of the response using server-driven negotiation.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_VERSION"></span><span id="winhttp_query_version"></span>**WINHTTP\_QUERY\_VERSION**
</dt> <dd> <dl> <dt>



Retrieves the HTTP version that is present in the status line.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_VIA"></span><span id="winhttp_query_via"></span>**WINHTTP\_QUERY\_VIA**
</dt> <dd> <dl> <dt>



Retrieves the intermediate protocols and recipients between the user agent and the server on requests, and between the origin server and the client on responses.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_WARNING"></span><span id="winhttp_query_warning"></span>**WINHTTP\_QUERY\_WARNING**
</dt> <dd> <dl> <dt>



Retrieves additional information about the status of a response that might not be reflected by the response status code.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_WWW_AUTHENTICATE"></span><span id="winhttp_query_www_authenticate"></span>**WINHTTP\_QUERY\_WWW\_AUTHENTICATE**
</dt> <dd> <dl> <dt>



Retrieves the authentication scheme and realm returned by the server.


</dt> </dl> </dd> </dl>

The modifier flags are used in conjunction with an attribute flag to modify the request. Modifier flags either modify the format of the data returned or indicate where the [**WinHttpQueryHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryheaders) function should search for the information.

<dl> <dt>

<span id="WINHTTP_QUERY_FLAG_NUMBER"></span><span id="winhttp_query_flag_number"></span>**WINHTTP\_QUERY\_FLAG\_NUMBER**
</dt> <dd> <dl> <dt>



Returns the data as a 32-bit number for headers whose value is a number, such as the status code.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_FLAG_REQUEST_HEADERS"></span><span id="winhttp_query_flag_request_headers"></span>**WINHTTP\_QUERY\_FLAG\_REQUEST\_HEADERS**
</dt> <dd> <dl> <dt>



Queries request headers only.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_QUERY_FLAG_SYSTEMTIME"></span><span id="winhttp_query_flag_systemtime"></span>**WINHTTP\_QUERY\_FLAG\_SYSTEMTIME**
</dt> <dd> <dl> <dt>



Returns the header value as a [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure, which does not require the application to parse the data. Use for headers whose value is a date/time string, such as "Last-Modified-Time".


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>      |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>   |
| Header<br/>                   | <dl> <dt>Winhttp.h</dt> </dl> |



## See also

<dl> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

