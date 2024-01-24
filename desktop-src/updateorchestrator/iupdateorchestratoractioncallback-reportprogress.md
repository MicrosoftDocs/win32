---
title: IUpdateOrchestratorActionCallback::ReportProgress method
description: Called to report progress.
ms.date: 01/29/2020
ms.topic: reference
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
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorActionCallback](iupdateorchestratoractioncallback.md)

[IUpdateOrchestratorActionCallback::ReportCompleted](iupdateorchestratoractioncallback-reportcompleted.md)

[IUpdateOrchestratorActionCallback::ReportFailed](iupdateorchestratoractioncallback-reportfailed.md)
