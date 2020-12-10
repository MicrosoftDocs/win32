---
title: IDeliveryOptimizationJob2::SetProperty method
description: This method is unused.
keywords:
- SetProperty method
- SetProperty method, IDeliveryOptimizationJob2 interface
- IDeliveryOptimizationJob2 interface, SetProperty method
topic_type:
- apiref
api_name:
- IDeliveryOptimizationJob2.SetProperty
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/18/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationJob2::SetProperty method

This method is unused.

## Syntax

```C++
HRESULT SetProperty(
  [in]               DOJobPropertyId propId,
  [in, unique] const VARIANT         *propValue
);
```

## Parameters

<dl> <dt>

*propId* \[in\]
</dt> <dd>

Unused.

</dd> <dt>

*propValue* \[in\]
</dt> <dd>

Unused.

</dd> </dl>

## Return value

If propId is **DOJobPropertyId_ExtendedErrorInfo**, the returned value is **DO_E_READ_ONLY_PROPERTY**, otherwise the function returns **DO_E_UNKNOWN_PROPERTY_ID**.

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
