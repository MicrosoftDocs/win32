---
title: IpcfEncryptFile function
description: Encrypts a file on disk.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 8777F766-8FB7-438F-B1F5-7F23E4F6F545
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfEncryptFile function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfEncryptFile
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcfEncryptFile function

Encrypts a file on disk.

## Syntax


```C++
HRESULT WINAPI IpcfEncryptFile(
  _In_      LPCWSTR          wszInputFilePath,
  _In_      LPCVOID          pvLicenseInfo,
  _In_      DWORD            dwType,
  _In_      DWORD            dwFlags,
  _In_opt_  PCIPC_PROMPT_CTX pContext,
  _In_opt_  LPCWSTR          wszOutputFileDirectory,
  _Out_opt_ LPCWSTR          *pwszOutputFilePath
);
```



## Parameters

<dl> <dt>

*wszInputFilePath* \[in\]
</dt> <dd>

The path to the file to encrypt. The path must include the file name and, if one exists, the file name extension.

The path is limited to **MAX\_PATH** characters. To extend this limit to 32,767 characters, prepend "\\\\?\\" to the path. For more information, see [Naming Files, Paths, and Namespaces](https://msdn.microsoft.com/library/windows/desktop/aa365247.aspx).

</dd> <dt>

*pvLicenseInfo* \[in\]
</dt> <dd>

A pointer to the license information to use for encryption. The value of this parameter depends on the *dwType* parameter.

</dd> <dt>

*dwType* \[in\]
</dt> <dd>

The type of license information to use for encryption. For more information, see [**Encrypt file input type**](encrypt-file-input-type.md).

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Specifies optional behavior for this function. For more information, see [**Encrypt file flags**](encrypt-file-flags.md).

</dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

An optional pointer to information that helps the RMS Client 2.1 determine what the user prompt behavior should be. For more information, see [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure.

</dd> <dt>

*wszOutputFileDirectory* \[in, optional\]
</dt> <dd>

An optional pointer to the output file directory. If the parameter is not specified, the output file will be placed in the same directory as the input file. If the parameter is specified, the output file will be placed in the specified folder. The original file will be deleted.

The path is limited to **MAX\_PATH** characters. To extend this limit to 32,767 characters, prepend "\\\\?\\" to the path. For more information, see [Naming Files, Paths, and Namespaces](https://msdn.microsoft.com/library/windows/desktop/aa365247.aspx).

</dd> <dt>

*pwszOutputFilePath* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives a pointer to the output file path. If the file is encrypted in place (the output file path does not change), the value will be **NULL**. If the output file path is returned, it will be an absolute file path. The buffer that contains the output file path is allocated by the File API and must be freed by using [**IpcFreeMemory**](ipcfreememory.md).

If native protection is used, the value of *pwszOutputFilePath* will be **NULL** when the function returns.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_FILE\_ENCRYPT\_BLOCKED**
</dt> <dt>

**IPCERROR\_FILE\_UPDATELICENSE\_BLOCKED**
</dt> <dt>

**ERROR\_FILE\_READ\_ONLY**
</dt> <dt>

**IPCERROR\_FILE\_SYSTEM\_FILE**
</dt> <dt>

**IPCERROR\_FILE\_PROTECTOR\_BAD\_INSTALL**
</dt> </dl>

## Remarks

The value of the **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** property set on a license handle passed in the *pvLicenseInfo* parameter is ignored by **IpcfEncryptFile**.

If your application is scanning a protected file, you should perform operations against a copy of the protected file, not on the actual file itself. Your application should create a copy of the protected file, unprotect the copy, scan it, re-encrypt it, and then replace the original protected file with the newly re-encrypted one. This should happen in a single transaction. Operating on a copy of the protected file ensures that if re-encryption fails -- for example, because a user opens the file while it is being operated on -- then the original file will not be lost.

If the input file is in a read-only folder, **IpcfEncryptFile** will fail. In this case, you can either copy the file to the folder in which want the encrypted copy placed and call **IpcfEncryptFile** without setting the *wszOutputFilePath* parameter, or you can copy the file to a temporary folder and call **IpcfEncryptFile** with *wszOutputFilePath* set to the directory where you want the encrypted file to be placed. In both cases, **IpcfEncryptFile** will delete the copy of the original, unencrypted file.

PDF files which are signed, linearized, are not supported for native protection and will cause an error.

For supporting information on using the File API part of RMS SDK 2.1 see, [Supported File Formats](supported-file-formats.md), [File API configuration](file-api-configuration.md) and [Setting the API security](setting-the-api-security-mode--api-mode-.md) mode in the [AD RMS developer notes](developer-notes.md) topic.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[Naming Files, Paths, and Namespaces](https://msdn.microsoft.com/library/windows/desktop/aa365247.aspx)
</dt> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
</dt> <dt>

[**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md)
</dt> <dt>

[**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[Supported File Formats](supported-file-formats.md)
</dt> <dt>

[File API configuration](file-api-configuration.md)
</dt> <dt>

[Setting the API security](setting-the-api-security-mode--api-mode-.md)
</dt> <dt>

[AD RMS developer notes](developer-notes.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





