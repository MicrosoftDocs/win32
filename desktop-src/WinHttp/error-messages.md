---
description: The error values identified in this topic are returned by GetLastError when one of the Microsoft Windows HTTP Services (WinHTTP) functions fails.
ms.assetid: c8a863cd-d36c-4ec8-ac49-0b714a5e4cc2
title: Error Messages (Winhttp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Error Messages (Winhttp.h)

The error values listed below are returned by [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) when one of the Microsoft Windows HTTP Services (WinHTTP) functions fails, and are also returned in the lower 16 bits of [**HRESULT**](../com/structure-of-com-error-codes.md) error returns from the [**WinHttpRequest**](winhttprequest.md) object.

Error values whose names begin with "ERROR\_WINHTTP\_" are specific to the WinHTTP functions. The WinHTTP functions also return Windows error messages where appropriate.

<dl> <dt>

<span id="ERROR_WINHTTP_AUTO_PROXY_SERVICE_ERROR"></span><span id="error_winhttp_auto_proxy_service_error"></span>**ERROR\_WINHTTP\_AUTO\_PROXY\_SERVICE\_ERROR**
</dt> <dd> <dl> <dt>

12178
</dt> <dt>



Returned by [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl) when a proxy for the specified URL cannot be located.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_AUTODETECTION_FAILED"></span><span id="error_winhttp_autodetection_failed"></span>**ERROR\_WINHTTP\_AUTODETECTION\_FAILED**
</dt> <dd> <dl> <dt>

12180
</dt> <dt>



Returned by [**WinHttpDetectAutoProxyConfigUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpdetectautoproxyconfigurl) if WinHTTP was unable to discover the URL of the Proxy Auto-Configuration (PAC) file.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_BAD_AUTO_PROXY_SCRIPT"></span><span id="error_winhttp_bad_auto_proxy_script"></span>**ERROR\_WINHTTP\_BAD\_AUTO\_PROXY\_SCRIPT**
</dt> <dd> <dl> <dt>

12166
</dt> <dt>



An error occurred executing the script code in the Proxy Auto-Configuration (PAC) file.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CANNOT_CALL_AFTER_OPEN"></span><span id="error_winhttp_cannot_call_after_open"></span>**ERROR\_WINHTTP\_CANNOT\_CALL\_AFTER\_OPEN**
</dt> <dd> <dl> <dt>

12103
</dt> <dt>



Returned by the [**HttpRequest**](winhttprequest.md) object if a specified option cannot be requested after the [**Open**](iwinhttprequest-open.md) method has been called.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CANNOT_CALL_AFTER_SEND"></span><span id="error_winhttp_cannot_call_after_send"></span>**ERROR\_WINHTTP\_CANNOT\_CALL\_AFTER\_SEND**
</dt> <dd> <dl> <dt>

12102
</dt> <dt>



Returned by the [**HttpRequest**](winhttprequest.md) object if a requested operation cannot be performed after calling the [**Send**](iwinhttprequest-send.md) method.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CANNOT_CALL_BEFORE_OPEN"></span><span id="error_winhttp_cannot_call_before_open"></span>**ERROR\_WINHTTP\_CANNOT\_CALL\_BEFORE\_OPEN**
</dt> <dd> <dl> <dt>

12100
</dt> <dt>



Returned by the [**HttpRequest**](winhttprequest.md) object if a requested operation cannot be performed before calling the [**Open**](iwinhttprequest-open.md) method.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CANNOT_CALL_BEFORE_SEND"></span><span id="error_winhttp_cannot_call_before_send"></span>**ERROR\_WINHTTP\_CANNOT\_CALL\_BEFORE\_SEND**
</dt> <dd> <dl> <dt>

12101
</dt> <dt>



Returned by the [**HttpRequest**](winhttprequest.md) object if a requested operation cannot be performed before calling the [**Send**](iwinhttprequest-send.md) method.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CANNOT_CONNECT"></span><span id="error_winhttp_cannot_connect"></span>**ERROR\_WINHTTP\_CANNOT\_CONNECT**
</dt> <dd> <dl> <dt>

12029
</dt> <dt>



Returned if connection to the server failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED"></span><span id="error_winhttp_client_auth_cert_needed"></span>**ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**
</dt> <dd> <dl> <dt>



The server requires SSL client Authentication. The application retrieves the list of certificate issuers by calling [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) with the **WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST** option. For more information, see the **WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST** option.

If the server requests the client certificate, but does not require it, the application can alternately call [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) with the **WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT** option. In this case, the application specifies the WINHTTP\_NO\_CLIENT\_CERT\_CONTEXT macro in the *lpBuffer* parameter of **WinHttpSetOption**. For more information, see the **WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT** option.

**Windows Server 2003 with SP1 and Windows XP with SP2:** This error is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CLIENT_CERT_NO_ACCESS_PRIVATE_KEY"></span><span id="error_winhttp_client_cert_no_access_private_key"></span>**ERROR\_WINHTTP\_CLIENT\_CERT\_NO\_ACCESS\_PRIVATE\_KEY**
</dt> <dd> <dl> <dt>



The application does not have the required privileges to access the private key associated with the client certificate.

**Windows Server 2003 with SP1 and Windows XP with SP2:** This error is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CLIENT_CERT_NO_PRIVATE_KEY"></span><span id="error_winhttp_client_cert_no_private_key"></span>**ERROR\_WINHTTP\_CLIENT\_CERT\_NO\_PRIVATE\_KEY**
</dt> <dd> <dl> <dt>



The context for the SSL client certificate does not have a private key associated with it. The client certificate may have been imported to the computer without the private key.

**Windows Server 2003 with SP1 and Windows XP with SP2:** This error is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CHUNKED_ENCODING_HEADER_SIZE_OVERFLOW"></span><span id="error_winhttp_chunked_encoding_header_size_overflow"></span>**ERROR\_WINHTTP\_CHUNKED\_ENCODING\_HEADER\_SIZE\_OVERFLOW**
</dt> <dd> <dl> <dt>

12183
</dt> <dt>



Returned by [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) when an overflow condition is encountered in the course of parsing chunked encoding.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED"></span><span id="error_winhttp_client_auth_cert_needed"></span>**ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**
</dt> <dd> <dl> <dt>

12044
</dt> <dt>



Returned by [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) when the server requests client authentication.

**Windows Server 2003 with SP1 and Windows XP with SP2:** This error is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_CONNECTION_ERROR"></span><span id="error_winhttp_connection_error"></span>**ERROR\_WINHTTP\_CONNECTION\_ERROR**
</dt> <dd> <dl> <dt>

12030
</dt> <dt>



The connection with the server has been reset or terminated, or an incompatible SSL protocol was encountered. For example, WinHTTP version 5.1 does not support SSL2 unless the client specifically enables it.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_HEADER_ALREADY_EXISTS"></span><span id="error_winhttp_header_already_exists"></span>**ERROR\_WINHTTP\_HEADER\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

12155
</dt> <dt>



Obsolete; no longer used.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_HEADER_COUNT_EXCEEDED"></span><span id="error_winhttp_header_count_exceeded"></span>**ERROR\_WINHTTP\_HEADER\_COUNT\_EXCEEDED**
</dt> <dd> <dl> <dt>

12181
</dt> <dt>



Returned by [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) when a larger number of headers were present in a response than WinHTTP could receive.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_HEADER_NOT_FOUND"></span><span id="error_winhttp_header_not_found"></span>**ERROR\_WINHTTP\_HEADER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

12150
</dt> <dt>



The requested header cannot be located.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_HEADER_SIZE_OVERFLOW"></span><span id="error_winhttp_header_size_overflow"></span>**ERROR\_WINHTTP\_HEADER\_SIZE\_OVERFLOW**
</dt> <dd> <dl> <dt>

12182
</dt> <dt>



Returned by [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) when the size of headers received exceeds the limit for the request handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_INCORRECT_HANDLE_STATE"></span><span id="error_winhttp_incorrect_handle_state"></span>**ERROR\_WINHTTP\_INCORRECT\_HANDLE\_STATE**
</dt> <dd> <dl> <dt>

12019
</dt> <dt>



The requested operation cannot be carried out because the handle supplied is not in the correct state.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_INCORRECT_HANDLE_TYPE"></span><span id="error_winhttp_incorrect_handle_type"></span>**ERROR\_WINHTTP\_INCORRECT\_HANDLE\_TYPE**
</dt> <dd> <dl> <dt>

12018
</dt> <dt>



The type of handle supplied is incorrect for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_INTERNAL_ERROR"></span><span id="error_winhttp_internal_error"></span>**ERROR\_WINHTTP\_INTERNAL\_ERROR**
</dt> <dd> <dl> <dt>

12004
</dt> <dt>



An internal error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_INVALID_OPTION"></span><span id="error_winhttp_invalid_option"></span>**ERROR\_WINHTTP\_INVALID\_OPTION**
</dt> <dd> <dl> <dt>

12009
</dt> <dt>



A request to [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) or [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) specified an invalid option value.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_INVALID_QUERY_REQUEST"></span><span id="error_winhttp_invalid_query_request"></span>**ERROR\_WINHTTP\_INVALID\_QUERY\_REQUEST**
</dt> <dd> <dl> <dt>

12154
</dt> <dt>



Obsolete; no longer used.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_INVALID_SERVER_RESPONSE"></span><span id="error_winhttp_invalid_server_response"></span>**ERROR\_WINHTTP\_INVALID\_SERVER\_RESPONSE**
</dt> <dd> <dl> <dt>

12152
</dt> <dt>



The server response cannot be parsed.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_INVALID_URL"></span><span id="error_winhttp_invalid_url"></span>**ERROR\_WINHTTP\_INVALID\_URL**
</dt> <dd> <dl> <dt>

12005
</dt> <dt>



The URL is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_LOGIN_FAILURE"></span><span id="error_winhttp_login_failure"></span>**ERROR\_WINHTTP\_LOGIN\_FAILURE**
</dt> <dd> <dl> <dt>

12015
</dt> <dt>



The login attempt failed. When this error is encountered, the request handle should be closed with [**WinHttpCloseHandle**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpclosehandle). A new request handle must be created before retrying the function that originally produced this error.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_NAME_NOT_RESOLVED"></span><span id="error_winhttp_name_not_resolved"></span>**ERROR\_WINHTTP\_NAME\_NOT\_RESOLVED**
</dt> <dd> <dl> <dt>

12007
</dt> <dt>



The server name cannot be resolved.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_NOT_INITIALIZED"></span><span id="error_winhttp_not_initialized"></span>**ERROR\_WINHTTP\_NOT\_INITIALIZED**
</dt> <dd> <dl> <dt>

12172
</dt> <dt>



Obsolete; no longer used.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_OPERATION_CANCELLED"></span><span id="error_winhttp_operation_cancelled"></span>**ERROR\_WINHTTP\_OPERATION\_CANCELLED**
</dt> <dd> <dl> <dt>

12017
</dt> <dt>



The operation was canceled, usually because the handle on which the request was operating was closed before the operation completed.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_OPTION_NOT_SETTABLE"></span><span id="error_winhttp_option_not_settable"></span>**ERROR\_WINHTTP\_OPTION\_NOT\_SETTABLE**
</dt> <dd> <dl> <dt>

12011
</dt> <dt>



The requested option cannot be set, only queried.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_OUT_OF_HANDLES"></span><span id="error_winhttp_out_of_handles"></span>**ERROR\_WINHTTP\_OUT\_OF\_HANDLES**
</dt> <dd> <dl> <dt>

12001
</dt> <dt>



Obsolete; no longer used.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_REDIRECT_FAILED"></span><span id="error_winhttp_redirect_failed"></span>**ERROR\_WINHTTP\_REDIRECT\_FAILED**
</dt> <dd> <dl> <dt>

12156
</dt> <dt>



The redirection failed because either the scheme changed or all attempts made to redirect failed (default is five attempts).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_RESEND_REQUEST"></span><span id="error_winhttp_resend_request"></span>**ERROR\_WINHTTP\_RESEND\_REQUEST**
</dt> <dd> <dl> <dt>

12032
</dt> <dt>



The WinHTTP function failed. The desired function can be retried on the same request handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_RESPONSE_DRAIN_OVERFLOW"></span><span id="error_winhttp_response_drain_overflow"></span>**ERROR\_WINHTTP\_RESPONSE\_DRAIN\_OVERFLOW**
</dt> <dd> <dl> <dt>

12184
</dt> <dt>



Returned when an incoming response exceeds an internal WinHTTP size limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SCRIPT_EXECUTION_ERROR"></span><span id="error_winhttp_script_execution_error"></span>**ERROR\_WINHTTP\_SCRIPT\_EXECUTION\_ERROR**
</dt> <dd> <dl> <dt>

12177
</dt> <dt>



An error was encountered while executing a script.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_CERT_CN_INVALID"></span><span id="error_winhttp_secure_cert_cn_invalid"></span>**ERROR\_WINHTTP\_SECURE\_CERT\_CN\_INVALID**
</dt> <dd> <dl> <dt>

12038
</dt> <dt>



Returned when a certificate CN name does not match the passed value (equivalent to a **CERT\_E\_CN\_NO\_MATCH** error).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_CERT_DATE_INVALID"></span><span id="error_winhttp_secure_cert_date_invalid"></span>**ERROR\_WINHTTP\_SECURE\_CERT\_DATE\_INVALID**
</dt> <dd> <dl> <dt>

12037
</dt> <dt>



Indicates that a required certificate is not within its validity period when verifying against the current system clock or the timestamp in the signed file, or that the validity periods of the certification chain do not nest correctly (equivalent to a **CERT\_E\_EXPIRED** or a **CERT\_E\_VALIDITYPERIODNESTING** error).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_CERT_REV_FAILED"></span><span id="error_winhttp_secure_cert_rev_failed"></span>**ERROR\_WINHTTP\_SECURE\_CERT\_REV\_FAILED**
</dt> <dd> <dl> <dt>

12057
</dt> <dt>



Indicates that revocation cannot be checked because the revocation server was offline (equivalent to **CRYPT\_E\_REVOCATION\_OFFLINE**).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_CERT_REVOKED"></span><span id="error_winhttp_secure_cert_revoked"></span>**ERROR\_WINHTTP\_SECURE\_CERT\_REVOKED**
</dt> <dd> <dl> <dt>

12170
</dt> <dt>



Indicates that a certificate has been revoked (equivalent to **CRYPT\_E\_REVOKED**).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_CERT_WRONG_USAGE"></span><span id="error_winhttp_secure_cert_wrong_usage"></span>**ERROR\_WINHTTP\_SECURE\_CERT\_WRONG\_USAGE**
</dt> <dd> <dl> <dt>

12179
</dt> <dt>



Indicates that a certificate is not valid for the requested usage (equivalent to **CERT\_E\_WRONG\_USAGE**).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_CHANNEL_ERROR"></span><span id="error_winhttp_secure_channel_error"></span>**ERROR\_WINHTTP\_SECURE\_CHANNEL\_ERROR**
</dt> <dd> <dl> <dt>

12157
</dt> <dt>



Indicates that an error occurred having to do with a secure channel (equivalent to error codes that begin with "SEC\_E\_" and "SEC\_I\_" listed in the "winerror.h" header file).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_FAILURE"></span><span id="error_winhttp_secure_failure"></span>**ERROR\_WINHTTP\_SECURE\_FAILURE**
</dt> <dd> <dl> <dt>

12175
</dt> <dt>



One or more errors were found in the Secure Sockets Layer (SSL) certificate sent by the server. To determine what type of error was encountered, check for a [**WINHTTP\_CALLBACK\_STATUS\_SECURE\_FAILURE**](/windows/win32/api/winhttp/nc-winhttp-winhttp_status_callback) notification in a status callback function. For more information, see [**WINHTTP\_STATUS\_CALLBACK**](/windows/win32/api/winhttp/nc-winhttp-winhttp_status_callback).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_INVALID_CA"></span><span id="error_winhttp_secure_invalid_ca"></span>**ERROR\_WINHTTP\_SECURE\_INVALID\_CA**
</dt> <dd> <dl> <dt>

12045
</dt> <dt>



Indicates that a certificate chain was processed, but terminated in a root certificate that is not trusted by the trust provider (equivalent to **CERT\_E\_UNTRUSTEDROOT**).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SECURE_INVALID_CERT"></span><span id="error_winhttp_secure_invalid_cert"></span>**ERROR\_WINHTTP\_SECURE\_INVALID\_CERT**
</dt> <dd> <dl> <dt>

12169
</dt> <dt>



Indicates that a certificate is invalid (equivalent to errors such as **CERT\_E\_ROLE**, **CERT\_E\_PATHLENCONST**, **CERT\_E\_CRITICAL**, **CERT\_E\_PURPOSE**, **CERT\_E\_ISSUERCHAINING**, **CERT\_E\_MALFORMED** and **CERT\_E\_CHAINING**).


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_SHUTDOWN"></span><span id="error_winhttp_shutdown"></span>**ERROR\_WINHTTP\_SHUTDOWN**
</dt> <dd> <dl> <dt>

12012
</dt> <dt>



The WinHTTP function support is being shut down or unloaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_TIMEOUT"></span><span id="error_winhttp_timeout"></span>**ERROR\_WINHTTP\_TIMEOUT**
</dt> <dd> <dl> <dt>

12002
</dt> <dt>



The request has timed out.

This error can be returned as a result of TCP/IP time-out behavior, regardless of time-out values set in Windows HTTP Services.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_UNABLE_TO_DOWNLOAD_SCRIPT"></span><span id="error_winhttp_unable_to_download_script"></span>**ERROR\_WINHTTP\_UNABLE\_TO\_DOWNLOAD\_SCRIPT**
</dt> <dd> <dl> <dt>

12167
</dt> <dt>



The PAC file cannot be downloaded. For example, the server referenced by the PAC URL may not have been reachable, or the server returned a 404 NOT FOUND response.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_UNHANDLED_SCRIPT_TYPE"></span><span id="error_winhttp_unhandled_script_type"></span>**ERROR\_WINHTTP\_UNHANDLED\_SCRIPT\_TYPE**
</dt> <dd> <dl> <dt>

12176
</dt> <dt>



The script type is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP_UNRECOGNIZED_SCHEME"></span><span id="error_winhttp_unrecognized_scheme"></span>**ERROR\_WINHTTP\_UNRECOGNIZED\_SCHEME**
</dt> <dd> <dl> <dt>

12006
</dt> <dt>



The URL specified a scheme other than "http:" or "https:".


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_ENOUGH_MEMORY"></span><span id="error_not_enough_memory"></span>**ERROR\_NOT\_ENOUGH\_MEMORY**
</dt> <dd> <dl> <dt>



Not enough memory was available to complete the requested operation.

**Header:** Declared in Winerror.h


</dt> </dl> </dd> <dt>

<span id="ERROR_INSUFFICIENT_BUFFER"></span><span id="error_insufficient_buffer"></span>**ERROR\_INSUFFICIENT\_BUFFER**
</dt> <dd> <dl> <dt>



The size, in bytes, of the buffer supplied to a function was insufficient to contain the returned data. For more information, see the specific function.

**Header:** Declared in Winerror.h


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_HANDLE"></span><span id="error_invalid_handle"></span>**ERROR\_INVALID\_HANDLE**
</dt> <dd> <dl> <dt>



The handle passed to the application programming interface (API) has been either invalidated or closed.

**Header:** Declared in Winerror.h


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_FILES"></span><span id="error_no_more_files"></span>**ERROR\_NO\_MORE\_FILES**
</dt> <dd> <dl> <dt>



No more files have been found.

**Header:** Declared in Winerror.h


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_ITEMS"></span><span id="error_no_more_items"></span>**ERROR\_NO\_MORE\_ITEMS**
</dt> <dd> <dl> <dt>



No more items have been found.

**Header:** Declared in Winerror.h


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SUPPORTED"></span><span id="error_not_supported"></span>**ERROR\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>



The required protocol stack is not loaded and the application cannot start WinSock.

**Header:** Declared in Winerror.h


</dt> </dl> </dd> </dl>

## Remarks

For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHttp start page.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>            |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>         |
| Redistributable<br/>          | WinHTTP 5.0 and Internet Explorer 5.01 or later on Windows XP and Windows 2000.<br/> |
| Header<br/>                   | <dl> <dt>Winhttp.h</dt> </dl>       |



## See also

<dl> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

