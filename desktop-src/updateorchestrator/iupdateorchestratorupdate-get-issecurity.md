---
title: IUpdateOrchestratorUpdate::get_IsSecurity method
description: Gets whether or not the update is a security update.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::get_IsSecurity method

Gets whether or not the update is a security update.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdate::get_IsSecurity(
    [out, retval] BOOL* isSecurity);
```

## Parameters

`isSecurity`

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::get_Action](iupdateorchestratorupdate-get-action.md)

[IUpdateOrchestratorUpdate::get_Deadline](iupdateorchestratorupdate-get-deadline.md)

[IUpdateOrchestratorUpdate::get_Description](iupdateorchestratorupdate-get-description.md)

[IUpdateOrchestratorUpdate::get_Title](iupdateorchestratorupdate-get-title.md)

[IUpdateOrchestratorUpdate::get_UniqueId](iupdateorchestratorupdate-get-uniqueid.md)
