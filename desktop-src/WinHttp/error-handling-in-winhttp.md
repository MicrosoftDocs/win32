---
description: Error Handling in WinHTTP
ms.assetid: 96bceda2-ca96-4f88-ab38-35021889c2dd
title: Error Handling in WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling in WinHTTP

Not all WinHTTP API functions report errors in the same way.

Some functions, such as [**WinHttpSetTimeouts**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsettimeouts), return a **BOOL** that indicates failure when **FALSE**. If **FALSE** is returned, callers interested in the error should call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror). If **GetLastError** is called when the function succeded (returned anything but **FALSE**), the returned value is unpredictable and may change between Windows versions, Service Packs, or even between calls to the same function.

Some functions, such as [**WinHttpConnect**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpconnect), return an [HINTERNET](hinternet-handles-in-winhttp.md) pseudo handle. These functions are exactly the same, except failure is indicated by returning **NULL**. If **NULL** is returned, callers interested in the error should call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror). If **GetLastError** is called when the function succeded (returned anything but **NULL**), the returned value is unpredictable and may change between Windows versions, Service Packs, or even between calls to the same function.

Some functions, such as [**WinHttpGetProxyResult**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpgetproxyresult), return a **DWORD** error code and there is no need to call any other functions for more error information. For these functions, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) should not be called. If **GetLastError** is called, regardless of the success or failure of the function, the returned value is unpredictable and may change between Windows versions, Service Packs, or even between calls to the same function.

 

 
