---
title: IEnumBackgroundCopyFiles Reset method (Deliveryoptimization.h)
description: IEnumBackgroundCopyFiles::Reset method - Resets the enumeration sequence to the beginning.
ms.assetid: 6A303069-105C-4053-A8C5-2ECF60E789DE
keywords:
- Reset method
- Reset method, IEnumBackgroundCopyFiles interface
- IEnumBackgroundCopyFiles interface, Reset method
topic_type:
- apiref
api_name:
- IEnumBackgroundCopyFiles.Reset
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IEnumBackgroundCopyFiles::Reset method

Resets the enumeration sequence to the beginning.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

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

 

 





