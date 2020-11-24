---
title: IUpdateOrchestratorActionCallback::ReportFailed method
description: Called if the action fails instead of completing.
ms.date: 12/01/2020
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

## See Also

[IUpdateOrchestratorActionCallback](iupdateorchestratoractioncallback.md)

[IUpdateOrchestratorActionCallback::ReportCompleted](iupdateorchestratoractioncallback-reportcompleted.md)

[IUpdateOrchestratorActionCallback::ReportProgress](iupdateorchestratoractioncallback-reportprogress.md)