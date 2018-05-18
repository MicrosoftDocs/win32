---
title: IpcfEncryptFileStream function
description: Encrypts a file as a byte stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '95AC8059-1FD9-43EC-8F96-E6D250B86DC8'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcfEncryptFileStream function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcfEncryptFileStream
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcfEncryptFileStream function

Encrypts a file as a byte stream.

## Syntax


```C++
HRESULT WINAPI IpcfEncryptFileStream(
  _In_      ILockBytes       *pInputFileStream,
  _In_      LPCWSTR          wszInputFilePath,
  _In_      LPCVOID          pvLicenseInfo,
  _In_      DWORD            dwType,
  _In_      DWORD            dwFlags,
  _In_opt_  PCIPC_PROMPT_CTX pContext,
  _Out_     ILockBytes       *pOutputFileStream,
  _Out_opt_ LPCWSTR          *pwszOutputFilePath
);
```



## Parameters

<dl> <dt>

*pInputFileStream* \[in\]
</dt> <dd>

Pointer to the byte stream that represents the file to be encrypted.

</dd> <dt>

*wszInputFilePath* \[in\]
</dt> <dd>

The path to the file to encrypt. The path must include the file name and, if one exists, the file name extension.

This parameter is only used to determine the file format, based on the file name extension of the file in the input file stream. Based on this, the suggested output filename is returned via *pwszOutputFilePath* parameter.

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

An optional pointer to information that helps the RMS Client 2.1 determine what the user prompt behavior should be. For more information, see [**IPC\_PROMPT\_CTX**](ipc-prompt-ctx.md) structure.

</dd> <dt>

*pOutputFileStream* \[out\]
</dt> <dd>

A pointer to get the encrypted bytes as a result of an encryption operation on a byte stream.

You will need to initialize this interface before calling the API, and free it after the API is done using **ILockBytes::Release**. For more information on using ILockBytes see, [ILockBytes interface](https://msdn.microsoft.com/library/aa379238.aspx).

</dd> <dt>

*pwszOutputFilePath* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives a pointer to the suggested output file path.

The file needs to be saved with the same extension suggested in the parameter for encryption to be possible. If the suggested output file path is same as the one provided via *wszInputFilePath*, this value will be **NULL**.

If the output file path is returned, it will be an absolute file path. The buffer that contains the output file path is allocated by the File API and must be freed by using [**IpcFreeMemory**](ipcfreememory.md).

If native protection is used, the value of *pwszOutputFilePath* will be **NULL** when the function returns.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_FILE\_ENCRYPT\_BLOCKED**
</dt> <dd></dd> <dt>

**IPCERROR\_FILE\_UPDATELICENSE\_BLOCKED**
</dt> <dd></dd> <dt>

**ERROR\_FILE\_READ\_ONLY**
</dt> <dd></dd> </dl>

## Remarks

PDF files which are signed, linearized, are not supported for native protection and will cause an error.

For supporting information on using the File API part of RMS SDK 2.1 see, [Supported File Formats](supported-file-formats.md), [File API configuration](file-api-configuration.md) and [Setting the API security](setting-the-api-security-mode--api-mode-.md) mode in the [AD RMS developer notes](developer-notes.md) topic.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
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

 

 





