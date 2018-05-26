---
title: IpcfEncryptFileWithMetadata function
description: Used to encrypt a file and optionally add metadata to the file encryption license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 151F51B5-E005-4809-9A78-258A2DE4BAA7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcfEncryptFileWithMetadata function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcfEncryptFileWithMetadata
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcfEncryptFileWithMetadata function

Used to encrypt a file and optionally add metadata to the file encryption license.

## Syntax


```C++
HRESULT WINAPI IpcfEncryptFileWithMetadata(
  _In_      LPCWSTR                wszInputFilePath,
  _In_      LPCVOID                pvLicenseInfo,
  _In_      DWORD                  dwType,
  _In_      DWORD                  dwFlags,
  _In_opt_  PCIPC_PROMPT_CTX       pContext,
  _In_opt_  LPCWSTR                wszOutputFileDirectory,
  _In_opt_  PCIPC_LICENSE_METADATA pLicenseMetadata,
  _Out_opt_ LPCWSTR                *pwszOutputFilePath
);
```



## Parameters

<dl> <dt>

*wszInputFilePath* \[in\]
</dt> <dd>

Specifies a file name and file extension.

The file name and may also contain the path to the file. If a relative path is specified, the current working directory is used to create the absolute path.

</dd> <dt>

*pvLicenseInfo* \[in\]
</dt> <dd>

License information used for encryption.

For more information, see [**Encrypt file input type**](encrypt-file-input-type.md)

</dd> <dt>

*dwType* \[in\]
</dt> <dd>

Type of license information used for encryption.

For a list of valid values, see [**Encrypt file input type**](encrypt-file-input-type.md)

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Specify optional behavior for this API.

For a list of valid values, see [**Encrypt file flags**](encrypt-file-flags.md)

</dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

Optional pointer to user prompt information, [**PCIPC\_PROMPT\_CTX**](ipc-prompt-ctx.md), for the client.

</dd> <dt>

*wszOutputFileDirectory* \[in, optional\]
</dt> <dd>

Optional pointer to the output file directory.

If *wszOutputFileDirectory* is not specified, the output file will be placed in the same directory as the input file.

If *wszOutputFileDirectory* is specified, the output file will be placed in this folder and the original file will be deleted.

</dd> <dt>

*pLicenseMetadata* \[in, optional\]
</dt> <dd>

Optional pointer to metadata information, [**PCIPC\_LICENSE\_METADATA**](ipc-license-metadata.md), to be added to the file protection license.

</dd> <dt>

*pwszOutputFilePath* \[out, optional\]
</dt> <dd>

On success, the full path of the output file.

This should be freed using [**IpcFreeMemory**](ipcfreememory.md).

If neither the file name nor directory changes, *pwszOutputFilePath* will be **NULL**.

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

[**License metadata property types**](license-metadata-property-types.md)
</dt> <dt>

[**Notification preference**](notification-preference.md)
</dt> <dt>

[**Notification type**](notification-type.md)
</dt> <dt>

[**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md)
</dt> <dt>

[**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md)
</dt> <dt>

[**IpcSerializeLicenseWithMetadata**](ipcserializelicensemetadata.md)
</dt> <dt>

[**IpcfEncryptFileWithMetadata**](ipcfencryptfilewithmetadata.md)
</dt> <dt>

[**IpcfEncryptFileStreamWithMetadata**](ipcfencryptfilestreamwithmetadata.md)
</dt> <dt>

[**IpcRegisterLicense**](ipcregisterlicense.md)
</dt> </dl>

 

 





