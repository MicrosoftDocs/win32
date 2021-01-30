---
title: IUpdateOrchestratorUpdate::get_Deadline method
description: Gets the deadline for an update.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::get_Deadline method

Gets the deadline for an update.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdate::get_Deadline(
    [out, retval] FILETIME* deadline);
```

## Parameters

`deadline`


## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::get_Action](iupdateorchestratorupdate-get-action.md)

[IUpdateOrchestratorUpdate::get_Description](iupdateorchestratorupdate-get-description.md)

[IUpdateOrchestratorUpdate::get_IsSecurity](iupdateorchestratorupdate-get-issecurity.md)

[IUpdateOrchestratorUpdate::get_Title](iupdateorchestratorupdate-get-title.md)

[IUpdateOrchestratorUpdate::get_UniqueId](iupdateorchestratorupdate-get-uniqueid.md)
