---
title: IpcGetLicenseProperty function
description: Returns information about a license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: b94d228d-645b-442c-adb4-2bf8c041423d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcGetLicenseProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcGetLicenseProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcGetLicenseProperty function

Retrieves the information available from a license.

## Syntax


```C++
HRESULT WINAPI IpcGetLicenseProperty(
  _In_  IPC_LICENSE_HANDLE hLicense,
        DWORD              dwPropID,
        LCID               lcid,
  _Out_ LPVOID             *ppvProperty
);
```



## Parameters

<dl> <dt>

*hLicense* \[in\]
</dt> <dd>

A handle to the license or template to be queried.

You can get a license handle from these functions:

-   [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
-   [**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md)

</dd> <dt>

*dwPropID* 
</dt> <dd>

The ID of the license property for which to query. The *pvLicenseInfo* parameter must match this property ID. For a list of valid property IDs, see [**License Property Types**](license-property-types.md).

When querying for user rights, take note of the setting of **cbSize** on the [**IPC\_USER\_RIGHTS\_LIST**](ipc-user-rights-list.md) structure. For more information, see **IPC\_USER\_RIGHTS\_LIST**.

</dd> <dt>

*lcid* 
</dt> <dd>

For localized properties, contains the locale identifier (LCID) of the descriptor to query. This parameter is ignored unless *dwPropID* is **IPC\_LI\_DESCRIPTOR**.

> [!Note]  
> See the Frequently asked questions section of the [Release notes](release-notes--rtm-.md) topic for information about the API behavior regarding language.

 

</dd> <dt>

*ppvProperty* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the buffer that contains the license information. The buffer is allocated by the RMS Client 2.1 and must be freed by calling [**IpcFreeMemory**](ipcfreememory.md). The structure of the data returned depends on the property ID specified in *dwPropID*. For more information, see [**License Property Types**](license-property-types.md).

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

[**IPC\_USER\_RIGHTS\_LIST**](ipc-user-rights-list.md)
</dt> <dt>

[**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)
</dt> <dt>

[**IpcCreateLicenseFromTemplateID**](ipccreatelicensefromtemplateid.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**IpcSetLicenseProperty**](ipcsetlicenseproperty.md)
</dt> <dt>

[**License Property Types**](license-property-types.md)
</dt> <dt>

[Release notes](release-notes--rtm-.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





