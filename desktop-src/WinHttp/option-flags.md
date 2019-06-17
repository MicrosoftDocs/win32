---
Description: The following option flags are supported by WinHttpQueryOption and WinHttpSetOption.
ms.assetid: 2d0441f4-ddba-4f2a-8861-8803cad6f1ac
title: Option Flags
ms.topic: article
ms.date: 05/31/2018
---

# Option Flags

The following option flags are supported by [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) and [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption).

<dl> <dt>

<span id="SECURITY_FLAG_IGNORE_WEAK_SIGNATURE"></span><span id="security_flag_ignore_weak_signature"></span>**SECURITY\_FLAG\_IGNORE\_WEAK\_SIGNATURE**
</dt> <dd> <dl> <dt>



Allows a weak signature check to be ignored.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_ASSURED_NON_BLOCKING_CALLBACKS"></span><span id="winhttp_option_assured_non_blocking_callbacks"></span>**WINHTTP\_OPTION\_ASSURED\_NON\_BLOCKING\_CALLBACKS**
</dt> <dd> <dl> <dt>



The default is FALSE. If set to TRUE, WinHTTP does not guarantee progress if status callbacks are blocked by the client application.

The client application must take special care to perform minimal operations within the callback without blocking, returning as quickly as possible, and in particular must not wait for any subsequent WinHTTP calls. If it does not follow these guidelines, there is likely to be a negative performance impact or a potential application hang. If used in the prescribed manner, this option may improve performance.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_AUTOLOGON_POLICY"></span><span id="winhttp_option_autologon_policy"></span>**WINHTTP\_OPTION\_AUTOLOGON\_POLICY**
</dt> <dd> <dl> <dt>



Sets an unsigned long integer value that specifies the [Automatic Logon Policy](authentication-in-winhttp.md) with one of the following values.

<dl> <dt>

<span id="WINHTTP_AUTOLOGON_SECURITY_LEVEL_HIGH"></span><span id="winhttp_autologon_security_level_high"></span>WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_HIGH
</dt> <dd>

Default credentials are not used. Note that this flag takes effect only if you specify the server by the actual machine name. It will not take effect, if you specify the server by "localhost" or IP address.

</dd> <dt>

<span id="WINHTTP_AUTOLOGON_SECURITY_LEVEL_LOW"></span><span id="winhttp_autologon_security_level_low"></span>WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_LOW
</dt> <dd>

An authenticated log on using the default credentials is performed for all requests.

</dd> <dt>

<span id="WINHTTP_AUTOLOGON_SECURITY_LEVEL_MEDIUM"></span><span id="winhttp_autologon_security_level_medium"></span>WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_MEDIUM
</dt> <dd>

An authenticated log on using the default credentials is performed only for requests on the local Intranet.

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_CALLBACK"></span><span id="winhttp_option_callback"></span>**WINHTTP\_OPTION\_CALLBACK**
</dt> <dd> <dl> <dt>



Retrieves the pointer to the callback function set with [**WinHttpSetStatusCallback**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetstatuscallback).


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_CLIENT_CERT_CONTEXT"></span><span id="winhttp_option_client_cert_context"></span>**WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT**
</dt> <dd> <dl> <dt>



Sets the client certificate context. If an application receives [**ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**](error-messages.md), it must call [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) to supply a certificate before retrying the request. As a part of processing this option, WinHttp calls [**CertDuplicateCertificateContext**](https://docs.microsoft.com/windows/desktop/api/wincrypt/nf-wincrypt-certduplicatecertificatecontext) on the caller-provided certificate context so that the certificate context can be independently released by the caller.

> [!Note]  
> The application should not attempt to close the certificate store with the CERT\_CLOSE\_STORE\_FORCE\_FLAG flag in the call to [**CertCloseStore**](https://docs.microsoft.com/windows/desktop/api/wincrypt/nf-wincrypt-certclosestore) on the certificate store from which the certificate context was retrieved. An access violation may occur.

 

When the server requests a client certificate, [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest), or [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) returns an [**ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**](error-messages.md) error. If the server requests the certificate but does not require it, the application can specify this option to indicate that it does not have a certificate. The server can choose another authentication scheme or allow anonymous access to the server. The application provides the **WINHTTP\_NO\_CLIENT\_CERT\_CONTEXT** macro in the *lpBuffer* parameter of [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) as shown in the following code example.

``` syntax
BOOL fRet = WinHttpSetOption ( hRequest,
                               WINHTTP_OPTION_CLIENT_CERT_CONTEXT,
                               WINHTTP_NO_CLIENT_CERT_CONTEXT,
                               0); 
```

> [!Note]  
> This flag is available for Windows Vista and later.

 

If the server requires a client certificate, it may send a 403 HTTP status code in response. For more information, see the **WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST** option.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST"></span><span id="winhttp_option_client_cert_issuer_list"></span>**WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST**
</dt> <dd> <dl> <dt>



Retrieves a [**SecPkgContext\_IssuerListInfoEx**](https://docs.microsoft.com/windows/desktop/api/schannel/ns-schannel-_secpkgcontext_issuerlistinfoex) structure when the error from [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) or [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) is **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**. The issuer list in the structure contains a list of acceptable Certificate Authorities (CA) from the server. The client application can filter the CA list to retrieve the client certificate for SSL authentication.

Alternately, if the server requests the client certificate, but does not require it, the application can call [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) with the **WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT** option. For more information, see the **WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT** option.

> [!Note]  
> This flag is available for Windows Vista and later.

 


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_CODEPAGE"></span><span id="winhttp_option_codepage"></span>**WINHTTP\_OPTION\_CODEPAGE**
</dt> <dd> <dl> <dt>



Sets the [*code page*](glossary.md) that is used to process the URL (that is, query string). The default is UTF8.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_CONFIGURE_PASSPORT_AUTH"></span><span id="winhttp_option_configure_passport_auth"></span>**WINHTTP\_OPTION\_CONFIGURE\_PASSPORT\_AUTH**
</dt> <dd> <dl> <dt>



Sets an unsigned long integer value that specifies whether [Passport Authentication in WinHTTP](passport-authentication-in-winhttp.md) authentication is enabled. The value can be one of the following:

<dl> <dt>

<span id="WINHTTP_DISABLE_PASSPORT_AUTH"></span><span id="winhttp_disable_passport_auth"></span>WINHTTP\_DISABLE\_PASSPORT\_AUTH
</dt> <dd>

Microsoft Passport authentication is disabled. This is the default.

</dd> <dt>

<span id="WINHTTP_DISABLE_PASSPORT_KEYRING"></span><span id="winhttp_disable_passport_keyring"></span>WINHTTP\_DISABLE\_PASSPORT\_KEYRING
</dt> <dd>

The Passport keyring is disabled. This is the default.

</dd> <dt>

<span id="WINHTTP_ENABLE_PASSPORT_AUTH"></span><span id="winhttp_enable_passport_auth"></span>WINHTTP\_ENABLE\_PASSPORT\_AUTH
</dt> <dd>

Passport authentication is enabled.

</dd> <dt>

<span id="WINHTTP_ENABLE_PASSPORT_KEYRING"></span><span id="winhttp_enable_passport_keyring"></span>WINHTTP\_ENABLE\_PASSPORT\_KEYRING
</dt> <dd>

The Passport keyring is enabled.

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_CONNECT_RETRIES"></span><span id="winhttp_option_connect_retries"></span>**WINHTTP\_OPTION\_CONNECT\_RETRIES**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the number of timesWinHTTP attempts to connect to a host. Microsoft Windows HTTP Services (WinHTTP) only attempts once per Internet Protocol (IP) address. For example, if you attempt to connect to a multihomed host that has 10 IP addresses and **WINHTTP\_OPTION\_CONNECT\_RETRIES** is set to 7, then WinHTTP only attempts to connect to the first seven IP address. Given the same set of 10 IP addresses, if **WINHTTP\_OPTION\_CONNECT\_RETRIES** is set to 20, WinHTTP attempts each of the 10 only once. If a connection attempt still fails after the specified number of attempts, or if the connect timeout expired before then, the request is canceled. The default value for **WINHTTP\_OPTION\_CONNECT\_RETRIES** is five attempts.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_CONNECT_TIMEOUT"></span><span id="winhttp_option_connect_timeout"></span>**WINHTTP\_OPTION\_CONNECT\_TIMEOUT**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds. Setting this option to infinite (0xFFFFFFFF) will disable this timer.

If a TCP connection request takes longer than this time-out value, the request is canceled. The default timeout is 60 seconds. When you are attempting to connect to multiple IP addresses for a single host (a multihomed host), the timeout limit is for each individual connection.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_CONNECTION_INFO_"></span><span id="winhttp_option_connection_info_"></span>**WINHTTP\_OPTION\_CONNECTION\_INFO** 
</dt> <dd> <dl> <dt>



Retrieves the source and destination IP address, and port of the request that generated the response when [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) returns. The application calls [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) with the **WINHTTP\_OPTION\_CONNECTION\_INFO** option, and provides the [**WINHTTP\_CONNECTION\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-winhttp_connection_info) structure in the *lpBuffer* parameter. For more information, see **WINHTTP\_CONNECTION\_INFO**.

**Windows Server 2003 with SP1 and Windows XP with SP2:** This flag is obsolete.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_CONTEXT_VALUE"></span><span id="winhttp_option_context_value"></span>**WINHTTP\_OPTION\_CONTEXT\_VALUE**
</dt> <dd> <dl> <dt>



Sets or retrieves a **DWORD\_PTR** that contains a pointer to the context value associated with this [HINTERNET](hinternet-handles-in-winhttp.md) handle. The value stored in the buffer is used and the **WINHTTP\_OPTION\_CONTEXT\_VALUE** option flag is assigned a new value.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_DECOMPRESSION"></span><span id="winhttp_option_decompression"></span>**WINHTTP\_OPTION\_DECOMPRESSION**
</dt> <dd> <dl> <dt>



Sets a DWORD of flags which determine whether WinHTTP will automatically decompress response bodies with compressed Content-Encodings. WinHTTP will also set an appropriate Accept-Encoding header, overriding any supplied by the caller. Supported values are:



|                                       |                                                           |
|---------------------------------------|-----------------------------------------------------------|
| Value                                 | Meaning                                                   |
| WINHTTP\_DECOMPRESSION\_FLAG\_GZIP    | Decompress Content-Encoding: gzip responses.              |
| WINHTTP\_DECOMPRESSION\_FLAG\_DEFLATE | Decompress Content-Encoding: deflate responses.           |
| WINHTTP\_DECOMPRESSION\_FLAG\_ALL     | Decompress responses with any supported Content-Encoding. |



 

By default, WinHTTP will deliver compressed responses to the caller unmodified. Supported in Windows 8.1 and newer.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_DISABLE_FEATURE"></span><span id="winhttp_option_disable_feature"></span>**WINHTTP\_OPTION\_DISABLE\_FEATURE**
</dt> <dd> <dl> <dt>



Sets an unsigned long integer value that specifies which features are disabled with one or more of the following flags. Be aware that this feature should only be passed to [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) on request handles after the request handle is created with [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest), and before the request is sent with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest).

<dl> <dt>

<span id="WINHTTP_DISABLE_AUTHENTICATION"></span><span id="winhttp_disable_authentication"></span>WINHTTP\_DISABLE\_AUTHENTICATION
</dt> <dd>

Automatic authentication is disabled.

</dd> <dt>

<span id="WINHTTP_DISABLE_COOKIES"></span><span id="winhttp_disable_cookies"></span>WINHTTP\_DISABLE\_COOKIES
</dt> <dd>

Automatic addition of cookie headers to requests is disabled. Also, returned cookies are not automatically added to the cookie database. Disabling cookies can result in poor performance for Passport authentication.

</dd> <dt>

<span id="WINHTTP_DISABLE_KEEP_ALIVE"></span><span id="winhttp_disable_keep_alive"></span>WINHTTP\_DISABLE\_KEEP\_ALIVE
</dt> <dd>

Disables keep-alive semantics for the connection. Keep-alive semantics are required for MSN, NTLM, and other types of authentication.

</dd> <dt>

<span id="WINHTTP_DISABLE_REDIRECTS"></span><span id="winhttp_disable_redirects"></span>WINHTTP\_DISABLE\_REDIRECTS
</dt> <dd>

Automatic redirection is disabled when sending requests with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest). If automatic redirection is disabled, an application must register a callback function in order for Passport authentication to succeed.

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_ENABLE_FEATURE"></span><span id="winhttp_option_enable_feature"></span>**WINHTTP\_OPTION\_ENABLE\_FEATURE**
</dt> <dd> <dl> <dt>



Sets an unsigned long integer value that specifies the features currently enabled. Can be one of the following values.



| Term                                                                                                                                                                       | Description                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINHTTP_ENABLE_SSL_REVERT_IMPERSONATION"></span><span id="winhttp_enable_ssl_revert_impersonation"></span>WINHTTP\_ENABLE\_SSL\_REVERT\_IMPERSONATION<br/> | If enabled, WinHTTP temporarily reverts client impersonation for the duration of SSL certificate authentication operations. This value can be set only on the session handle.<br/> |
| <span id="WINHTTP_ENABLE_SSL_REVOCATION"></span><span id="winhttp_enable_ssl_revocation"></span>WINHTTP\_ENABLE\_SSL\_REVOCATION<br/>                                | If enabled, WinHTTP allows SSL revocation. This value can be set only on the request handle.<br/>                                                                                  |



 


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_ENABLE_HTTP_PROTOCOL"></span><span id="winhttp_option_enable_http_protocol"></span>**WINHTTP\_OPTION\_ENABLE\_HTTP\_PROTOCOL**
</dt> <dd> <dl> <dt>



Sets a DWORD bitmask of acceptable advanced HTTP versions. Supported on Windows 10, version 1607 and newer. Possible values are:

-   WINHTTP\_PROTOCOL\_FLAG\_HTTP2 (0x1). Supported on Windows 10, version 1607 and newer

Legacy versions of HTTP (1.1 and prior) cannot be disabled using this option. The default is 0x0.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_ENABLETRACING"></span><span id="winhttp_option_enabletracing"></span>**WINHTTP\_OPTION\_ENABLETRACING**
</dt> <dd> <dl> <dt>



Sets a **BOOL** value that specifies whether tracing is currently enabled. For more information about the trace facility in WinHTTP, see [WinHTTP Trace Facility](winhttptracecfg-exe--a-trace-configuration-tool.md). This option can only be set on a **NULL** **HINTERNET** handle.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_EXTENDED_ERROR"></span><span id="winhttp_option_extended_error"></span>**WINHTTP\_OPTION\_EXTENDED\_ERROR**
</dt> <dd> <dl> <dt>



Retrieves an unsigned long integer value that contains a Microsoft Windows Sockets error code that was mapped to the ERROR\_WINHTTP\_\* error messages last returned in this thread context. You can pass **NULL** as the handle value.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_GLOBAL_SERVER_CREDS"></span><span id="winhttp_option_global_server_creds"></span>**WINHTTP\_OPTION\_GLOBAL\_SERVER\_CREDS**
</dt> <dd> <dl> <dt>



Takes a pointer to a [**WINHTTP\_CREDS\_EX**](/windows/desktop/api/Winhttp/ns-winhttp-tagwinhttp_creds_ex) structure with the *hInternet* function parameter set to **NULL**. This option requires registry key **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings!ShareCredsWithWinHttp**. If this registry key is not set WinHTTP will return error **ERROR\_WINHTTP\_INVALID\_OPTION**. This registry key is not present by default. When it is set, WinINet will send credentials down to WinHTTP. Whenever WinHttp gets an authentication challenge and if there are no credentials set on the current handle, it will use the credentials provided by WinINet. In order to share server credentials in addition to proxy credentials, users needs to set **WINHTTP\_OPTION\_USE\_GLOBAL\_SERVER\_CREDENTIALS** .


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_GLOBAL_PROXY_CREDS"></span><span id="winhttp_option_global_proxy_creds"></span>**WINHTTP\_OPTION\_GLOBAL\_PROXY\_CREDS**
</dt> <dd> <dl> <dt>



Takes a pointer to a [**WINHTTP\_CREDS\_EX**](/windows/desktop/api/Winhttp/ns-winhttp-tagwinhttp_creds_ex) structure with the *hInternet* function parameter set to **NULL**. This option requires registry key **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings!ShareCredsWithWinHttp**. If this registry key is not set WinHTTP will return error **ERROR\_WINHTTP\_INVALID\_OPTION**. This registry key is not present by default. When it is set, WinINet will send credentials down to WinHTTP. Whenever WinHttp gets an authentication challenge and if there are no credentials set on the current handle, it will use the credentials provided by WinINet. In order to share server credentials in addition to proxy credentials, users needs to set **WINHTTP\_OPTION\_USE\_GLOBAL\_SERVER\_CREDENTIALS** .


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_HANDLE_TYPE"></span><span id="winhttp_option_handle_type"></span>**WINHTTP\_OPTION\_HANDLE\_TYPE**
</dt> <dd> <dl> <dt>



Retrieves an unsigned long integer value that contains the type of the [HINTERNET](hinternet-handles-in-winhttp.md) handle passed in. The return value can be one of the following:

<dl> <dt>

<span id="WINHTTP_HANDLE_TYPE_CONNECT"></span><span id="winhttp_handle_type_connect"></span>WINHTTP\_HANDLE\_TYPE\_CONNECT
</dt> <dd>

The handle is a connection handle.

</dd> <dt>

<span id="WINHTTP_HANDLE_TYPE_REQUEST"></span><span id="winhttp_handle_type_request"></span>WINHTTP\_HANDLE\_TYPE\_REQUEST
</dt> <dd>

The handle is a request handle.

</dd> <dt>

<span id="WINHTTP_HANDLE_TYPE_SESSION"></span><span id="winhttp_handle_type_session"></span>WINHTTP\_HANDLE\_TYPE\_SESSION
</dt> <dd>

The handle is a session handle.

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_HTTP_PROTOCOL_USED"></span><span id="winhttp_option_http_protocol_used"></span>**WINHTTP\_OPTION\_HTTP\_PROTOCOL\_USED**
</dt> <dd> <dl> <dt>



Gets a DWORD indicating which advanced HTTP version was used on a given request. Possible values are:

-     WINHTTP\_PROTOCOL\_FLAG\_HTTP2 (0x1). Supported on Windows 10, version 1607 and newer.

0x0 indicates HTTP/1.1 or earlier. Supported on Windows 10, version 1607 and newer.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_HTTP_VERSION"></span><span id="winhttp_option_http_version"></span>**WINHTTP\_OPTION\_HTTP\_VERSION**
</dt> <dd> <dl> <dt>



Sets or retrieves an [**HTTP\_VERSION\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_1) structure that contains the HTTP version being supported. This is a process-wide option; use **NULL** for the handle.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_IS_PROXY_CONNECT_RESPONSE"></span><span id="winhttp_option_is_proxy_connect_response"></span>**WINHTTP\_OPTION\_IS\_PROXY\_CONNECT\_RESPONSE**
</dt> <dd> <dl> <dt>



Gets whether or not a Proxy Return Connect Response can be retrieved.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_MAX_CONNS_PER_1_0_SERVER"></span><span id="winhttp_option_max_conns_per_1_0_server"></span>**WINHTTP\_OPTION\_MAX\_CONNS\_PER\_1\_0\_SERVER**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the maximum number of connections allowed per HTTP/1.0 server. The default value is **INFINITE**.

**Windows Vista with SP1 and Windows Server 2008:** This flag is obsolete.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_MAX_CONNS_PER_SERVER"></span><span id="winhttp_option_max_conns_per_server"></span>**WINHTTP\_OPTION\_MAX\_CONNS\_PER\_SERVER**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the maximum number of connections allowed per server. The default value is **INFINITE**.

When this option is set to zero, WinHTTP sets the limit on the number of connections to 2.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_MAX_HTTP_AUTOMATIC_REDIRECTS"></span><span id="winhttp_option_max_http_automatic_redirects"></span>**WINHTTP\_OPTION\_MAX\_HTTP\_AUTOMATIC\_REDIRECTS**
</dt> <dd> <dl> <dt>



Sets the maximum number of redirects that WinHTTP follows; the default is 10. This limit prevents unauthorized sites from making the WinHTTP client pause following a large number of redirects.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_MAX_HTTP_STATUS_CONTINUE"></span><span id="winhttp_option_max_http_status_continue"></span>**WINHTTP\_OPTION\_MAX\_HTTP\_STATUS\_CONTINUE**
</dt> <dd> <dl> <dt>



The maximum number of Informational 100-199 status code responses ignored before returning the final status code to the WinHTTP client. Informational 100-199 status codes can be sent by the server before the final status code, and are described in the specification for HTTP/1.1 (for more information, see [RFC 2616](https://go.microsoft.com/fwlink/p/?linkid=84048)). The default is 10.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_MAX_RESPONSE_DRAIN_SIZE"></span><span id="winhttp_option_max_response_drain_size"></span>**WINHTTP\_OPTION\_MAX\_RESPONSE\_DRAIN\_SIZE**
</dt> <dd> <dl> <dt>



A bound on the amount of data drained from responses in order to reuse a connection, specified in bytes. The default is 1MB.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_MAX_RESPONSE_HEADER_SIZE"></span><span id="winhttp_option_max_response_header_size"></span>**WINHTTP\_OPTION\_MAX\_RESPONSE\_HEADER\_SIZE**
</dt> <dd> <dl> <dt>



A bound set on the maximum size of the header portion of the server response, specified in bytes. This bound protects the client from an unauthorized server attempting to stall the client by sending a response with an infinite amount of header data. The default value is 64KB.

**Windows XP with SP1 and Windows 2000 with SP3:** This flag is obsolete.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PARENT_HANDLE"></span><span id="winhttp_option_parent_handle"></span>**WINHTTP\_OPTION\_PARENT\_HANDLE**
</dt> <dd> <dl> <dt>



Retrieves the parent handle to this handle.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PASSPORT_COBRANDING_TEXT"></span><span id="winhttp_option_passport_cobranding_text"></span>**WINHTTP\_OPTION\_PASSPORT\_COBRANDING\_TEXT**
</dt> <dd> <dl> <dt>



Retrieves a string that contains the [*cobranding*](glossary.md) text provided by the Passport logon server. This option should be retrieved immediately after the logon server responds with a 401 status code. An application should pass in a buffer size, in bytes, that is big enough to hold the returned string.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PASSPORT_COBRANDING_URL"></span><span id="winhttp_option_passport_cobranding_url"></span>**WINHTTP\_OPTION\_PASSPORT\_COBRANDING\_URL**
</dt> <dd> <dl> <dt>



Retrieves a string that contains a URL for a [*cobranding*](glossary.md) graphic provided by the Passport logon server. This option should be retrieved immediately after the logon server responds with a 401 status code. An application should pass in a buffer size, in bytes, that is big enough to hold the returned string.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PASSPORT_RETURN_URL"></span><span id="winhttp_option_passport_return_url"></span>**WINHTTP\_OPTION\_PASSPORT\_RETURN\_URL**
</dt> <dd> <dl> <dt>



Sets a read-only option on a request handle that retrieves the Passport return URL.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PASSPORT_SIGN_OUT"></span><span id="winhttp_option_passport_sign_out"></span>**WINHTTP\_OPTION\_PASSPORT\_SIGN\_OUT**
</dt> <dd> <dl> <dt>



Sets the option on a session handle to sign out of any Passport logins. An application should pass in the Passport return URL that was retrieved with **WINHTTP\_OPTION\_PASSPORT\_RETURN\_URL**. All cookies related to the return URL are cleared.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PASSWORD"></span><span id="winhttp_option_password"></span>**WINHTTP\_OPTION\_PASSWORD**
</dt> <dd> <dl> <dt>



Sets or retrieves a string value that contains the password associated with a request handle.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PROXY"></span><span id="winhttp_option_proxy"></span>**WINHTTP\_OPTION\_PROXY**
</dt> <dd> <dl> <dt>



Sets or retrieves an [**WINHTTP\_PROXY\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_3) structure that contains the proxy data on an existing session handle or request handle. When retrieving proxy data, an application must free the **lpszProxy** and **lpszProxyBypass** strings contained in this structure (if they are non-**NULL**) using the [**GlobalFree**](https://docs.microsoft.com/windows/desktop/api/winbase/nf-winbase-globalfree) function. An application can query for the global proxy data (the default proxy) by passing a **NULL** handle.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PROXY_PASSWORD"></span><span id="winhttp_option_proxy_password"></span>**WINHTTP\_OPTION\_PROXY\_PASSWORD**
</dt> <dd> <dl> <dt>



Sets or retrieves a string value that contains the password used to access the proxy.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PROXY_SPN_USED"></span><span id="winhttp_option_proxy_spn_used"></span>**WINHTTP\_OPTION\_PROXY\_SPN\_USED**
</dt> <dd> <dl> <dt>



Gets the proxy Server Principal Name that WinHTTP supplied to SSPI during authentication. This string value is usefor passing to [**SspiPromptForCredentials**](https://docs.microsoft.com/windows/desktop/api/sspi/nf-sspi-sspipromptforcredentialsa) after an authentication failure.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_PROXY_USERNAME"></span><span id="winhttp_option_proxy_username"></span>**WINHTTP\_OPTION\_PROXY\_USERNAME**
</dt> <dd> <dl> <dt>



Sets or retrieves a string value that contains the user name used to access the proxy.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_READ_BUFFER_SIZE"></span><span id="winhttp_option_read_buffer_size"></span>**WINHTTP\_OPTION\_READ\_BUFFER\_SIZE**
</dt> <dd> <dl> <dt>



This option has been deprecated; it has no effect.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_RECEIVE_PROXY_CONNECT_RESPONSE"></span><span id="winhttp_option_receive_proxy_connect_response"></span>**WINHTTP\_OPTION\_RECEIVE\_PROXY\_CONNECT\_RESPONSE**
</dt> <dd> <dl> <dt>



Sets whether or not the proxy response entity can be retrieved. This option is disabled by default.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_RECEIVE_RESPONSE_TIMEOUT"></span><span id="winhttp_option_receive_response_timeout"></span>**WINHTTP\_OPTION\_RECEIVE\_RESPONSE\_TIMEOUT**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the timeout value, in milliseconds, to wait to receive all response headers to a request. If WinHTTP fails to receive all the headers within this timeout period, the request is canceled. The default timeout value is 90 seconds.

This timeout is checked only when data is received from the socket. As a result, when the timeout expires the client application is not notified until more data arrives from the server. If no data arrives from the server, the delay between the timeout expiration and notification of the client application could be as large as the timeout value set using the *dwReceiveTimeout* parameter of the [**WinHttpSetTimeouts**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsettimeouts) function.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_RECEIVE_TIMEOUT"></span><span id="winhttp_option_receive_timeout"></span>**WINHTTP\_OPTION\_RECEIVE\_TIMEOUT**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds, to receive a partial response to a request or read some data. If the response takes longer than this time-out value, the request is canceled. The default timeout value is 30 seconds.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_REDIRECT_POLICY"></span><span id="winhttp_option_redirect_policy"></span>**WINHTTP\_OPTION\_REDIRECT\_POLICY**
</dt> <dd> <dl> <dt>



Sets the behavior of WinHTTP regarding the handling of a 30x HTTP redirect status code. This option can be set on a session or request handle to one of the following values:



| Term                                                                                                                                                                                                                    | Description                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINHTTP_OPTION_REDIRECT_POLICY_ALWAYS"></span><span id="winhttp_option_redirect_policy_always"></span>WINHTTP\_OPTION\_REDIRECT\_POLICY\_ALWAYS<br/>                                                    | All redirects are followed automatically.<br/>                                                                                                 |
| <span id="WINHTTP_OPTION_REDIRECT_POLICY_DISALLOW_HTTPS_TO_HTTP"></span><span id="winhttp_option_redirect_policy_disallow_https_to_http"></span>WINHTTP\_OPTION\_REDIRECT\_POLICY\_DISALLOW\_HTTPS\_TO\_HTTP<br/> | All redirects are followed, except those that originate from a secure (https) URL to an unsecure (http) URL. This is the default setting.<br/> |
| <span id="WINHTTP_OPTION_REDIRECT_POLICY_NEVER"></span><span id="winhttp_option_redirect_policy_never"></span>WINHTTP\_OPTION\_REDIRECT\_POLICY\_NEVER<br/>                                                       | Redirects are never followed. The 30x status is returned to the application.<br/>                                                              |



 


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_REJECT_USERPWD_IN_URL"></span><span id="winhttp_option_reject_userpwd_in_url"></span>**WINHTTP\_OPTION\_REJECT\_USERPWD\_IN\_URL**
</dt> <dd> <dl> <dt>



Rejects URLs that contain a username and password. This option also rejects URLs that contain *username:password* semantics, even if no username or password is specified. For example, "u:p@hostname", ":@hostname", "u:@hostname", and ":p@hostname" would all be flagged as invalid. If an invalid URL is passed to the function, it returns [ERROR\_WINHTTP\_INVALID\_URL](error-messages.md). This option is turned off by default.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_REQUEST_PRIORITY"></span><span id="winhttp_option_request_priority"></span>**WINHTTP\_OPTION\_REQUEST\_PRIORITY**
</dt> <dd> <dl> <dt>



This option has been deprecated; it has no effect.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_RESOLVE_TIMEOUT"></span><span id="winhttp_option_resolve_timeout"></span>**WINHTTP\_OPTION\_RESOLVE\_TIMEOUT**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds, to resolve a host name. The default timeout value is **INFINITE**. If a non-default value is specified, there is an overhead of one thread-creation per name resolution.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_SECURE_PROTOCOLS"></span><span id="winhttp_option_secure_protocols"></span>**WINHTTP\_OPTION\_SECURE\_PROTOCOLS**
</dt> <dd> <dl> <dt>



Sets an unsigned long integer value that specifies which secure protocols are acceptable. By default only SSL3 and TLS1 are enabled in Windows 7 and Windows 8. By default only SSL3, TLS1.0, TLS1.1, and TLS1.2 are enabled in Windows 8.1 and Windows 10. The value can be a combination of one or more of the following values.

<dl> <dt>

<span id="WINHTTP_FLAG_SECURE_PROTOCOL_ALL"></span><span id="winhttp_flag_secure_protocol_all"></span>WINHTTP\_FLAG\_SECURE\_PROTOCOL\_ALL
</dt> <dd>

The Secure Sockets Layer (SSL) 2.0, SSL 3.0, and Transport Layer Security (TLS) 1.0 protocols can be used.

</dd> <dt>

<span id="WINHTTP_FLAG_SECURE_PROTOCOL_SSL2"></span><span id="winhttp_flag_secure_protocol_ssl2"></span>WINHTTP\_FLAG\_SECURE\_PROTOCOL\_SSL2
</dt> <dd>

The SSL 2.0 protocol can be used.

</dd> <dt>

<span id="WINHTTP_FLAG_SECURE_PROTOCOL_SSL3"></span><span id="winhttp_flag_secure_protocol_ssl3"></span>WINHTTP\_FLAG\_SECURE\_PROTOCOL\_SSL3
</dt> <dd>

The SSL 3.0 protocol can be used.

</dd> <dt>

<span id="WINHTTP_FLAG_SECURE_PROTOCOL_TLS1"></span><span id="winhttp_flag_secure_protocol_tls1"></span>WINHTTP\_FLAG\_SECURE\_PROTOCOL\_TLS1
</dt> <dd>

The TLS 1.0 protocol can be used.

</dd> <dt>

<span id="WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_1"></span><span id="winhttp_flag_secure_protocol_tls1_1"></span>WINHTTP\_FLAG\_SECURE\_PROTOCOL\_TLS1\_1
</dt> <dd>

The TLS 1.1 protocol can be used.

</dd> <dt>

<span id="WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_2"></span><span id="winhttp_flag_secure_protocol_tls1_2"></span>WINHTTP\_FLAG\_SECURE\_PROTOCOL\_TLS1\_2
</dt> <dd>

The TLS 1.2 protocol can be used.

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_SECURITY_CERTIFICATE_STRUCT"></span><span id="winhttp_option_security_certificate_struct"></span>**WINHTTP\_OPTION\_SECURITY\_CERTIFICATE\_STRUCT**
</dt> <dd> <dl> <dt>



Retrieves the certificate for a SSL/TLS server into the [**WINHTTP\_CERTIFICATE\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_5) structure. The application must free the **lpszSubjectInfo** and **lpszIssuerInfo** members with [**LocalFree**](https://docs.microsoft.com/windows/desktop/api/winbase/nf-winbase-localfree).


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_SECURITY_FLAGS"></span><span id="winhttp_option_security_flags"></span>**WINHTTP\_OPTION\_SECURITY\_FLAGS**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the security flags for a handle. It can be a combination of these values:

<dl> <dt>

<span id="SECURITY_FLAG_IGNORE_CERT_CN_INVALID"></span><span id="security_flag_ignore_cert_cn_invalid"></span>SECURITY\_FLAG\_IGNORE\_CERT\_CN\_INVALID
</dt> <dd>

Allows an invalid common name in a certificate; that is, the server name specified by the application does not match the common name in the certificate. If this flag is set, the application does not receive a **WINHTTP\_CALLBACK\_STATUS\_FLAG\_CERT\_CN\_INVALID** callback.

</dd> <dt>

<span id="SECURITY_FLAG_IGNORE_CERT_DATE_INVALID"></span><span id="security_flag_ignore_cert_date_invalid"></span>SECURITY\_FLAG\_IGNORE\_CERT\_DATE\_INVALID
</dt> <dd>

Allows an invalid certificate date, that is, an expired or not-yet-effective certificate. If this flag is set, the application does not receive a **WINHTTP\_CALLBACK\_STATUS\_FLAG\_CERT\_DATE\_INVALID** callback.

</dd> <dt>

<span id="SECURITY_FLAG_IGNORE_UNKNOWN_CA_"></span><span id="security_flag_ignore_unknown_ca_"></span>SECURITY\_FLAG\_IGNORE\_UNKNOWN\_CA 
</dt> <dd>

Allows an invalid certificate authority. If this flag is set, the application does not receive a **WINHTTP\_CALLBACK\_STATUS\_FLAG\_INVALID\_CA** callback.

</dd> <dt>

<span id="SECURITY_FLAG_IGNORE_CERT_WRONG_USAGE"></span><span id="security_flag_ignore_cert_wrong_usage"></span>SECURITY\_FLAG\_IGNORE\_CERT\_WRONG\_USAGE
</dt> <dd>

Allows the identity of a server to be established with a non-server certificate (for example, a client certificate).

</dd> <dt>

<span id="SECURITY_FLAG_IGNORE_WEAK_SIGNATURE"></span><span id="security_flag_ignore_weak_signature"></span>SECURITY\_FLAG\_IGNORE\_WEAK\_SIGNATURE
</dt> <dd>

Allows a weak signature to be ignored.

This flag is available in the rollup update for each OS starting with Windows 7 and Windows Server 2008 R2.

</dd> <dt>

<span id="SECURITY_FLAG_SECURE"></span><span id="security_flag_secure"></span>SECURITY\_FLAG\_SECURE
</dt> <dd>

Uses secure transfers. This is only returned in a call to [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption).

</dd> <dt>

<span id="SECURITY_FLAG_STRENGTH_MEDIUM"></span><span id="security_flag_strength_medium"></span>SECURITY\_FLAG\_STRENGTH\_MEDIUM
</dt> <dd>

Uses medium (56-bit) encryption. This is only returned in a call to [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption).

</dd> <dt>

<span id="SECURITY_FLAG_STRENGTH_STRONG"></span><span id="security_flag_strength_strong"></span>SECURITY\_FLAG\_STRENGTH\_STRONG
</dt> <dd>

Uses strong (128-bit) encryption. This is only returned in a call to [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption).

</dd> <dt>

<span id="SECURITY_FLAG_STRENGTH_WEAK"></span><span id="security_flag_strength_weak"></span>SECURITY\_FLAG\_STRENGTH\_WEAK
</dt> <dd>

Uses weak (40-bit) encryption. This is only returned in a call to [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption).

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_SECURITY_KEY_BITNESS"></span><span id="winhttp_option_security_key_bitness"></span>**WINHTTP\_OPTION\_SECURITY\_KEY\_BITNESS**
</dt> <dd> <dl> <dt>



Retrieves an unsigned long integer value that contains the cipher strength of the encryption key. A larger number indicates stronger cipher strength encryption.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_SEND_TIMEOUT"></span><span id="winhttp_option_send_timeout"></span>**WINHTTP\_OPTION\_SEND\_TIMEOUT**
</dt> <dd> <dl> <dt>



Sets or retrieves an unsigned long integer value that contains the time-out value, in milliseconds, to send a request or write some data. If sending the request takes longer than the timeout, the send operation is canceled. The default timeout is 30 seconds.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_SERVER_CBT"></span><span id="winhttp_option_server_cbt"></span>**WINHTTP\_OPTION\_SERVER\_CBT**
</dt> <dd> <dl> <dt>



Gets a pointer to [**SecPkgContext\_Bindings**](https://docs.microsoft.com/windows/desktop/api/sspi/ns-sspi-_secpkgcontext_bindings) structure that specifies a Channel Binding Token (CBT).

A Channel Binding Token is a property of a secure transport channel and is used to bind an authentication channel to the secure transport channel. This token can only be obtained by this option after an SSL connection has been established.

> [!Note]  
> Passing this option and a **null** value for *lpBuffer* to [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) will return ERROR\_INSUFFICIENT\_BUFFER and the required byte size for the buffer in the *lpdwBufferLength* parameter. This returned buffer size value can be passed in a subsequent call to query for the Channel Binding Token. These steps are necessary when handling WINHTTP\_CALLBACK\_STATUS\_REQUEST if you want to modify request headers based on the Channel Binding Token. Note that Windows XP and Vista do not support modifying request headers during this callback.

 


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_SERVER_CERT_CONTEXT"></span><span id="winhttp_option_server_cert_context"></span>**WINHTTP\_OPTION\_SERVER\_CERT\_CONTEXT**
</dt> <dd> <dl> <dt>



Retrieves the server certification context. **WINHTTP\_OPTION\_SERVER\_CERT\_CONTEXT** can be passed to obtain a duplicated pointer to the [**CERT CONTEXT**](https://docs.microsoft.com/windows/desktop/api/wincrypt/ns-wincrypt-_cert_context) for a server certificate received during a negotiated SSL connection. The client must call [**CertFreeCertificateContext**](https://docs.microsoft.com/windows/desktop/api/wincrypt/nf-wincrypt-certfreecertificatecontext) on the returned PCCERT\_CONTEXT pointer that is filled into the buffer.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_SERVER_SPN_USED"></span><span id="winhttp_option_server_spn_used"></span>**WINHTTP\_OPTION\_SERVER\_SPN\_USED**
</dt> <dd> <dl> <dt>



Gets the server Server Principal Name that WinHTTP supplied to SSPI during authentication. This string value can be passed to [**SspiPromptForCredentials**](https://docs.microsoft.com/windows/desktop/api/sspi/nf-sspi-sspipromptforcredentialsa) after an authentication failure.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_SPN"></span><span id="winhttp_option_spn"></span>**WINHTTP\_OPTION\_SPN**
</dt> <dd> <dl> <dt>



Includes or removes the server port number when the SPN (service principal name) is built for Kerberos or Negotiate Kerberos authentication. This flag is one of the following values:

<dl> <dt>

<span id="WINHTTP_DISABLE_SPN_SERVER_PORT"></span><span id="winhttp_disable_spn_server_port"></span>WINHTTP\_DISABLE\_SPN\_SERVER\_PORT
</dt> <dd>

Removes the server port number.

</dd> <dt>

<span id="WINHTTP_ENABLE_SPN_SERVER_PORT"></span><span id="winhttp_enable_spn_server_port"></span>WINHTTP\_ENABLE\_SPN\_SERVER\_PORT
</dt> <dd>

Includes the server port number.

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_UNLOAD_NOTIFY_EVENT"></span><span id="winhttp_option_unload_notify_event"></span>**WINHTTP\_OPTION\_UNLOAD\_NOTIFY\_EVENT**
</dt> <dd> <dl> <dt>



Takes an event that will be set when the last callback has completed for a particular session. This flag must be must be used on a session handle. The event cannot be closed until after it has been set by WinHTTP.

<dl> <dt>

<span id="WINHTTP_FLAG_SECURE_PROTOCOL_ALL"></span><span id="winhttp_flag_secure_protocol_all"></span>WINHTTP\_FLAG\_SECURE\_PROTOCOL\_ALL
</dt> <dd>

The buffer length is incorrect for a handle, the handle is invalid, or the option has already been set.

</dd> <dt>

<span id="ERROR_WINHTTP_INCORRECT_HANDLE_TYPE"></span><span id="error_winhttp_incorrect_handle_type"></span>ERROR\_WINHTTP\_INCORRECT\_HANDLE\_TYPE
</dt> <dd>

The target is not a session handle.

</dd> </dl>

</dl> </dd> <dt>

<span id="WINHTTP_OPTION_UNSAFE_HEADER_BLOCKING"></span><span id="winhttp_option_unsafe_header_blocking"></span>**WINHTTP\_OPTION\_UNSAFE\_HEADER\_BLOCKING**
</dt> <dd> <dl> <dt>



This option is reserved for internal use and should not be called.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_UPGRADE_TO_WEB_SOCKET"></span><span id="winhttp_option_upgrade_to_web_socket"></span>**WINHTTP\_OPTION\_UPGRADE\_TO\_WEB\_SOCKET**
</dt> <dd> <dl> <dt>



Instructs the stack to start a WebSocket handshake process with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest). This option takes no parameters.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_URL"></span><span id="winhttp_option_url"></span>**WINHTTP\_OPTION\_URL**
</dt> <dd> <dl> <dt>



Retrieves a string value that contains the full URL of a downloaded resource. If the original URL contained any extra data, such as search strings or anchors, or if the call was redirected, the URL returned differs from the original. The application should pass in a buffer, sized in bytes, that is big enough to hold the returned URL in wide char.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS_"></span><span id="winhttp_option_use_global_server_credentials_"></span>**WINHTTP\_OPTION\_USE\_GLOBAL\_SERVER\_CREDENTIALS** 
</dt> <dd> <dl> <dt>



Takes a **BOOL** and can be set only a session handle. It will only propagate down to handles created from the session handle after the option has been set. If **TRUE**, this option causes as a last resort the use of global server credentials that were pushed down from WinInet. The default for this option is **FALSE**. This option requires registry key **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings!ShareCredsWithWinHttp**. This registry key is not present by default. When it is set, WinINet will send credentials down to WinHTTP. Whenever WinHttp gets an authentication challenge and if there are no credentials set on the current handle, it will use the credentials provided by WinINet.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_USER_AGENT"></span><span id="winhttp_option_user_agent"></span>**WINHTTP\_OPTION\_USER\_AGENT**
</dt> <dd> <dl> <dt>



Sets or retrieves the [*user agent*](glossary.md) string on handles supplied by [**WinHttpOpen**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopen) and used in subsequent [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) functions, as long as it is not overridden by a header added by [**WinHttpAddRequestHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpaddrequestheaders) or **WinHttpSendRequest**. When retrieving a user agent, the application should pass in a buffer, sized in bytes, that is big enough to hold the returned URL in wide char. When setting the user agent, the buffer size is the length of the string, in characters, plus the **NULL** terminator.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_USERNAME"></span><span id="winhttp_option_username"></span>**WINHTTP\_OPTION\_USERNAME**
</dt> <dd> <dl> <dt>



Sets or retrieves a string that contains the user name.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_WEB_SOCKET_CLOSE_TIMEOUT"></span><span id="winhttp_option_web_socket_close_timeout"></span>**WINHTTP\_OPTION\_WEB\_SOCKET\_CLOSE\_TIMEOUT**
</dt> <dd> <dl> <dt>



Sets the time, in milliseconds, that [**WinHttpWebSocketClose**](/windows/desktop/api/winhttp/nf-winhttp-winhttpwebsocketclose) should wait to complete the close handshake. The default is 10 seconds.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_WEB_SOCKET_KEEPALIVE_INTERVAL"></span><span id="winhttp_option_web_socket_keepalive_interval"></span>**WINHTTP\_OPTION\_WEB\_SOCKET\_KEEPALIVE\_INTERVAL**
</dt> <dd> <dl> <dt>



Sets the interval, in milliseconds, to send a keep-alive packet over the connection. The default interval is 30000 (30 seconds). The minimum interval is 15000 (15 seconds). Using [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) to set a value lower than 15000 will return with **ERROR\_INVALID\_PARAMETER**.

> [!Note]  
> The default value for **WINHTTP\_OPTION\_WEB\_SOCKET\_KEEPALIVE\_INTERVAL** is read from **HKLM:\\SOFTWARE\\Microsoft\\WebSocket\\KeepaliveInterval**. If a value is not set, the default value of 30000 will be used. It is not possible to have a lower keepalive interval than 15000 milliseconds.

 


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_WEB_SOCKET_RECEIVE_BUFFER_SIZE"></span><span id="winhttp_option_web_socket_receive_buffer_size"></span>**WINHTTP\_OPTION\_WEB\_SOCKET\_RECEIVE\_BUFFER\_SIZE**
</dt> <dd> <dl> <dt>



Sets or retrieves a DWORD which specifies the receive buffer size to be used on WebSocket connections. Supported in Windows 8.1 and newer.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_WEB_SOCKET_SEND_BUFFER_SIZE"></span><span id="winhttp_option_web_socket_send_buffer_size"></span>**WINHTTP\_OPTION\_WEB\_SOCKET\_SEND\_BUFFER\_SIZE**
</dt> <dd> <dl> <dt>



Sets or retrieves a DWORD which specifies the send buffer size to be used on WebSocket connections. Supported in Windows 8.1 and newer.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_WORKER_THREAD_COUNT"></span><span id="winhttp_option_worker_thread_count"></span>**WINHTTP\_OPTION\_WORKER\_THREAD\_COUNT**
</dt> <dd> <dl> <dt>



Sets an unsigned long integer value that specifies the number of worker threads the thread pool should use for asynchronous completions. The default value of this option is zero, which specifies that the number of worker threads is equal to the number of CPUs on the system. This option can only be set on a **NULL**  [HINTERNET](hinternet-handles-in-winhttp.md) handle before an asynchronous operation has occurred. This option can only be set once.

**Windows Server 2008 R2 and Windows 7:** This flag is obsolete.


</dt> </dl> </dd> <dt>

<span id="WINHTTP_OPTION_WRITE_BUFFER_SIZE"></span><span id="winhttp_option_write_buffer_size"></span>**WINHTTP\_OPTION\_WRITE\_BUFFER\_SIZE**
</dt> <dd> <dl> <dt>



This option has been deprecated; it has no effect.


</dt> </dl> </dd> </dl>

## Remarks

The following table lists the option flags by specifying which handles they can act upon, whether they can be queried and set, and the data type used. An "X" indicates that the option flag is valid for use with the function or handle, while a "-" specifies that the option flag is invalid.



| Option flag                                        | Session handle | Request handle | Query option | Set option | Data type                                                                        |
|----------------------------------------------------|----------------|----------------|--------------|------------|----------------------------------------------------------------------------------|
| WINHTTP\_OPTION\_ASSURED\_NON\_BLOCKING\_CALLBACKS | X              | \-             | \-           | X          | **BOOL**                                                                         |
| WINHTTP\_OPTION\_AUTOLOGON\_POLICY                 | \-             | X              | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_CALLBACK                          | X              | X              | X            | X          | **LPVOID**                                                                       |
| WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT             | \-             | X              | \-           | X          | [**CERT\_CONTEXT**](https://docs.microsoft.com/windows/desktop/api/wincrypt/ns-wincrypt-_cert_context)                                       |
| WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST        | \-             | X              | X            | \-         | [**SecPkgContext\_IssuerListInfoEx**](https://docs.microsoft.com/windows/desktop/api/schannel/ns-schannel-_secpkgcontext_issuerlistinfoex)\* |
| WINHTTP\_OPTION\_CODEPAGE                          | X              | \-             | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_CONFIGURE\_PASSPORT\_AUTH         | X              | \-             | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_CONNECT\_INFO                     | \-             | X              | X            | \-         | [**WINHTTP\_CONNECTION\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-winhttp_connection_info)                     |
| WINHTTP\_OPTION\_CONNECT\_RETRIES                  | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_CONNECT\_TIMEOUT                  | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_CONTEXT\_VALUE                    | X              | X              | X            | X          | **DWORD\_PTR**                                                                   |
| WINHTTP\_OPTION\_DISABLE\_FEATURE                  | \-             | X              | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_ENABLE\_FEATURE                   | \*             | \*             | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_ENABLE\_HTTP\_PROTOCOL            | X              | X              | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_ENABLETRACING                     | \-             | \-             | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_EXTENDED\_ERROR                   | X              | X              | X            | \-         | **DWORD**                                                                        |
| WINHTTP\_OPTION\_GLOBAL\_PROXY\_CREDS              | X              | X              | \-           | X          | [**WINHTTP\_CREDS**](/windows/desktop/api/Winhttp/ns-winhttp-tagwinhttp_creds)                                          |
| WINHTTP\_OPTION\_GLOBAL\_SERVER\_CREDS             | X              | X              | \-           | X          | [**WINHTTP\_CREDS\_EX**](/windows/desktop/api/Winhttp/ns-winhttp-tagwinhttp_creds_ex)                                   |
| WINHTTP\_OPTION\_HANDLE\_TYPE                      | X              | X              | X            | \-         | **DWORD**                                                                        |
| WINHTTP\_OPTION\_HTTP\_VERSION                     | X              | X              | X            | X          | [**HTTP\_VERSION\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_1)                                 |
| WINHTTP\_OPTION\_HTTP\_PROTOCOL\_USED              | \-             | X              | X            | \-         | **DWORD**                                                                        |
| WINHTTP\_OPTION\_IS\_PROXY\_CONNECT\_RESPONSE      | X              | X              | X            | \-         | **BOOL**                                                                         |
| WINHTTP\_OPTION\_MAX\_CONNS\_PER\_1\_0\_SERVER     | X              | \-             | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_MAX\_CONNS\_PER\_SERVER           | X              | \-             | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_MAX\_HTTP\_AUTOMATIC\_REDIRECTS   | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_MAX\_HTTP\_STATUS\_CONTINUE       | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_MAX\_RESPONSE\_DRAIN\_SIZE        | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_MAX\_RESPONSE\_HEADER\_SIZE       | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_UPGRADE\_TO\_WEB\_SOCKET          | \-             | X              | \-           | X          | N/A                                                                              |
| WINHTTP\_OPTION\_PARENT\_HANDLE                    | X              | X              | X            | \-         | [HINTERNET](hinternet-handles-in-winhttp.md)                                    |
| WINHTTP\_OPTION\_PASSPORT\_COBRANDING\_TEXT        | \-             | X              | X            | \-         | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_PASSPORT\_COBRANDING\_URL         | \-             | X              | X            | \-         | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_PASSPORT\_RETURN\_URL             | \-             | X              | X            | \-         | **LPVOID**                                                                       |
| WINHTTP\_OPTION\_PASSPORT\_SIGN\_OUT               | X              | \-             | \-           | X          | **LPVOID**                                                                       |
| WINHTTP\_OPTION\_PASSWORD                          | \-             | X              | X            | X          | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_PROXY                             | X              | X              | X            | X          | [**WINHTTP\_PROXY\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_3)                              |
| WINHTTP\_OPTION\_PROXY\_PASSWORD                   | \-             | X              | X            | X          | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_PROXY\_SPN\_USED                  | \-             | X              | X            | \-         | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_PROXY\_USERNAME                   | \-             | X              | X            | X          | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_READ\_BUFFER\_SIZE                | \-             | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_RECEIVE\_PROXY\_CONNECT\_RESPONSE | X              | X              | \-           | X          | **BOOL**                                                                         |
| WINHTTP\_OPTION\_RECEIVE\_TIMEOUT                  | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_RECEIVE\_RESPONSE\_TIMEOUT        | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_REDIRECT\_POLICY                  | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_REJECT\_USERPWD\_IN\_URL          | \-             | X              | \-           | X          | **BOOL**                                                                         |
| WINHTTP\_OPTION\_REQUEST\_PRIORITY                 | \-             | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_RESOLVE\_TIMEOUT                  | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_SECURE\_PROTOCOLS                 | X              | \-             | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_SECURITY\_CERTIFICATE\_STRUCT     | \-             | X              | X            | \-         | [**WINHTTP\_CERTIFICATE\_INFO**](/windows/desktop/api/Winhttp/ns-winhttp-__unnamed_struct_5)                  |
| WINHTTP\_OPTION\_SECURITY\_FLAGS                   | \-             | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_SECURITY\_KEY\_BITNESS            | \-             | X              | X            | \-         | **DWORD**                                                                        |
| WINHTTP\_OPTION\_SEND\_TIMEOUT                     | X              | X              | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_SERVER\_CBT                       | \-             | X              | X            | \-         | [**SecPkgContext\_Bindings**](https://docs.microsoft.com/windows/desktop/api/sspi/ns-sspi-_secpkgcontext_bindings)\*                 |
| WINHTTP\_OPTION\_SERVER\_CERT\_CONTEXT             | \-             | X              | X            | \-         | [**CERT CONTEXT**](https://docs.microsoft.com/windows/desktop/api/wincrypt/ns-wincrypt-_cert_context)                                        |
| WINHTTP\_OPTION\_SERVER\_SPN\_USED                 | \-             | X              | X            | \-         | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_SPN                               | \-             | X              | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_UNLOAD\_NOTIFY\_EVEN              | X              | \-             | \-           | X          | [HINTERNET](hinternet-handles-in-winhttp.md)                                    |
| WINHTTP\_OPTION\_URL                               | \-             | X              | X            | \-         | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_USE\_GLOBAL\_SERVER\_CREDENTIALS  | X              | X              | \-           | X          | **BOOL**                                                                         |
| WINHTTP\_OPTION\_USER\_AGENT                       | X              | \-             | X            | X          | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_USERNAME                          | \-             | X              | X            | X          | **LPWSTR**                                                                       |
| WINHTTP\_OPTION\_WEB\_SOCKET\_CLOSE\_TIMEOUT       | \-             | \-             | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_WEB\_SOCKET\_KEEPALIVE\_INTERVAL  | \-             | \-             | X            | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_WORKER\_THREAD\_COUNT             | \-             | \-             | \-           | X          | **DWORD**                                                                        |
| WINHTTP\_OPTION\_WRITE\_BUFFER\_SIZE               | \-             | X              | X            | X          | **DWORD**                                                                        |



 

\* See the documentation for this flag earlier in this topic.

> [!Note]  
> For Windows XP and Windows 2000, see [Run-Time Requirements](winhttp-start-page.md).

 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>            |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>         |
| Redistributable<br/>          | WinHTTP 5.0 and Internet Explorer 5.01 or later on Windows XP and Windows 2000.<br/> |
| Header<br/>                   | <dl> <dt>Winhttp.h</dt> </dl>       |



## See also

<dl> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




