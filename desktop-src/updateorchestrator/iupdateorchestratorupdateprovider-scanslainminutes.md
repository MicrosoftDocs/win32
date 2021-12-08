---
title: IUpdateOrchestratorUpdateProvider::get_ScanSlaInMinutes method
description: Gets the default Scan SLA. This value is how often the provider wishes to have a successful scan.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorUpdateProvider::get_ScanSlaInMinutes method

Gets the default Scan SLA. This value is how often the provider wishes to have a successful scan.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdateProvider::get_ScanSlaInMinutes(
    [out, retval] DWORD* slaInMinutes);
```
## Parameters

`slaInMinutes`


## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

## See Also

[IUpdateOrchestratorUpdateProvider](iupdateorchestratorupdateprovider.md)

[IUpdateOrchestratorUpdateProvider::CancelScan](iupdateorchestratorupdateprovider-cancelscan.md)

[IUpdateOrchestratorUpdateProvider::Deserialize](iupdateorchestratorupdateprovider-deserialize.md)

[IUpdateOrchestratorUpdateProvider::get_ScanAttemptFrequencyInMinutes](iupdateorchestratorupdateprovider-scanattemptfrequencyinminutes.md)

[IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates](iupdateorchestratorupdateprovider-scanforpendingupdates.md) 
