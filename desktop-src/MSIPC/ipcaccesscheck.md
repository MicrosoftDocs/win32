---
title: IpcAccessCheck function
description: Checks whether a key object grants the requested right.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7bb9a985-173a-4d92-86f7-afdf72f2be6e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcAccessCheck function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcAccessCheck
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcAccessCheck function

Checks whether a key object grants the requested right.

## Syntax


```C++
HRESULT WINAPI IpcAccessCheck(
  _In_  IPC_KEY_HANDLE hKey,
  _In_  LPCWSTR        wszRequestedRight,
  _Out_ LPBOOL         pfAccessGranted
);
```



## Parameters

<dl> <dt>

*hKey* \[in\]
</dt> <dd>

A handle to a key object returned by either [**IpcSerializeLicense**](ipcserializelicense.md) or [**IpcGetKey**](ipcgetkey.md).

</dd> <dt>

*wszRequestedRight* \[in\]
</dt> <dd>

A Unicode string that represents a single right. The string is not case-sensitive. Rights can be defined by the application or can be one of the rights defined by RMS SDK 2.1. For more information, see [**Rights**](rights.md).

</dd> <dt>

*pfAccessGranted* \[out\]
</dt> <dd>

A pointer to a variable that receives the result of the operation. The result is **TRUE** if the requested right has been granted; otherwise, **FALSE.**

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

This function should be used to determine whether to enforce a usage restriction, application defined or otherwise. For more information, see the [Usage restriction reference](usage-restriction-reference.md).

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**Rights**](rights.md)
</dt> <dt>

[Usage restriction reference](usage-restriction-reference.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





