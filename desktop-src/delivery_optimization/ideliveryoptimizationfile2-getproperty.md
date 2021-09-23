---
title: IDeliveryOptimizationFile2::GetProperty method
description: This method returns a single property of the Delivery Optimization file. | IDeliveryOptimizationFile2::GetProperty method
keywords:
- GetProperty method
- GetProperty method, IDeliveryOptimizationFile2 interface
- IDeliveryOptimizationFile2 interface, GetProperty method
topic_type:
- apiref
api_name:
- IDeliveryOptimizationFile2.GetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/18/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationFile2::GetProperty method

This method returns a single property of the Delivery Optimization file.

## Syntax

```C++
HRESULT GetProperty(
  [in]  DOFilePropertyId propId,
  [out] VARIANT          *propValue
);
```

## Parameters

<dl> <dt>

*propId* \[in\]
</dt> <dd>

The required property ID to get of type DOFilePropertyId.

</dd> <dt>

*propValue* \[out\]
</dt> <dd>

The property value stored in a VARIANT.

</dd> </dl>

## Return value

This method returns the following HRESULT values.

| Return code                  | Description                                         |
|------------------------------|-----------------------------------------------------|
| **S_OK**                     | Success                                             |
| **DO_E_UNKNOWN_PROPERTY_ID** | Unknown property ID.                                |
| **DO_E_WRITE_ONLY_PROPERTY** | The property is Write only and cannot be read.      |
| **E_NOT_SET**                | No property was set through the SetProperty method. |
| **E_OUTOFMEMORY**            |  Memory allocation failure                          |

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
