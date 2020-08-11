---
title: IUpdateOrchestratorActionCallback::ReportFailed method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorActionCallback::ReportFailed method
Called if the action fails instead of completing.

## Syntax
```cpp
HRESULT ReportFailed(
    [in] HRESULT actionHr);
```

## Parameters

`actionHr`

The failure code.

## Returns