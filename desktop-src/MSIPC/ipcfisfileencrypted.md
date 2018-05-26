---
title: IpcfIsFileEncrypted function
description: Determines whether a file on disk is encrypted.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 6EC4343D-1D34-4C28-B716-1971A0ABA6E0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfIsFileEncrypted function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfIsFileEncrypted
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcfIsFileEncrypted function

Determines whether a file on disk is encrypted.

## Syntax


```C++
HRESULT WINAPI IpcfIsFileEncrypted(
  _In_  LPCWSTR wszInputFilePath,
  _Out_ LPDWORD pdwFileStatus
);
```



## Parameters

<dl> <dt>

*wszInputFilePath* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The path to the file to query. The path must include the file name and, if one exists, the file name extension.

The path is limited to **MAX\_PATH** characters. To extend this limit to 32,767 characters, prepend "\\\\?\\" to the path. For more information, see [Naming Files, Paths, and Namespaces](https://msdn.microsoft.com/library/windows/desktop/aa365247.aspx).

</dd> <dt>

*pdwFileStatus* \[out\]
</dt> <dd>

Type: **LPDWORD**

A pointer to a variable that receives a **DWORD** that indicates whether and how the file is protected. When the function returns, this parameter can be one of the following values.

<dt>

<span id="IPCF_FILE_STATUS_DECRYPTED"></span><span id="ipcf_file_status_decrypted"></span>

<span id="IPCF_FILE_STATUS_DECRYPTED"></span><span id="ipcf_file_status_decrypted"></span>**IPCF\_FILE\_STATUS\_DECRYPTED** (0)


</dt> <dd>

The file is not encrypted.

</dd> <dt>

<span id="IPCF_FILE_STATUS_ENCRYPTED_CUSTOM"></span><span id="ipcf_file_status_encrypted_custom"></span>

<span id="IPCF_FILE_STATUS_ENCRYPTED_CUSTOM"></span><span id="ipcf_file_status_encrypted_custom"></span>**IPCF\_FILE\_STATUS\_ENCRYPTED\_CUSTOM** (1)


</dt> <dd>

The file is encrypted using native protection; that is, using an AD RMS file format that is based on its MIME type. Some RMS functionality may not be available.

</dd> <dt>

<span id="IPCF_FILE_STATUS_ENCRYPTED"></span><span id="ipcf_file_status_encrypted"></span>

<span id="IPCF_FILE_STATUS_ENCRYPTED"></span><span id="ipcf_file_status_encrypted"></span>**IPCF\_FILE\_STATUS\_ENCRYPTED** (2)


</dt> <dd>

The file is encrypted.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

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

 

 





