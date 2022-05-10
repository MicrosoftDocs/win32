---
title: IUpdateOrchestratorUpdate::Pause method
description: Called to pause the current action.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorUpdate::Pause method

Called to pause the current action.

## Syntax
```cpp
HRESULT Pause();
```

## Returns
Returns **S_OK** if the action could be paused and a failure if not.

## Remarks

This method should make a best effort to pause the update. It is ok to block until the update is paused if it can not be completed immediately.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::PerformAction](iupdateorchestratorupdate-performaction.md)

[IUpdateOrchestratorUpdate::Serialize](iupdateorchestratorupdate-serialize.md)