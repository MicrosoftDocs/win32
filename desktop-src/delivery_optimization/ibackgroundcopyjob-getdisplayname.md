---
title: IBackgroundCopyJob GetDisplayName method (Deliveryoptimization.h)
description: Retrieves the display name for the job. Typically, you use the display name to identify the job in a user interface.
ms.assetid: E3D906E1-5D58-4BA8-A3AB-24BCDCD487F5
keywords:
- GetDisplayName method
- GetDisplayName method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetDisplayName method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetDisplayName
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetDisplayName method

Retrieves the display name for the job. Typically, you use the display name to identify the job in a user interface.

## Syntax


```C++
HRESULT GetDisplayName(
  [out] LPWSTR *ppDisplayName
);
```



## Parameters

<dl> <dt>

*ppDisplayName* \[out\]
</dt> <dd>

Null-terminated string that contains the display name that identifies the job. More than one job can have the same display name. Call the [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) function to free *ppDisplayName* when done.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                                  | Description                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl>     | Display name was successfully retrieved.<br/>          |
| <dl> <dt>**E_INVALIDARG**</dt> </dl> | The *ppDisplayName* parameter cannot be **NULL**.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyJob is defined as 37668D37-507E-4160-9316-26306D150B12<br/>               |



## See also

<dl> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> </dl>

 

