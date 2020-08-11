---
title: IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates method
Scans for pending updates 

## Syntax
```cpp
HRESULT ScanForPendingUpdates(
    [out, retval] IUpdateOrchestratorUpdateCollection** updateCollection;
```
## Parameters

`updateCollection`

an out parameter with the collection of found updates

## Returns
Returns **S_OK** if successful, a failure otherwise.

## Remarks

The provider should return the collection of updates that it still needs to complete actions on. This method will be called daily by the UpdateOrchestrator.
