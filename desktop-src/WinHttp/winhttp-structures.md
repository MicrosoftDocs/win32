---
description: This topic identifies the structures that WinHTTP uses.
ms.assetid: e1567393-162e-48d4-8e6b-7620e351136c
title: WinHTTP structures
ms.topic: article
ms.date: 05/31/2018
---

# WinHTTP structures

WinHTTP uses the following structures:

<dl> <dt>

[**HTTP_VERSION_INFO**](/windows/win32/api/winhttp/ns-winhttp-http_version_info)
</dt> <dd>

Contains the global HTTP version.

</dd> <dt>

[**URL_COMPONENTS**](/windows/win32/api/winhttp/ns-winhttp-url_components)
</dt> <dd>

Contains the constituent parts of a URL. This structure is used with the [**WinHttpCrackUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcrackurl) and [**WinHttpCreateUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcreateurl) functions.

</dd> <dt>

[**WINHTTP_ASYNC_RESULT**](/windows/win32/api/winhttp/ns-winhttp-winhttp_async_result)
</dt> <dd>

Contains the result of a call to an asynchronous function. This structure is used with the [**WINHTTP_STATUS_CALLBACK**](/windows/win32/api/winhttp/nc-winhttp-winhttp_status_callback) prototype.

</dd> <dt>

[**WINHTTP_AUTOPROXY_OPTIONS**](/windows/win32/api/winhttp/ns-winhttp-winhttp_autoproxy_options)
</dt> <dd>

Used to indicate to the [**WinHttpGetProxyForURL**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) function whether to specify the URL of the Proxy Auto-Configuration (PAC) file or to automatically locate the URL with DHCP or DNS queries to the network.

</dd> <dt>

[**WINHTTP_CERTIFICATE_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_certificate_info)
</dt> <dd>

Contains certificate information returned from the server. This structure is used by the [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) function.

</dd> <dt>

[**WINHTTP_CONNECTION_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-winhttp_connection_info)
</dt> <dd>

Contains the source and destination IP address of the request that generated the response.

</dd> <dt>

[**WINHTTP_CREDS**](/windows/win32/api/winhttp/ns-winhttp-winhttp_creds)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

> [!Note]
> This structure has been deprecated. Instead, the use of the [**WINHTTP_CREDS_EX**](/windows/win32/api/winhttp/ns-winhttp-winhttp_creds_ex) structure is recommended.

</dd> <dt>

[**WINHTTP_CREDS_EX**](/windows/win32/api/winhttp/ns-winhttp-winhttp_creds_ex)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

</dd> <dt>

[**WINHTTP_CURRENT_USER_IE_PROXY_CONFIG**](/windows/win32/api/winhttp/ns-winhttp-winhttp_current_user_ie_proxy_config)
</dt> <dd>

Contains the Internet Explorer proxy configuration information.

</dd> <dt>

[**WINHTTP_PROXY_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info)
</dt> <dd>

Contains the session or default proxy configuration.

</dd> <dt>

[**WINHTTP_PROXY_RESULT**](/windows/desktop/api/winhttp/ns-winhttp-winhttp_proxy_result)
</dt> <dd>

A collection of proxy result entries provided by [**WinHttpGetProxyResult**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyresult).

</dd> <dt>

[**WINHTTP_PROXY_RESULT_ENTRY**](/windows/desktop/api/winhttp/ns-winhttp-winhttp_proxy_result_entry)
</dt> <dd>

A result entry from a call to [**WinHttpGetProxyResult**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyresult).

</dd> <dt>

[**WINHTTP_REQUEST_STATS**](/windows/desktop/api/winhttp/ns-winhttp-winhttp_request_stats)
</dt> <dd>

Contains statistics for a request.

</dd> <dt>

[**WINHTTP_REQUEST_TIMES**](/windows/desktop/api/winhttp/ns-winhttp-winhttp_request_times)
</dt> <dd>

Contains timing information for a request.

</dd> <dt>

[**WINHTTP_SECURITY_INFO**](/windows/desktop/api/winhttp/ns-winhttp-winhttp_security_info)
</dt> <dd>

Contains SChannel connection and cipher information for a request.

</dd> <dt>

[**WINHTTP_WEB_SOCKET_ASYNC_RESULT**](/windows/desktop/api/winhttp/ns-winhttp-winhttp_web_socket_async_result)
</dt> <dd>

Result status of a WebSocket operation.

</dd> <dt>

[**WINHTTP_WEB_SOCKET_STATUS**](/windows/desktop/api/winhttp/ns-winhttp-winhttp_web_socket_status)
</dt> <dd>

Status of a WebSocket operation.

</dd> </dl>
