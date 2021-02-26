---
title: IDeliveryOptimizationFile2::SetProperty method
description: This method returns a single property of the DO file. | IDeliveryOptimizationFile2::SetProperty method
keywords:
- SetProperty method
- SetProperty method, IDeliveryOptimizationFile2 interface
- IDeliveryOptimizationFile2 interface, SetProperty method
topic_type:
- apiref
api_name:
- IDeliveryOptimizationFile2.SetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/18/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationFile2::SetProperty method

This method returns a single property of the DO file.

## Syntax

```C++
HRESULT SetProperty(
  [in]               DOFilePropertyId propId,
  [in, unique] const VARIANT          *propValue
);
```

## Parameters

<dl> <dt>

*propId* \[in\]
</dt> <dd>

The required property ID to set of type DOFilePropertyId.

</dd> <dt>

*propValue* \[in\]
</dt> <dd>

The property value to set, of type VARIANT.

</dd> </dl>

## Return value

This method returns the following HRESULT values.

| Return code                  | Description                                                        |
|------------------------------|--------------------------------------------------------------------|
| **S_OK**                     | Success                                                            |
| **DO_E_UNKNOWN_PROPERTY_ID** | Unknown property ID                                                |
| **DO_E_INVALID_STATE**       | The job is not currently in a state that allows a property setting |

## Requirements

| Requirement | Value |
|---------------------------|----------------------------------------------------------------------------------|
| Minimum supported client  | Windows 10, version 1803 \[desktop apps only\]                                   |
| Minimum supported server  | Windows Server, version 1709 \[desktop apps only\]                               |
| Header                    | Deliveryoptimization.h                                                           |
| IDL                       | DeliveryOptimization.idl                                                         |
| Library                   | Dosvc.lib                                                                        |
| DLL                       | Dosvc.dll                                                                        |
| IID                       | IID_IDeliveryOptimizationJob2 is defined as 18995A26-BF59-4ABE-9F8B-D5092D5A2405 |

## See also

[**IDeliveryOptimizationFile2**](ideliveryoptimizationfile2.md)
