---
title: IUpdateOrchestratorUnlock::Unlock method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorUnlock::Unlock method


## Syntax
```cpp
HRESULT Unlock(
    [in] LPCWSTR token);
```
## Parameters

`token`

## Returns
Returns **S_OK** if the instance was unlocked and has permission to the methods in IUpdateOrchestrator.

## Remarks

This routine must be called on the object before access the functions in IUpdateOrchestrator are available.
