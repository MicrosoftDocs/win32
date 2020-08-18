---
title: IUpdateOrchestratorActionCallback::ReportProgress method
ms.date: 03/20/2020
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
