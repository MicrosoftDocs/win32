---
title: IUpdateOrchestratorUpdate::PerformAction method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::PerformAction method
Perform the given action.


## Syntax
```cpp
HRESULT PerformAction(
        [in] IUpdateOrchestratorAction* action,
        [in] IUpdateOrchestratorActionCallback* actionCallback);
```

## Parameters

`action`
the action to be performed.

`actionCallback`
callback to be called with progress, failures and when the action completes

## Returns
Returns **Returns **S_OK**** if the PerformAction was able to start the action, or a failure if not. 

If S_OK is returned then the UpdateOrchestrator will wait for either the Complete or Failed call on the callback supplied.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::Pause](iupdateorchestratorupdate-pause.md)

[IUpdateOrchestratorUpdate::Serialize](iupdateorchestratorupdate-serialize.md)