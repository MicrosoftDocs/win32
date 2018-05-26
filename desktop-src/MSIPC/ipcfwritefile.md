---
title: IpcfWriteFile function
description: Modifies protected content of a protected file to a given logical file range.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 548b402b-038d-4066-8ea1-a9cf7b8fcfe5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfWriteFile function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfWriteFile
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcfWriteFile function

Modifies protected content of a protected file to a given logical file range.

## Syntax


```C++
EXTERN_C HRESULT WINAPI IpcfWriteFile(
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

This needs to be obtained from the function [**IpcfOpenFileOnILockBytes**](ipcfopenfileonilockbytes.md) or [**IpcfOpenFileOnHandle**](ipcfopenfileonhandle.md).

</dd> <dt>

*pDataRange* \[in\]
</dt> <dd>

Pointer to [**IPCF\_FILE\_RANGE**](ipcf-file-range.md) structure indicating the data range to write.

</dd> <dt>

*pvBuffer* \[in\]
</dt> <dd>

The unencrypted data which needs to be written at the given data range specified through *pDataRange*.

</dd> <dt>

*cbBufferSize* \[in, out\]
</dt> <dd>

Pointer to size of *pvBuffer* in bytes.

On return, this contains the actual number of bytes written to the file represented by *hFile* parameter.

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



 

 





