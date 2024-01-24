---
title: IUpdateOrchestratorUpdate::get_Description method
description: Gets the update’s description for telemetry and diagnostic purposes.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorUpdate::get_Description method

Gets the update’s description for telemetry and diagnostic purposes.

## Syntax
```cpp
HRESULT IUpdateOrchestratorUpdate::get_Description(
    [out, retval] BSTR* description);
```

## Parameters

`description`

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

This is only going to be used for telemetry.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::get_Action](iupdateorchestratorupdate-get-action.md)

[IUpdateOrchestratorUpdate::get_Deadline](iupdateorchestratorupdate-get-deadline.md)

[IUpdateOrchestratorUpdate::get_IsSecurity](iupdateorchestratorupdate-get-issecurity.md)

[IUpdateOrchestratorUpdate::get_Title](iupdateorchestratorupdate-get-title.md)

[IUpdateOrchestratorUpdate::get_UniqueId](iupdateorchestratorupdate-get-uniqueid.md)
