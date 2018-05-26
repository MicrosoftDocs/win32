---
Description: This topic identifies the functions that WinHTTP provides.
ms.assetid: dcb56d5d-ed0d-49bb-95bf-940a49c033f1
title: WinHTTP Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WinHTTP Functions

WinHTTP provides the following functions:

<dl> <dt>

[**WinHttpAddRequestHeaders**](/windows/win32/Winhttp/nf-winhttp-winhttpaddrequestheaders?branch=master)
</dt> <dd>

Adds one or more HTTP request headers to the HTTP request handle.

</dd> <dt>

[**WinHttpCheckPlatform**](/windows/win32/Winhttp/nf-winhttp-winhttpcheckplatform?branch=master)
</dt> <dd>

Determines whether the current platform is supported by WinHTTP.

</dd> <dt>

[**WinHttpCloseHandle**](/windows/win32/Winhttp/nf-winhttp-winhttpclosehandle?branch=master)
</dt> <dd>

Closes a single [HINTERNET](hinternet-handles-in-winhttp.md) handle.

</dd> <dt>

[**WinHttpConnect**](/windows/win32/Winhttp/nf-winhttp-winhttpconnect?branch=master)
</dt> <dd>

Specifies the initial target server of an HTTP request.

</dd> <dt>

[**WinHttpCrackUrl**](/windows/win32/Winhttp/nf-winhttp-winhttpcrackurl?branch=master)
</dt> <dd>

Separates a URL into its component parts, for example, host name and path.

</dd> <dt>

[**WinHttpCreateProxyResolver**](/windows/win32/Winhttp/nf-winhttp-winhttpcreateproxyresolver?branch=master)
</dt> <dd>

Creates a handle for use by [**WinHttpGetProxyForUrlEx**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyforurlex?branch=master).

</dd> <dt>

[**WinHttpCreateUrl**](/windows/win32/Winhttp/nf-winhttp-winhttpcreateurl?branch=master)
</dt> <dd>

Creates a URL from component parts, for example, the host name and path.

</dd> <dt>

[**WinHttpDetectAutoProxyConfigUrl**](/windows/win32/Winhttp/nf-winhttp-winhttpdetectautoproxyconfigurl?branch=master)
</dt> <dd>

Finds the URL for the Proxy Auto-Configuration (PAC) file. This function reports the URL of the PAC file, but it does not download the file.

</dd> <dt>

[**WinHttpFreeProxyResult**](/windows/win32/Winhttp/nf-winhttp-winhttpfreeproxyresult?branch=master)
</dt> <dd>

Frees the data retrieved from a previous call to [**WinHttpGetProxyResult**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyresult?branch=master).

</dd> <dt>

[**WinHttpGetDefaultProxyConfiguration**](/windows/win32/Winhttp/nf-winhttp-winhttpgetdefaultproxyconfiguration?branch=master)
</dt> <dd>

Retrieves the default WinHTTP proxy configuration from the registry.

</dd> <dt>

[**WinHTTPGetIEProxyConfigForCurrentUser**](/windows/win32/Winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser?branch=master)
</dt> <dd>

Obtains the Internet Explorer (IE) proxy configuration for the current user.

</dd> <dt>

[**WinHttpGetProxyForUrl**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyforurl?branch=master)
</dt> <dd>

Retrieves the proxy information for the specified URL.

</dd> <dt>

[**WinHttpGetProxyForUrlEx**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyforurlex?branch=master)
</dt> <dd>

Retrieves the proxy information for the specified URL.

</dd> <dt>

[**WinHttpGetProxyResult**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyresult?branch=master)
</dt> <dd>

Retrieves the results of a call to [**WinHttpGetProxyForUrlEx**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyforurlex?branch=master).

</dd> <dt>

[**WinHttpOpen**](/windows/win32/Winhttp/nf-winhttp-winhttpopen?branch=master)
</dt> <dd>

Initializes an application's use of the WinHTTP functions.

</dd> <dt>

[**WinHttpOpenRequest**](/windows/win32/Winhttp/nf-winhttp-winhttpopenrequest?branch=master)
</dt> <dd>

Creates an HTTP request handle.

</dd> <dt>

[**WinHttpQueryAuthSchemes**](/windows/win32/Winhttp/nf-winhttp-winhttpqueryauthschemes?branch=master)
</dt> <dd>

Returns the authorization schemes that the server supports.

</dd> <dt>

[**WinHttpQueryDataAvailable**](/windows/win32/Winhttp/nf-winhttp-winhttpquerydataavailable?branch=master)
</dt> <dd>

Returns the number of bytes of data that are available immediately to be read with [**WinHttpReadData**](/windows/win32/Winhttp/nf-winhttp-winhttpreaddata?branch=master).

</dd> <dt>

[**WinHttpQueryHeaders**](/windows/win32/Winhttp/nf-winhttp-winhttpqueryheaders?branch=master)
</dt> <dd>

Retrieves header information associated with an HTTP request.

</dd> <dt>

[**WinHttpQueryOption**](/windows/win32/Winhttp/nf-winhttp-winhttpqueryoption?branch=master)
</dt> <dd>

Queries an Internet option on the specified handle.

</dd> <dt>

[**WinHttpReadData**](/windows/win32/Winhttp/nf-winhttp-winhttpreaddata?branch=master)
</dt> <dd>

Reads data from a handle opened by the [**WinHttpOpenRequest**](/windows/win32/Winhttp/nf-winhttp-winhttpopenrequest?branch=master) function.

</dd> <dt>

[**WinHttpReceiveResponse**](/windows/win32/Winhttp/nf-winhttp-winhttpreceiveresponse?branch=master)
</dt> <dd>

Ends an HTTP request that is initiated by [**WinHttpSendRequest**](/windows/win32/Winhttp/nf-winhttp-winhttpsendrequest?branch=master).

</dd> <dt>

[**WinHttpResetAutoProxy**](/windows/win32/Winhttp/nf-winhttp-winhttpresetautoproxy?branch=master)
</dt> <dd>

Resets the auto-proxy.

</dd> <dt>

[**WinHttpSendRequest**](/windows/win32/Winhttp/nf-winhttp-winhttpsendrequest?branch=master)
</dt> <dd>

Sends the specified request to the HTTP server.

</dd> <dt>

[**WinHttpSetCredentials**](/windows/win32/Winhttp/nf-winhttp-winhttpsetcredentials?branch=master)
</dt> <dd>

Passes the required authorization credentials to the server.

</dd> <dt>

[**WinHttpSetDefaultProxyConfiguration**](/windows/win32/Winhttp/nf-winhttp-winhttpsetdefaultproxyconfiguration?branch=master)
</dt> <dd>

Sets the default WinHTTP proxy configuration in the registry.

</dd> <dt>

[**WinHttpSetOption**](/windows/win32/Winhttp/nf-winhttp-winhttpsetoption?branch=master)
</dt> <dd>

Sets an Internet option.

</dd> <dt>

[**WinHttpSetStatusCallback**](/windows/win32/Winhttp/nf-winhttp-winhttpsetstatuscallback?branch=master)
</dt> <dd>

Sets up a callback function that WinHTTP can call as progress is made during an operation.

</dd> <dt>

[**WinHttpSetTimeouts**](/windows/win32/Winhttp/nf-winhttp-winhttpsettimeouts?branch=master)
</dt> <dd>

Sets the various time-outs that are involved with HTTP transactions.

</dd> <dt>

[**WinHttpTimeFromSystemTime**](/windows/win32/Winhttp/nf-winhttp-winhttptimefromsystemtime?branch=master)
</dt> <dd>

Formats a date and time according to the HTTP version 1.0 specification.

</dd> <dt>

[**WinHttpTimeToSystemTime**](/windows/win32/Winhttp/nf-winhttp-winhttptimetosystemtime?branch=master)
</dt> <dd>

Takes an HTTP time/date string and converts it to a [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure.

</dd> <dt>

[**WinHttpWriteData**](/windows/win32/Winhttp/nf-winhttp-winhttpwritedata?branch=master)
</dt> <dd>

Writes request data to an HTTP server.

</dd> <dt>

[**WinHttpWebSocketClose**](/windows/win32/winhttp/nf-winhttp-winhttpwebsocketclose?branch=master)
</dt> <dd>

Closes a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketCompleteUpgrade**](/windows/win32/winhttp/nf-winhttp-winhttpwebsocketcompleteupgrade?branch=master)
</dt> <dd>

Completes a WebSocket handshake started by [**WinHttpSendRequest**](/windows/win32/Winhttp/nf-winhttp-winhttpsendrequest?branch=master).

</dd> <dt>

[**WinHttpWebSocketQueryCloseStatus**](/windows/win32/winhttp/nf-winhttp-winhttpwebsocketqueryclosestatus?branch=master)
</dt> <dd>

Gets the close status sent by a server.

</dd> <dt>

[**WinHttpWebSocketReceive**](/windows/win32/winhttp/nf-winhttp-winhttpwebsocketreceive?branch=master)
</dt> <dd>

Receives data from a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketSend**](/windows/win32/winhttp/nf-winhttp-winhttpwebsocketsend?branch=master)
</dt> <dd>

Sends data over a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketShutdown**](/windows/win32/winhttp/nf-winhttp-winhttpwebsocketshutdown?branch=master)
</dt> <dd>

Sends a close frame to a WebSocket connection.

</dd> </dl>

 

 



