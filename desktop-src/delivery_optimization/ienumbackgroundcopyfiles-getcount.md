---
title: IEnumBackgroundCopyFiles GetCount method (Deliveryoptimization.h)
description: Retrieves a count of the number of files in the enumeration.
ms.assetid: EE27679D-3AC0-49DA-992F-8DEA10C21646
keywords:
- GetCount method
- GetCount method, IEnumBackgroundCopyFiles interface
- IEnumBackgroundCopyFiles interface, GetCount method
topic_type:
- apiref
api_name:
- IEnumBackgroundCopyFiles.GetCount
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IEnumBackgroundCopyFiles::GetCount method

Retrieves a count of the number of files in the enumeration.

## Syntax


```C++
HRESULT GetCount(
  [out] ULONG *pCount
);
```



## Parameters

<dl> <dt>

*pCount* \[out\]
</dt> <dd>

Number of files in the enumeration.

</dd> </dl>

## Return value

This method returns **S_OK** on success or one of the standard COM **HRESULT** values on error.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IEnumBackgroundCopyFiles is defined as CA51E165-C365-424C-8D41-24AAA4FF3C40<br/>         |



## See also

<dl> <dt>

[**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles-.md)
</dt> </dl>

 

 





