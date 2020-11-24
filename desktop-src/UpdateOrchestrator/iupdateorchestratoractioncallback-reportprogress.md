---
title: IUpdateOrchestratorActionCallback::ReportProgress method
description: Called to report progress.
ms.date: 12/01/2020
ms.topic: method
---

# IUpdateOrchestratorActionCallback::ReportProgress method

Called to report progress.

## Syntax
```cpp
HRESULT ReportProgress(
    [in] BYTE percentComplete);
```

## Parameters

`percentComplete`

The percent complete with the action.

## Returns

## See Also

[IUpdateOrchestratorActionCallback](iupdateorchestratoractioncallback.md)

[IUpdateOrchestratorActionCallback::ReportCompleted](iupdateorchestratoractioncallback-reportcompleted.md)

[IUpdateOrchestratorActionCallback::ReportFailed](iupdateorchestratoractioncallback-reportfailed.md)
