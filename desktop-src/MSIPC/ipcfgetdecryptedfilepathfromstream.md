---
title: IpcfGetDecryptedFilePathFromStream function
description: Used to get the expected, decrypted, absolute file path.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 72FB0C29-FBA8-4938-8CF1-BEE03D3BC007
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfGetDecryptedFilePathFromStream function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfGetDecryptedFilePathFromStream
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcfGetDecryptedFilePathFromStream function

Used to get the expected, decrypted, absolute file path. Note that, this function does not actually decrypt the file.

## Syntax


```C++
HRESULT WINAPI IpcfGetDecryptedFilePathFromStream(
  _In_      ILockBytes pInputFileStream,
  _In_      LPCWSTR    wszInputFilePath,
  _In_      DWORD      dwFlags,
  _Out_opt_ LPCWSTR    *pwszOutputFilePath
);
```



## Parameters

<dl> <dt>

*pInputFileStream* \[in\]
</dt> <dd>

Pointer to the byte stream representing the protected file data.

</dd> <dt>

*wszInputFilePath* \[in\]
</dt> <dd>

Specifies file name and file extension of the file and, may contain the path to the file.

If a relative path is specified, the current working directory is used to create the absolute path.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Specifies optional behavior for this API. For a list of valid values, see [**Decrypt file flags**](decrypt-file-flags.md).

</dd> <dt>

*pwszOutputFilePath* \[out, optional\]
</dt> <dd>

On success, this parameter points to the expected full path of the decrypted file.

This should be freed using [**IpcFreeMemory**](ipcfreememory.md).

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



 

 





