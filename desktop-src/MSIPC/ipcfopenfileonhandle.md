---
title: IpcfOpenFileOnHandle function
description: Gets an IPCF\_FILE\_HANDLE associated with an encrypted file which can be used to access and modify that file's data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'd67f5a99-a38f-4a34-b0b4-1d3d453f0c8f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcfOpenFileOnHandle function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcfOpenFileOnHandle
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcfOpenFileOnHandle function

Gets an **IPCF\_FILE\_HANDLE** associated with an encrypted file which can be used to access and modify that file's data. This operation requires that the current user has at least the **VIEW** right for the content.

## Syntax


```C++
EXTERN_C HRESULT WINAPI IpcfOpenFileOnHandle(
  _In_     HANDLE            hFileStream,
  _In_opt_ PCIPC_PROMPT_CTX  pContext,
           DWORD             dwFlags,
  _Out_    PIPCF_FILE_HANDLE phFile
);
```



## Parameters

<dl> <dt>

*hFileStream* \[in\]
</dt> <dd>

HANDLE to a file, opened by a Windows API **::CreateFile** function, that represents an encrypted file.

This function will fail for un-unencrypted files or custom-encrypted files (i.e., files for which [**IpcfIsFileEncrypted**](ipcfisfileencrypted.md) returns **IPCF\_FILE\_STATUS\_ENCRYPTED\_CUSTOM**.

*hFileStream* must not be freed or modified until the *phFile* is closed.

</dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

Optional pointer to information that helps the MSIPC client decide what the user prompt behavior should be.

</dd> <dt>

*dwFlags* 
</dt> <dd>

This must be set to 0 (zero).

</dd> <dt>

*phFile* \[out\]
</dt> <dd>

Pointer to an **IPCF\_FILE\_HANDLE** which can be used to read/write the encrypted data. This pointer must be closed using the [**IpcCloseHandle**](ipcclosehandle.md) function.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_FILE\_NOT\_ENCRYPTED**
</dt> <dd>

Function failed due to an un-unencrypted files.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



 

 





