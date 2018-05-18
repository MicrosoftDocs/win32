---
Description: 'This topic identifies the functions that WinHTTP provides.'
ms.assetid: 'dcb56d5d-ed0d-49bb-95bf-940a49c033f1'
title: WinHTTP Functions
---

# WinHTTP Functions

WinHTTP provides the following functions:

<dl> <dt>

[**WinHttpAddRequestHeaders**](winhttpaddrequestheaders.md)
</dt> <dd>

Adds one or more HTTP request headers to the HTTP request handle.

</dd> <dt>

[**WinHttpCheckPlatform**](winhttpcheckplatform.md)
</dt> <dd>

Determines whether the current platform is supported by WinHTTP.

</dd> <dt>

[**WinHttpCloseHandle**](winhttpclosehandle.md)
</dt> <dd>

Closes a single [HINTERNET](hinternet-handles-in-winhttp.md) handle.

</dd> <dt>

[**WinHttpConnect**](winhttpconnect.md)
</dt> <dd>

Specifies the initial target server of an HTTP request.

</dd> <dt>

[**WinHttpCrackUrl**](winhttpcrackurl.md)
</dt> <dd>

Separates a URL into its component parts, for example, host name and path.

</dd> <dt>

[**WinHttpCreateProxyResolver**](winhttpcreateproxyresolver.md)
</dt> <dd>

Creates a handle for use by [**WinHttpGetProxyForUrlEx**](winhttpgetproxyforurlex.md).

</dd> <dt>

[**WinHttpCreateUrl**](winhttpcreateurl.md)
</dt> <dd>

Creates a URL from component parts, for example, the host name and path.

</dd> <dt>

[**WinHttpDetectAutoProxyConfigUrl**](winhttpdetectautoproxyconfigurl.md)
</dt> <dd>

Finds the URL for the Proxy Auto-Configuration (PAC) file. This function reports the URL of the PAC file, but it does not download the file.

</dd> <dt>

[**WinHttpFreeProxyResult**](winhttpfreeproxyresult.md)
</dt> <dd>

Frees the data retrieved from a previous call to [**WinHttpGetProxyResult**](winhttpgetproxyresult.md).

</dd> <dt>

[**WinHttpGetDefaultProxyConfiguration**](winhttpgetdefaultproxyconfiguration.md)
</dt> <dd>

Retrieves the default WinHTTP proxy configuration from the registry.

</dd> <dt>

[**WinHTTPGetIEProxyConfigForCurrentUser**](winhttpgetieproxyconfigforcurrentuser.md)
</dt> <dd>

Obtains the Internet Explorer (IE) proxy configuration for the current user.

</dd> <dt>

[**WinHttpGetProxyForUrl**](winhttpgetproxyforurl.md)
</dt> <dd>

Retrieves the proxy information for the specified URL.

</dd> <dt>

[**WinHttpGetProxyForUrlEx**](winhttpgetproxyforurlex.md)
</dt> <dd>

Retrieves the proxy information for the specified URL.

</dd> <dt>

[**WinHttpGetProxyResult**](winhttpgetproxyresult.md)
</dt> <dd>

Retrieves the results of a call to [**WinHttpGetProxyForUrlEx**](winhttpgetproxyforurlex.md).

</dd> <dt>

[**WinHttpOpen**](winhttpopen.md)
</dt> <dd>

Initializes an application's use of the WinHTTP functions.

</dd> <dt>

[**WinHttpOpenRequest**](winhttpopenrequest.md)
</dt> <dd>

Creates an HTTP request handle.

</dd> <dt>

[**WinHttpQueryAuthSchemes**](winhttpqueryauthschemes.md)
</dt> <dd>

Returns the authorization schemes that the server supports.

</dd> <dt>

[**WinHttpQueryDataAvailable**](winhttpquerydataavailable.md)
</dt> <dd>

Returns the number of bytes of data that are available immediately to be read with [**WinHttpReadData**](winhttpreaddata.md).

</dd> <dt>

[**WinHttpQueryHeaders**](winhttpqueryheaders.md)
</dt> <dd>

Retrieves header information associated with an HTTP request.

</dd> <dt>

[**WinHttpQueryOption**](winhttpqueryoption.md)
</dt> <dd>

Queries an Internet option on the specified handle.

</dd> <dt>

[**WinHttpReadData**](winhttpreaddata.md)
</dt> <dd>

Reads data from a handle opened by the [**WinHttpOpenRequest**](winhttpopenrequest.md) function.

</dd> <dt>

[**WinHttpReceiveResponse**](winhttpreceiveresponse.md)
</dt> <dd>

Ends an HTTP request that is initiated by [**WinHttpSendRequest**](winhttpsendrequest.md).

</dd> <dt>

[**WinHttpResetAutoProxy**](winhttpresetautoproxy.md)
</dt> <dd>

Resets the auto-proxy.

</dd> <dt>

[**WinHttpSendRequest**](winhttpsendrequest.md)
</dt> <dd>

Sends the specified request to the HTTP server.

</dd> <dt>

[**WinHttpSetCredentials**](winhttpsetcredentials.md)
</dt> <dd>

Passes the required authorization credentials to the server.

</dd> <dt>

[**WinHttpSetDefaultProxyConfiguration**](winhttpsetdefaultproxyconfiguration.md)
</dt> <dd>

Sets the default WinHTTP proxy configuration in the registry.

</dd> <dt>

[**WinHttpSetOption**](winhttpsetoption.md)
</dt> <dd>

Sets an Internet option.

</dd> <dt>

[**WinHttpSetStatusCallback**](winhttpsetstatuscallback.md)
</dt> <dd>

Sets up a callback function that WinHTTP can call as progress is made during an operation.

</dd> <dt>

[**WinHttpSetTimeouts**](winhttpsettimeouts.md)
</dt> <dd>

Sets the various time-outs that are involved with HTTP transactions.

</dd> <dt>

[**WinHttpTimeFromSystemTime**](winhttptimefromsystemtime.md)
</dt> <dd>

Formats a date and time according to the HTTP version 1.0 specification.

</dd> <dt>

[**WinHttpTimeToSystemTime**](winhttptimetosystemtime.md)
</dt> <dd>

Takes an HTTP time/date string and converts it to a [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure.

</dd> <dt>

[**WinHttpWriteData**](winhttpwritedata.md)
</dt> <dd>

Writes request data to an HTTP server.

</dd> <dt>

[**WinHttpWebSocketClose**](winhttpwebsocketclose.md)
</dt> <dd>

Closes a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketCompleteUpgrade**](winhttpwebsocketcompleteupgrade.md)
</dt> <dd>

Completes a WebSocket handshake started by [**WinHttpSendRequest**](winhttpsendrequest.md).

</dd> <dt>

[**WinHttpWebSocketQueryCloseStatus**](winhttpwebsocketqueryclosestatus.md)
</dt> <dd>

Gets the close status sent by a server.

</dd> <dt>

[**WinHttpWebSocketReceive**](winhttpwebsocketreceive.md)
</dt> <dd>

Receives data from a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketSend**](winhttpwebsocketsend.md)
</dt> <dd>

Sends data over a WebSocket connection.

</dd> <dt>

[**WinHttpWebSocketShutdown**](winhttpwebsocketshutdown.md)
</dt> <dd>

Sends a close frame to a WebSocket connection.

</dd> </dl>

 

 



