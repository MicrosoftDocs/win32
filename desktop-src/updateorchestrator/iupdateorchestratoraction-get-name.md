---
title: IUpdateOrchestratorAction::get_Name method
description: Returns the action name string.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorAction::get_Name method

Returns the action name string.

## Syntax
```cpp
HRESULT IUpdateOrchestratorAction::get_Name(
    [out, retval] BSTR* name);
```

## Parameters

`name`

The action name string.

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorAction](iupdateorchestratoraction.md)

[IUpdateOrchestratorAction::get_ActionKind](iupdateorchestratoraction-get-actionkind.md)

[IUpdateOrchestratorAction::get_IsExclusive](iupdateorchestratoraction-get-isexclusive.md)

[IUpdateOrchestratorAction::get_IsPausable](iupdateorchestratoraction-get-ispausable.md)

[IUpdateOrchestratorAction::get_RequiresNetwork](iupdateorchestratoraction-get-requiresnetwork.md)