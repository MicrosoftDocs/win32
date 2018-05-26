---
title: IpcfGetEncryptedFilePath function
description: Used to get the expected, encrypted, absolute file path.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 618E69AC-B87E-4E0A-8219-663EF2A15117
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfGetEncryptedFilePath function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfGetEncryptedFilePath
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcfGetEncryptedFilePath function

Used to get the expected, encrypted, absolute file path. Note that, this function does not actually encrypt the file.

## Syntax


```C++
HRESULT WINAPI IpcfGetEncryptedFilePath(
  _In_      LPCWSTR wszInputFilePath,
            DWORD   dwFlags,
  _Out_opt_ LPCWSTR *pwszOutputFilePath
);
```



## Parameters

<dl> <dt>

*wszInputFilePath* \[in\]
</dt> <dd>

Specifies file name and file extension of the file and, may contain the path to the file.

If a relative path is specified, the current working directory is used to create the absolute path.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Specify optional behavior for this function. For a list of valid values, see [**Encrypt file flags**](encrypt-file-flags.md).

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



 

 





