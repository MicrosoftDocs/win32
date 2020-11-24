---
title: IUpdateOrchestratorAction::get_ActionKind method
description: Returns the action kind.
ms.date: 12/01/2020
ms.topic: method
---

# IUpdateOrchestratorAction::get_ActionKind method

Returns the action kind.

## Syntax
```cpp
IUpdateOrchestratorAction::get_ActionKind(
    [out, retval] UPDATE_ORCHESTRATOR_ACTION_KIND* actionKind);
```

## Parameters

`actionKind`

Displays the status of an update. For a list of possible values, see the [UPDATE_ORCHESTRATOR_ACTION_KIND](updateorchestratoractionkind.md) enumeration.

## Returns

## See Also

[IUpdateOrchestratorAction](iupdateorchestratoraction.md)

[IUpdateOrchestratorAction::get_IsExclusive](iupdateorchestratoraction-get-isexclusive.md)

[IUpdateOrchestratorAction::get_IsPausable](iupdateorchestratoraction-get-ispausable.md)

[IUpdateOrchestratorAction::get_Name](iupdateorchestratoraction-get-name.md)

[IUpdateOrchestratorAction::get_RequiresNetwork](iupdateorchestratoraction-get-requiresnetwork.md)
