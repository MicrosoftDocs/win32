---
title: IDeliveryOptimizationFile GetStats method (Deliveryoptimization.h)
description: Returns download and upload stats for a specific file.
ms.assetid: 8A3AD658-F1AD-4EA5-B010-AB7B88126FD6
keywords:
- GetStats method
- GetStats method, IDeliveryOptimizationFile interface
- IDeliveryOptimizationFile interface, GetStats method
topic_type:
- apiref
api_name:
- IDeliveryOptimizationFile.GetStats
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationFile::GetStats method

Returns download and upload stats for a specific file.

## Syntax


```C++
HRESULT GetStats(
  [out] DOSwarmStats *swarmStats
);
```



## Parameters

<dl> <dt>

*swarmStats* \[out\]
</dt> <dd>

Returns download and upload stats for a specific file. See the [**DOSwarmStats**](doswarmstats.md) structure for details.

</dd> </dl>

## Return value

This method should return **S_OK**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IDeliveryOptimizationFile is defined as B76B9699-E99E-4101-803F-A20E325D93E2<br/>        |



## See also

<dl> <dt>

[**IDeliveryOptimizationFile**](ideliveryoptimizationfile.md)
</dt> </dl>

 

 





