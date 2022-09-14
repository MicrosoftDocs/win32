---
title: Using String Buffers
description: Functions that return strings contain an input parameter, lpszBuffer, and a size parameter, lpdwBufferLength. Although lpszBuffer can be NULL, lpdwBufferLength must be a valid pointer to a DWORD variable.
ms.assetid: ae7f84ba-15d4-483b-bdda-0042854f9e1b
ms.topic: article
ms.date: 05/31/2018
---

# Using String Buffers

Functions that return strings contain an input parameter, *lpszBuffer*, and a size parameter, *lpdwBufferLength*. Although *lpszBuffer* can be **NULL**, *lpdwBufferLength* must be a valid pointer to a **DWORD** variable. If the input buffer pointed to by *lpszBuffer* is **NULL** or too small to hold the output string, the function fails and [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **ERROR\_INSUFFICIENT\_BUFFER**. The variable pointed to by *lpdwBufferLength* contains a number that represents the number of bytes the function requires to return the requested string, including the **null** terminator. The application should allocate a buffer of this size, set the variable pointed to by *lpdwBufferLength* to this value, and resubmit the request. If the buffer size is sufficient to receive the requested string, the string is copied to the output buffer with a **null** terminator and the function returns a success indication. The variable pointed to by *lpdwBufferLength* now contains the number of characters stored in the buffer, excluding the **null** terminator.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

 