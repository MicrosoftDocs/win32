---
title: Content Encoding
description: Starting in Windows Server 2008 and Windows Vista, the application can direct WinINet to perform content decoding for the gzip and deflate content encoding schemes.
ms.assetid: 136f22a6-e5ca-41c5-8651-6e132655d268
keywords:
- Content Encoding
ms.topic: article
ms.date: 05/31/2018
---

# Content Encoding

As specified in the HTTP protocol (RFC 2616) applications can request that the server return HTTP responses in encoded format. Prior to Windows Server 2008 and Windows Vista, requests with content encoding were sent to the application for processing at their level. Starting in Windows Server 2008 and Windows Vista, the application can direct WinINet to perform content decoding for the gzip and deflate content encoding schemes.

To enable content decoding, the application sets the decoding option requesting that WinINet perform decoding on their behalf. However, enabling decoding does not guarantee that WinINet will perform content decoding, and the application should be prepared to handle decoding. WinINet strips the content-encoding header from the response when content decoding is successfully performed. Applications are expected to handle content decoding regardless of whether the decoding option is enabled or disabled when the content-encoding header is present in the response.

When decoding is enabled, the application must specify the list of supported encodings in the Accept-Encoding header of the request. The Accept-Encoding header, however, does not obligate the server to send an encoded response. WinINet will send responses that do not match the list of acceptable encodings back to the application.

The following list describes the conditions under which WinINet will perform content decoding when the option is enabled:

-   The Accept-Encoding header must be present in the request, and it must specify the gzip, deflate, or both gzip and deflate encoding schemes.
-   The encoding scheme specified in the Content-Encoding header must match one of the encoding schemes specified in the Accept-Encoding header.
-   The Content-Encoding header in the response specifies only one encoding scheme.
-   The response must contain only one Content- Encoding header. WinINet decodes content that is encoded with only one encoding scheme.
-   The Cache-Control header must not contain the no-transform directive.
-   The Content-Range header must not be present in the response.

## Setting the Decompression Option

The decoding option can be set on the session handle, the request handle or the connection handle. The handle on which the decoding option is set, defines the scope of the decoding option. For example, setting decoding on the session will enable decoding an all connections and requests created under that handle.

To set the decoding option, the application calls [**InternetSetOption**](/windows/desktop/api/Wininet/nf-wininet-internetsetoptiona) with the handle returned from [**InternetOpen**](/windows/desktop/api/Wininet/nf-wininet-internetopena), [**InternetConnect**](/windows/desktop/api/Wininet/nf-wininet-internetconnecta), or [**HttpOpenRequest**](/windows/desktop/api/Wininet/nf-wininet-httpopenrequesta). The **INTERNET\_OPTION\_HTTP\_DECODING** option is specified in the *dwOption* parameter, and the *lpBuffer* parameter points to a boolean variable set to true. To disable decoding, the application calls **InternetSetOption** with the **INTERNET\_OPTION\_HTTP\_DECODING** option and the boolean variable set to false.

When the decoding option is set, WinINet performs decoding on the request when the application calls [**InternetReadFile**](/windows/desktop/api/Wininet/nf-wininet-internetreadfile). If WinINet encounters an error while performing content decoding, the call to **InternetReadFile** fails with an **ERROR\_INTERNET\_DECODING\_FAILED**. When decoding fails, the application has two options: it can remove the Accept-Encoding header and resend the request, or it can set the **INTERNET\_OPTION\_HTTP\_DECODING** option on the request to false and then resend the request. If the decoding option is set to false, the application must check the Content-Encoding header and perform any decoding at the application level.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

 