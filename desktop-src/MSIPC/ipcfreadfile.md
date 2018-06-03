---
title: IpcfReadFile function
description: Reads protected content of a protected file given a logical file range.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7edba7fc-288d-48dd-8858-f18b9a35de31
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfReadFile function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfReadFile
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcfReadFile function

Reads protected content of a protected file given a logical file range. This operation requires that the current user has at least the VIEW right for the content.

## Syntax


```C++
EXTERN_C HRESULT WINAPI IpcfReadFile(
  _In_    IPCF_FILE_HANDLE  hFile,
  _In_    PCIPCF_FILE_RANGE pDataRange,
  _In_    PBYTE             pvBuffer,
  _Inout_ DWORD64           *cbBufferSize
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

Handle to the protected file.

This needs to be obtained from the function [**IpcfOpenFileOnILockBytes**](ipcfopenfileonilockbytes.md) or [**IpcfOpenFileOnHandle**](ipcfopenfileonhandle.md). .

</dd> <dt>

*pDataRange* \[in\]
</dt> <dd>

Pointer to [**IPCF\_FILE\_RANGE**](ipcf-file-range.md) structure indicating the data range to read.

</dd> <dt>

*pvBuffer* \[in\]
</dt> <dd>

Buffer to which the decrypted data will be returned.

</dd> <dt>

*cbBufferSize* \[in, out\]
</dt> <dd>

Pointer to size of *pvBuffer* in bytes.

On return, this contains the actual number of bytes copied into *pvBuffer*.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



 

 





