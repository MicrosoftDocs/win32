---
title: IUpdateOrchestratorUpdateProvider::get_ScanAttempFrequencyInMinutes method
description: Get the scan attempt frequency.
ms.date: 12/01/2020
ms.topic: method
---

# IUpdateOrchestratorUpdateProvider::get_ScanAttempFrequencyInMinutes method

Get the scan attempt frequency.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdateProvider::get_ScanAttempFrequencyInMinutes(
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