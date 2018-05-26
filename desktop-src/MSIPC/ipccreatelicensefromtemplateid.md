---
title: IpcCreateLicenseFromTemplateID function
description: Returns a handle to a license created from a template.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 1f140f83-06a8-4755-8687-df89a81b6cd7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcCreateLicenseFromTemplateID function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcCreateLicenseFromTemplateID
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcCreateLicenseFromTemplateID function

Returns a handle to a license created from a template. The license can be edited by calling the [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md) function.

## Syntax


```C++
HRESULT WINAPI IpcCreateLicenseFromTemplateID(
  _In_       LPCWSTR             wszTemplateID,
             DWORD               dwFlags,
  _Reserved_ LPVOID              pvReserved,
  _Out_      PIPC_LICENSE_HANDLE phLicense
);
```



## Parameters

<dl> <dt>

*wszTemplateID* \[in\]
</dt> <dd>

A template ID obtained from a call to the [**IpcGetTemplateList**](ipcgettemplatelist.md) function.

</dd> <dt>

*dwFlags* 
</dt> <dd>

This parameter must be 0.

</dd> <dt>

*pvReserved* 
</dt> <dd>

This parameter is reserved and must be **NULL**.

</dd> <dt>

*phLicense* \[out\]
</dt> <dd>

A pointer to a variable that receives a handle to the created license.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

When you have finished using the license handle created with this function, close it by using the [**IpcCloseHandle**](ipcclosehandle.md) function.

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

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**IpcSetLicenseProperty**](ipcsetlicenseproperty.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





