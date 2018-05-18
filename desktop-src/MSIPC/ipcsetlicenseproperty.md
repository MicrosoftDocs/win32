---
title: IpcSetLicenseProperty function
description: Sets license properties for the platform.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '4af11fe6-d67a-41a4-a2da-50294193f56a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcSetLicenseProperty function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcSetLicenseProperty
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcSetLicenseProperty function

Sets license properties for the platform.

## Syntax


```C++
HRESULT WINAPI IpcSetLicenseProperty(
  _In_     IPC_LICENSE_HANDLE hLicense,
           BOOL               fDelete,
           DWORD              dwPropID,
  _In_opt_ LPCVOID            pvProperty
);
```



## Parameters

<dl> <dt>

*hLicense* \[in\]
</dt> <dd>

A handle to the license to be modified.

</dd> <dt>

*fDelete* 
</dt> <dd>

Set to **TRUE** to delete the existing information in the license. When set to **TRUE**; *pvProperty* is ignored.

Set to **FALSE** to replace the license info for the property specified by *dwPropId* with the value specified by *pvProperty*; *pvProperty* cannot be **NULL**.

</dd> <dt>

*dwPropID* 
</dt> <dd>

The ID of the license property to modify. The data specified by *pvProperty* must match this type. For a list of valid property IDs, see [**License property types**](license-property-types.md).

</dd> <dt>

*pvProperty* \[in, optional\]
</dt> <dd>

A pointer to the license information data to be written. If *fDelete* is false, this parameter cannot be **NULL**. The structure of the data depends on the property ID specified in *dwPropID*. For more information, see [**License property types**](license-property-types.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**E\_INVALIDARGS**
</dt> <dd>

Meaning: The *fDelete* parameter is **TRUE**, but the license property specified by the *dwPropID* parameter is not a property that can be deleted with this function. For more information about which properties cannot be deleted with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), see [**License property types**](license-property-types.md).

Action: Do not try to delete the specified property with this function.

</dd> </dl>

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

[**IpcGetLicenseProperty**](ipcgetlicenseproperty.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**License property types**](license-property-types.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





