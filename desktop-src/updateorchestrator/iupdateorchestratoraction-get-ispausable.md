---
title: IUpdateOrchestratorAction::get_IsPausable method
description: Determines if an action can be paused. 
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorAction::get_IsPausable method

Determines if an action can be paused. 

## Syntax
```cpp
HRESULT IUpdateOrchestratorAction::get_IsPausable(
    [out, retval] BOOL* isPausable);
```

## Parameters

`isPausable`

Set to true if the action can be paused.

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorAction](iupdateorchestratoraction.md)

[IUpdateOrchestratorAction::get_ActionKind](iupdateorchestratoraction-get-actionkind.md)

[IUpdateOrchestratorAction::get_IsExclusive](iupdateorchestratoraction-get-isexclusive.md)

[IUpdateOrchestratorAction::get_Name](iupdateorchestratoraction-get-name.md)

[IUpdateOrchestratorAction::get_RequiresNetwork](iupdateorchestratoraction-get-requiresnetwork.md)