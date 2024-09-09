---
description: This topic identifies the functions that WinHTTP provides.
ms.assetid: dcb56d5d-ed0d-49bb-95bf-940a49c033f1
title: WinHTTP Functions
ms.topic: article
ms.date: 05/31/2018
---

# WinHTTP Functions

WinHTTP provides the following functions:

<dl> <dt>

[**WinHttpAddRequestHeaders**](/windows/win32/api/winhttp/nf-winhttp-winhttpaddrequestheaders)
</dt> <dd>

Adds one or more HTTP request headers to the HTTP request handle.

</dd> <dt>

[**WinHttpAddRequestHeadersEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpaddrequestheadersex)
</dt> <dd>

Adds one or more HTTP request headers to an HTTP request handle, allowing you to use separate name/value strings.

</dd> <dt>

[**WinHttpCheckPlatform**](/windows/win32/api/winhttp/nf-winhttp-winhttpcheckplatform)
</dt> <dd>

Determines whether the current platform is supported by WinHTTP.

</dd> <dt>

[**WinHttpCloseHandle**](/windows/win32/api/winhttp/nf-winhttp-winhttpclosehandle)
</dt> <dd>

Closes a single [HINTERNET](hinternet-handles-in-winhttp.md) handle.

</dd> <dt>

[**WinHttpConnect**](/windows/win32/api/winhttp/nf-winhttp-winhttpconnect)
</dt> <dd>

Specifies the initial target server of an HTTP request.

</dd> <dt>

[**WinHttpCrackUrl**](/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
</dt> <dd>

Separates a URL into its component parts, for example, host name and path.

</dd> <dt>

[**WinHttpCreateProxyResolver**](/windows/win32/api/winhttp/nf-winhttp-winhttpcreateproxyresolver)
</dt> <dd>

Creates a handle for use by [**WinHttpGetProxyForUrlEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyforurlex).

</dd> <dt>

[**WinHttpCreateUrl**](/windows/win32/api/winhttp/nf-winhttp-winhttpcreateurl)
</dt> <dd>

Creates a URL from component parts, for example, the host name and path.

</dd> <dt>

[**WinHttpDetectAutoProxyConfigUrl**](/windows/win32/api/winhttp/nf-winhttp-winhttpdetectautoproxyconfigurl)
</dt> <dd>

Finds the URL for the Proxy Auto-Configuration (PAC) file. This function reports the URL of the PAC file, but it does not download the file.

</dd> <dt>

[**WinHttpFreeProxyResult**](/windows/win32/api/winhttp/nf-winhttp-winhttpfreeproxyresult)
</dt> <dd>

Frees the data retrieved from a previous call to [**WinHttpGetProxyResult**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyresult).

</dd> <dt>

[**WinHttpFreeProxySettingsEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpfreeproxysettingsex)
</dt> <dd>

Frees the data retrieved from a previous call to [WinHttpGetProxySettingsResultEx](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxysettingsresultex).

</dd> <dt>

[**WinHttpFreeQueryConnectionGroupResult**](/windows/win32/api/winhttp/nf-winhttp-winhttpfreequeryconnectiongroupresult)
</dt> <dd>

Frees the memory allocated by a previous call to [WinHttpQueryConnectionGroup](/windows/win32/api/winhttp/nf-winhttp-winhttpqueryconnectiongroup).

</dd> <dt>

[**WinHttpGetDefaultProxyConfiguration**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetdefaultproxyconfiguration)
</dt> <dd>

Retrieves the default WinHTTP proxy configuration from the registry.

</dd> <dt>

[**WinHTTPGetIEProxyConfigForCurrentUser**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser)
</dt> <dd>

Obtains the Internet Explorer (IE) proxy configuration for the current user.

</dd> <dt>

[**WinHttpGetProxyForUrl**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyforurl)
</dt> <dd>

Retrieves the proxy information for the specified URL.

</dd> <dt>

[**WinHttpGetProxyForUrlEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyforurlex)

</dt> <dd>

Retrieves the proxy information for the specified URL.

</dd> <dt>

[**WinHttpGetProxyResult**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyresult)
</dt> <dd>

Retrieves the results of a call to [**WinHttpGetProxyForUrlEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxyforurlex).

</dd> <dt>

[**WinHttpGetProxySettingsEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxysettingsex)
</dt> <dd>

Retrieves extended proxy settings.

</dd> <dt>

[**WinHttpGetProxySettingsResultEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxysettingsresultex)
</dt> <dd>

Retrieves the results of a call to [WinHttpGetProxySettingsEx](/windows/win32/api/winhttp/nf-winhttp-winhttpgetproxysettingsex).

</dd> <dt>

[**WinHttpOpen**](/windows/win32/api/winhttp/nf-winhttp-winhttpopen)
</dt> <dd>

Initializes an application's use of the WinHTTP functions.

</dd> <dt>

[**WinHttpOpenRequest**](/windows/win32/api/winhttp/nf-winhttp-winhttpopenrequest)
</dt> <dd>

Creates an HTTP request handle.

</dd> <dt>

[**WinHttpQueryAuthSchemes**](/windows/win32/api/winhttp/nf-winhttp-winhttpqueryauthschemes)
</dt> <dd>

Returns the authorization schemes that the server supports.

</dd> <dt>

[**WinHttpQueryConnectionGroup**](/windows/win32/api/winhttp/nf-winhttp-winhttpqueryconnectiongroup)
</dt> <dd>

Retrieves a description of the current state of WinHttp's connections.

</dd> <dt>

[**WinHttpQueryDataAvailable**](/windows/win32/api/winhttp/nf-winhttp-winhttpquerydataavailable)
</dt> <dd>

Returns the number of bytes of data that are available immediately to be read with [**WinHttpReadData**](/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata).

</dd> <dt>

[**WinHttpQueryHeaders**](/windows/win32/api/winhttp/nf-winhttp-winhttpqueryheaders)
</dt> <dd>

Retrieves header information associated with an HTTP request.

</dd> <dt>

[**WinHttpQueryHeadersEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpqueryheadersex)
</dt> <dd>

Retrieves header information associated with an HTTP request; offers a way to retrieve parsed header name and value strings.

</dd> <dt>

[**WinHttpQueryOption**](/windows/win32/api/winhttp/nf-winhttp-winhttpqueryoption)
</dt> <dd>

Queries an Internet option on the specified handle.

</dd> <dt>

[**WinHttpReadData**](/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata)
</dt> <dd>

Reads data from a handle opened by the [**WinHttpOpenRequest**](/windows/win32/api/winhttp/nf-winhttp-winhttpopenrequest) function.

</dd> <dt>

[**WinHttpReadDataEx**](/windows/win32/api/winhttp/nf-winhttp-winhttpreaddataex)
</dt> <dd>

Reads data from a handle opened by the [**WinHttpOpenRequest**](/windows/win32/api/winhttp/nf-winhttp-winhttpopenrequest) function.

</dd> <dt>

[**WinHttpReceiveResponse**](/windows/win32/api/winhttp/nf-winhttp-winhttpreceiveresponse)
</dt> <dd>

Ends an HTTP request that is initiated by [**WinHttpSendRequest**](/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest).

</dd> <dt>

[**WinHttpRegisterProxyChangeNotification**](/windows/win32/api/winhttp/nf-winhttp-winhttpregisterproxychangenotification)
</dt> <dd>

Registers a callback function that WinHTTP calls when the effective proxy settings change.

</dd> <dt>

[**WinHttpResetAutoProxy**](/windows/win32/api/winhttp/nf-winhttp-winhttpresetautoproxy)
</dt> <dd>

Resets the auto-proxy.

</dd> <dt>

[**WinHttpSendRequest**](/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
</dt> <dd>

Sends the specified request to the HTTP server.

</dd> <dt>

[**WinHttpSetCredentials**](/windows/win32/api/winhttp/nf-winhttp-winhttpsetcredentials)
</dt> <dd>

Passes the required authorization credentials to the server.

</dd> <dt>

[**WinHttpSetDefaultProxyConfiguration**](/windows/win32/api/winhttp/nf-winhttp-winhttpsetdefaultproxyconfiguration)
</dt> <dd>

Sets the default WinHTTP proxy configuration in the registry.

</dd> <dt>

[**WinHttpSetOption**](/windows/win32/api/winhttp/nf-winhttp-winhttpsetoption)
</dt> <dd>

Sets an Internet option.

</dd> <dt>

[**WinHttpSetStatusCallback**](/windows/win32/api/winhttp/nf-winhttp-winhttpsetstatuscallback)
</dt> <dd>

Sets up a callback function that WinHTTP can call as progress is made during an operation.

</dd> <dt>

[**WinHttpSetTimeouts**](/windows/win32/api/winhttp/nf-winhttp-winhttpsettimeouts)
</dt> <dd>

Sets the various time-outs that are involved with HTTP transactions.

</dd> <dt>

[**WinHttpTimeFromSystemTime**](/windows/win32/api/winhttp/nf-winhttp-winhttptimefromsystemtime)
</dt> <dd>

Formats a date and time according to the HTTP version 1.0 specification.

</dd> <dt>

[**WinHttpTimeToSystemTime**](/windows/win32/api/winhttp/nf-winhttp-winhttptimetosystemtime)
</dt> <dd>

Takes an HTTP time/date string and converts it to a [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure.

</dd> <dt>

[**WinHttpUnregisterProxyChangeNotification**](/windows/win32/api/winhttp/nf-winhttp-winhttpunregisterproxychangenotification)
</dt> <dd>

Unregisters a callback function that was registered by calling [WinHttpRegisterProxyChangeNotification](/windows/win32/api/winhttp/nf-winhttp-winhttpregisterproxychangenotification).

</dd> <dt>

[**WinHttpWriteData**](/windows/win32/api/winhttp/nf-winhttp-winhttpwritedata)
</dt> <dd>

Writes request data to an HTTP server.

</dd> <dt>

[**WinHttpWebSocketClose**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketclose)
</dt> <dd>

Closes a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketCompleteUpgrade**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketcompleteupgrade)
</dt> <dd>

Completes a WebSocket handshake started by [**WinHttpSendRequest**](/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest).

</dd> <dt>

[**WinHttpWebSocketQueryCloseStatus**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketqueryclosestatus)
</dt> <dd>

Gets the close status sent by a server.

</dd> <dt>

[**WinHttpWebSocketReceive**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketreceive)
</dt> <dd>

Receives data from a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketSend**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketsend)
</dt> <dd>

Sends data over a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketShutdown**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketshutdown)
</dt> <dd>

Sends a close frame to a WebSocket connection.

</dd> </dl>


