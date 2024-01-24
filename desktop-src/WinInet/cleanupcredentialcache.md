---
title: CleanupCredentialCache function
description: Implemented by certain Security Support Providers (SSP) to flush the SSP credential cache.
ms.assetid: e60870e6-22d3-4321-abca-a5b9d2b0ce2d
keywords:
- CleanupCredentialCache function WinINet
topic_type:
- apiref
api_name:
- CleanupCredentialCache
api_location:
- MSNSSPC.dll
- MSAPSSPC.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# CleanupCredentialCache function

The **CleanupCredentialCache** function is implemented by certain Security Support Providers (SSP) to flush the SSP credential cache.

## Syntax


```C++
BOOL WINAPI CleanupCredentialCache(void);
```



## Parameters

This function has no parameters.

## Return value

**TRUE** if the function succeeds; otherwise, **FALSE**.

## Remarks

The **CleanupCredentialCache** function is implemented by the following SSPs:

-   MSNSSPC.dll
-   MSAPSSPC.dll

The implementation of **CleanupCredentialCache** by these SSPs always returns **TRUE**.

Before attempting to obtain a module handle to export **CleanupCredentialCache**, the application must verify that the SSP that has been loaded is one of the known SSPs implementing the **CleanupCredentialCache** function.

In order to flush the SSP credential cache, the application must obtain a module handle for the SSP by calling the [**GetModuleHandle**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulehandlea) function. After obtaining the module, the application should export the **CleanupCredentialCache** function implemented by the SSP by calling the [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) function, passing the module returned by **GetModuleHandle** and **CleanupCredentialCache** as input parameters.

Like all other aspects of the WinINet API, this function cannot be safely called from within DllMain or the constructors and destructors of global objects.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                                 |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                       |
| DLL<br/>                      | <dl> <dt>MSNSSPC.dll; </dt> <dt>MSAPSSPC.dll</dt> </dl> |



 

