---
title: IpcfSetEndOfFile function
description: Truncates a protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'feee7654-4671-4ba2-aa97-204cfce21c78'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcfSetEndOfFile function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcfSetEndOfFile
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcfSetEndOfFile function

Truncates a protected file.

## Syntax


```C++
EXTERN_C HRESULT WINAPI IpcfSetEndOfFile(
  _In_ IPCF_FILE_HANDLE hFile,
  _In_ DWORD64          qwOffset
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

Handle to the protected file.

This needs to be obtained from the function [**IpcfOpenFileOnILockBytes**](ipcfopenfileonilockbytes.md) or [**IpcfOpenFileOnHandle**](ipcfopenfileonhandle.md).

</dd> <dt>

*qwOffset* \[in\]
</dt> <dd>

The logical offset of the file to set as EOF (end of file).

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



 

 





