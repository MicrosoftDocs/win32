---
title: IpcCloseHandle function
description: Closes a handle.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 85b46fcc-b69a-4800-89f6-904e6bcee42c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcCloseHandle function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcCloseHandle
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcCloseHandle function

Closes a handle to an Rights Management Services SDK 2.1 object and frees any resources associated with it.

## Syntax


```C++
HRESULT WINAPI IpcCloseHandle(
  _In_ IPC_HANDLE handle
);
```



## Parameters

<dl> <dt>

*handle* \[in\]
</dt> <dd>

The handle to close.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

This function clears up sensitive data from memory and allows the RMS SDK 2.1 system to keep an accurate reference count on objects used.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





