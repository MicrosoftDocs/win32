---
title: TLSConnectToLsServer function
description: Opens a handle to the specified Remote Desktop license server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9e90a8e8-9319-42ee-b541-a1d028b6ed4d
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- TLSConnectToLsServer function Remote Desktop Services
topic_type:
- apiref
api_name:
- TLSConnectToLsServer
api_location:
- Mstlsapi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TLSConnectToLsServer function

Opens a handle to the specified Remote Desktop license server.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to Mstlsapi.dll.

 

## Syntax


```C++
TLS_HANDLE WINAPI TLSConnectToLsServer(
  _In_ LPTSTR pszLsServer
);
```



## Parameters

<dl> <dt>

*pszLsServer* \[in\]
</dt> <dd>

Pointer to a **null**-terminated string that specifies the NetBIOS name of the Remote Desktop license server. If the value of this parameter is **NULL**, the specified server is the local computer.

</dd> </dl>

## Return value

If the function succeeds, the return value is a handle to the specified server.

If the function fails, the return value is **NULL**. To get extended error information, call the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

## Remarks

When you have finished using the handle that is returned by the **TLSConnectToLsServer** function, release it by calling the [**TLSDisconnectFromServer**](tlsdisconnectfromserver.md) function.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Mstlsapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**TLS\_HANDLE**](tls-handle.md)
</dt> <dt>

[**TLSDisconnectFromServer**](tlsdisconnectfromserver.md)
</dt> </dl>

 

 





