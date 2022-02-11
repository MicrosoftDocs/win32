---
title: IUpdateOrchestratorUpdateProvider::get_ScanAttemptFrequencyInMinutes method
description: Get the scan attempt frequency.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorUpdateProvider::get_ScanAttemptFrequencyInMinutes method

Gets the scan attempt frequency.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdateProvider::get_ScanAttemptFrequencyInMinutes(
    [out, retval] DWORD* frequencyInMinutes);
```
## Parameters

`frequencyInMinutes`

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

Gets the Default Scan Attempt Frequency which is the minimum amount of time we should wait between Scan attempts.

## See Also

[IUpdateOrchestratorUpdateProvider](iupdateorchestratorupdateprovider.md)

[IUpdateOrchestratorUpdateProvider::CancelScan](iupdateorchestratorupdateprovider-cancelscan.md)

[IUpdateOrchestratorUpdateProvider::Deserialize](iupdateorchestratorupdateprovider-deserialize.md)

[IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates](iupdateorchestratorupdateprovider-scanforpendingupdates.md) 

[IUpdateOrchestratorUpdateProvider::get_ScanSlaInMinutes](iupdateorchestratorupdateprovider-scanslainminutes.md)