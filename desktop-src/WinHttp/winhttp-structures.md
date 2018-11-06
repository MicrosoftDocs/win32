---
Description: This topic identifies the structures that WinHTTP uses.
ms.assetid: e1567393-162e-48d4-8e6b-7620e351136c
title: WinHTTP Structures
ms.topic: article
ms.date: 05/31/2018
---

# WinHTTP Structures

WinHTTP uses the following structures:

<dl> <dt>

[**HTTP\_VERSION\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_1)
</dt> <dd>

Contains the global HTTP version.

</dd> <dt>

[**URL\_COMPONENTS**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_2)
</dt> <dd>

Contains the constituent parts of a URL. This structure is used with the [**WinHttpCrackUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcrackurl) and [**WinHttpCreateUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcreateurl) functions.

</dd> <dt>

[**WINHTTP\_ASYNC\_RESULT**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_0)
</dt> <dd>

Contains the result of a call to an asynchronous function. This structure is used with the [**WINHTTP\_STATUS\_CALLBACK**](https://msdn.microsoft.com/en-us/library/Aa383917(v=VS.85).aspx) prototype.

</dd> <dt>

[**WINHTTP\_AUTOPROXY\_OPTIONS**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_4)
</dt> <dd>

Used to indicate to the [**WinHttpGetProxyForURL**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) function whether to specify the URL of the Proxy Auto-Configuration (PAC) file or to automatically locate the URL with DHCP or DNS queries to the network.

</dd> <dt>

[**WINHTTP\_CERTIFICATE\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_5)
</dt> <dd>

Contains certificate information returned from the server. This structure is used by the [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) function.

</dd> <dt>

[**WINHTTP\_CONNECTION\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-winhttp_connection_info)
</dt> <dd>

Contains the source and destination IP address of the request that generated the response.

</dd> <dt>

[**WINHTTP\_CREDS**](/windows/desktop/api/Winhttp/ns-winhttp-tagwinhttp_creds)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

> [!Note]  
> This structure has been deprecated. Instead, the use of the [**WINHTTP\_CREDS\_EX**](/windows/desktop/api/Winhttp/ns-winhttp-tagwinhttp_creds_ex) structure is recommended.

 

</dd> <dt>

[**WINHTTP\_CREDS\_EX**](/windows/desktop/api/Winhttp/ns-winhttp-tagwinhttp_creds_ex)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

</dd> <dt>

[**WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG**](/windows/desktop/api/Winhttp/ns-winhttp-winhttp_current_user_ie_proxy_config)
</dt> <dd>

Contains the Internet Explorer proxy configuration information.

</dd> <dt>

[**WINHTTP\_PROXY\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_3)
</dt> <dd>

Contains the session or default proxy configuration.

</dd> <dt>

[**WINHTTP\_PROXY\_RESULT**](/windows/desktop/api/winhttp/ns-winhttp-_winhttp_proxy_result)
</dt> <dd>

A collection of proxy result entries provided by [**WinHttpGetProxyResult**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyresult).

</dd> <dt>

[**WINHTTP\_PROXY\_RESULT\_ENTRY**](/windows/desktop/api/winhttp/ns-winhttp-_winhttp_proxy_result_entry)
</dt> <dd>

A result entry from a call to [**WinHttpGetProxyResult**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyresult).

</dd> <dt>

[**WINHTTP\_WEB\_SOCKET\_ASYNC\_RESULT**](/windows/desktop/api/winhttp/ns-winhttp-_winhttp_web_socket_async_result)
</dt> <dd>

Result status of a WebSocket operation.

</dd> <dt>

[**WINHTTP\_WEB\_SOCKET\_STATUS**](/windows/desktop/api/winhttp/ns-winhttp-_winhttp_web_socket_status)
</dt> <dd>

Status of a WebSocket operation.

</dd> </dl>

 

 



