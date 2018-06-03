---
title: IpcSerializeLicenseWithMetadata function
description: Used to finalize the metadata of the license and serialize it.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 77093E90-5A84-47C8-B8BE-4065C183C0BD
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcSerializeLicenseWithMetadata function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcSerializeLicenseWithMetadata
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcSerializeLicenseWithMetadata function

Used to finalize the metadata of the license and serialize it.

## Syntax


```C++
HRESULT WINAPI IpcSerializeLicenseWithMetadata(
  _In_       IPC_LICENSE_METADATA_HANDLE hLicenseMetadata,
  _Reserved_ LPVOID                      pvReserved,
  _In_opt_   PCIPC_PROMPT_CTX            pContext,
  _Out_      PIPC_BUFFER                 *ppvLicense
);
```



## Parameters

<dl> <dt>

*hLicenseMetadata* \[in\]
</dt> <dd>

Handle representing the license metadata. This can be obtained from the method [**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md). See [**Data types**](microsoft-information-protection-and-control-client-data-types.md) for more information about the type of this parameter.

</dd> <dt>

*pvReserved* 
</dt> <dd>

This is a reserved parameter and must be set to **NULL**.

</dd> <dt>

*pContext* \[in, optional\]
</dt> <dd>

Optional pointer to information that helps the IPC Client decide what the user prompt behavior should be.

This can be used in cases where authentication prompts are not desirable or when an application wants to control the modal behavior of any prompt dialogs.

</dd> <dt>

*ppvLicense* \[out\]
</dt> <dd>

Pointer to the pointer to the buffer for serialized license with metadata.

The buffer is allocated by the API and must be freed using [**IpcFreeMemory**](ipcfreememory.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**E\_INVALIDARG**
</dt> <dt>

**E\_OUTOFMEMORY**
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
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

 

 





