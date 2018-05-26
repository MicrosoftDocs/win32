---
title: IpcGetSerializedLicenseProperty function
description: Retrieves the information available from a serialized license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 572F68EE-CCBF-4B88-AB41-D63EE948CE25
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcGetSerializedLicenseProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcGetSerializedLicenseProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcGetSerializedLicenseProperty function

Retrieves the information available from a serialized license. This is functionally equivalent to information that could be gathered from [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md), but it may be performed by the consumer of content who only has the serialized license.

## Syntax


```C++
HRESULT WINAPI IpcGetSerializedLicenseProperty(
  _In_     PCIPC_BUFFER    pvLicense,
           DWORD           dwPropID,
  _In_opt_ IPC_KEY_HANDLE  hKey,
           LCID            lcid,
  _Out_    LPVOID          *ppvProperty
);
```



## Parameters

<dl> <dt>

*pvLicense* \[in\]
</dt> <dd>

A buffer which stores a serialized license. For more information, see [**AD RMS data types**](microsoft-information-protection-and-control-client-data-types.md).

</dd> <dt>

*dwPropID* 
</dt> <dd>

ID of the property to query. For more information on valid IDs, see [**License property types**](license-property-types.md).

When querying for user rights, take note of the setting of **cbSize** on the [**IPC\_USER\_RIGHTS\_LIST**](ipc-user-rights-list.md) structure. For more information, see **IPC\_USER\_RIGHTS\_LIST**.

</dd> <dt>

*hKey* \[in, optional\]
</dt> <dd>

Handle to a key object acquired by using the [**IpcGetKey**](ipcgetkey.md) function.

</dd> <dt>

*lcid* 
</dt> <dd>

For localized properties, *lcid* contains the locale ID of the descriptor to query. This parameter is ignored unless *dwPropID* is **IPC\_LI\_DESCRIPTOR**.

> [!Note]  
> See the Frequently asked questions section of the [Release notes](release-notes--rtm-.md) topic for information about the API behavior regarding language ID.

 

</dd> <dt>

*ppvProperty* \[out\]
</dt> <dd>

Pointer to a Pointer of a buffer to hold the license information. The buffer is allocated by the API and must be de-allocated using [**IpcFreeMemory**](ipcfreememory.md). The structure returned depends on the value of *dwPropID*. For more information on valid types, see [**License property types**](license-property-types.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_LOCALE\_NOT\_FOUND**
</dt> <dd>

Meaning: The application specified a nonzero *lcid*, but no templates were available that had a descriptor in this locale.

Action: For more information about *lcid* see, the description of **IPC\_LI\_DESCRIPTOR** in [**License Property Types**](license-property-types.md). Also see the Frequently asked questions section of the [Release notes](release-notes--rtm-.md) topic.

</dd> <dt>

**IPCERROR\_NEEDS\_KEY\_PARAMETER**
</dt> <dd>

Meaning: The *hKey* parameter was needed with this call due to the property being accessed by using the *dwPropID* parameter. For more information about properties needing a key, see [**License property types**](license-property-types.md).

Action: Provide the *hKey* parameter acquired by using the [**IpcGetKey**](ipcgetkey.md) function.

</dd> <dt>

**IPCERROR\_RIGHT\_NOT\_GRANTED**
</dt> <dd>

Meaning: The user does not have **IPC\_GENERIC\_VIEW\_RIGHTS** to the license passed in, when trying to reuse a license.

> \[!Tip\]  
> Consider messaging the user about this absence of rights.

 

</dd> </dl>

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

[**AD RMS data types**](microsoft-information-protection-and-control-client-data-types.md)
</dt> <dt>

[**IPC\_USER\_RIGHTS\_LIST**](ipc-user-rights-list.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**IpcGetLicenseProperty**](ipcgetlicenseproperty.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**License property types**](license-property-types.md)
</dt> <dt>

[Release notes](release-notes--rtm-.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





