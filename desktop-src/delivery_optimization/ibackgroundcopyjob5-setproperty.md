---
title: IBackgroundCopyJob5 SetProperty method (Deliveryoptimization.h)
description: A generic method for setting Delivery Optimization (DO) job properties.
ms.assetid: 9A8CCE04-B3EB-43CC-A135-7054EC40ABEC
keywords:
- SetProperty method
- SetProperty method, IBackgroundCopyJob5 interface
- IBackgroundCopyJob5 interface, SetProperty method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob5.SetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob5::SetProperty method

A generic method for setting Delivery Optimization (DO) job properties.

## Syntax


```C++
HRESULT SetProperty(
  [in] BITS_JOB_PROPERTY_ID    PropertyId,
  [in] BITS_JOB_PROPERTY_VALUE PropertyValue
);
```



## Parameters

<dl> <dt>

*PropertyId* \[in\]
</dt> <dd>

The ID of the property that is being set specified as a [**BITS_JOB_PROPERTY_ID**](bits-job-property-id.md) enum value.

</dd> <dt>

*PropertyValue* \[in\]
</dt> <dd>

The value of the property that is being set. In order to hold a value whose type is appropriate to the property, this value is specified via the [**BITS_JOB_PROPERTY_VALUE**](bits-job-property-value-.md) union that is composed of all the known property types.

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

[**IBackgroundCopyJob5::GetProperty**](ibackgroundcopyjob5-getproperty.md)
</dt> </dl>

 

 





