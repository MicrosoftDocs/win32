---
title: IUpdateOrchestratorUpdate::Pause method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::Pause method
Called to pause the current action.



## Syntax
```cpp
HRESULT Pause();
```

## Returns
Returns **Returns **S_OK**** if the action could be paused and a failure if not.

## Remarks

This method should make a best effort to pause the update. It is ok to block until the update is paused if it can not be completed immediately.