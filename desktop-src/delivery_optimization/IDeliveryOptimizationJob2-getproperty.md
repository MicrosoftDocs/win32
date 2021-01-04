---
title: IDeliveryOptimizationJob2::GetProperty method
description: Returns a single property of the DO job.
keywords:
- GetProperty method
- GetProperty method, IDeliveryOptimizationJob2 interface
- IDeliveryOptimizationJob2 interface, GetProperty method
topic_type:
- apiref
api_name:
- IDeliveryOptimizationJob2.GetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/18/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationJob2::GetProperty method

This method returns a single property of the DO job.

## Syntax

```C++
HRESULT GetProperty(
  [in]  DOJobPropertyId propId,
  [out] VARIANT         *propValue
);
```

## Parameters

<dl> <dt>

*propId* \[in\]
</dt> <dd>

The required property ID to get. Only **DOJobPropertyId_ExtendedErrorInfo** of type VT_BSTR is supported.

</dd> <dt>

*propValue* \[out\]
</dt> <dd>

The resultant property value, stored in a VARIANT type.

</dd> </dl>

## Return value

This method returns the following HRESULT values.

| Return code                  | Description          |
|------------------------------|----------------------|
| **S_OK**                     | Success              |
| **DO_E_UNKNOWN_PROPERTY_ID** | Unknown property ID. |

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

[**IDeliveryOptimizationJob2**](ideliveryoptimizationjob2.md)
