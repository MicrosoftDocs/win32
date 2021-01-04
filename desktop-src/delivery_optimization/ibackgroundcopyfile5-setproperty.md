---
title: IBackgroundCopyFile5 SetProperty method (Deliveryoptimization.h)
description: Sets a generic property of a Delivery Optimization (DO) file transfer.
ms.assetid: 63B6806E-47D6-49B0-9867-628C110540D0
keywords:
- SetProperty method
- SetProperty method, IBackgroundCopyFile5 interface
- IBackgroundCopyFile5 interface, SetProperty method
topic_type:
- apiref
api_name:
- IBackgroundCopyFile5.SetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyFile5::SetProperty method

Sets a generic property of a Delivery Optimization (DO) file transfer.

## Syntax


```C++
HRESULT SetProperty(
  [in]  BITS_FILE_PROPERTY_ID    PropertyId,
  [out] BITS_FILE_PROPERTY_VALUE *ProertyValue
);
```



## Parameters

<dl> <dt>

*PropertyId* \[in\]
</dt> <dd>

Specifies the property to be set.

</dd> <dt>

*ProertyValue* \[out\]
</dt> <dd>

A pointer to a union that specifies the value to be set. The union member appropriate for the property ID is used.

</dd> </dl>

## Return value

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyFile5 is defined as 85C1657F-DAFC-40E8-8834-DF18EA25717E<br/>             |



## See also

<dl> <dt>

[**IBackgroundCopyFile5**](ibackgroundcopyfile5.md)
</dt> <dt>

[**IBackgroundCopyFile5.GetProperty**](ibackgroundcopyfile5-getproperty.md)
</dt> </dl>

 

 





