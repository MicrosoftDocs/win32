---
Description: The Windows Networking functions return WN\_SUCCESS on success, or they return a unique nonzero value if the function encounters an error. In addition, they return extended error information using WNetSetLastError and SetLastError.
ms.assetid: cb9d29a1-b3a5-4440-a069-3cd1565b1699
title: Returning Values to the MPR
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Returning Values to the MPR

The Windows Networking functions return WN\_SUCCESS on success, or they return a unique nonzero value if the function encounters an error. In addition, they return extended error information using [**WNetSetLastError**](/windows/win32/Npapi/nf-npapi-wnetsetlasterrora?branch=master) and [**SetLastError**](base.setlasterror).

To support the above behavior, network provider functions should not call [**SetLastError**](base.setlasterror) before returning. This is because the MPR calls **SetLastError** for the functions in the Network Provider API after they return. If the network providers call **SetLastError** directly, they will be making redundant function calls. Network provider functions should simply return an error code. The error codes are specified in the function description or [Return Values](network-security-return-values.md). Also, network provider functions may return any [System Error Codes](base.system_error_codes), such as insufficient memory. The only exception is [**NPGetCaps**](/windows/win32/Npapi/nf-npapi-npgetcaps?branch=master), which should return a mask indicating the functions supported by the network provider.

If a network provider function needs to return extended error information, it should call [**WNetSetLastError**](/windows/win32/Npapi/nf-npapi-wnetsetlasterrora?branch=master). This function is provided by the Windows operating system for use by network providers. When the provider calls **WNetSetLastError**, it can set a string containing additional information about the error. This information is stored on a per-thread basis. This is analogous to [**SetLastError**](base.setlasterror) for Windows applications. The Windows operating system calls **WNetSetLastError** to check for a string stored using **WNetSetLastError** and, if found, returns the extended error information to the calling application that initiated the network request.

> [!Note]  
> The WNet prefix of [**WNetSetLastError**](/windows/win32/Npapi/nf-npapi-wnetsetlasterrora?branch=master) is misleading since this API, unlike **WNetSetLastError**, is not part of the Windows Networking API set. **WNetSetLastError** is intended for use only by network providers. The name, **WNetSetLastError**, is retained for compatibility with existing providers.

 

 

 



