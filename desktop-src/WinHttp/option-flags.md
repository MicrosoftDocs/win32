---
title: Option flags (Winhttp.h)
description: The following option flags are supported by [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption) and [**WinHttpSetOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetoption).
ms.assetid: 2d0441f4-ddba-4f2a-8861-8803cad6f1ac
ms.topic: reference
ms.custom: snippet-project
ms.date: 06/20/2022
---

# Option flags

The following option flags are supported by [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption) and [**WinHttpSetOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetoption).

## WINHTTP_OPTION_ASSURED_NON_BLOCKING_CALLBACKS

The default is FALSE. If set to TRUE, WinHTTP doesn't guarantee progress if status callbacks are blocked by the client application.

The client application must take special care to perform minimal operations within the callback without blocking, returning as quickly as possible, and in particular must not wait for any subsequent WinHTTP calls. If it doesn't follow these guidelines, there is likely to be a negative performance impact or a potential application hang. If used in the prescribed manner, this option may improve performance.

## WINHTTP_OPTION_AUTOLOGON_POLICY

Sets an unsigned long integer value that specifies the [Automatic Logon Policy](authentication-in-winhttp.md) with one of the following values.

| Term | Description |
|-|-|
| <span id="WINHTTP_AUTOLOGON_SECURITY_LEVEL_HIGH"></span><span id="winhttp_autologon_security_level_high"></span>WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_HIGH | Default credentials are not used. Note that this flag takes effect only if you specify the server by the actual machine name. It will not take effect, if you specify the server by "localhost" or IP address. |
| <span id="WINHTTP_AUTOLOGON_SECURITY_LEVEL_LOW"></span><span id="winhttp_autologon_security_level_low"></span>WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_LOW | An authenticated log on using the default credentials is performed for all requests. |
| <span id="WINHTTP_AUTOLOGON_SECURITY_LEVEL_MEDIUM"></span><span id="winhttp_autologon_security_level_medium"></span>WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_MEDIUM | An authenticated log on using the default credentials is performed only for requests on the local Intranet. |

## WINHTTP_OPTION_BACKGROUND_CONNECTIONS

When you set this option on a session handle, you must pass the number of connections you wish to open. Then, upon first sending a request, rather than opening only a single connection, WinHttp opens a number of connections in parallel. This can improve the performance of subsequent requests to the same destination, which won't have the overhead of connection establishment.

## WINHTTP_OPTION_CALLBACK

Retrieves the pointer to the callback function set with [**WinHttpSetStatusCallback**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetstatuscallback).

## WINHTTP_OPTION_CLIENT_CERT_CONTEXT

Sets the client certificate context. If an application receives [**ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**](error-messages.md), it must call [**WinHttpSetOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetoption) to supply a certificate before retrying the request. As a part of processing this option, WinHttp calls [**CertDuplicateCertificateContext**](/windows/win32/api/wincrypt/nf-wincrypt-certduplicatecertificatecontext) on the caller-provided certificate context so that the certificate context can be independently released by the caller.

> [!NOTE]
> The application should not attempt to close the certificate store with the CERT\_CLOSE\_STORE\_FORCE\_FLAG flag in the call to [**CertCloseStore**](/windows/win32/api/wincrypt/nf-wincrypt-certclosestore) on the certificate store from which the certificate context was retrieved. An access violation may occur.

When the server requests a client certificate, [**WinHttpSendRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsendrequest), or [**WinHttpReceiveResponse**](/windows/win32/api/Winhttp/nf-winhttp-winhttpreceiveresponse) returns an [**ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**](error-messages.md) error. If the server requests the certificate but doesn't require it, the application can specify this option to indicate that it doesn't have a certificate. The server can choose another authentication scheme or allow anonymous access to the server. The application provides the **WINHTTP\_NO\_CLIENT\_CERT\_CONTEXT** macro in the *lpBuffer* parameter of [**WinHttpSetOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetoption) as shown in the following code example.

``` syntax
BOOL fRet = WinHttpSetOption(hRequest,
                             WINHTTP_OPTION_CLIENT_CERT_CONTEXT,
                             WINHTTP_NO_CLIENT_CERT_CONTEXT,
                             0);
```

If the server requires a client certificate, it may send a 403 HTTP status code in response. For more information, see the **WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST** option.

## WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST

Retrieves a [**SecPkgContext\_IssuerListInfoEx**](/windows/win32/api/schannel/ns-schannel-secpkgcontext_issuerlistinfoex) structure when the error from [**WinHttpSendRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsendrequest) or [**WinHttpReceiveResponse**](/windows/win32/api/Winhttp/nf-winhttp-winhttpreceiveresponse) is **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**. The issuer list in the structure contains a list of acceptable Certificate Authorities (CA) from the server. The client application can filter the CA list to retrieve the client certificate for SSL authentication.

Alternately, if the server requests the client certificate, but doesn't require it, the application can call [**WinHttpSetOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetoption) with the **WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT** option. For more information, see the **WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT** option.

## WINHTTP_OPTION_CODEPAGE

Sets the [*code page*](glossary.md) that is used to process the URL (that is, query string). The default is UTF8.

## WINHTTP_OPTION_CONFIGURE_PASSPORT_AUTH

Sets an unsigned long integer value that specifies whether [Passport Authentication in WinHTTP](passport-authentication-in-winhttp.md) authentication is enabled. The value can be one of the following:

| Term | Description |
|-|-|
| <span id="WINHTTP_DISABLE_PASSPORT_AUTH"></span><span id="winhttp_disable_passport_auth"></span>WINHTTP\_DISABLE\_PASSPORT\_AUTH | Microsoft Passport authentication is disabled. This is the default. |
| <span id="WINHTTP_DISABLE_PASSPORT_KEYRING"></span><span id="winhttp_disable_passport_keyring"></span>WINHTTP\_DISABLE\_PASSPORT\_KEYRING | The Passport keyring is disabled. This is the default. |
| <span id="WINHTTP_ENABLE_PASSPORT_AUTH"></span><span id="winhttp_enable_passport_auth"></span>WINHTTP\_ENABLE\_PASSPORT\_AUTH | Passport authentication is enabled. |
| <span id="WINHTTP_ENABLE_PASSPORT_KEYRING"></span><span id="winhttp_enable_passport_keyring"></span>WINHTTP\_ENABLE\_PASSPORT\_KEYRING | The Passport keyring is enabled. |

## WINHTTP_OPTION_CONNECT_RETRIES

Sets or retrieves an unsigned long integer value that contains the number of timesWinHTTP attempts to connect to a host. Microsoft Windows HTTP Services (WinHTTP) only attempts once per Internet Protocol (IP) address. For example, if you attempt to connect to a multihomed host that has 10 IP addresses and **WINHTTP\_OPTION\_CONNECT\_RETRIES** is set to 7, then WinHTTP only attempts to connect to the first seven IP address. Given the same set of 10 IP addresses, if **WINHTTP\_OPTION\_CONNECT\_RETRIES** is set to 20, WinHTTP attempts each of the 10 only once. If a connection attempt still fails after the specified number of attempts, or if the connect timeout expired before then, the request is canceled. The default value for **WINHTTP\_OPTION\_CONNECT\_RETRIES** is five attempts.

## WINHTTP_OPTION_CONNECT_TIMEOUT

Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds. Setting this option to infinite (0xFFFFFFFF) will disable this timer.

If a TCP connection request takes longer than this time-out value, the request is canceled. The default timeout is 60 seconds. When you are attempting to connect to multiple IP addresses for a single host (a multihomed host), the timeout limit is for each individual connection.

## WINHTTP_OPTION_CONNECTION_INFO

Retrieves the source and destination IP address, and port of the request that generated the response when [**WinHttpReceiveResponse**](/windows/win32/api/Winhttp/nf-winhttp-winhttpreceiveresponse) returns. The application calls [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption) with the **WINHTTP\_OPTION\_CONNECTION\_INFO** option, and provides the [**WINHTTP\_CONNECTION\_INFO**](/windows/win32/api/Winhttp/ns-winhttp-winhttp_connection_info) structure in the *lpBuffer* parameter. For more information, see **WINHTTP\_CONNECTION\_INFO**.

**Windows Server 2003 with SP1 and Windows XP with SP2:** This flag is obsolete.

## WINHTTP_OPTION_CONNECTION_GUID

Mark the connection associated with the WinHTTP request handle with a GUID. This allows custom control over which requests use which groups of connections with the **WINHTTP_OPTION_MATCH_CONNECTION_GUID** option.

## WINHTTP_OPTION_CONNECTION_STATS_V0

Retreives the [**TCP\_INFO\_v0**](/windows/win32/api/mstcpip/ns-mstcpip-tcp_info_v0) struct for the underlying connection used by the request. The returned struct may contain statistics from prior requests sent over the same connection.

> [!NOTE]
> This option has been superseded by **WINHTTP\_OPTION\_CONNECTION\_STATS\_V1**.

## WINHTTP_OPTION_CONNECTION_STATS_V1

Retreives the [**TCP\_INFO\_v1**](/windows/win32/api/mstcpip/ns-mstcpip-tcp_info_v1) struct for the underlying connection used by the request. The returned struct may contain statistics from prior requests sent over the same connection.

## WINHTTP_OPTION_CONTEXT_VALUE

Sets or retrieves a **DWORD\_PTR** that contains a pointer to the context value associated with this [HINTERNET](hinternet-handles-in-winhttp.md) handle. The value stored in the buffer is used and the **WINHTTP\_OPTION\_CONTEXT\_VALUE** option flag is assigned a new value.

## WINHTTP_OPTION_DECOMPRESSION

Sets a DWORD of flags which determine whether WinHTTP will automatically decompress response bodies with compressed Content-Encodings. WinHTTP will also set an appropriate Accept-Encoding header, overriding any supplied by the caller. Supported values are:

| Term | Description |
|-|-|
| <span id="WINHTTP_DECOMPRESSION_FLAG_GZIP"></span><span id="winhttp_decompression_flag_gzip"></span>WINHTTP\_DECOMPRESSION\_FLAG\_GZIP | Decompress Content-Encoding: gzip responses. |
| <span id="WINHTTP_DECOMPRESSION_FLAG_DEFLATE"></span><span id="winhttp_decompression_flag_deflate"></span>WINHTTP\_DECOMPRESSION\_FLAG\_DEFLATE | Decompress Content-Encoding: deflate responses. |
| <span id="WINHTTP_DECOMPRESSION_FLAG_ALL"></span><span id="winhttp_decompression_flag_all"></span>WINHTTP\_DECOMPRESSION\_FLAG\_ALL | Decompress responses with any supported Content-Encoding. |

By default, WinHTTP will deliver compressed responses to the caller unmodified.

## WINHTTP_OPTION_DISABLE_CERT_CHAIN_BUILDING

Setting this option on a WinHttp session handle allows you to enable/disable whether the server certificate chain is built.

## WINHTTP_OPTION_DISABLE_FEATURE

Sets an unsigned long integer value that specifies which features are disabled with one or more of the following flags. Be aware that this feature should only be passed to [**WinHttpSetOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetoption) on request handles after the request handle is created with [**WinHttpOpenRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpopenrequest), and before the request is sent with [**WinHttpSendRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsendrequest).

| Term | Description |
|-|-|
| <span id="WINHTTP_DISABLE_AUTHENTICATION"></span><span id="winhttp_disable_authentication"></span>WINHTTP\_DISABLE\_AUTHENTICATION | Automatic authentication is disabled. |
| <span id="WINHTTP_DISABLE_COOKIES"></span><span id="winhttp_disable_cookies"></span>WINHTTP\_DISABLE\_COOKIES | Automatic addition of cookie headers to requests is disabled. Also, returned cookies are not automatically added to the cookie database. Disabling cookies can result in poor performance for Passport authentication. |
| <span id="WINHTTP_DISABLE_KEEP_ALIVE"></span><span id="winhttp_disable_keep_alive"></span>WINHTTP\_DISABLE\_KEEP\_ALIVE | Disables keep-alive semantics for the connection. Keep-alive semantics are required for MSN, NTLM, and other types of authentication. |
| <span id="WINHTTP_DISABLE_REDIRECTS"></span><span id="winhttp_disable_redirects"></span>WINHTTP\_DISABLE\_REDIRECTS | Automatic redirection is disabled when sending requests with [**WinHttpSendRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsendrequest). If automatic redirection is disabled, an application must register a callback function in order for Passport authentication to succeed. |

## WINHTTP_OPTION_DISABLE_GLOBAL_POOLING

Disables global, cross-session pooling. This is recommended practice because global, cross-session pooling is legacy behavior that's supported by default for compatibility reasons. This is impacted by later setting max connections manually.

## WINHTTP_OPTION_DISABLE_PROXY_AUTH_SCHEMES

Disables one or more of the following proxy authentication practices on the WinHTTP session by providing the `OR` of all applicable choices. These are all schemes, except for **WINHTTP_PROXY_DISABLE_AUTH_LOCAL_SERVICE**, which forces the use of the local machine account when sending requests to a loopback or local address. That prevents leaking system credentials to local HTTP proxies.

| Term | Description |
| - | - |
| WINHTTP_PROXY_DISABLE_SCHEME_BASIC | Disables the Basic authentication scheme. |
| WINHTTP_PROXY_DISABLE_SCHEME_DIGEST | Disables the Digest authentication scheme. |
| WINHTTP_PROXY_DISABLE_SCHEME_NTLM | Disables the NTLM authentication scheme. |
| WINHTTP_PROXY_DISABLE_SCHEME_KERBEROS | Disables the Kerberos authentication scheme. |
| WINHTTP_PROXY_DISABLE_SCHEME_NEGOTIATE | Disables the Negotiate authentication scheme. |
| WINHTTP_PROXY_DISABLE_AUTH_LOCAL_SERVICE | Forces the use of the local machine account when sending requests to a loopback or local address. |

## WINHTTP_OPTION_DISABLE_SECURE_PROTOCOL_FALLBACK

Prevents WinHTTP from retrying a connection with a lower version of the security protocol when the initial protocol negotiation fails.

## WINHTTP_OPTION_DISABLE_STREAM_QUEUE

Allows new requests to open an additional HTTP/2 connection when the maximum concurrent stream limit is reached, rather than waiting for the next available stream on an existing connection.

## WINHTTP_OPTION_ENABLE_FEATURE

Sets an unsigned long integer value that specifies the features currently enabled. Can be one of the following values.

| Term | Description |
|-|-|
| <span id="WINHTTP_ENABLE_SSL_REVERT_IMPERSONATION"></span><span id="winhttp_enable_ssl_revert_impersonation"></span>WINHTTP\_ENABLE\_SSL\_REVERT\_IMPERSONATION | If enabled, WinHTTP temporarily reverts client impersonation for the duration of SSL certificate authentication operations. This value can be set only on the session handle. |
| <span id="WINHTTP_ENABLE_SSL_REVOCATION"></span><span id="winhttp_enable_ssl_revocation"></span>WINHTTP\_ENABLE\_SSL\_REVOCATION | If enabled, WinHTTP allows SSL revocation. This value can be set only on the request handle. |

## WINHTTP_OPTION_ENABLE_HTTP_PROTOCOL

Sets a DWORD bitmask of acceptable advanced HTTP versions. Possible values are:

| Term | Description |
|-|-|
| WINHTTP\_PROTOCOL\_FLAG\_HTTP2 (0x1) | Enables HTTP/2 for the request. |
| WINHTTP\_PROTOCOL\_FLAG\_HTTP3 (0x2) | Enables HTTP/3 for the request. |
| None (0x0) | Restricts the request to HTTP/1.1 and prior. |

Legacy versions of HTTP (1.1 and prior) can't be disabled using this option. The default is 0x0.

## WINHTTP_OPTION_ENABLE_HTTP2_PLUS_CLIENT_CERT

This option can be set on a WinHttp session handle to allow WinHttp to use the caller-provided client certificate context when HTTP/2 is being used.

## WINHTTP_OPTION_ENABLETRACING

Sets a **BOOL** value that specifies whether tracing is currently enabled. For more information about the trace facility in WinHTTP, see [WinHTTP Trace Facility](winhttptracecfg-exe--a-trace-configuration-tool.md). This option can only be set on a **NULL** **HINTERNET** handle.

## WINHTTP_OPTION_ENCODE_EXTRA

Enables URL percent encoding for path and query string.

Alternatively, you can percent encode before calling WinHttp.

## WINHTTP_OPTION_EXPIRE_CONNECTION

This option can only be set on a request handle which is still active (sending or receiving). Setting this option will tell WinHttp to stop serving requests on the connection associated with the request handle passed in. The connection will be closed after the request handle this option is called with is completed. This option doesn't take any parameters.

## WINHTTP_OPTION_EXTENDED_ERROR

Retrieves an unsigned long integer value that contains a Microsoft Windows Sockets error code that was mapped to the ERROR\_WINHTTP\_\* error messages last returned in this thread context. You can pass **NULL** as the handle value.

## WINHTTP_OPTION_FEATURE_SUPPORTED

Check to see whether a provided option flag is supported by this version of WinHTTP.

## WINHTTP_OPTION_FIRST_AVAILABLE_CONNECTION

By default, when WinHttp sends a request, if there are no available connections to serve the request, WinHttp will attempt to establish a new connection, and the request will be bound to this new connection. When you set this option, such a request will instead be served on the first connection that becomes available, and not necessarily the one being established.

## WINHTTP_OPTION_GLOBAL_PROXY_CREDS

Takes a pointer to a [**WINHTTP\_CREDS\_EX**](/windows/win32/api/winhttp/ns-winhttp-winhttp_creds_ex) structure with the *hInternet* function parameter set to **NULL**. This option requires registry key **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings!ShareCredsWithWinHttp**. If this registry key is not set WinHTTP will return error **ERROR\_WINHTTP\_INVALID\_OPTION**. This registry key is not present by default. When it is set, WinINet will send credentials down to WinHTTP. Whenever WinHttp gets an authentication challenge and if there are no credentials set on the current handle, it will use the credentials provided by WinINet. In order to share server credentials in addition to proxy credentials, users needs to set **WINHTTP\_OPTION\_USE\_GLOBAL\_SERVER\_CREDENTIALS** .

## WINHTTP_OPTION_GLOBAL_SERVER_CREDS

Takes a pointer to a [**WINHTTP\_CREDS\_EX**](/windows/win32/api/winhttp/ns-winhttp-winhttp_creds_ex) structure with the *hInternet* function parameter set to **NULL**. This option requires registry key **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings!ShareCredsWithWinHttp**. If this registry key is not set WinHTTP will return error **ERROR\_WINHTTP\_INVALID\_OPTION**. This registry key is not present by default. When it is set, WinINet will send credentials down to WinHTTP. Whenever WinHttp gets an authentication challenge and if there are no credentials set on the current handle, it will use the credentials provided by WinINet. In order to share server credentials in addition to proxy credentials, users needs to set **WINHTTP\_OPTION\_USE\_GLOBAL\_SERVER\_CREDENTIALS** .

## WINHTTP_OPTION_HANDLE_TYPE

Retrieves an unsigned long integer value that contains the type of the [HINTERNET](hinternet-handles-in-winhttp.md) handle passed in. The return value can be one of the following:

| Term | Description |
|-|-|
| <span id="WINHTTP_HANDLE_TYPE_CONNECT"></span><span id="winhttp_handle_type_connect"></span>WINHTTP\_HANDLE\_TYPE\_CONNECT | The handle is a connection handle. |
| <span id="WINHTTP_HANDLE_TYPE_REQUEST"></span><span id="winhttp_handle_type_request"></span>WINHTTP\_HANDLE\_TYPE\_REQUEST | The handle is a request handle. |
| <span id="WINHTTP_HANDLE_TYPE_SESSION"></span><span id="winhttp_handle_type_session"></span>WINHTTP\_HANDLE\_TYPE\_SESSION | The handle is a session handle. |

## WINHTTP_OPTION_HTTP_PROTOCOL_REQUIRED

Prevents protocol versions other than those enabled by **WINHTTP\_OPTION\_ENABLE\_HTTP\_PROTOCOL** from being used for the request.

## WINHTTP_OPTION_HTTP_PROTOCOL_USED

Gets a DWORD indicating which advanced HTTP version was used on a given request. For a list of possible values, see **WINHTTP\_OPTION\_ENABLE\_HTTP\_PROTOCOL**.

## WINHTTP_OPTION_HTTP_VERSION

Sets or retrieves an [**HTTP\_VERSION\_INFO**](/windows/win32/api/winhttp/ns-winhttp-http_version_info) structure that contains the HTTP version being supported. This is a process-wide option; use **NULL** for the handle.

## WINHTTP_OPTION_HTTP2_KEEPALIVE

This option can be set on a session handle to have WinHttp use HTTP/2 PING frames as a keepalive mechanism. Callers specify a timeout in milliseconds, and after there is no activity on a connection for that timeout period, WinHttp will begin to send HTTP/2 PING frames. Callers cannot set a timeout value less than 5000 milliseconds.

## WINHTTP_OPTION_HTTP2_PLUS_TRANSFER_ENCODING

This option can be set on a WinHttp request handle to control how WinHttp behaves when an HTTP/2 response contains a "Transfer-Encoding" header. In such a case, WinHttp will return an error if this option is set to **FALSE**.

## WINHTTP_OPTION_HTTP2_RECEIVE_WINDOW

Set the initial HTTP/2 stream receive window size and the threshold for sending window updates using the **WINHTTP_HTTP2_RECEIVE_WINDOW** struct.

## WINHTTP_OPTION_HTTP3_HANDSHAKE_TIMEOUT

Uses the buffer to set the HTTP/3 handshake timeout in milliseconds as a PDWORD.
 
## WINHTTP_OPTION_HTTP3_INITIAL_RTT

Configures the initial RTT in milliseconds used by [msquic](https://github.com/microsoft/msquic).
 
## WINHTTP_OPTION_HTTP3_KEEPALIVE

Enables keep-alive semantics for the connection. Uses the buffer to set the keep-alive timeout in milliseconds as a PDWORD.
 
## WINHTTP_OPTION_HTTP3_STREAM_ERROR_CODE

Retrieves the server-provided error on the HTTP/3 stream used to send the request. 

## WINHTTP_OPTION_IGNORE_CERT_REVOCATION_OFFLINE

Allows secure connections to use security certificates for which the certificate revocation list could not be downloaded.

## WINHTTP_OPTION_IPV6_FAST_FALLBACK

Enables IPv6 fast fallback (Happier Eyeballs) for the connection. This behavior is similar to the Happy Eyeballs behavior described in [RFC 6555](https://tools.ietf.org/html/rfc6555) for improving connection times on networks where IPv6 is unreliable.
- If both IPv6 and IPv4 addresses are resolved for a given host, WinHttp will begin by connecting to the first resolved IPv6 address with a short (300ms) timeout.
- Should that connection fail, WinHttp will attempt to connect to the first resolved IPv4 address with the standard timeout.
- Should the second connection fail, WinHttp will retry the first resolved IPv6 address with the standard timeout.
- Should the third connection fail, WinHttp will revert to the default behavior for any remaining addresses, attempting a connection to each one with the standard timeout until a connection is made or no addresses remain.

## WINHTTP_OPTION_IS_PROXY_CONNECT_RESPONSE

Gets whether or not a Proxy Return Connect Response can be retrieved.

## WINHTTP_OPTION_MATCH_CONNECTION_GUID

Takes a [**WINHTTP_MATCH_CONNECTION_GUID**](/windows/win32/api/winhttp/ns-winhttp-winhttp_match_connection_guid) struct to tell WinHTTP to serve the request on a matching connection. If **WINHTTP_MATCH_CONNECTION_GUID_FLAG_REQUIRED** is set, then only connections with a matching GUID can be used. Otherwise, connections with matching GUIDs and connections that are not marked with any GUID can be used.

## WINHTTP_OPTION_MAX_CONNS_PER_1_0_SERVER

Sets or retrieves an unsigned long integer value that contains the maximum number of connections allowed per HTTP/1.0 server. The default value is **INFINITE**.

**Windows Vista with SP1 and Windows Server 2008:** This flag is obsolete.

## WINHTTP_OPTION_MAX_CONNS_PER_SERVER

Sets or retrieves an unsigned long integer value that contains the maximum number of connections allowed per server. The default value is **INFINITE**.

When this option is set to zero, WinHTTP sets the limit on the number of connections to 2.

## WINHTTP_OPTION_MAX_HTTP_AUTOMATIC_REDIRECTS

Sets the maximum number of redirects that WinHTTP follows; the default is 10. This limit prevents unauthorized sites from making the WinHTTP client pause following a large number of redirects.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.

## WINHTTP_OPTION_MAX_HTTP_STATUS_CONTINUE

The maximum number of Informational 100-199 status code responses ignored before returning the final status code to the WinHTTP client. Informational 100-199 status codes can be sent by the server before the final status code, and are described in the specification for HTTP/1.1 (for more information, see [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt)). The default is 10.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.

## WINHTTP_OPTION_MAX_RESPONSE_DRAIN_SIZE

A bound on the amount of data drained from responses in order to reuse a connection, specified in bytes. The default is 1MB.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.

## WINHTTP_OPTION_MAX_RESPONSE_HEADER_SIZE

A bound set on the maximum size of the header portion of the server response, specified in bytes. This bound protects the client from an unauthorized server attempting to stall the client by sending a response with an infinite amount of header data. The default value is 64KB.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.

## WINHTTP_OPTION_PARENT_HANDLE

Retrieves the parent handle to this handle.

## WINHTTP_OPTION_PASSPORT_COBRANDING_TEXT

Retrieves a string that contains the [*cobranding*](glossary.md) text provided by the Passport logon server. This option should be retrieved immediately after the logon server responds with a 401 status code. An application should pass in a buffer size, in bytes, that is big enough to hold the returned string.

## WINHTTP_OPTION_PASSPORT_COBRANDING_URL

Retrieves a string that contains a URL for a [*cobranding*](glossary.md) graphic provided by the Passport logon server. This option should be retrieved immediately after the logon server responds with a 401 status code. An application should pass in a buffer size, in bytes, that is big enough to hold the returned string.

## WINHTTP_OPTION_PASSPORT_RETURN_URL

Sets a read-only option on a request handle that retrieves the Passport return URL.

## WINHTTP_OPTION_PASSPORT_SIGN_OUT

Sets the option on a session handle to sign out of any Passport logins. An application should pass in the Passport return URL that was retrieved with **WINHTTP\_OPTION\_PASSPORT\_RETURN\_URL**. All cookies related to the return URL are cleared.

## WINHTTP_OPTION_PASSWORD

Sets or retrieves a string value that contains the password associated with a request handle.

## WINHTTP_OPTION_PROXY

Sets or retrieves an [**WINHTTP\_PROXY\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info) structure that contains the proxy data on an existing session handle or request handle. When retrieving proxy data, an application must free the **lpszProxy** and **lpszProxyBypass** strings contained in this structure (if they are non-**NULL**) using the [**GlobalFree**](/windows/win32/api/winbase/nf-winbase-globalfree) function. An application can query for the global proxy data (the default proxy) by passing a **NULL** handle.

## WINHTTP_OPTION_PROXY_PASSWORD

Sets or retrieves a string value that contains the password used to access the proxy.

## WINHTTP_OPTION_PROXY_SPN_USED

Gets the proxy Server Principal Name that WinHTTP supplied to SSPI during authentication. This string value is usefor passing to [**SspiPromptForCredentials**](/windows/win32/api/sspi/nf-sspi-sspipromptforcredentialsa) after an authentication failure.

## WINHTTP_OPTION_PROXY_USERNAME

Sets or retrieves a string value that contains the user name used to access the proxy.

## WINHTTP_OPTION_QUIC_STATS

Retrieves a **QUIC_STATISTICS** structure that contains connection information such as RTT and bytes sent and received.

## WINHTTP_OPTION_READ_BUFFER_SIZE

This option is deprecated; it has no effect.

## WINHTTP_OPTION_RECEIVE_PROXY_CONNECT_RESPONSE

Sets whether or not the proxy response entity can be retrieved. This option is disabled by default.

## WINHTTP_OPTION_RECEIVE_RESPONSE_TIMEOUT

Sets or retrieves an unsigned long integer value that contains the timeout value, in milliseconds, to wait to receive all response headers to a request. If WinHTTP fails to receive all the headers within this timeout period, the request is canceled. The default timeout value is 90 seconds.

This timeout is checked only when data is received from the socket. As a result, when the timeout expires the client application is not notified until more data arrives from the server. If no data arrives from the server, the delay between the timeout expiration and notification of the client application could be as large as the timeout value set using the *dwReceiveTimeout* parameter of the [**WinHttpSetTimeouts**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsettimeouts) function.

## WINHTTP_OPTION_RECEIVE_TIMEOUT

Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds, to receive a partial response to a request or read some data. If the response takes longer than this time-out value, the request is canceled. The default timeout value is 30 seconds.

## WINHTTP_OPTION_REDIRECT_POLICY

Sets the behavior of WinHTTP regarding the handling of a 30x HTTP redirect status code. This option can be set on a session or request handle to one of the following values:

| Term | Description |
|-|-|
| <span id="WINHTTP_OPTION_REDIRECT_POLICY_ALWAYS"></span><span id="winhttp_option_redirect_policy_always"></span>WINHTTP\_OPTION\_REDIRECT\_POLICY\_ALWAYS | All redirects are followed automatically. |
| <span id="WINHTTP_OPTION_REDIRECT_POLICY_DISALLOW_HTTPS_TO_HTTP"></span><span id="winhttp_option_redirect_policy_disallow_https_to_http"></span>WINHTTP\_OPTION\_REDIRECT\_POLICY\_DISALLOW\_HTTPS\_TO\_HTTP | All redirects are followed, except those that originate from a secure (https) URL to an unsecure (http) URL. This is the default setting. |
| <span id="WINHTTP_OPTION_REDIRECT_POLICY_NEVER"></span><span id="winhttp_option_redirect_policy_never"></span>WINHTTP\_OPTION\_REDIRECT\_POLICY\_NEVER | Redirects are never followed. The 30x status is returned to the application. |

## WINHTTP_OPTION_REJECT_USERPWD_IN_URL

Rejects URLs that contain a username and password. This option also rejects URLs that contain *username:password* semantics, even if no username or password is specified. For example, "u:p@hostname", ":@hostname", "u:@hostname", and ":p@hostname" would all be flagged as invalid. If an invalid URL is passed to the function, it returns [ERROR\_WINHTTP\_INVALID\_URL](error-messages.md). This option is turned off by default.

## WINHTTP_OPTION_REQUEST_ANNOTATION

Enables getting and setting a request annotation for the provided annotation name. That allows the caller to attach a string to the request for later retrieval to identify requests by whatever custom logic the caller finds useful.

## WINHTTP_OPTION_REQUEST_PRIORITY

This option is deprecated; it has no effect.

## WINHTTP_OPTION_REQUEST_STATS

Retreives statistics for the request.  For a list of the available statistics, see [**WINHTTP\_REQUEST\_STATS**](/windows/win32/api/winhttp/ns-winhttp-winhttp_request_stats).

## WINHTTP_OPTION_REQUEST_TIMES

Retreives timing information for the request. For a list of the available timings, see [**WINHTTP\_REQUEST\_TIMES**](/windows/win32/api/winhttp/ns-winhttp-winhttp_request_times).

## WINHTTP_OPTION_REQUIRE_STREAM_END

This option tells WinHttp to ignore "Content-Length" response headers, and continue receiving on a stream until the END_STREAM flag is received.

## WINHTTP_OPTION_RESOLUTION_HOSTNAME

This option can be set on a WinHttp request handle before it has been sent. If set, WinHttp will use the caller-provided string as the hostname for DNS resolution.

## WINHTTP_OPTION_RESOLVE_TIMEOUT

Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds, to resolve a host name. The default timeout value is **INFINITE**. If a non-default value is specified, there is an overhead of one thread-creation per name resolution.

## WINHTTP_OPTION_REVERT_IMPERSONATION_SERVER_CERT

Reverts any thread impersonation when building the server cert chain, forcing the use of the process token instead.

## WINHTTP_OPTION_SECURE_PROTOCOLS

Sets an unsigned long integer value that specifies which secure protocols are acceptable.

* Windows 11, Windows 10, and Windows 8.1. By default, only SSL3, TLS1.0, TLS1.1, and TLS1.2 are enabled.
* Windows 8 and Windows 7. By default, only SSL3 and TLS1 are enabled.

The value can be a combination of one or more of the following values.

| Term | Description |
|-|-|
| WINHTTP\_FLAG\_SECURE\_PROTOCOL\_ALL | The Secure Sockets Layer (SSL) 2.0, SSL 3.0, and Transport Layer Security (TLS) 1.0 protocols can be used. |
| WINHTTP\_FLAG\_SECURE\_PROTOCOL\_SSL2 | The SSL 2.0 protocol can be used. |
| WINHTTP\_FLAG\_SECURE\_PROTOCOL\_SSL3 | The SSL 3.0 protocol can be used. |
| WINHTTP\_FLAG\_SECURE\_PROTOCOL\_TLS1 | The TLS 1.0 protocol can be used. |
| WINHTTP\_FLAG\_SECURE\_PROTOCOL\_TLS1\_1 | The TLS 1.1 protocol can be used. |
| WINHTTP\_FLAG\_SECURE\_PROTOCOL\_TLS1\_2 | The TLS 1.2 protocol can be used. |
| WINHTTP\_FLAG\_SECURE\_PROTOCOL\_TLS1\_3 | The TLS 1.3 protocol can be used. |

If you need to add support for TLS 1.1 or TLS 1.2 protocols, but you're unable to recompile your application to use the appropriate values of **WINHTTP_OPTION_SECURE_PROTOCOLS**, then you can instead add the `DefaultSecureProtocols` registry entry. That registry entry allows you to specify which SSL protocols should be used when the **WINHTTP_OPTION_SECURE_PROTOCOLS** flag is used.

> [!IMPORTANT]
> The instructions below involve modifying the registry. However, serious problems might occur if you modify the registry incorrectly. Therefore, make sure that you follow these instructions carefully. For added protection, back up the registry before you modify it. Then, you can restore the registry if a problem occurs. For more information about how to back up and restore the registry, see [How to back up and restore the registry in Windows](https://support.microsoft.com/topic/how-to-back-up-and-restore-the-registry-in-windows-855140ad-e318-2a13-2829-d428a2ab0692).

When an application specifies **WINHTTP_OPTION_SECURE_PROTOCOLS**, the system checks for the `DefaultSecureProtocols` registry entry and, if it's present, overrides the default protocols specified by **WINHTTP_OPTION_SECURE_PROTOCOLS** with the protocols specified in the `DefaultSecureProtocols` registry entry. If the registry entry is not present, then WinHTTP uses the existing operating system defaults for WinHTTP. These WinHTTP defaults follow the existing precedence rules, and are overruled by Secure Channel (Schannel) disabled protocols and protocols set per application by [**WinHttpSetOption**](/windows/win32/api/winhttp/nf-winhttp-winhttpsetoption).

You can add the `DefaultSecureProtocols` registry entry in the following path:

**HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp**

On x64-based computers, you must also add `DefaultSecureProtocols` to the `Wow6432Node` path:

**HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp**

The registry value is a DWORD bitmap. The value to use is determined by adding the values corresponding to the protocols desired.

| DefaultSecureProtocols value | Protocol enabled |
| - | - |
| 0x00000008 | Enable SSL 2.0 by default |
| 0x00000020 | Enable SSL 3.0 by default |
| 0x00000080 | Enable TLS 1.0 by default |
| 0x00000200 | Enable TLS 1.1 by default |
| 0x00000800 | Enable TLS 1.2 by default |

For example, if you want to override the default values for **WINHTTP_OPTION_SECURE_PROTOCOLS** to specify TLS 1.1 and TLS 1.2. In that case, take the value for TLS 1.1 (0x00000200) and the value for TLS 1.2 (0x00000800), add them together in calculator (in programmer mode), and the resulting registry value would be 0x00000A00.

## WINHTTP_OPTION_SECURITY_CERTIFICATE_STRUCT

Retrieves the certificate for a SSL/TLS server into the [**WINHTTP\_CERTIFICATE\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_certificate_info) structure. The application must free the **lpszSubjectInfo** and **lpszIssuerInfo** members with [**LocalFree**](/windows/win32/api/winbase/nf-winbase-localfree).

## WINHTTP_OPTION_SECURITY_FLAGS

Sets or retrieves an unsigned long integer value that contains the security flags for a handle. It can be a combination of these values:

| Term | Description |
|-|-|
| <span id="SECURITY_FLAG_IGNORE_CERT_CN_INVALID"></span><span id="security_flag_ignore_cert_cn_invalid"></span>SECURITY\_FLAG\_IGNORE\_CERT\_CN\_INVALID |Allows an invalid common name in a certificate; that is, the server name specified by the application doesn't match the common name in the certificate. If this flag is set, the application doesn't receive a **WINHTTP\_CALLBACK\_STATUS\_FLAG\_CERT\_CN\_INVALID** callback. |
| <span id="SECURITY_FLAG_IGNORE_CERT_DATE_INVALID"></span><span id="security_flag_ignore_cert_date_invalid"></span>SECURITY\_FLAG\_IGNORE\_CERT\_DATE\_INVALID |Allows an invalid certificate date, that is, an expired or not-yet-effective certificate. If this flag is set, the application doesn't receive a **WINHTTP\_CALLBACK\_STATUS\_FLAG\_CERT\_DATE\_INVALID** callback. |
| <span id="SECURITY_FLAG_IGNORE_UNKNOWN_CA"></span><span id="security_flag_ignore_unknown_ca"></span>SECURITY\_FLAG\_IGNORE\_UNKNOWN\_CA | Allows an invalid certificate authority. If this flag is set, the application doesn't receive a **WINHTTP\_CALLBACK\_STATUS\_FLAG\_INVALID\_CA** callback. |
| <span id="SECURITY_FLAG_IGNORE_CERT_WRONG_USAGE"></span><span id="security_flag_ignore_cert_wrong_usage"></span>SECURITY\_FLAG\_IGNORE\_CERT\_WRONG\_USAGE | Allows the identity of a server to be established with a non-server certificate (for example, a client certificate). |
| <span id="SECURITY_FLAG_IGNORE_WEAK_SIGNATURE"></span><span id="security_flag_ignore_weak_signature"></span>SECURITY\_FLAG\_IGNORE\_WEAK\_SIGNATURE | Allows a weak signature to be ignored.<br/>This flag is available in the rollup update for each OS starting with Windows 7 and Windows Server 2008 R2. |
| <span id="SECURITY_FLAG_SECURE"></span><span id="security_flag_secure"></span>SECURITY\_FLAG\_SECURE | Uses secure transfers. This is only returned in a call to [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption). |
| <span id="SECURITY_FLAG_STRENGTH_MEDIUM"></span><span id="security_flag_strength_medium"></span>SECURITY\_FLAG\_STRENGTH\_MEDIUM | Uses medium (56-bit) encryption. This is only returned in a call to [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption). |
| <span id="SECURITY_FLAG_STRENGTH_STRONG"></span><span id="security_flag_strength_strong"></span>SECURITY\_FLAG\_STRENGTH\_STRONG | Uses strong (128-bit) encryption. This is only returned in a call to [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption). |
| <span id="SECURITY_FLAG_STRENGTH_WEAK"></span><span id="security_flag_strength_weak"></span>SECURITY\_FLAG\_STRENGTH\_WEAK | Uses weak (40-bit) encryption. This is only returned in a call to [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption). |

## WINHTTP_OPTION_SECURITY_INFO

Retreives the SChannel connection and cipher information for a request.

## WINHTTP_OPTION_SECURITY_KEY_BITNESS

Retrieves an unsigned long integer value that contains the cipher strength of the encryption key. A larger number indicates stronger cipher strength encryption.

## WINHTTP_OPTION_SEND_TIMEOUT

Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds, to send a request or write some data. If sending the request takes longer than the timeout, the send operation is canceled. The default timeout is 30 seconds.

## WINHTTP_OPTION_SERVER_CBT

Gets a pointer to [**SecPkgContext\_Bindings**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_bindings) structure that specifies a Channel Binding Token (CBT).

A Channel Binding Token is a property of a secure transport channel and is used to bind an authentication channel to the secure transport channel. This token can only be obtained by this option after an SSL connection has been established.

> [!NOTE]
> Passing this option and a **null** value for *lpBuffer* to [**WinHttpQueryOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpqueryoption) will return ERROR\_INSUFFICIENT\_BUFFER and the required byte size for the buffer in the *lpdwBufferLength* parameter. This returned buffer size value can be passed in a subsequent call to query for the Channel Binding Token. These steps are necessary when handling WINHTTP\_CALLBACK\_STATUS\_REQUEST if you want to modify request headers based on the Channel Binding Token. Note that Windows XP and Vista do not support modifying request headers during this callback.

## WINHTTP_OPTION_SERVER_CERT_CHAIN_CONTEXT

Retrieves the server certification chain context. **WINHTTP\_OPTION\_SERVER\_CERT\_CHAIN\_CONTEXT** can be passed to obtain a duplicated pointer to the **CERT\_CHAIN\_CONTEXT** for a server certificate chain received during a negotiated SSL connection. The client must call [**CertFreeCertificateContext**](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatecontext) on the returned PCCERT\_CONTEXT pointer that is filled into the buffer.

## WINHTTP_OPTION_SERVER_CERT_CONTEXT

Retrieves the server certification context. **WINHTTP\_OPTION\_SERVER\_CERT\_CONTEXT** can be passed to obtain a duplicated pointer to the [**CERT CONTEXT**](/windows/win32/api/wincrypt/ns-wincrypt-cert_context) for a server certificate received during a negotiated SSL connection. The client must call [**CertFreeCertificateContext**](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatecontext) on the returned PCCERT\_CONTEXT pointer that is filled into the buffer.

## WINHTTP_OPTION_SERVER_SPN_USED

Gets the server Server Principal Name that WinHTTP supplied to SSPI during authentication. This string value can be passed to [**SspiPromptForCredentials**](/windows/win32/api/sspi/nf-sspi-sspipromptforcredentialsa) after an authentication failure.

## WINHTTP_OPTION_SPN

Includes or removes the server port number when the SPN (service principal name) is built for Kerberos or Negotiate Kerberos authentication. This flag is one of the following values:

| Term | Description |
|-|-|
| <span id="WINHTTP_DISABLE_SPN_SERVER_PORT"></span><span id="winhttp_disable_spn_server_port"></span>WINHTTP\_DISABLE\_SPN\_SERVER\_PORT | Removes the server port number. |
| <span id="WINHTTP_ENABLE_SPN_SERVER_PORT"></span><span id="winhttp_enable_spn_server_port"></span>WINHTTP\_ENABLE\_SPN\_SERVER\_PORT | Includes the server port number. |

## WINHTTP_OPTION_STREAM_ERROR_CODE

This option can be queried on a WinHttp request handle, and will return the error code indicated by a RST_STREAM frame received on an HTTP stream.

## WINHTTP_OPTION_TCP_FAST_OPEN

Enables TCP Fast Open for the connection.

## WINHTTP_OPTION_TCP_KEEPALIVE

This option can be set on a WinHttp session handle to enable TCP keep-alive behavior on the underlying socket. Takes a [**tcp\_keepalive**](/windows/win32/winsock/sio-keepalive-vals) struct.

## WINHTTP_OPTION_TLS_FALSE_START

Enables TLS False Start for the connection.

## WINHTTP_OPTION_TCP_PRIORITY_STATUS

Query the hinted priority of the TCP socket set with **WINHTTP_OPTION_TCP_PRIORITY_HINT**. See the documentation for [**SIO_SET_PRIORITY_HINT**](/windows/win32/winsock/winsock-ioctls#sio_set_priority_hint-opcode-setting-i-t3) for more details.

## WINHTTP_OPTION_TLS_PROTOCOL_INSECURE_FALLBACK

This option can be set on a WinHttp session handle to control whether fallback to TLS 1.0 is allowed if there is a TLS handshake failure with a newer protocol version.

## WINHTTP_OPTION_UNLOAD_NOTIFY_EVENT

Takes an event that will be set when the last callback has completed for a particular session. This flag must be must be used on a session handle. The event cannot be closed until after it has been set by WinHTTP.

## WINHTTP_OPTION_UNSAFE_HEADER_PARSING

This option is reserved for internal use and should not be called.

## WINHTTP_OPTION_UPGRADE_TO_WEB_SOCKET

Instructs the stack to start a WebSocket handshake process with [**WinHttpSendRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsendrequest). This option takes no parameters.

## WINHTTP_OPTION_URL

Retrieves a string value that contains the full URL of a downloaded resource. If the original URL contained any extra data, such as search strings or anchors, or if the call was redirected, the URL returned differs from the original. The application should pass in a buffer, sized in bytes, that is big enough to hold the returned URL in wide char.

## WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS

Takes a **BOOL** and can be set only a session handle. It will only propagate down to handles created from the session handle after the option has been set. If **TRUE**, this option causes as a last resort the use of global server credentials that were pushed down from WinInet. The default for this option is **FALSE**. This option requires registry key **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings!ShareCredsWithWinHttp**. This registry key is not present by default. When it is set, WinINet will send credentials down to WinHTTP. Whenever WinHttp gets an authentication challenge and if there are no credentials set on the current handle, it will use the credentials provided by WinINet.

## WINHTTP_OPTION_USE_SESSION_SCH_CRED

Allows setting a single credential to use by default for all endpoints within the session instead of having per-endpoint default credentials. That might improve performance by reducing credential management overhead. Note that this default credential will have no effect when a client certificate is explicitly provided.

## WINHTTP_OPTION_USER_AGENT

Sets or retrieves the [*user agent*](glossary.md) string on handles supplied by [**WinHttpOpen**](/windows/win32/api/Winhttp/nf-winhttp-winhttpopen) and used in subsequent [**WinHttpSendRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsendrequest) functions, as long as it is not overridden by a header added by [**WinHttpAddRequestHeaders**](/windows/win32/api/Winhttp/nf-winhttp-winhttpaddrequestheaders) or **WinHttpSendRequest**. When retrieving a user agent, the application should pass in a buffer, sized in bytes, that is big enough to hold the returned URL in wide char. When setting the user agent, the buffer size is the length of the string, in characters, plus the **NULL** terminator.

## WINHTTP_OPTION_USERNAME

Sets or retrieves a string that contains the user name.

## WINHTTP_OPTION_WEB_SOCKET_CLOSE_TIMEOUT

Sets the time, in milliseconds, that [**WinHttpWebSocketClose**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketclose) should wait to complete the close handshake. The default is 10 seconds.

## WINHTTP_OPTION_WEB_SOCKET_KEEPALIVE_INTERVAL

Sets the interval, in milliseconds, to send a keep-alive packet over the connection. The default interval is 30000 (30 seconds). The minimum interval is 15000 (15 seconds). Using [**WinHttpSetOption**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsetoption) to set a value lower than 15000 will return with **ERROR\_INVALID\_PARAMETER**.

> [!NOTE]
> The default value for **WINHTTP\_OPTION\_WEB\_SOCKET\_KEEPALIVE\_INTERVAL** is read from **HKLM:\\SOFTWARE\\Microsoft\\WebSocket\\KeepaliveInterval**. If a value is not set, the default value of 30000 will be used. It is not possible to have a lower keepalive interval than 15000 milliseconds.

## WINHTTP_OPTION_WEB_SOCKET_RECEIVE_BUFFER_SIZE

Sets or retrieves a DWORD which specifies the receive buffer size to be used on WebSocket connections.

## WINHTTP_OPTION_WEB_SOCKET_SEND_BUFFER_SIZE

Sets or retrieves a DWORD which specifies the send buffer size to be used on WebSocket connections.

## WINHTTP_OPTION_WORKER_THREAD_COUNT

Sets an unsigned long integer value that specifies the number of worker threads the thread pool should use for asynchronous completions. The default value of this option is zero, which specifies that the number of worker threads is equal to the number of CPUs on the system. This option can only be set on a **NULL**  [HINTERNET](hinternet-handles-in-winhttp.md) handle before an asynchronous operation has occurred. This option can only be set once.

**Windows Server 2008 R2 and Windows 7:** This flag is obsolete.

## WINHTTP_OPTION_WRITE_BUFFER_SIZE

This option is deprecated; it has no effect.

## Remarks

The following table lists the option flags by specifying which handles they can act upon, whether they can be queried and set, and the data type used. An "X" indicates that the option flag is valid for use with the function or handle, while a "-" specifies that the option flag is invalid.

Attempting to set or query an option flag on a Windows version where it is not supported will result in **ERROR\_WINHTTP\_INVALID\_OPTION**.

| Option flag, and data type | Session handle | Request handle | Query option | Set option | Minimum Windows Version |
|-|-|-|-|-|-|
| WINHTTP\_OPTION\_ASSURED\_NON\_BLOCKING\_CALLBACKS<br/>**BOOL** | X | \- | \- | X | \- |
| WINHTTP\_OPTION\_AUTOLOGON\_POLICY<br/>**DWORD** | \- | X | \- | X | \- |
| WINHTTP\_OPTION\_BACKGROUND\_CONNECTIONS<br/>**DWORD** | X | \- | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_CALLBACK<br/>**LPVOID** | X | X | X | X | \- |
| WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT<br/>[**CERT\_CONTEXT**](/windows/win32/api/wincrypt/ns-wincrypt-cert_context) | \- | X | \- | X | Windows Vista |
| WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST<br/>[**SecPkgContext\_IssuerListInfoEx**](/windows/win32/api/schannel/ns-schannel-secpkgcontext_issuerlistinfoex) | \- | X | X | \- | Windows Vista |
| WINHTTP\_OPTION\_CODEPAGE<br/>**DWORD** | X | \- | \- | X | \- |
| WINHTTP\_OPTION\_CONFIGURE\_PASSPORT\_AUTH<br/>**DWORD** | X | \- | \- | X | \- |
| WINHTTP\_OPTION\_CONNECT\_RETRIES<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_CONNECT\_TIMEOUT<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_CONNECTION\_INFO<br/>[**WINHTTP\_CONNECTION\_INFO**](/windows/win32/api/Winhttp/ns-winhttp-winhttp_connection_info) | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_CONNECTION\_STATS\_V0<br/>[**TCP\_INFO\_v0**](/windows/win32/api/mstcpip/ns-mstcpip-tcp_info_v0) | \- | X | X | \- | Windows 10 Version 1903 |
| WINHTTP\_OPTION\_CONNECTION\_STATS\_V1<br/>[**TCP\_INFO\_v1**](/windows/win32/api/mstcpip/ns-mstcpip-tcp_info_v1) | \- | X | X | \- | Windows 10 Version 2004 |
| WINHTTP\_OPTION\_CONTEXT\_VALUE<br/>**DWORD\_PTR** | X | X | X | X | \- |
| WINHTTP\_OPTION\_DECOMPRESSION<br/>**DWORD** | X | X | \- | X | Windows 8.1 |
| WINHTTP\_OPTION\_DISABLE\_CERT\_CHAIN\_BUILDING<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_DISABLE\_FEATURE<br/>**DWORD** | \- | X | \- | X | \- |
| WINHTTP\_OPTION\_DISABLE\_SECURE\_PROTOCOL\_FALLBACK<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 1903 |
| WINHTTP\_OPTION\_DISABLE\_STREAM\_QUEUE<br/>**BOOL** | X | X | \- | X | Windows 10 Version 1809 |
| WINHTTP\_OPTION\_ENABLE\_FEATURE<br/>**DWORD** | \* | \* | \- | X | \- |
| WINHTTP\_OPTION\_ENABLE\_HTTP\_PROTOCOL<br/>**DWORD** | X | X | \- | X | Windows 10 Version 1607 |
| WINHTTP\_OPTION\_ENABLE\_HTTP2\_PLUS\_CLIENT\_CERT\_CONTEXT<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_ENABLETRACING<br/>**DWORD** | \- | \- | X | X | \- |
| WINHTTP\_OPTION\_ENCODE\_EXTRA<br/>**BOOL** | X | X | \- | X | Windows 10 Version 1803 |
| WINHTTP\_OPTION\_EXPIRE\_CONNECTION<br/>N/A | \- | X | \- | X | Windows 10 Version 1903 |
| WINHTTP\_OPTION\_EXTENDED\_ERROR<br/>**DWORD** | X | X | X | \- | \- |
| WINHTTP\_OPTION\_FIRST\_AVAILABLE\_CONNECTION<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_GLOBAL\_PROXY\_CREDS<br/>[**WINHTTP\_CREDS**](/windows/win32/api/winhttp/ns-winhttp-winhttp_creds) | X | X | \- | X | \- |
| WINHTTP\_OPTION\_GLOBAL\_SERVER\_CREDS<br/>[**WINHTTP\_CREDS\_EX**](/windows/win32/api/winhttp/ns-winhttp-winhttp_creds_ex) | X | X | \- | X | \- |
| WINHTTP\_OPTION\_HANDLE\_TYPE<br/>**DWORD** | X | X | X | \- | \- |
| WINHTTP\_OPTION\_HTTP\_PROTOCOL\_REQUIRED<br/>**BOOL** | X | X | \- | X | Windows 10 Version 1903 |
| WINHTTP\_OPTION\_HTTP\_PROTOCOL\_USED<br/>**DWORD** | \- | X | X | \- | Windows 10 Version 1607 |
| WINHTTP\_OPTION\_HTTP\_VERSION<br/>[**HTTP\_VERSION\_INFO**](/windows/win32/api/winhttp/ns-winhttp-http_version_info) | X | X | X | X | \- |
| WINHTTP\_OPTION\_HTTP2\_KEEPALIVE<br/>**DWORD** | X | \- | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_HTTP2\_PLUS\_TRANSFER\_ENCODING<br/>**BOOL** | X | X | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_IGNORE\_CERT\_REVOCATION\_OFFLINE<br/>**BOOL** | \- | X | \- | X | Windows 10 Version 2004 |
| WINHTTP\_OPTION\_IPV6\_FAST\_FALLBACK<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 1903 |
| WINHTTP\_OPTION\_IS\_PROXY\_CONNECT\_RESPONSE<br/>**BOOL** | X | X | X | \- | \- |
| WINHTTP\_OPTION\_MAX\_CONNS\_PER\_1\_0\_SERVER<br/>**DWORD** | X | \- | X | X | \- |
| WINHTTP\_OPTION\_MAX\_CONNS\_PER\_SERVER<br/>**DWORD** | X | \- | X | X | \- |
| WINHTTP\_OPTION\_MAX\_HTTP\_AUTOMATIC\_REDIRECTS<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_MAX\_HTTP\_STATUS\_CONTINUE<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_MAX\_RESPONSE\_DRAIN\_SIZE<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_MAX\_RESPONSE\_HEADER\_SIZE<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_PARENT\_HANDLE<br/>[HINTERNET](hinternet-handles-in-winhttp.md) | X | X | X | \- | \- |
| WINHTTP\_OPTION\_PASSPORT\_COBRANDING\_TEXT<br/>**LPWSTR** | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_PASSPORT\_COBRANDING\_URL<br/>**LPWSTR** | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_PASSPORT\_RETURN\_URL<br/>**LPVOID** | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_PASSPORT\_SIGN\_OUT<br/>**LPVOID** | X | \- | \- | X | \- |
| WINHTTP\_OPTION\_PASSWORD<br/>**LPWSTR** | \- | X | X | X | \- |
| WINHTTP\_OPTION\_PROXY<br/>[**WINHTTP\_PROXY\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_proxy_info) | X | X | X | X | \- |
| WINHTTP\_OPTION\_PROXY\_PASSWORD<br/>**LPWSTR** | \- | X | X | X | \- |
| WINHTTP\_OPTION\_PROXY\_SPN\_USED<br/>**LPWSTR** | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_PROXY\_USERNAME<br/>**LPWSTR** | \- | X | X | X | \- |
| WINHTTP\_OPTION\_READ\_BUFFER\_SIZE<br/>**DWORD** | \- | X | X | X | \- |
| WINHTTP\_OPTION\_RECEIVE\_PROXY\_CONNECT\_RESPONSE<br/>**BOOL** | X | X | \- | X | \- |
| WINHTTP\_OPTION\_RECEIVE\_RESPONSE\_TIMEOUT<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_RECEIVE\_TIMEOUT<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_REDIRECT\_POLICY<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_REJECT\_USERPWD\_IN\_URL<br/>**BOOL** | \- | X | \- | X | \- |
| WINHTTP\_OPTION\_REQUEST\_PRIORITY<br/>**DWORD** | \- | X | X | X | \- |
| WINHTTP\_OPTION\_REQUEST\_STATS<br/>[**WINHTTP\_REQUEST\_STATS**](/windows/win32/api/winhttp/ns-winhttp-winhttp_request_stats) | \- | X | X | \- | Windows 10 Version 1903 |
| WINHTTP\_OPTION\_REQUEST\_TIMES<br/>[**WINHTTP\_REQUEST\_TIMES**](/windows/win32/api/winhttp/ns-winhttp-winhttp_request_times) | \- | X | X | \- | Windows 10 Version 1903 |
| WINHTTP\_OPTION\_REQUIRE\_STREAM\_END<br/>**BOOL** | X | X | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_RESOLUTION\_HOSTNAME<br/>**LPWSTR** | \- | X | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_RESOLVE\_TIMEOUT<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_SECURE\_PROTOCOLS<br/>**DWORD** | X | \- | \- | X | \- |
| WINHTTP\_OPTION\_SECURITY\_CERTIFICATE\_STRUCT<br/>[**WINHTTP\_CERTIFICATE\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_certificate_info) | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_SECURITY\_FLAGS<br/>**DWORD** | \- | X | X | X | \- |
| WINHTTP\_OPTION\_SECURITY\_INFO<br/>[**WINHTTP_SECURITY_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_security_info) | \- | X | X | \- | Windows 10 Version 2004 |
| WINHTTP\_OPTION\_SECURITY\_KEY\_BITNESS<br/>**DWORD** | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_SEND\_TIMEOUT<br/>**DWORD** | X | X | X | X | \- |
| WINHTTP\_OPTION\_SERVER\_CBT<br/>[**SecPkgContext\_Bindings**](/windows/win32/api/sspi/ns-sspi-secpkgcontext_bindings)\* | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_SERVER\_CERT\_CHAIN\_CONTEXT<br/>[**CERT_CHAIN_CONTEXT**](/windows/win32/api/wincrypt/ns-wincrypt-cert_chain_context) | \- | X | X | \- | Windows 10 Version 2004 |
| WINHTTP\_OPTION\_SERVER\_CERT\_CONTEXT<br/>[**CERT CONTEXT**](/windows/win32/api/wincrypt/ns-wincrypt-cert_context) | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_SERVER\_SPN\_USED<br/>**LPWSTR** | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_SPN<br/>**DWORD** | \- | X | \- | X | \- |
| WINHTTP\_OPTION\_STREAM\_ERROR\_CODE<br/>**DWORD** | \- | X | X | \- | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_TCP\_FAST\_OPEN<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 2004 |
| WINHTTP\_OPTION\_TCP\_KEEPALIVE<br/>[**tcp\_keepalive**](/windows/win32/winsock/sio-keepalive-vals) | X | \- | \- | X | Windows 10 Version 2004 |
| WINHTTP\_OPTION\_TLS\_FALSE\_START<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 2004 |
| WINHTTP\_OPTION\_TLS\_PROTOCOL\_INSECURE\_FALLBACK<br/>**BOOL** | X | \- | \- | X | Windows 10 Version 21H1 |
| WINHTTP\_OPTION\_UNLOAD\_NOTIFY\_EVENT<br/>[HINTERNET](hinternet-handles-in-winhttp.md) | X | \- | \- | X | \- |
| WINHTTP\_OPTION\_UNSAFE\_HEADER\_PARSING<br/>**DWORD** | \- | X | \- | X | \- |
| WINHTTP\_OPTION\_UPGRADE\_TO\_WEB\_SOCKET<br/>N/A | \- | X | \- | X | \- |
| WINHTTP\_OPTION\_URL<br/>**LPWSTR** | \- | X | X | \- | \- |
| WINHTTP\_OPTION\_USE\_GLOBAL\_SERVER\_CREDENTIALS<br/>**BOOL** | X | X | \- | X | \- |
| WINHTTP\_OPTION\_USER\_AGENT<br/>**LPWSTR** | X | \- | X | X | \- |
| WINHTTP\_OPTION\_USERNAME<br/>**LPWSTR** | \- | X | X | X | \- |
| WINHTTP\_OPTION\_WEB\_SOCKET\_CLOSE\_TIMEOUT<br/>**DWORD** | \- | \- | X | X | \- |
| WINHTTP\_OPTION\_WEB\_SOCKET\_KEEPALIVE\_INTERVAL<br/>**DWORD** | \- | \- | X | X | \- |
| WINHTTP\_OPTION\_WEB\_SOCKET\_RECEIVE\_BUFFER\_SIZE<br/>**DWORD** | X | X | X | X | Windows 8.1 |
| WINHTTP\_OPTION\_WEB\_SOCKET\_SEND\_BUFFER\_SIZE<br/>**DWORD** | X | X | X | X | Windows 8.1 |
| WINHTTP\_OPTION\_WORKER\_THREAD\_COUNT<br/>**DWORD** | \- | \- | \- | X | \- |
| WINHTTP\_OPTION\_WRITE\_BUFFER\_SIZE<br/>**DWORD** | \- | X | X | X | \- |

> [!NOTE]
> For Windows XP and Windows 2000, see [Run-Time Requirements](winhttp-start-page.md).

## Requirements

| Requirement | Value |
|--------------------------|---------------------------------------------------------------------------------|
| Minimum supported client | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]            |
| Minimum supported server | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]         |
| Redistributable          | WinHTTP 5.0 and Internet Explorer 5.01 or later on Windows XP and Windows 2000. |
| Header                   | Winhttp.h                                                                       |

## See also

* [WinHTTP versions](winhttp-versions.md)
