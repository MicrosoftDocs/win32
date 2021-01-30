---
title: IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates method
description: Scans for pending updates.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates method

Scans for pending updates.

## Syntax
```cpp
HRESULT ScanForPendingUpdates(
    [out, retval] IUpdateOrchestratorUpdateCollection** updateCollection;
```
## Parameters

`updateCollection`

an out parameter with the collection of found updates

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

The provider should return the collection of updates that it still needs to complete actions on. This method will be called by the UpdateOrchestrator in a cadence that is in accordance with the SLA. 

## See Also

[IUpdateOrchestratorUpdateProvider](iupdateorchestratorupdateprovider.md)

[IUpdateOrchestratorUpdateProvider::CancelScan](iupdateorchestratorupdateprovider-cancelscan.md)

[IUpdateOrchestratorUpdateProvider::Deserialize](iupdateorchestratorupdateprovider-deserialize.md)

[IUpdateOrchestratorUpdateProvider::get_ScanAttemptFrequencyInMinutes](iupdateorchestratorupdateprovider-scanattemptfrequencyinminutes.md)

[IUpdateOrchestratorUpdateProvider::get_ScanSlaInMinutes](iupdateorchestratorupdateprovider-scanslainminutes.md)
