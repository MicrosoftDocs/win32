---
title: IpcGetErrorMessageText function
description: Returns the error message text associated with a supplied error code.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 1f992315-e97f-4593-a21f-23bdac17e042
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcGetErrorMessageText function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcGetErrorMessageText
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcGetErrorMessageText function

Returns the error message text associated with a supplied error code. This function can translate both Windows errors and errors returned by another Rights Management Services SDK 2.1 function.

## Syntax


```C++
HRESULT WINAPI IpcGetErrorMessageText(
        HRESULT hrError,
        DWORD   dwLanguageId,
  _Out_ LPCWSTR *ppwszErrorMessageText
);
```



## Parameters

<dl> <dt>

*hrError* 
</dt> <dd>

The error code to translate.

</dd> <dt>

*dwLanguageId* 
</dt> <dd>

The language identifier for the requested message. If zero, the function searches for LANGIDs in the order specified by [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351).

</dd> <dt>

*ppwszErrorMessageText* \[out\]
</dt> <dd>

A pointer to a variable that receives a **NULL**-terminated string that contains the translated error text. This buffer is allocated by the RMS Client 2.1 and must be freed by calling [**IpcFreeMemory**](ipcfreememory.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

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

[**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





