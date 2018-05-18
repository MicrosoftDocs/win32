---
Description: 'This topic identifies the structures that WinHTTP uses.'
ms.assetid: 'e1567393-162e-48d4-8e6b-7620e351136c'
title: WinHTTP Structures
---

# WinHTTP Structures

WinHTTP uses the following structures:

<dl> <dt>

[**HTTP\_VERSION\_INFO**](http-version-info.md)
</dt> <dd>

Contains the global HTTP version.

</dd> <dt>

[**URL\_COMPONENTS**](url-components.md)
</dt> <dd>

Contains the constituent parts of a URL. This structure is used with the [**WinHttpCrackUrl**](winhttpcrackurl.md) and [**WinHttpCreateUrl**](winhttpcreateurl.md) functions.

</dd> <dt>

[**WINHTTP\_ASYNC\_RESULT**](winhttp-async-result.md)
</dt> <dd>

Contains the result of a call to an asynchronous function. This structure is used with the [**WINHTTP\_STATUS\_CALLBACK**](internet-status-callback-prototype.md) prototype.

</dd> <dt>

[**WINHTTP\_AUTOPROXY\_OPTIONS**](winhttp-autoproxy-options.md)
</dt> <dd>

Used to indicate to the [**WinHttpGetProxyForURL**](winhttpgetproxyforurl.md) function whether to specify the URL of the Proxy Auto-Configuration (PAC) file or to automatically locate the URL with DHCP or DNS queries to the network.

</dd> <dt>

[**WINHTTP\_CERTIFICATE\_INFO**](internet-certificate-info.md)
</dt> <dd>

Contains certificate information returned from the server. This structure is used by the [**WinHttpQueryOption**](winhttpqueryoption.md) function.

</dd> <dt>

[**WINHTTP\_CONNECTION\_INFO**](winhttp-connection-info.md)
</dt> <dd>

Contains the source and destination IP address of the request that generated the response.

</dd> <dt>

[**WINHTTP\_CREDS**](winhttp-creds.md)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

> [!Note]  
> This structure has been deprecated. Instead, the use of the [**WINHTTP\_CREDS\_EX**](winhttp-creds-ex.md) structure is recommended.

 

</dd> <dt>

[**WINHTTP\_CREDS\_EX**](winhttp-creds-ex.md)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

</dd> <dt>

[**WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG**](winhttp-current-user-ie-proxy-config.md)
</dt> <dd>

Contains the Internet Explorer proxy configuration information.

</dd> <dt>

[**WINHTTP\_PROXY\_INFO**](internet-proxy-info.md)
</dt> <dd>

Contains the session or default proxy configuration.

</dd> <dt>

[**WINHTTP\_PROXY\_RESULT**](winhttp-proxy-result.md)
</dt> <dd>

A collection of proxy result entries provided by [**WinHttpGetProxyResult**](winhttpgetproxyresult.md).

</dd> <dt>

[**WINHTTP\_PROXY\_RESULT\_ENTRY**](winhttp-proxy-result-entry.md)
</dt> <dd>

A result entry from a call to [**WinHttpGetProxyResult**](winhttpgetproxyresult.md).

</dd> <dt>

[**WINHTTP\_WEB\_SOCKET\_ASYNC\_RESULT**](winhttp-web-socket-async-result.md)
</dt> <dd>

Result status of a WebSocket operation.

</dd> <dt>

[**WINHTTP\_WEB\_SOCKET\_STATUS**](winhttp-web-socket-status.md)
</dt> <dd>

Status of a WebSocket operation.

</dd> </dl>

 

 



