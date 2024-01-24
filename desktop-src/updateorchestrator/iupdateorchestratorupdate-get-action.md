---
title: IUpdateOrchestratorUpdate::get_Action method
description: Gets the action that needs to be performed.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorUpdate::get_Action method

Gets the action that needs to be performed.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdate::get_Action(
    [out, retval] IUpdateOrchestratorAction** action);
```

## Parameters

`action`


## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::get_Deadline](iupdateorchestratorupdate-get-deadline.md)

[IUpdateOrchestratorUpdate::get_Description](iupdateorchestratorupdate-get-description.md)

[IUpdateOrchestratorUpdate::get_IsSecurity](iupdateorchestratorupdate-get-issecurity.md)

[IUpdateOrchestratorUpdate::get_Title](iupdateorchestratorupdate-get-title.md)

[IUpdateOrchestratorUpdate::get_UniqueId](iupdateorchestratorupdate-get-uniqueid.md)
