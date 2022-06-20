---
description: Microsoft Windows HTTP Services (WinHTTP) is targeted at middle-tier and back-end server applications that require access to an HTTP client stack.
ms.assetid: 5b0cf321-8f69-4526-a628-e6ca0f9d4a58
title: Porting WinINet Applications to WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# Porting WinINet Applications to WinHTTP

Microsoft Windows HTTP Services (WinHTTP) is targeted at middle-tier and back-end server applications that require access to an HTTP client stack. [Microsoft Windows Internet (WinINet)](winhttp-start-page.md) provides an HTTP client stack for client applications, as well as access to the File Transfer Protocol (FTP), SOCKSv4, and Gopher protocols. This overview can help determine whether porting your WinINet applications to WinHTTP would be beneficial. It also describes specific conversion requirements.

-   [Things to Consider Before Porting Your WinINet Application](#things-to-consider-before-porting-your-wininet-application)
-   [WinHTTP Equivalents to WinINet Functions](#winhttp-equivalents-to-wininet-functions)
-   [Different Handling of Asynchronous Requests](#different-handling-of-asynchronous-requests)
-   [Differences in WinHTTP Callback Notifications](#differences-in-winhttp-callback-notifications)
-   [Authentication Differences](#authentication-differences)
-   [Differences in Secure HTTP Transactions](#differences-in-secure-http-transactions)

## Things to Consider Before Porting Your WinINet Application

Consider porting your WinINet application to WinHTTP if your application would benefit from:

-   A server-safe HTTP client stack.
-   Minimized stack usage.
-   The scalability of a server application.
-   Fewer dependencies on platform-related APIs.
-   Support for thread impersonation.
-   A service-friendly HTTP stack.
-   Access to the scriptable [**WinHttpRequest**](winhttprequest.md) object.

Do not consider porting your WinINet application to WinHTTP if it must support one or more of the following:

-   The FTP or Gopher protocol from the HTTP stack.
-   Support for SOCKSv4 protocol for communicating with SOCKS proxies.
-   Automatic dial-up services.

If you decide to port your application to WinHTTP, the following sections guide you through the conversion process.

For a sample application for both WinINet and WinHTTP, compare the AsyncDemo sample for WinINet with the AsyncDemo sample for WinHTTP.

## WinHTTP Equivalents to WinINet Functions

The following table lists WinINet functions related to the HTTP client stack together with the WinHTTP equivalents.

If your application requires WinINet functions that are not listed, do not port your application to WinHTTP.



| WinINet function                                                       | WinHTTP equivalent                                                                                                                                                                                     | Notable changes                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**HttpAddRequestHeaders**](/windows/desktop/api/wininet/nf-wininet-httpaddrequestheadersa)             | [**WinHttpAddRequestHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpaddrequestheaders)                                                                                                                                           | None.                                                                                                                                                                                                                                                                                                                                |
| [**HttpEndRequest**](/windows/desktop/api/wininet/nf-wininet-httpendrequesta)                           | [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse)                                                                                                                                               | The context value is set with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) or [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption). Request options are set with [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest). [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) must be called after sending a request.                      |
| [**HttpOpenRequest**](/windows/desktop/api/wininet/nf-wininet-httpopenrequesta)                         | [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest)                                                                                                                                                       | The context value is set with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) or [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption).                                                                                                                                                                                                      |
| [**HttpQueryInfo**](/windows/desktop/api/wininet/nf-wininet-httpqueryinfoa)                             | [**WinHttpQueryHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryheaders)                                                                                                                                                     | None.                                                                                                                                                                                                                                                                                                                                |
| [**HttpSendRequest**](/windows/desktop/api/wininet/nf-wininet-httpsendrequesta)                         | [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest)                                                                                                                                                       | The context value can be set with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest).                                                                                                                                                                                                                                                  |
| [**HttpSendRequestEx**](/windows/desktop/api/wininet/nf-wininet-httpsendrequestexa)                     | [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest)                                                                                                                                                       | Buffers cannot be provided.                                                                                                                                                                                                                                                                                                          |
| [**InternetCanonicalizeUrl**](/windows/desktop/api/wininet/nf-wininet-internetcanonicalizeurla)         | No equivalent                                                                                                                                                                                          | URLs are now put in canonical form in [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest).                                                                                                                                                                                                                                              |
| [**InternetCheckConnection**](/windows/desktop/api/wininet/nf-wininet-internetcheckconnectiona)         | No equivalent                                                                                                                                                                                          | Not implemented in WinHTTP.                                                                                                                                                                                                                                                                                                          |
| [**InternetCloseHandle**](/windows/desktop/api/wininet/nf-wininet-internetclosehandle)                 | [**WinHttpCloseHandle**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpclosehandle)                                                                                                                                                       | Closing a parent handle in WinHTTP does not recursively close child handles.                                                                                                                                                                                                                                                         |
| [**InternetCombineUrl**](/windows/desktop/api/wininet/nf-wininet-internetcombineurla)                   | No equivalent                                                                                                                                                                                          | URLs can be assembled with the [**WinHttpCreateUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcreateurl) function.                                                                                                                                                                                                                                                |
| [**InternetConfirmZoneCrossing**](/windows/desktop/api/wininet/nf-wininet-internetconfirmzonecrossing) | No equivalent                                                                                                                                                                                          | Not implemented in WinHTTP.                                                                                                                                                                                                                                                                                                          |
| [**InternetConnect**](/windows/desktop/api/wininet/nf-wininet-internetconnecta)                         | [**WinHttpConnect**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpconnect)                                                                                                                                                               | The context value is set with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) or [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption). Request options are set with [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest). User credentials are set with [**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials).                                 |
| [**InternetCrackUrl**](/windows/desktop/api/wininet/nf-wininet-internetcrackurla)                       | [**WinHttpCrackUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcrackurl)                                                                                                                                                             | Opposite behavior of the ICU\_ESCAPE flag: with [**InternetCrackUrl**](/windows/desktop/api/wininet/nf-wininet-internetcrackurla), this flag causes escape sequences (%xx) to be converted to characters, but with [**WinHttpCrackUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcrackurl), it causes characters that must be escaped from in an HTTP request to be converted to escape sequences. |
| [**InternetCreateUrl**](/windows/desktop/api/wininet/nf-wininet-internetcreateurla)                     | [**WinHttpCreateUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpcreateurl)                                                                                                                                                           | None.                                                                                                                                                                                                                                                                                                                                |
| [**InternetErrorDlg**](/windows/desktop/api/wininet/nf-wininet-interneterrordlg)                       | No equivalent                                                                                                                                                                                          | Because WinHTTP is targeted at server-side applications, it does not implement any user interface.                                                                                                                                                                                                                                   |
| [**InternetGetCookie**](/windows/desktop/api/wininet/nf-wininet-internetgetcookiea)                     | No equivalent                                                                                                                                                                                          | WinHTTP does not persist data between sessions and cannot access WinINet cookies.                                                                                                                                                                                                                                                    |
| [**InternetOpen**](/windows/desktop/api/wininet/nf-wininet-internetopena)                               | [**WinHttpOpen**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopen)                                                                                                                                                                     | None.                                                                                                                                                                                                                                                                                                                                |
| [**InternetOpenUrl**](/windows/desktop/api/wininet/nf-wininet-internetopenurla)                         | [**WinHttpConnect**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpconnect), [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest), [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest), [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) | This functionality is available in the WinHTTP functions listed.                                                                                                                                                                                                                                                                     |
| [**InternetQueryDataAvailable**](/windows/desktop/api/wininet/nf-wininet-internetquerydataavailable)   | [**WinHttpQueryDataAvailable**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpquerydataavailable)                                                                                                                                         | No reserved parameters.                                                                                                                                                                                                                                                                                                              |
| [**InternetQueryOption**](/windows/desktop/api/wininet/nf-wininet-internetqueryoptiona)                 | [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption)                                                                                                                                                       | WinHTTP offers a different set of options from WinINet. For more information and options offered by WinHTTP, see [**Option flags**](option-flags.md).                                                                                                                                                                               |
| [**InternetReadFile**](/windows/desktop/api/wininet/nf-wininet-internetreadfile)                       | [**WinHttpReadData**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreaddata)                                                                                                                                                             | None.                                                                                                                                                                                                                                                                                                                                |
| [**InternetReadFileEx**](/windows/desktop/api/wininet/nf-wininet-internetreadfileexa)                   | [**WinHttpReadData**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreaddata)                                                                                                                                                             | Rather than a structure, the buffer is a region of memory addressed with a pointer.                                                                                                                                                                                                                                                  |
| [**InternetSetOption**](/windows/desktop/api/wininet/nf-wininet-internetsetoptiona)                     | [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption)                                                                                                                                                           | None.                                                                                                                                                                                                                                                                                                                                |
| [**InternetSetStatusCallback**](/windows/desktop/api/wininet/nf-wininet-internetsetstatuscallback)     | [**WinHttpSetStatusCallback**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetstatuscallback)                                                                                                                                           | For more information, see "Different Handling of Asynchronous Requests" in this topic.                                                                                                                                                                                                                                               |
| [**InternetTimeFromSystemTime**](/windows/desktop/api/wininet/nf-wininet-internettimefromsystemtime)   | [**WinHttpTimeFromSystemTime**](/windows/desktop/api/Winhttp/nf-winhttp-winhttptimefromsystemtime)                                                                                                                                         | None.                                                                                                                                                                                                                                                                                                                                |
| [**InternetTimeToSystemTime**](/windows/desktop/api/wininet/nf-wininet-internettimetosystemtime)       | [**WinHttpTimeToSystemTime**](/windows/desktop/api/Winhttp/nf-winhttp-winhttptimetosystemtime)                                                                                                                                             | None.                                                                                                                                                                                                                                                                                                                                |
| [**InternetWriteFile**](/windows/desktop/api/wininet/nf-wininet-internetwritefile)                     | [**WinHttpWriteData**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpwritedata)                                                                                                                                                           | None.                                                                                                                                                                                                                                                                                                                                |



 

## Different Handling of Asynchronous Requests

Be aware that in WinINet and WinHTTP, some functions can complete asynchronous requests either synchronously or asynchronously. Your application must handle either situation. There are significant differences in how WinINet and WinHTTP handle these potentially asynchronous functions.

WinINet

-   Synchronous completion: If a potentially asynchronous WinINet function call completes synchronously, the OUT parameters of the function return the results of the operation. When an error occurs, retrieve the error code by calling [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) after the WinINet function call.

-   Asynchronous completion: If a potentially asynchronous function call completes asynchronously, the results of the operation, and any errors, are accessible in the callback function. The callback function is executed on a worker thread, not on the thread that made the initial function call.

In other words, your application must duplicate logic to handle the results of such operations in two places: both immediately after the function call and in the callback function.

WinHTTP simplifies this model by enabling you to implement the operational logic only in the callback function, which receives a completion notification regardless of whether the operation completed synchronously or asynchronously. When asynchronous operation is enabled, the OUT parameters of WinHTTP functions do not return meaningful data and must be set to **NULL**.

The only significant difference between asynchronous and synchronous completion in WinHTTP, from the application perspective, is in where the callback function is executed.

WinHTTP

-   Synchronous completion: When an operation completes synchronously, the results are returned in a callback function that executes in the same thread as the original function call.

-   Asynchronous completion: When an operation completes asynchronously, the results are returned in a callback function that executes in a worker thread.

Although most errors can also be handled entirely within the callback function, WinHTTP applications must still be prepared for a function to return **FALSE** because of an ERROR\_INVALID\_PARAMETER or other similar error retrieved by calling [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

Unlike WinINet, which can execute multiple asynchronous operations simultaneously, WinHTTP enforces a policy of one pending asynchronous operation per request handle. If one operation is pending and another WinHTTP function is called, the second function fails and [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INVALID\_OPERATION.

WinHTTP simplifies this model by enabling you to implement the operational logic only in the callback function, which receives a completion notification regardless of whether the operation completed synchronously or asynchronously. When asynchronous operation is enabled, the OUT parameters of WinHTTP functions do not return meaningful data and must be set to **NULL**.

## Differences in WinHTTP Callback Notifications

The status callback function receives updates on the status of operations through notification flags. In WinHTTP, notifications are selected using the *dwNotificationFlags* parameter of the [**WinHttpSetStatusCallback**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetstatuscallback) function. Use the **WINHTTP\_CALLBACK\_FLAG\_ALL\_NOTIFICATIONS** flag to be notified of all status updates.

Notifications that indicate a particular operation is complete are called completion notifications, or just completions. In WinINet, each time the callback function receives a completion, the *lpvStatusInformation* parameter contains an [**INTERNET\_ASYNC\_RESULT**](/windows/desktop/api/wininet/ns-wininet-internet_async_result) structure. In WinHTTP, this structure is not available for all completions. It is important to review the reference page for [**WINHTTP\_STATUS\_CALLBACK**](/windows/win32/api/winhttp/nc-winhttp-winhttp_status_callback), which contains information about notifications and what type of data can be expected for each.

In WinHTTP, a single completion, **WINHTTP\_CALLBACK\_STATUS\_REQUEST\_ERROR**, indicates that an operation failed. All other completions indicate a successful operation.

Both WinINet and WinHTTP use a user-defined context value to pass information from the main thread to the status callback function, which can be executed on a worker thread. In WinINet, the context value used by the status callback function is set by calling one of several functions. In WinHTTP, the context value is set only with [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) or [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption). Because of this, it is possible in WinHTTP for a notification to occur before a context value is set. If the callback function receives a notification before the context value is set, the application must be prepared to receive **NULL** in the *dwContext* parameter of the callback function.

## Authentication Differences

In WinINet, user credentials are set by calling the [**InternetSetOption**](/windows/desktop/api/wininet/nf-wininet-internetsetoptiona) function, using code similar to that provided in the following code example.

``` syntax
// Use the WinINet InternetSetOption function to set the 
// user credentials to the user name contained in strUsername 
// and the password to the contents of strPassword.
       
InternetSetOption( hRequest, INTERNET_OPTION_PROXY_USERNAME, 
                   strUsername, strlen(strUsername) + 1 );

InternetSetOption( hRequest, INTERNET_OPTION_PROXY_PASSWORD, 
                   strPassword, strlen(strPassword) + 1 );
```

For compatibility, user credentials can similarly be set in WinHTTP using the [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) function, but this is not recommended because it can pose a security vulnerability.

Instead, when an application receives a 401 status code in WinHTTP, the recommended method of setting credentials is first to identify an authentication scheme using [**WinHttpQueryAuthSchemes**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryauthschemes) and, second, set the credentials using [**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials). The following code example shows how to do this.

``` syntax
DWORD dwSupportedSchemes;
DWORD dwPrefered;
DWORD dwTarget;

// Obtain the supported and first schemes.
WinHttpQueryAuthSchemes( hRequest, &dwSupportedSchemes, &dwPrefered, &dwTarget );

// Set the credentials before resending the request.
WinHttpSetCredentials( hRequest, dwTarget, dwPrefered, strUsername, strPassword, NULL );
```

Because there is no equivalent to [**InternetErrorDlg**](/windows/desktop/api/wininet/nf-wininet-interneterrordlg) in WinHTTP, applications that obtain credentials through a user interface must provide their own interface.

Unlike WinINet, WinHTTP does not cache passwords. Valid user credentials must be supplied for each request.

WinHTTP does not support the Distributed Password Authentication (DPA) scheme supported by WinINet. WinHTTP does, however, support Microsoft Passport 1.4. For more information about using Passport authentication in WinHTTP, see [Passport Authentication in WinHTTP](passport-authentication-in-winhttp.md).

WinHTTP does not rely on Internet Explorer settings to determine the automatic logon policy. Instead, the auto-logon policy is set with [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption). For more information about authentication in WinHTTP, including the auto-logon policy, see [Authentication in WinHTTP](authentication-in-winhttp.md).

## Differences in Secure HTTP Transactions

In WinINet, initiate a secure session using either [**HttpOpenRequest**](/windows/desktop/api/wininet/nf-wininet-httpopenrequesta) or [**InternetConnect**](/windows/desktop/api/wininet/nf-wininet-internetconnecta), but in WinHTTP, you must call [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest) using the **WINHTTP\_FLAG\_SECURE** flag.

In a secure HTTP transaction, server certificates can be used to authenticate a server to the client. In WinINet, if a server certificate contains errors, [**HttpSendRequest**](/windows/desktop/api/wininet/nf-wininet-httpsendrequesta) fails and provides details about the certificate errors.

In WinHttp, server certificate errors are handled according to the version as follows:

-   Starting with WinHttp 5.1, if a server certificate fails or contains errors, the call to [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) reports a **WINHTTP\_CALLBACK\_STATUS\_SECURE\_FAILURE** in the callback function. If the error generated by **WinHttpSendRequest** is ignored, subsequent calls to [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) fail with an ERROR\_WINHTTP\_OPERATION\_CANCELLED error.
-   In WinHTTP 5.0, errors in server certificates do not, by default, cause a request to fail. Instead, the errors are reported in the callback function with the **WINHTTP\_CALLBACK\_STATUS\_SECURE\_FAILURE** notification.

On some earlier platforms, WinINet supported the Private Communication Technology (PCT) and/or Fortezza protocols, although not on Windows XP.

WinHTTP does not support the PCT and Fortezza protocols on any platform, and instead relies on Secure Sockets Layer (SSL) 2.0, SSL 3.0, or Transport Layer Security (TLS) 1.0.

 

 
