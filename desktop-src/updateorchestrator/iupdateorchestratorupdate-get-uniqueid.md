---
title: IUpdateOrchestratorUpdate::get_UniqueId method
description: Gets the update's unique Id.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::get_UniqueId method

Gets the update's unique Id.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdate::get_UniqueId(
    [out, retval] BSTR* uniqueId);
```

## Parameters

`uniqueId`


## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::get_Action](iupdateorchestratorupdate-get-action.md)

[IUpdateOrchestratorUpdate::get_Deadline](iupdateorchestratorupdate-get-deadline.md)

[IUpdateOrchestratorUpdate::get_Description](iupdateorchestratorupdate-get-description.md)

[IUpdateOrchestratorUpdate::get_IsSecurity](iupdateorchestratorupdate-get-issecurity.md)

[IUpdateOrchestratorUpdate::get_Title](iupdateorchestratorupdate-get-title.md)
