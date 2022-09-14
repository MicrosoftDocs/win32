---
description: Starting in Windows Server 2008 and Windows Vista, the WinHTTP API has been enhanced to include the following features.
ms.assetid: b47a2e38-67bd-4d43-936c-8781641cb7f6
title: Whats New in Windows Server 2008 and Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows Server 2008 and Windows Vista

Starting in Windows Server 2008 and Windows Vista, the WinHTTP API has been enhanced to include the following features.

## Greater Than 4-GB Upload.

[**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) can send only 4 GB of data because of limitations in the size of the DWORD total length parameter. To enable applications to send more than 4 GB of data, the Content-Length header is added to the request specifying data as large as a LARGE\_INTEGER (2^64 bytes). For more information, see **WinHttpSendRequest**. This feature is not supported on the [**IWinHttpRequest**](iwinhttprequest-interface.md) COM object.

## Transfer-Encoding Header

The Transfer-Encoding header enables applications to send chunked data to the server. When the Transfer-Encoding header is present on the request, the application sends the request with a zero length entity body in the call to [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest). The entity body is sent in subsequent calls to [**WinHttpWriteData**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpwritedata). This feature is not supported on the [**IWinHttpRequest**](iwinhttprequest-interface.md) COM object.

## SSL Client Certificate Issuer List Retrieval

The application can retrieve the SSL client certificate Issuer List when [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) fails with an **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**. A new option, **WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST**, allows applications to retrieve the certificate Issuer List and filter the list for the optimal certificate. For more information, see the [**Option flags**](option-flags.md) and [Issuer List Retrieval for SSL Client Authentication](ssl-in-winhttp.md) topics. This feature is not supported on the [**IWinHttpRequest**](iwinhttprequest-interface.md) COM object.

## Optional Client Certificates

When [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) fails with an **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**, the server may not require the SSL client certificate. The server may be able to revert to another form of authentication, or allow the client to proceed with anonymous access. The application sets the **WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT** option and specifies a macro that WinHttp uses to determine if the client certificate is required. For more information, see [**Option flags**](option-flags.md). This feature is not supported on the [**IWinHttpRequest**](iwinhttprequest-interface.md) COM object.

## Source and Destination IP Addresses

When [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) completes, the application can retrieve the source and destination IP address and port of the request that generated the response. A new structure is provided to receive the source and destination addresses when the **WINHTTP\_OPTION\_CONNECTION\_INFO** option is set. For more information, see [**Option flags**](option-flags.md). This feature is not supported on the [**IWinHttpRequest**](iwinhttprequest-interface.md) COM object.

## Additional SSL Client Authentication Errors

Additional SSL client authentication errors provide more information about the SSL Client certificate. **ERROR\_WINHTTP\_CLIENT\_CERT\_NO\_PRIVATE\_KEY** and **ERROR\_WINHTTP\_CERT\_NO\_ACCESS\_PRIVATE\_KEY** client certificate errors are new for Windows Server 2008 and Windows Vista. The [**IWinHttpRequest**](iwinhttprequest-interface.md) COM object returns these errors in an HRESULT.

 

 



