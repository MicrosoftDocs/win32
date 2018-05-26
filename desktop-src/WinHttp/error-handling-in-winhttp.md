---
Description: Error Handling in WinHTTP
ms.assetid: 96bceda2-ca96-4f88-ab38-35021889c2dd
title: Error Handling in WinHTTP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Error Handling in WinHTTP

Not all WinHTTP API functions report errors in the same way.

Some functions, such as [**WinHttpSetTimeouts**](/windows/win32/Winhttp/nf-winhttp-winhttpsettimeouts?branch=master), return a **BOOL** that indicates failure when **FALSE**. If **FALSE** is returned, callers interested in the error should call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360). If **GetLastError** is called when the function succeded (returned anything but **FALSE**), the returned value is unpredictable and may change between Windows versions, Service Packs, or even between calls to the same function.

Some functions, such as [**WinHttpConnect**](/windows/win32/Winhttp/nf-winhttp-winhttpconnect?branch=master), return an [HINTERNET](hinternet-handles-in-winhttp.md) pseudo handle. These functions are exactly the same, except failure is indicated by returning **NULL**. If **NULL** is returned, callers interested in the error should call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360). If **GetLastError** is called when the function succeded (returned anything but **NULL**), the returned value is unpredictable and may change between Windows versions, Service Packs, or even between calls to the same function.

Some functions, such as [**WinHttpGetProxyResult**](/windows/win32/Winhttp/nf-winhttp-winhttpgetproxyresult?branch=master), return a **DWORD** error code and there is no need to call any other functions for more error information. For these functions, [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) should not be called. If **GetLastError** is called, regardless of the success or failure of the function, the returned value is unpredictable and may change between Windows versions, Service Packs, or even between calls to the same function.

 

 



