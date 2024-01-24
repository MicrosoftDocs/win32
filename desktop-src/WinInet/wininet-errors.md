---
title: Error Messages (Wininet.h)
description: The WinINet functions return error codes where appropriate. The following errors are specific to the WinINet functions.
ms.assetid: 338bf65f-ebe5-4434-8407-9ab2a4c8d381
topic_type:
- apiref
api_name:
- ERROR_FTP_DROPPED
- ERROR_FTP_NO_PASSIVE_MODE
- ERROR_FTP_TRANSFER_IN_PROGRESS
- ERROR_GOPHER_ATTRIBUTE_NOT_FOUND
- ERROR_GOPHER_DATA_ERROR
- ERROR_GOPHER_END_OF_DATA
- ERROR_GOPHER_INCORRECT_LOCATOR_TYPE
- ERROR_GOPHER_INVALID_LOCATOR
- ERROR_GOPHER_NOT_FILE
- ERROR_GOPHER_NOT_GOPHER_PLUS
- ERROR_GOPHER_PROTOCOL_ERROR
- ERROR_GOPHER_UNKNOWN_LOCATOR
- ERROR_HTTP_COOKIE_DECLINED
- ERROR_HTTP_COOKIE_NEEDS_CONFIRMATION
- ERROR_HTTP_DOWNLEVEL_SERVER
- ERROR_HTTP_HEADER_ALREADY_EXISTS
- ERROR_HTTP_HEADER_NOT_FOUND
- ERROR_HTTP_INVALID_HEADER
- ERROR_HTTP_INVALID_QUERY_REQUEST
- ERROR_HTTP_INVALID_SERVER_RESPONSE
- ERROR_HTTP_NOT_REDIRECTED
- ERROR_HTTP_REDIRECT_FAILED
- ERROR_HTTP_REDIRECT_NEEDS_CONFIRMATION
- ERROR_INTERNET_ASYNC_THREAD_FAILED
- ERROR_INTERNET_BAD_AUTO_PROXY_SCRIPT
- ERROR_INTERNET_BAD_OPTION_LENGTH
- ERROR_INTERNET_BAD_REGISTRY_PARAMETER
- ERROR_INTERNET_CANNOT_CONNECT
- ERROR_INTERNET_CHG_POST_IS_NON_SECURE
- ERROR_INTERNET_CLIENT_AUTH_CERT_NEEDED
- ERROR_INTERNET_CLIENT_AUTH_NOT_SETUP
- ERROR_INTERNET_CONNECTION_ABORTED
- ERROR_INTERNET_CONNECTION_RESET
- ERROR_INTERNET_DECODING_FAILED
- ERROR_INTERNET_DIALOG_PENDING
- ERROR_INTERNET_DISCONNECTED
- ERROR_INTERNET_EXTENDED_ERROR
- ERROR_INTERNET_FAILED_DUETOSECURITYCHECK
- ERROR_INTERNET_FORCE_RETRY
- ERROR_INTERNET_FORTEZZA_LOGIN_NEEDED
- ERROR_INTERNET_HANDLE_EXISTS
- ERROR_INTERNET_HTTP_TO_HTTPS_ON_REDIR
- ERROR_INTERNET_HTTPS_HTTP_SUBMIT_REDIR
- ERROR_INTERNET_HTTPS_TO_HTTP_ON_REDIR
- ERROR_INTERNET_INCORRECT_FORMAT
- ERROR_INTERNET_INCORRECT_HANDLE_STATE
- ERROR_INTERNET_INCORRECT_HANDLE_TYPE
- ERROR_INTERNET_INCORRECT_PASSWORD
- ERROR_INTERNET_INCORRECT_USER_NAME
- ERROR_INTERNET_INSERT_CDROM
- ERROR_INTERNET_INTERNAL_ERROR
- ERROR_INTERNET_INVALID_CA
- ERROR_INTERNET_INVALID_OPERATION
- ERROR_INTERNET_INVALID_OPTION
- ERROR_INTERNET_INVALID_PROXY_REQUEST
- ERROR_INTERNET_INVALID_URL
- ERROR_INTERNET_ITEM_NOT_FOUND
- ERROR_INTERNET_LOGIN_FAILURE
- ERROR_INTERNET_LOGIN_FAILURE_DISPLAY_ENTITY_BODY
- ERROR_INTERNET_MIXED_SECURITY
- ERROR_INTERNET_NAME_NOT_RESOLVED
- ERROR_INTERNET_NEED_MSN_SSPI_PKG
- ERROR_INTERNET_NEED_UI
- ERROR_INTERNET_NO_CALLBACK
- ERROR_INTERNET_NO_CONTEXT
- ERROR_INTERNET_NO_DIRECT_ACCESS
- ERROR_INTERNET_NOT_INITIALIZED
- ERROR_INTERNET_NOT_PROXY_REQUEST
- ERROR_INTERNET_OPERATION_CANCELLED
- ERROR_INTERNET_OPTION_NOT_SETTABLE
- ERROR_INTERNET_OUT_OF_HANDLES
- ERROR_INTERNET_POST_IS_NON_SECURE
- ERROR_INTERNET_PROTOCOL_NOT_FOUND
- ERROR_INTERNET_PROXY_SERVER_UNREACHABLE
- ERROR_INTERNET_REDIRECT_SCHEME_CHANGE
- ERROR_INTERNET_REGISTRY_VALUE_NOT_FOUND
- ERROR_INTERNET_REQUEST_PENDING
- ERROR_INTERNET_RETRY_DIALOG
- ERROR_INTERNET_SEC_CERT_CN_INVALID
- ERROR_INTERNET_SEC_CERT_DATE_INVALID
- ERROR_INTERNET_SEC_CERT_ERRORS
- ERROR_INTERNET_SEC_CERT_NO_REV
- ERROR_INTERNET_SEC_CERT_REV_FAILED
- ERROR_INTERNET_SEC_CERT_REVOKED
- ERROR_INTERNET_SEC_INVALID_CERT
- ERROR_INTERNET_SECURITY_CHANNEL_ERROR
- ERROR_INTERNET_SERVER_UNREACHABLE
- ERROR_INTERNET_SHUTDOWN
- ERROR_INTERNET_TCPIP_NOT_INSTALLED
- ERROR_INTERNET_TIMEOUT
- ERROR_INTERNET_UNABLE_TO_CACHE_FILE
- ERROR_INTERNET_UNABLE_TO_DOWNLOAD_SCRIPT
- ERROR_INTERNET_UNRECOGNIZED_SCHEME
- ERROR_INVALID_HANDLE
- ERROR_MORE_DATA
- ERROR_NO_MORE_FILES
- ERROR_NO_MORE_ITEMS
api_location:
- Wininet.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Error Messages (Wininet.h)

The WinINet functions return error codes where appropriate. The following errors are specific to the WinINet functions.

<dl> <dt>

<span id="ERROR_FTP_DROPPED"></span><span id="error_ftp_dropped"></span>**ERROR\_FTP\_DROPPED**
</dt> <dd> <dl> <dt>

12111
</dt> <dt>



The FTP operation was not completed because the session was aborted.


</dt> </dl> </dd> <dt>

<span id="ERROR_FTP_NO_PASSIVE_MODE"></span><span id="error_ftp_no_passive_mode"></span>**ERROR\_FTP\_NO\_PASSIVE\_MODE**
</dt> <dd> <dl> <dt>

12112
</dt> <dt>



Passive mode is not available on the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_FTP_TRANSFER_IN_PROGRESS"></span><span id="error_ftp_transfer_in_progress"></span>**ERROR\_FTP\_TRANSFER\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

12110
</dt> <dt>



The requested operation cannot be made on the FTP session handle because an operation is already in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_ATTRIBUTE_NOT_FOUND"></span><span id="error_gopher_attribute_not_found"></span>**ERROR\_GOPHER\_ATTRIBUTE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

12137
</dt> <dt>



The requested attribute could not be located.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_DATA_ERROR"></span><span id="error_gopher_data_error"></span>**ERROR\_GOPHER\_DATA\_ERROR**
</dt> <dd> <dl> <dt>

12132
</dt> <dt>



An error was detected while receiving data from the Gopher server.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_END_OF_DATA"></span><span id="error_gopher_end_of_data"></span>**ERROR\_GOPHER\_END\_OF\_DATA**
</dt> <dd> <dl> <dt>

12133
</dt> <dt>



The end of the data has been reached.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_INCORRECT_LOCATOR_TYPE"></span><span id="error_gopher_incorrect_locator_type"></span>**ERROR\_GOPHER\_INCORRECT\_LOCATOR\_TYPE**
</dt> <dd> <dl> <dt>

12135
</dt> <dt>



The type of the locator is not correct for this operation.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_INVALID_LOCATOR"></span><span id="error_gopher_invalid_locator"></span>**ERROR\_GOPHER\_INVALID\_LOCATOR**
</dt> <dd> <dl> <dt>

12134
</dt> <dt>



The supplied locator is not valid.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_NOT_FILE"></span><span id="error_gopher_not_file"></span>**ERROR\_GOPHER\_NOT\_FILE**
</dt> <dd> <dl> <dt>

12131
</dt> <dt>



The request must be made for a file locator.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_NOT_GOPHER_PLUS"></span><span id="error_gopher_not_gopher_plus"></span>**ERROR\_GOPHER\_NOT\_GOPHER\_PLUS**
</dt> <dd> <dl> <dt>

12136
</dt> <dt>



The requested operation can be made only against a Gopher+ server, or with a locator that specifies a Gopher+ operation.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_PROTOCOL_ERROR"></span><span id="error_gopher_protocol_error"></span>**ERROR\_GOPHER\_PROTOCOL\_ERROR**
</dt> <dd> <dl> <dt>

12130
</dt> <dt>



An error was detected while parsing data returned from the Gopher server.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_GOPHER_UNKNOWN_LOCATOR"></span><span id="error_gopher_unknown_locator"></span>**ERROR\_GOPHER\_UNKNOWN\_LOCATOR**
</dt> <dd> <dl> <dt>

12138
</dt> <dt>



The locator type is unknown.

> [!Note]  
> Windows XP and Windows Server 2003 R2 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_COOKIE_DECLINED"></span><span id="error_http_cookie_declined"></span>**ERROR\_HTTP\_COOKIE\_DECLINED**
</dt> <dd> <dl> <dt>

12162
</dt> <dt>



The HTTP cookie was declined by the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_COOKIE_NEEDS_CONFIRMATION"></span><span id="error_http_cookie_needs_confirmation"></span>**ERROR\_HTTP\_COOKIE\_NEEDS\_CONFIRMATION**
</dt> <dd> <dl> <dt>

12161
</dt> <dt>



The HTTP cookie requires confirmation.

> [!Note]  
> Windows Vista and Windows Server 2008 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_DOWNLEVEL_SERVER"></span><span id="error_http_downlevel_server"></span>**ERROR\_HTTP\_DOWNLEVEL\_SERVER**
</dt> <dd> <dl> <dt>

12151
</dt> <dt>



The server did not return any headers.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_HEADER_ALREADY_EXISTS"></span><span id="error_http_header_already_exists"></span>**ERROR\_HTTP\_HEADER\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

12155
</dt> <dt>



The header could not be added because it already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_HEADER_NOT_FOUND"></span><span id="error_http_header_not_found"></span>**ERROR\_HTTP\_HEADER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

12150
</dt> <dt>



The requested header could not be located.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_INVALID_HEADER"></span><span id="error_http_invalid_header"></span>**ERROR\_HTTP\_INVALID\_HEADER**
</dt> <dd> <dl> <dt>

12153
</dt> <dt>



The supplied header is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_INVALID_QUERY_REQUEST"></span><span id="error_http_invalid_query_request"></span>**ERROR\_HTTP\_INVALID\_QUERY\_REQUEST**
</dt> <dd> <dl> <dt>

12154
</dt> <dt>



The request made to [**HttpQueryInfo**](/windows/desktop/api/Wininet/nf-wininet-httpqueryinfoa) is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_INVALID_SERVER_RESPONSE"></span><span id="error_http_invalid_server_response"></span>**ERROR\_HTTP\_INVALID\_SERVER\_RESPONSE**
</dt> <dd> <dl> <dt>

12152
</dt> <dt>



The server response could not be parsed.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_NOT_REDIRECTED"></span><span id="error_http_not_redirected"></span>**ERROR\_HTTP\_NOT\_REDIRECTED**
</dt> <dd> <dl> <dt>

12160
</dt> <dt>



The HTTP request was not redirected.


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_REDIRECT_FAILED"></span><span id="error_http_redirect_failed"></span>**ERROR\_HTTP\_REDIRECT\_FAILED**
</dt> <dd> <dl> <dt>

12156
</dt> <dt>



The redirection failed because either the scheme changed (for example, HTTP to FTP) or all attempts made to redirect failed (default is five attempts).


</dt> </dl> </dd> <dt>

<span id="ERROR_HTTP_REDIRECT_NEEDS_CONFIRMATION"></span><span id="error_http_redirect_needs_confirmation"></span>**ERROR\_HTTP\_REDIRECT\_NEEDS\_CONFIRMATION**
</dt> <dd> <dl> <dt>

12168
</dt> <dt>



The redirection requires user confirmation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_ASYNC_THREAD_FAILED"></span><span id="error_internet_async_thread_failed"></span>**ERROR\_INTERNET\_ASYNC\_THREAD\_FAILED**
</dt> <dd> <dl> <dt>

12047
</dt> <dt>



The application could not start an asynchronous thread.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_BAD_AUTO_PROXY_SCRIPT"></span><span id="error_internet_bad_auto_proxy_script"></span>**ERROR\_INTERNET\_BAD\_AUTO\_PROXY\_SCRIPT**
</dt> <dd> <dl> <dt>

12166
</dt> <dt>



There was an error in the automatic proxy configuration script.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_BAD_OPTION_LENGTH"></span><span id="error_internet_bad_option_length"></span>**ERROR\_INTERNET\_BAD\_OPTION\_LENGTH**
</dt> <dd> <dl> <dt>

12010
</dt> <dt>



The length of an option supplied to [**InternetQueryOption**](/windows/desktop/api/Wininet/nf-wininet-internetqueryoptiona) or [**InternetSetOption**](/windows/desktop/api/Wininet/nf-wininet-internetsetoptiona) is incorrect for the type of option specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_BAD_REGISTRY_PARAMETER"></span><span id="error_internet_bad_registry_parameter"></span>**ERROR\_INTERNET\_BAD\_REGISTRY\_PARAMETER**
</dt> <dd> <dl> <dt>

12022
</dt> <dt>



A required registry value was located but is an incorrect type or has an invalid value.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_CANNOT_CONNECT"></span><span id="error_internet_cannot_connect"></span>**ERROR\_INTERNET\_CANNOT\_CONNECT**
</dt> <dd> <dl> <dt>

12029
</dt> <dt>



The attempt to connect to the server failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_CHG_POST_IS_NON_SECURE"></span><span id="error_internet_chg_post_is_non_secure"></span>**ERROR\_INTERNET\_CHG\_POST\_IS\_NON\_SECURE**
</dt> <dd> <dl> <dt>

12042
</dt> <dt>



The application is posting and attempting to change multiple lines of text on a server that is not secure.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_CLIENT_AUTH_CERT_NEEDED"></span><span id="error_internet_client_auth_cert_needed"></span>**ERROR\_INTERNET\_CLIENT\_AUTH\_CERT\_NEEDED**
</dt> <dd> <dl> <dt>

12044
</dt> <dt>



The server is requesting client authentication.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_CLIENT_AUTH_NOT_SETUP"></span><span id="error_internet_client_auth_not_setup"></span>**ERROR\_INTERNET\_CLIENT\_AUTH\_NOT\_SETUP**
</dt> <dd> <dl> <dt>

12046
</dt> <dt>



Client authorization is not set up on this computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_CONNECTION_ABORTED"></span><span id="error_internet_connection_aborted"></span>**ERROR\_INTERNET\_CONNECTION\_ABORTED**
</dt> <dd> <dl> <dt>

12030
</dt> <dt>



The connection with the server has been terminated.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_CONNECTION_RESET"></span><span id="error_internet_connection_reset"></span>**ERROR\_INTERNET\_CONNECTION\_RESET**
</dt> <dd> <dl> <dt>

12031
</dt> <dt>



The connection with the server has been reset.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_DECODING_FAILED"></span><span id="error_internet_decoding_failed"></span>**ERROR\_INTERNET\_DECODING\_FAILED**
</dt> <dd> <dl> <dt>

12175
</dt> <dt>



WinINet failed to perform content decoding on the response. For more information, see the [**Content Encoding**](content-encoding.md) topic.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_DIALOG_PENDING"></span><span id="error_internet_dialog_pending"></span>**ERROR\_INTERNET\_DIALOG\_PENDING**
</dt> <dd> <dl> <dt>

12049
</dt> <dt>



Another thread has a password dialog box in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_DISCONNECTED"></span><span id="error_internet_disconnected"></span>**ERROR\_INTERNET\_DISCONNECTED**
</dt> <dd> <dl> <dt>

12163
</dt> <dt>



The Internet connection has been lost.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_EXTENDED_ERROR"></span><span id="error_internet_extended_error"></span>**ERROR\_INTERNET\_EXTENDED\_ERROR**
</dt> <dd> <dl> <dt>

12003
</dt> <dt>



An extended error was returned from the server. This is typically a string or buffer containing a verbose error message. Call [**InternetGetLastResponseInfo**](/windows/desktop/api/Wininet/nf-wininet-internetgetlastresponseinfoa) to retrieve the error text.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_FAILED_DUETOSECURITYCHECK"></span><span id="error_internet_failed_duetosecuritycheck"></span>**ERROR\_INTERNET\_FAILED\_DUETOSECURITYCHECK**
</dt> <dd> <dl> <dt>

12171
</dt> <dt>



The function failed due to a security check.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_FORCE_RETRY"></span><span id="error_internet_force_retry"></span>**ERROR\_INTERNET\_FORCE\_RETRY**
</dt> <dd> <dl> <dt>

12032
</dt> <dt>



The function needs to redo the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_FORTEZZA_LOGIN_NEEDED"></span><span id="error_internet_fortezza_login_needed"></span>**ERROR\_INTERNET\_FORTEZZA\_LOGIN\_NEEDED**
</dt> <dd> <dl> <dt>

12054
</dt> <dt>



The requested resource requires Fortezza authentication.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_HANDLE_EXISTS"></span><span id="error_internet_handle_exists"></span>**ERROR\_INTERNET\_HANDLE\_EXISTS**
</dt> <dd> <dl> <dt>

12036
</dt> <dt>



The request failed because the handle already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_HTTP_TO_HTTPS_ON_REDIR"></span><span id="error_internet_http_to_https_on_redir"></span>**ERROR\_INTERNET\_HTTP\_TO\_HTTPS\_ON\_REDIR**
</dt> <dd> <dl> <dt>

12039
</dt> <dt>



The application is moving from a non-SSL to an SSL connection because of a redirect.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_HTTPS_HTTP_SUBMIT_REDIR"></span><span id="error_internet_https_http_submit_redir"></span>**ERROR\_INTERNET\_HTTPS\_HTTP\_SUBMIT\_REDIR**
</dt> <dd> <dl> <dt>

12052
</dt> <dt>



The data being submitted to an SSL connection is being redirected to a non-SSL connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_HTTPS_TO_HTTP_ON_REDIR"></span><span id="error_internet_https_to_http_on_redir"></span>**ERROR\_INTERNET\_HTTPS\_TO\_HTTP\_ON\_REDIR**
</dt> <dd> <dl> <dt>

12040
</dt> <dt>



The application is moving from an SSL to an non-SSL connection because of a redirect.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INCORRECT_FORMAT"></span><span id="error_internet_incorrect_format"></span>**ERROR\_INTERNET\_INCORRECT\_FORMAT**
</dt> <dd> <dl> <dt>

12027
</dt> <dt>



The format of the request is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INCORRECT_HANDLE_STATE"></span><span id="error_internet_incorrect_handle_state"></span>**ERROR\_INTERNET\_INCORRECT\_HANDLE\_STATE**
</dt> <dd> <dl> <dt>

12019
</dt> <dt>



The requested operation cannot be carried out because the handle supplied is not in the correct state.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INCORRECT_HANDLE_TYPE"></span><span id="error_internet_incorrect_handle_type"></span>**ERROR\_INTERNET\_INCORRECT\_HANDLE\_TYPE**
</dt> <dd> <dl> <dt>

12018
</dt> <dt>



The type of handle supplied is incorrect for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INCORRECT_PASSWORD"></span><span id="error_internet_incorrect_password"></span>**ERROR\_INTERNET\_INCORRECT\_PASSWORD**
</dt> <dd> <dl> <dt>

12014
</dt> <dt>



The request to connect and log on to an FTP server could not be completed because the supplied password is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INCORRECT_USER_NAME"></span><span id="error_internet_incorrect_user_name"></span>**ERROR\_INTERNET\_INCORRECT\_USER\_NAME**
</dt> <dd> <dl> <dt>

12013
</dt> <dt>



The request to connect and log on to an FTP server could not be completed because the supplied user name is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INSERT_CDROM"></span><span id="error_internet_insert_cdrom"></span>**ERROR\_INTERNET\_INSERT\_CDROM**
</dt> <dd> <dl> <dt>

12053
</dt> <dt>



The request requires a CD-ROM to be inserted in the CD-ROM drive to locate the resource requested.

> [!Note]  
> Windows Vista and Windows Server 2008 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INTERNAL_ERROR"></span><span id="error_internet_internal_error"></span>**ERROR\_INTERNET\_INTERNAL\_ERROR**
</dt> <dd> <dl> <dt>

12004
</dt> <dt>



An internal error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INVALID_CA"></span><span id="error_internet_invalid_ca"></span>**ERROR\_INTERNET\_INVALID\_CA**
</dt> <dd> <dl> <dt>

12045
</dt> <dt>



The function is unfamiliar with the Certificate Authority that generated the server's certificate.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INVALID_OPERATION"></span><span id="error_internet_invalid_operation"></span>**ERROR\_INTERNET\_INVALID\_OPERATION**
</dt> <dd> <dl> <dt>

12016
</dt> <dt>



The requested operation is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INVALID_OPTION"></span><span id="error_internet_invalid_option"></span>**ERROR\_INTERNET\_INVALID\_OPTION**
</dt> <dd> <dl> <dt>

12009
</dt> <dt>



A request to [**InternetQueryOption**](/windows/desktop/api/Wininet/nf-wininet-internetqueryoptiona) or [**InternetSetOption**](/windows/desktop/api/Wininet/nf-wininet-internetsetoptiona) specified an invalid option value.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INVALID_PROXY_REQUEST"></span><span id="error_internet_invalid_proxy_request"></span>**ERROR\_INTERNET\_INVALID\_PROXY\_REQUEST**
</dt> <dd> <dl> <dt>

12033
</dt> <dt>



The request to the proxy was invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_INVALID_URL"></span><span id="error_internet_invalid_url"></span>**ERROR\_INTERNET\_INVALID\_URL**
</dt> <dd> <dl> <dt>

12005
</dt> <dt>



The URL is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_ITEM_NOT_FOUND"></span><span id="error_internet_item_not_found"></span>**ERROR\_INTERNET\_ITEM\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

12028
</dt> <dt>



The requested item could not be located.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_LOGIN_FAILURE"></span><span id="error_internet_login_failure"></span>**ERROR\_INTERNET\_LOGIN\_FAILURE**
</dt> <dd> <dl> <dt>

12015
</dt> <dt>



The request to connect and log on to an FTP server failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_LOGIN_FAILURE_DISPLAY_ENTITY_BODY"></span><span id="error_internet_login_failure_display_entity_body"></span>**ERROR\_INTERNET\_LOGIN\_FAILURE\_DISPLAY\_ENTITY\_BODY**
</dt> <dd> <dl> <dt>

12174
</dt> <dt>



The MS-Logoff digest header has been returned from the website. This header specifically instructs the digest package to purge credentials for the associated realm. This error will only be returned if [INTERNET\_ERROR\_MASK\_LOGIN\_FAILURE\_DISPLAY\_ENTITY\_BODY](option-flags.md) option has been set; otherwise, **ERROR\_INTERNET\_LOGIN\_FAILURE** is returned.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_MIXED_SECURITY"></span><span id="error_internet_mixed_security"></span>**ERROR\_INTERNET\_MIXED\_SECURITY**
</dt> <dd> <dl> <dt>

12041
</dt> <dt>



The content is not entirely secure. Some of the content being viewed may have come from unsecured servers.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NAME_NOT_RESOLVED"></span><span id="error_internet_name_not_resolved"></span>**ERROR\_INTERNET\_NAME\_NOT\_RESOLVED**
</dt> <dd> <dl> <dt>

12007
</dt> <dt>



The server name could not be resolved.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NEED_MSN_SSPI_PKG"></span><span id="error_internet_need_msn_sspi_pkg"></span>**ERROR\_INTERNET\_NEED\_MSN\_SSPI\_PKG**
</dt> <dd> <dl> <dt>

12173
</dt> <dt>



Not currently implemented.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NEED_UI"></span><span id="error_internet_need_ui"></span>**ERROR\_INTERNET\_NEED\_UI**
</dt> <dd> <dl> <dt>

12034
</dt> <dt>



A user interface or other blocking operation has been requested.

> [!Note]  
> Windows Vista and Windows Server 2008 and earlier only.

 


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NO_CALLBACK"></span><span id="error_internet_no_callback"></span>**ERROR\_INTERNET\_NO\_CALLBACK**
</dt> <dd> <dl> <dt>

12025
</dt> <dt>



An asynchronous request could not be made because a callback function has not been set.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NO_CONTEXT"></span><span id="error_internet_no_context"></span>**ERROR\_INTERNET\_NO\_CONTEXT**
</dt> <dd> <dl> <dt>

12024
</dt> <dt>



An asynchronous request could not be made because a zero context value was supplied.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NO_DIRECT_ACCESS"></span><span id="error_internet_no_direct_access"></span>**ERROR\_INTERNET\_NO\_DIRECT\_ACCESS**
</dt> <dd> <dl> <dt>

12023
</dt> <dt>



Direct network access cannot be made at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NOT_INITIALIZED"></span><span id="error_internet_not_initialized"></span>**ERROR\_INTERNET\_NOT\_INITIALIZED**
</dt> <dd> <dl> <dt>

12172
</dt> <dt>



Initialization of the WinINet API has not occurred. Indicates that a higher-level function, such as [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena), has not been called yet.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_NOT_PROXY_REQUEST"></span><span id="error_internet_not_proxy_request"></span>**ERROR\_INTERNET\_NOT\_PROXY\_REQUEST**
</dt> <dd> <dl> <dt>

12020
</dt> <dt>



The request cannot be made via a proxy.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_OPERATION_CANCELLED"></span><span id="error_internet_operation_cancelled"></span>**ERROR\_INTERNET\_OPERATION\_CANCELLED**
</dt> <dd> <dl> <dt>

12017
</dt> <dt>



The operation was canceled, usually because the handle on which the request was operating was closed before the operation completed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_OPTION_NOT_SETTABLE"></span><span id="error_internet_option_not_settable"></span>**ERROR\_INTERNET\_OPTION\_NOT\_SETTABLE**
</dt> <dd> <dl> <dt>

12011
</dt> <dt>



The requested option cannot be set, only queried.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_OUT_OF_HANDLES"></span><span id="error_internet_out_of_handles"></span>**ERROR\_INTERNET\_OUT\_OF\_HANDLES**
</dt> <dd> <dl> <dt>

12001
</dt> <dt>



No more handles could be generated at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_POST_IS_NON_SECURE"></span><span id="error_internet_post_is_non_secure"></span>**ERROR\_INTERNET\_POST\_IS\_NON\_SECURE**
</dt> <dd> <dl> <dt>

12043
</dt> <dt>



The application is posting data to a server that is not secure.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_PROTOCOL_NOT_FOUND"></span><span id="error_internet_protocol_not_found"></span>**ERROR\_INTERNET\_PROTOCOL\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

12008
</dt> <dt>



The requested protocol could not be located.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_PROXY_SERVER_UNREACHABLE"></span><span id="error_internet_proxy_server_unreachable"></span>**ERROR\_INTERNET\_PROXY\_SERVER\_UNREACHABLE**
</dt> <dd> <dl> <dt>

12165
</dt> <dt>



The designated proxy server cannot be reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_REDIRECT_SCHEME_CHANGE"></span><span id="error_internet_redirect_scheme_change"></span>**ERROR\_INTERNET\_REDIRECT\_SCHEME\_CHANGE**
</dt> <dd> <dl> <dt>

12048
</dt> <dt>



The function could not handle the redirection, because the scheme changed (for example, HTTP to FTP).


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_REGISTRY_VALUE_NOT_FOUND"></span><span id="error_internet_registry_value_not_found"></span>**ERROR\_INTERNET\_REGISTRY\_VALUE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

12021
</dt> <dt>



A required registry value could not be located.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_REQUEST_PENDING"></span><span id="error_internet_request_pending"></span>**ERROR\_INTERNET\_REQUEST\_PENDING**
</dt> <dd> <dl> <dt>

12026
</dt> <dt>



The required operation could not be completed because one or more requests are pending.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_RETRY_DIALOG"></span><span id="error_internet_retry_dialog"></span>**ERROR\_INTERNET\_RETRY\_DIALOG**
</dt> <dd> <dl> <dt>

12050
</dt> <dt>



The dialog box should be retried.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SEC_CERT_CN_INVALID"></span><span id="error_internet_sec_cert_cn_invalid"></span>**ERROR\_INTERNET\_SEC\_CERT\_CN\_INVALID**
</dt> <dd> <dl> <dt>

12038
</dt> <dt>



SSL certificate common name (host name field) is incorrect for example, if you entered `www.server.com` and the common name on the certificate says `www.different.com`.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SEC_CERT_DATE_INVALID"></span><span id="error_internet_sec_cert_date_invalid"></span>**ERROR\_INTERNET\_SEC\_CERT\_DATE\_INVALID**
</dt> <dd> <dl> <dt>

12037
</dt> <dt>



SSL certificate date that was received from the server is bad. The certificate is expired.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SEC_CERT_ERRORS"></span><span id="error_internet_sec_cert_errors"></span>**ERROR\_INTERNET\_SEC\_CERT\_ERRORS**
</dt> <dd> <dl> <dt>

12055
</dt> <dt>



The SSL certificate contains errors.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SEC_CERT_NO_REV"></span><span id="error_internet_sec_cert_no_rev"></span>**ERROR\_INTERNET\_SEC\_CERT\_NO\_REV**
</dt> <dd> <dl> <dt>

12056
</dt> <dt>



The SSL certificate was not revoked.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SEC_CERT_REV_FAILED"></span><span id="error_internet_sec_cert_rev_failed"></span>**ERROR\_INTERNET\_SEC\_CERT\_REV\_FAILED**
</dt> <dd> <dl> <dt>

12057
</dt> <dt>



Revocation of the SSL certificate failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SEC_CERT_REVOKED"></span><span id="error_internet_sec_cert_revoked"></span>**ERROR\_INTERNET\_SEC\_CERT\_REVOKED**
</dt> <dd> <dl> <dt>

12170
</dt> <dt>



The SSL certificate was revoked.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SEC_INVALID_CERT"></span><span id="error_internet_sec_invalid_cert"></span>**ERROR\_INTERNET\_SEC\_INVALID\_CERT**
</dt> <dd> <dl> <dt>

12169
</dt> <dt>



The SSL certificate is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SECURITY_CHANNEL_ERROR"></span><span id="error_internet_security_channel_error"></span>**ERROR\_INTERNET\_SECURITY\_CHANNEL\_ERROR**
</dt> <dd> <dl> <dt>

12157
</dt> <dt>



The application experienced an internal error loading the SSL libraries.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SERVER_UNREACHABLE"></span><span id="error_internet_server_unreachable"></span>**ERROR\_INTERNET\_SERVER\_UNREACHABLE**
</dt> <dd> <dl> <dt>

12164
</dt> <dt>



The website or server indicated is unreachable.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_SHUTDOWN"></span><span id="error_internet_shutdown"></span>**ERROR\_INTERNET\_SHUTDOWN**
</dt> <dd> <dl> <dt>

12012
</dt> <dt>



WinINet support is being shut down or unloaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_TCPIP_NOT_INSTALLED"></span><span id="error_internet_tcpip_not_installed"></span>**ERROR\_INTERNET\_TCPIP\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

12159
</dt> <dt>



The required protocol stack is not loaded and the application cannot start WinSock.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_TIMEOUT"></span><span id="error_internet_timeout"></span>**ERROR\_INTERNET\_TIMEOUT**
</dt> <dd> <dl> <dt>

12002
</dt> <dt>



The request has timed out.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_UNABLE_TO_CACHE_FILE"></span><span id="error_internet_unable_to_cache_file"></span>**ERROR\_INTERNET\_UNABLE\_TO\_CACHE\_FILE**
</dt> <dd> <dl> <dt>

12158
</dt> <dt>



The function was unable to cache the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_UNABLE_TO_DOWNLOAD_SCRIPT"></span><span id="error_internet_unable_to_download_script"></span>**ERROR\_INTERNET\_UNABLE\_TO\_DOWNLOAD\_SCRIPT**
</dt> <dd> <dl> <dt>

12167
</dt> <dt>



The automatic proxy configuration script could not be downloaded. The INTERNET\_FLAG\_MUST\_CACHE\_REQUEST flag was set.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERNET_UNRECOGNIZED_SCHEME"></span><span id="error_internet_unrecognized_scheme"></span>**ERROR\_INTERNET\_UNRECOGNIZED\_SCHEME**
</dt> <dd> <dl> <dt>

12006
</dt> <dt>



The URL scheme could not be recognized, or is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_HANDLE"></span><span id="error_invalid_handle"></span>**ERROR\_INVALID\_HANDLE**
</dt> <dd> <dl> <dt>



The handle that was passed to the API has been either invalidated or closed.

**Header:** Declared in Winerror.h


</dt> </dl> </dd> <dt>

<span id="ERROR_MORE_DATA"></span><span id="error_more_data"></span>**ERROR\_MORE\_DATA**
</dt> <dd> <dl> <dt>



More data is available.

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


</dt> </dl> </dd> </dl>

## Remarks

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wininet.h</dt> </dl> |



 

