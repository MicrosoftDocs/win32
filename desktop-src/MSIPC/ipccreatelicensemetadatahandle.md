---
title: IpcCreateLicenseMetadataHandle function
description: Creates a handle for create or modify operations on the metadata of the serialized license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '03B40645-FE94-4F04-A622-FEBF230D9773'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcCreateLicenseMetadataHandle function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcCreateLicenseMetadataHandle
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcCreateLicenseMetadataHandle function

Creates a handle for create or modify operations on the metadata of the serialized license.

## Syntax


```C++
HRESULT WINAPI IpcCreateLicenseMetadataHandle(
  _In_       PCIPC_BUFFER         pvSerializedLicense,
             IPC_KEY_HANDLE       hKey,
  _Reserved_ LPVOID               pvReserved,
  _Out_      PIPC_METADATA_HANDLE phMetadata
);
```



## Parameters

<dl> <dt>

*pvSerializedLicense* \[in\]
</dt> <dd>

Pointer to the serialized license with or without the metadata information set.

</dd> <dt>

*hKey* 
</dt> <dd>

Handle to a key object acquired via [**IpcGetKey**](ipcgetkey.md) or via [**IpcGetSerializedLicense**](ipcgetserializedlicenseproperty.md).

</dd> <dt>

*pvReserved* 
</dt> <dd>

This is a reserved field and must be NULL.

</dd> <dt>

*phMetadata* \[out\]
</dt> <dd>

The resulting handle.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**E\_INVALIDARG**
</dt> </dl>

## Remarks

The user must be the owner of the PL to be able to modify the metadata.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
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

 

 





