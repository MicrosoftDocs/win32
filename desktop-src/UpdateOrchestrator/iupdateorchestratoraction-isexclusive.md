---
title: IUpdateOrchestratorAction::get_IsExclusive method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorAction::get_IsExclusive method
Determines if no two actions of its kind can be performed at the same time.

## Syntax
```cpp
IUpdateOrchestratorAction::get_IsExclusive(
    [out, retval] BOOL* isExclusive);
```

## Parameters

`isExclusive`

Set to true if no two actions of this kind can be performed at the same time. 

## Returns
