---
title: HTTP_LOG_FIELD_ Constants (Http.h)
description: Define the fields in the W3C log and the error logs.
ms.assetid: 44307d5a-f413-4ee9-9f9c-586c824d5493
topic_type:
- apiref
api_name:
- HTTP_LOG_FIELD_DATE
- HTTP_LOG_FIELD_TIME
- HTTP_LOG_FIELD_CLIENT_IP
- HTTP_LOG_FIELD_USER_NAME
- HTTP_LOG_FIELD_SITE_NAME
- HTTP_LOG_FIELD_COMPUTER_NAME
- HTTP_LOG_FIELD_SERVER_IP
- HTTP_LOG_FIELD_METHOD
- HTTP_LOG_FIELD_URI_STEM
- HTTP_LOG_FIELD_URI_QUERY
- HTTP_LOG_FIELD_STATUS
- HTTP_LOG_FIELD_WIN32_STATUS
- HTTP_LOG_FIELD_BYTES_SENT
- HTTP_LOG_FIELD_BYTES_RECV
- HTTP_LOG_FIELD_TIME_TAKEN
- HTTP_LOG_FIELD_SERVER_PORT
- HTTP_LOG_FIELD_USER_AGENT
- HTTP_LOG_FIELD_COOKIE
- HTTP_LOG_FIELD_REFERER
- HTTP_LOG_FIELD_VERSION
- HTTP_LOG_FIELD_HOST
- HTTP_LOG_FIELD_SUB_STATUS
- HTTP_LOG_FIELD_CLIENT_PORT
- HTTP_LOG_FIELD_URI
- HTTP_LOG_FIELD_SITE_ID
- HTTP_LOG_FIELD_REASON
- HTTP_LOG_FIELD_QUEUE_NAME
- HTTP_LOG_FIELD_STREAMID
api_location:
- http.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HTTP\_LOG\_FIELD\_ Constants

The **HTTP\_LOG\_FIELD\_** constants define the fields in the W3C log and the error logs.

These constants are used in the [**HTTP\_LOGGING\_INFO**](/windows/desktop/api/Http/ns-http-http_logging_info) structure.

<dl> <dt>

<span id="HTTP_LOG_FIELD_DATE"></span><span id="http_log_field_date"></span>**HTTP\_LOG\_FIELD\_DATE**
</dt> <dd> <dl> <dt>



The date on which the activity occurred.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_TIME"></span><span id="http_log_field_time"></span>**HTTP\_LOG\_FIELD\_TIME**
</dt> <dd> <dl> <dt>



The time, in coordinated universal time (UTC), at which the activity occurred.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_CLIENT_IP"></span><span id="http_log_field_client_ip"></span>**HTTP\_LOG\_FIELD\_CLIENT\_IP**
</dt> <dd> <dl> <dt>



The IP address of the client that made the request.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_USER_NAME"></span><span id="http_log_field_user_name"></span>**HTTP\_LOG\_FIELD\_USER\_NAME**
</dt> <dd> <dl> <dt>



The name of the authenticated user who accessed your server. Anonymous users are indicated by a hyphen.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_SITE_NAME"></span><span id="http_log_field_site_name"></span>**HTTP\_LOG\_FIELD\_SITE\_NAME**
</dt> <dd> <dl> <dt>



The name of the site on which the log file entry was generated.


</dt> </dl> </dd> <dt>

<span id="_HTTP_LOG_FIELD_COMPUTER_NAME"></span><span id="_http_log_field_computer_name"></span> **HTTP\_LOG\_FIELD\_COMPUTER\_NAME**
</dt> <dd> <dl> <dt>



The name of the computer on which the log file entry was generated.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_SERVER_IP"></span><span id="http_log_field_server_ip"></span>**HTTP\_LOG\_FIELD\_SERVER\_IP**
</dt> <dd> <dl> <dt>



The IP address of the server on which the log file entry was generated.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_METHOD"></span><span id="http_log_field_method"></span>**HTTP\_LOG\_FIELD\_METHOD**
</dt> <dd> <dl> <dt>



The requested action, for example, a get method.


</dt> </dl> </dd> <dt>

<span id="_HTTP_LOG_FIELD_URI_STEM"></span><span id="_http_log_field_uri_stem"></span> **HTTP\_LOG\_FIELD\_URI\_STEM**
</dt> <dd> <dl> <dt>



The target of the action, for example, Default.htm.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_URI_QUERY"></span><span id="http_log_field_uri_query"></span>**HTTP\_LOG\_FIELD\_URI\_QUERY**
</dt> <dd> <dl> <dt>



The query, if any, that the client was trying to perform. A Universal Resource Identifier (URI) query is necessary only for dynamic pages.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_STATUS"></span><span id="http_log_field_status"></span>**HTTP\_LOG\_FIELD\_STATUS**
</dt> <dd> <dl> <dt>



The HTTP status code.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_WIN32_STATUS"></span><span id="http_log_field_win32_status"></span>**HTTP\_LOG\_FIELD\_WIN32\_STATUS**
</dt> <dd> <dl> <dt>



The Windows status code.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_BYTES_SENT"></span><span id="http_log_field_bytes_sent"></span>**HTTP\_LOG\_FIELD\_BYTES\_SENT**
</dt> <dd> <dl> <dt>



The number, in bytes, sent by the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_BYTES_RECV"></span><span id="http_log_field_bytes_recv"></span>**HTTP\_LOG\_FIELD\_BYTES\_RECV**
</dt> <dd> <dl> <dt>



The number, in bytes, received by the server.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_TIME_TAKEN"></span><span id="http_log_field_time_taken"></span>**HTTP\_LOG\_FIELD\_TIME\_TAKEN**
</dt> <dd> <dl> <dt>



The time, in milliseconds, of the action.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_SERVER_PORT"></span><span id="http_log_field_server_port"></span>**HTTP\_LOG\_FIELD\_SERVER\_PORT**
</dt> <dd> <dl> <dt>



The server port number that is configured for the service.


</dt> </dl> </dd> <dt>

<span id="_HTTP_LOG_FIELD_USER_AGENT"></span><span id="_http_log_field_user_agent"></span> **HTTP\_LOG\_FIELD\_USER\_AGENT**
</dt> <dd> <dl> <dt>



The application that the client used.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_COOKIE"></span><span id="http_log_field_cookie"></span>**HTTP\_LOG\_FIELD\_COOKIE**
</dt> <dd> <dl> <dt>



The content of the cookie sent or received, if any.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_REFERER"></span><span id="http_log_field_referer"></span>**HTTP\_LOG\_FIELD\_REFERER**
</dt> <dd> <dl> <dt>



The site that the user last visited. This site provided a link to the current site.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_VERSION"></span><span id="http_log_field_version"></span>**HTTP\_LOG\_FIELD\_VERSION**
</dt> <dd> <dl> <dt>



The HTTP protocol version that the client used.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_HOST"></span><span id="http_log_field_host"></span>**HTTP\_LOG\_FIELD\_HOST**
</dt> <dd> <dl> <dt>



The host header name, if any.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_SUB_STATUS"></span><span id="http_log_field_sub_status"></span>**HTTP\_LOG\_FIELD\_SUB\_STATUS**
</dt> <dd> <dl> <dt>



The substatus error code.


</dt> </dl> </dd> </dl>

The following constants are used for HTTP error logging.

<dl> <dt>

<span id="HTTP_LOG_FIELD_CLIENT_PORT"></span><span id="http_log_field_client_port"></span>**HTTP\_LOG\_FIELD\_CLIENT\_PORT**
</dt> <dd> <dl> <dt>



The client port number from which the request is received. This log field is only used for error logging.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_URI"></span><span id="http_log_field_uri"></span>**HTTP\_LOG\_FIELD\_URI**
</dt> <dd> <dl> <dt>



The URI received in the request including the query portion. This log field is only used for error logging.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_SITE_ID"></span><span id="http_log_field_site_id"></span>**HTTP\_LOG\_FIELD\_SITE\_ID**
</dt> <dd> <dl> <dt>



The application-specific numeric ID of the URL Group on which the request is routed. This log field is only used for error logging.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_REASON"></span><span id="http_log_field_reason"></span>**HTTP\_LOG\_FIELD\_REASON**
</dt> <dd> <dl> <dt>



The error reason phrase. This log field is only used for error logging.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_QUEUE_NAME"></span><span id="http_log_field_queue_name"></span>**HTTP\_LOG\_FIELD\_QUEUE\_NAME**
</dt> <dd> <dl> <dt>



The name of the request queue to which the request is dispatched. This log field is only used for error logging.


</dt> </dl> </dd> <dt>

<span id="HTTP_LOG_FIELD_STREAMID"></span><span id="http_log_field_streamid"></span>**HTTP\_LOG\_FIELD\_STREAMID**
</dt> <dd> <dl> <dt>



The stream id.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Http.h</dt> </dl> |



## See also

<dl> <dt>

[HTTP Server API Version 2.0 Constants](http-server-api-version-2-0-constants.md)
</dt> <dt>

[**HTTP\_LOGGING\_INFO**](/windows/desktop/api/Http/ns-http-http_logging_info)
</dt> <dt>

[**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty)
</dt> <dt>

[**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty)
</dt> <dt>

[**HttpQueryUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpqueryurlgroupproperty)
</dt> <dt>

[**HttpQueryServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpqueryserversessionproperty)
</dt> </dl>

 

 





