---
title: IUpdateOrchestratorAction::get_IsExclusive method
description: Determines if no two actions of its kind can be performed at the same time.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorAction::get_IsExclusive method

Determines if no two actions of its kind can be performed at the same time.

## Syntax
```cpp
HRESULT IUpdateOrchestratorAction::get_IsExclusive(
    [out, retval] BOOL* isExclusive);
```

## Parameters

`isExclusive`

Set to true if no two actions of this kind can be performed at the same time. 

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorAction](iupdateorchestratoraction.md)

[IUpdateOrchestratorAction::get_ActionKind](iupdateorchestratoraction-get-actionkind.md)

[IUpdateOrchestratorAction::get_IsPausable](iupdateorchestratoraction-get-ispausable.md)

[IUpdateOrchestratorAction::get_Name](iupdateorchestratoraction-get-name.md)

[IUpdateOrchestratorAction::get_RequiresNetwork](iupdateorchestratoraction-get-requiresnetwork.md)