---
title: IpcSetLicenseMetadataProperty function
description: Used to set the metadata of the license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: F6C686C2-B7D5-4149-B05C-968E9C5629EC
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcSetLicenseMetadataProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcSetLicenseMetadataProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcSetLicenseMetadataProperty function

Used to set the metadata of the license.

## Syntax


```C++
HRESULT WINAPI IpcSetLicenseMetadataProperty(
  _In_     IPC_LICENSE_METADATA_HANDLE hLicenseMetadata,
           BOOL                        fDelete,
           DWORD                       dwPropID,
  _In_opt_ LPCVOID                     pvProperty
);
```



## Parameters

<dl> <dt>

*hLicenseMetadata* \[in\]
</dt> <dd>

Handle representing the license metadata. This can be obtained from the method [**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md). See [**Data types**](microsoft-information-protection-and-control-client-data-types.md) for more information about the type of this parameter.

</dd> <dt>

*fDelete* 
</dt> <dd>

If this parameter is **TRUE**, the property specified by *dwPropID* will be deleted from the license.

The parameter, *pvProperty* should be **NULL** if this is **TRUE**.

</dd> <dt>

*dwPropID* 
</dt> <dd>

Type of license metadata property to modify.

The *pvProperty* parameter must match this type.

For a list of valid IDs, [**License metadata property types**](license-metadata-property-types.md).

</dd> <dt>

*pvProperty* \[in, optional\]
</dt> <dd>

Pointer to various types of license information data.

For more information, see [**License metadata property types**](license-metadata-property-types.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**E\_INVALIDARG**
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

 

 





