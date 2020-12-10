---
title: IBackgroundCopyJob5 GetProperty method (Deliveryoptimization.h)
description: A generic method for getting Delivery Optimization (DO) job properties.
ms.assetid: 22BA2FAB-3F24-4801-8FB7-CB6F9E8DFBB3
keywords:
- GetProperty method
- GetProperty method, IBackgroundCopyJob5 interface
- IBackgroundCopyJob5 interface, GetProperty method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob5.GetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob5::GetProperty method

A generic method for getting Delivery Optimization (DO) job properties.

## Syntax


```C++
HRESULT GetProperty(
  [in]  BITS_JOB_PROPERTY_ID    PropertyId,
  [out] BITS_JOB_PROPERTY_VALUE *pPropertyValue
);
```



## Parameters

<dl> <dt>

*PropertyId* \[in\]
</dt> <dd>

The ID of the property that is being obtained specified as a [**BITS_JOB_PROPERTY_ID**](bits-job-property-id.md) enum value.

</dd> <dt>

*pPropertyValue* \[out\]
</dt> <dd>

The property value returned as a BITS_JOB_PROPERTY_VALUE union.

</dd> </dl>

## Return value

The method returns the following return values.



| Return code                                                                          | Description        |
|--------------------------------------------------------------------------------------|--------------------|
| <dl> <dt>**S_OK**</dt> </dl> | Success<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyJob5 is defined as E847030C-BBBA-4657-AF6D-484AA42BF1FE<br/>              |



## See also

<dl> <dt>

[**IBackgroundCopyJob5**](ibackgroundcopyjob5.md)
</dt> <dt>

[**IBackgroundCopyJob5::SetProperty**](ibackgroundcopyjob5-setproperty.md)
</dt> </dl>

 

 





