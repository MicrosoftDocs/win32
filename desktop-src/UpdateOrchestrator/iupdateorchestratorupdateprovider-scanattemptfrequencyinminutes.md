---
title: IUpdateOrchestratorUpdateProvider::get_ScanAttempFrequencyInMinutes method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorUpdateProvider::get_ScanAttempFrequencyInMinutes method

Get the scan attempt frequency.

## Syntax
```cpp
IUpdateOrchestratorUpdateProvider::get_ScanAttempFrequencyInMinutes(
    [out, retval] DWORD* frequencyInMinutes);
```
## Parameters

`frequencyInMinutes`

## Returns

## Remarks

Gets the Default Scan Attempt Frequency which is the minimum amount of time we should wait between Scan attempts.

## See Also

[IUpdateOrchestratorUpdateProvider](iupdateorchestratorupdateprovider.md)

[IUpdateOrchestratorUpdateProvider::CancelScan](iupdateorchestratorupdateprovider-cancelscan.md)

[IUpdateOrchestratorUpdateProvider::Deserialize](iupdateorchestratorupdateprovider-deserialize.md)

[IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates](iupdateorchestratorupdateprovider-scanforpendingupdates.md) 

[IUpdateOrchestratorUpdateProvider::ScanSlaInMinutes](iupdateorchestratorupdateprovider-scanslainminutes.md)