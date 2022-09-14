---
description: This topic describes the most important differences between WinHTTP version 5.1 and version 5.0.
ms.assetid: df3fcf27-3012-4818-b29c-b8a4dc409828
title: Whats New in WinHTTP 5.1
ms.topic: article
ms.date: 05/31/2018
---

# What's New in WinHTTP 5.1

This topic describes the most important differences between WinHTTP version 5.1 and version 5.0. Many of these differences require code changes in applications migrating from version 5.0 to version 5.1. Some of the features in version 5.1 are only available starting with Windows Server 2003 and Windows XP with Service Pack 2 (SP2), particularly features related to improving the security of the client against malicious Web servers.

> [!IMPORTANT]
> With the release of WinHTTP Version 5.1, the WinHTTP 5.0 download is no longer available. As of October 1, 2004, Microsoft has removed the WinHTTP 5.0 SDK download from MSDN and has terminated product support for version 5.0.

 

## DLL Name Change

The name of the new WinHTTP 5.1 DLL is Winhttp.dll, whereas the name of the WinHTTP 5.0 DLL is Winhttp5.dll.

WinHTTP 5.0 and 5.1 can coexist on the same system; WinHTTP 5.1 does not replace, or install over, WinHTTP 5.0.

## Redistribution

WinHTTP 5.1 is available only with Windows Server 2003, Windows 2000 Professional with Service Pack 3 (SP3), Windows XP with Service Pack 1 (SP1), and later operating systems. A redistributable merge module (.msm) file is not available for WinHTTP 5.1.

## WinHttpRequest ProgID

The ProgID of the WinHttpRequest component has changed from "WinHttp.WinHttpRequest.5" to "WinHttp.WinHttpRequest.5.1". The CLSID of the [**WinHttpRequest**](winhttprequest.md) class has also changed.

## Async Callback Behavior Change

When calling the [**WinHttpWriteData**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpwritedata), [**WinHttpQueryDataAvailable**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpquerydataavailable) and [**WinHttpReadData**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreaddata) functions in asynchronous mode, do not rely on the respective *lpdwNumberOfBytesWritten*, *lpdwNumberOfBytesAvailable*, and *lpdwNumberOfBytesRead* OUT parameters to be set. If the function call completes asynchronously, WinHTTP does not write to these pointers supplied by the application code. Instead, the application should retrieve these values using *lpvStatusInformation* and *dwStatusInformationLength* parameters to the callback function.

## Changes to Default Settings

Changes to default settings include:

-   SSL server certificate verification is enabled by default in WinHTTP 5.1. WinHTTP 5.0 does not handle failures encountered when validating the server certificate as fatal errors; they are reported to the application using a **SECURE\_FAILURE** callback notification, but does not cause the request to be aborted. WinHTTP 5.1, alternatively, handles server certificate validation failures as fatal errors that abort the request. The application can instruct WinHTTP to ignore a small subset of certificate errors such as unknown CA, invalid/expired certificate date, or invalid certificate subject name, using the **WINHTTP\_OPTION\_SECURITY\_FLAGS** option.
-   Passport authentication support is disabled by default in WinHTTP 5.1. Passport support can be enabled with the **WINHTTP\_OPTION\_CONFIGURE\_PASSPORT\_AUTH** option. Automatic Passport credential look-up in the Keyring is also disabled by default.
-   Redirect behavior change: HTTP redirects from a secure **https:** URL to a regular **http:** URL are no longer followed automatically by default for security reasons. There is a new option, **WINHTTP\_OPTION\_REDIRECT\_POLICY**, to override the default redirect behavior in WinHTTP 5.1. With the **WinHttpRequest** COM component, use the new **WinHttpRequestOption\_EnableHttpsToHttpRedirects** option to enable redirects from https: to http: URLs.
-   When a WinHTTP trace file is created, access is restricted with an ACL such that only administrators can read or write the file. The user account under which the tracefile was created can also modify the ACL to grant others access. This protection is available only on file systems which support security; that is, NTFS, not FAT32).
-   Starting with Windows Server 2003 and Windows XP with SP2, sending requests to the following well-known, non-HTTP, ports is restricted for security reasons: 21 (FTP), 25 (SMTP), 70 (GOPHER), 110 (POP3), 119 (NNTP), 143 (IMAP).
-   Starting with Windows Server 2003, and Windows XP with SP2, the maximum amount of header data WinHTTP accepts in an HTTP response is 64K, by default. If the server HTTP response contains more that 64K of total header data, WinHTTP fails the request with an **ERROR\_WINHTTP\_INVALID\_SERVER\_RESPONSE** error. This 64K limit can be overridden using the new **WINHTTP\_OPTION\_MAX\_RESPONSE\_HEADER\_SIZE** option.

## IPv6 Support

WinHTTP 5.1 adds support for Internet Protocol Version 6 (IPv6). WinHTTP can send HTTP requests to a server whose DNS name resolves into an IPv6 address, and starting with Windows Server 2003 and Windows XP with SP2, WinHTTP also supports IPv6 literal addresses.

## New Options in the C/C++ API for WinHTTP

WinHTTP 5.1 implements the following new options:

<dl> "\#define WINHTTP\_OPTION\_PASSPORT\_SIGN\_OUT 86"  
"\#define WINHTTP\_OPTION\_PASSPORT\_RETURN\_URL 87"  
"\#define WINHTTP\_OPTION\_REDIRECT\_POLICY 88"  
</dl>

Starting with Windows Server 2003 and Windows XP with SP2, WinHTTP 5.1 implements the following new options. On Windows 2000 Professional with SP3 or Windows XP with SP1, however, calls to [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) or [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) with these option IDs fail:

<dl> "\#define WINHTTP\_OPTION\_RECEIVE\_RESPONSE\_TIMEOUT 7"  
"\#define WINHTTP\_OPTION\_MAX\_HTTP\_AUTOMATIC\_REDIRECTS 89"  
"\#define WINHTTP\_OPTION\_MAX\_HTTP\_STATUS\_CONTINUE 90"  
"\#define WINHTTP\_OPTION\_MAX\_RESPONSE\_HEADER\_SIZE 91"  
"\#define WINHTTP\_OPTION\_MAX\_RESPONSE\_DRAIN\_SIZE 92"  
</dl>

## New Options in the WinHttpRequest 5.1 Component

The WinHttpRequest 5.1 component implements the following new options:

<dl> "WinHttpRequestOption\_RevertImpersonationOverSsl"  
"WinHttpRequestOption\_EnableHttpsToHttpRedirects"  
"WinHttpRequestOption\_EnablePassportAuthentication"  
</dl>

The following new WinHttpRequest 5.1 options are available starting with Windows Server 2003 and Windows XP with SP2:

<dl> "WinHttpRequestOption\_MaxAutomaticRedirects"  
"WinHttpRequestOption\_MaxResponseHeaderSize"  
"WinHttpRequestOption\_MaxResponseDrainSize"  
"WinHttpRequestOptions\_EnableHttp1\_1"  
</dl>

## Proxies Are Not Trusted When Auto-Logon Security is Set to High

In WinHTTP 5.0, proxy servers are always trusted for auto-logon. This is no longer valid for WinHTTP 5.1 running on Windows Server 2003 and Windows XP with SP2 when the **WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_HIGH** policy option is set.

## Web Proxy Auto-Discovery (AutoProxy) API

To ease the configuration of proxy settings for WinHTTP-based applications, WinHTTP now implements the Web Proxy Auto-Discovery (WPAD) protocol, also referred to as *autoproxy*. This is the same protocol that web browsers, such as Internet Explorer, implement to discover the proxy configuration automatically without requiring an end-user to specify a proxy server manually. To support autoproxy, WinHTTP 5.1 implements a new C/C++ function, [**WinHttpGetProxyForUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyforurl), plus two supporting functions, [**WinHttpDetectAutoProxyConfigUrl**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpdetectautoproxyconfigurl) and [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser).

## Known Issues

The following issues are known to exist in WinHTTP 5.1 on Windows 2000 Professional with SP3 and Windows XP with SP1. These issues are resolved for WinHTTP starting with Windows Server 2003 and Windows XP with SP2:

-   If the application uses the [**WinHttpSetTimeouts**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsettimeouts) function or the [**SetTimeouts**](iwinhttprequest-settimeouts.md) method on the [**WinHttpRequest**](iwinhttprequest-interface.md) component to set a non-infinite DNS resolve timeout such as the *dwResolveTimeout* parameter, a thread handle leak occurs each time WinHTTP resolves a DNS name. Over a large number of HTTP requests, this causes a significant memory leak. The workaround is to leave the default infinite resolve timeout setting unchanged (a value of 0 specifies an infinite timeout). This is strongly recommended in any case as supporting timeouts on DNS name resolutions in WinHTTP is expensive in terms of performance. For Windows 2000 and later, setting a DNS resolve timeout in WinHTTP is unnecessary as the underlying DNS client service implements its own resolve timeout.
-   When processing asynchronous requests, WinHTTP does not handle thread impersonation properly. This causes requests that require NTLM/Negotiate authentication to fail, unless credentials are explicitly given using the [**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials) or [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) functions.

 

 



