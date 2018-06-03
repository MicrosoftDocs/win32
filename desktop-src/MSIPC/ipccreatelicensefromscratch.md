---
title: IpcCreateLicenseFromScratch function
description: Returns a handle to a license created from scratch.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 021ad798-6e32-49c9-bef2-62f0867baf71
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcCreateLicenseFromScratch function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcCreateLicenseFromScratch
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcCreateLicenseFromScratch function

Returns a handle to a license created from scratch. The license can be edited by calling [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md).

## Syntax


```C++
HRESULT WINAPI IpcCreateLicenseFromScratch(
  _In_       PCIPC_TEMPLATE_ISSUER pTemplateIssuer,
             DWORD                 dwFlags,
  _Reserved_ LPVOID                pvReserved,
  _Out_      PIPC_LICENSE_HANDLE   phLicense
);
```



## Parameters

<dl> <dt>

*pTemplateIssuer* \[in\]
</dt> <dd>

A pointer to a [**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md) structure returned by a call to [**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md).

The license created will be protected to the AD RMS server pointed to by the **connectionInfo** member of this [**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md) structure.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Must be 0.

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

[**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md)
</dt> <dt>

[**IpcGetLicenseProperty**](ipcgetlicenseproperty.md)
</dt> <dt>

[**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md)
</dt> <dt>

[**IpcSerializeLicense**](ipcserializelicense.md)
</dt> <dt>

[**IpcSetLicenseProperty**](ipcsetlicenseproperty.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





