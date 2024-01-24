---
title: IUpdateOrchestratorAction::get_RequiresNetwork method
description: Determines if an action needs a network connection.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorAction::get_RequiresNetwork method

Determines if an action needs a network connection.

## Syntax
```cpp
HRESULT IUpdateOrchestratorAction::get_RequiresNetwork(
    [out, retval] BOOL* requiresNetwork);
```

## Parameters

`requiresNetwork`

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorAction](iupdateorchestratoraction.md)

[IUpdateOrchestratorAction::get_ActionKind](iupdateorchestratoraction-get-actionkind.md)

[IUpdateOrchestratorAction::get_IsExclusive](iupdateorchestratoraction-get-isexclusive.md)

[IUpdateOrchestratorAction::get_IsPausable](iupdateorchestratoraction-get-ispausable.md)

[IUpdateOrchestratorAction::get_Name](iupdateorchestratoraction-get-name.md)