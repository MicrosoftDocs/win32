---
Description: This topic identifies the structures that WinHTTP uses.
ms.assetid: e1567393-162e-48d4-8e6b-7620e351136c
title: WinHTTP Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WinHTTP Structures

WinHTTP uses the following structures:

<dl> <dt>

[**HTTP\_VERSION\_INFO**](/windows/win32/Winhttp/ns-winhttp-__unnamed_struct_1?branch=master)
</dt> <dd>

Contains the global HTTP version.

</dd> <dt>

[**URL\_COMPONENTS**](/windows/win32/Winhttp/ns-winhttp-__unnamed_struct_2?branch=master)
</dt> <dd>

Contains the constituent parts of a URL. This structure is used with the [**WinHttpCrackUrl**](/windows/win32/Winhttp/nf-winhttp-winhttpcrackurl?branch=master) and [**WinHttpCreateUrl**](/windows/win32/Winhttp/nf-winhttp-winhttpcreateurl?branch=master) functions.

</dd> <dt>

[**WINHTTP\_ASYNC\_RESULT**](/windows/win32/Winhttp/ns-winhttp-__unnamed_struct_0?branch=master)
</dt> <dd>

Contains the result of a call to an asynchronous function. This structure is used with the [**WINHTTP\_STATUS\_CALLBACK**](/windows/win32/Winhttp/nc-winhttp-winhttp_status_callback?branch=master) prototype.

</dd> <dt>

[**WINHTTP\_AUTOPROXY\_OPTIONS**](/windows/win32/Winhttp/ns-winhttp-__unnamed_struct_4?branch=master)
</dt> <dd>

Used to indicate to the [**WinHttpGetProxyForURL**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyforurl?branch=master) function whether to specify the URL of the Proxy Auto-Configuration (PAC) file or to automatically locate the URL with DHCP or DNS queries to the network.

</dd> <dt>

[**WINHTTP\_CERTIFICATE\_INFO**](/windows/win32/Winhttp/ns-winhttp-__unnamed_struct_5?branch=master)
</dt> <dd>

Contains certificate information returned from the server. This structure is used by the [**WinHttpQueryOption**](/windows/win32/Winhttp/nf-winhttp-winhttpqueryoption?branch=master) function.

</dd> <dt>

[**WINHTTP\_CONNECTION\_INFO**](/windows/win32/Winhttp/ns-winhttp-winhttp_connection_info?branch=master)
</dt> <dd>

Contains the source and destination IP address of the request that generated the response.

</dd> <dt>

[**WINHTTP\_CREDS**](/windows/win32/Winhttp/ns-winhttp-tagwinhttp_creds?branch=master)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

> [!Note]  
> This structure has been deprecated. Instead, the use of the [**WINHTTP\_CREDS\_EX**](/windows/win32/Winhttp/ns-winhttp-tagwinhttp_creds_ex?branch=master) structure is recommended.

 

</dd> <dt>

[**WINHTTP\_CREDS\_EX**](/windows/win32/Winhttp/ns-winhttp-tagwinhttp_creds_ex?branch=master)
</dt> <dd>

Contains user credential information used for server and proxy authentication.

</dd> <dt>

[**WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG**](/windows/win32/Winhttp/ns-winhttp-winhttp_current_user_ie_proxy_config?branch=master)
</dt> <dd>

Contains the Internet Explorer proxy configuration information.

</dd> <dt>

[**WINHTTP\_PROXY\_INFO**](/windows/win32/Winhttp/ns-winhttp-__unnamed_struct_3?branch=master)
</dt> <dd>

Contains the session or default proxy configuration.

</dd> <dt>

[**WINHTTP\_PROXY\_RESULT**](/windows/win32/winhttp/ns-winhttp-_winhttp_proxy_result?branch=master)
</dt> <dd>

A collection of proxy result entries provided by [**WinHttpGetProxyResult**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyresult?branch=master).

</dd> <dt>

[**WINHTTP\_PROXY\_RESULT\_ENTRY**](/windows/win32/winhttp/ns-winhttp-_winhttp_proxy_result_entry?branch=master)
</dt> <dd>

A result entry from a call to [**WinHttpGetProxyResult**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyresult?branch=master).

</dd> <dt>

[**WINHTTP\_WEB\_SOCKET\_ASYNC\_RESULT**](/windows/win32/winhttp/ns-winhttp-_winhttp_web_socket_async_result?branch=master)
</dt> <dd>

Result status of a WebSocket operation.

</dd> <dt>

[**WINHTTP\_WEB\_SOCKET\_STATUS**](/windows/win32/winhttp/ns-winhttp-_winhttp_web_socket_status?branch=master)
</dt> <dd>

Status of a WebSocket operation.

</dd> </dl>

 

 



