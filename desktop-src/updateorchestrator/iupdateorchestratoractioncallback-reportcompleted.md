---
title: IUpdateOrchestratorActionCallback::ReportCompleted method
description: Called when the action is complete and has not failed.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorActionCallback::ReportCompleted method

Called when the action is complete and has not failed.

## Syntax
```cpp
HRESULT ReportCompleted();
```

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code. 

If [IUpdateOrchestratorUpdate::PerformAction](iupdateorchestratorupdate-performaction.md) returns S_OK, it will wait until either IUpdateOrchestratorActionCallback::ReportCompleted or [IUpdateOrchestratorActionCallback::ReportFailed](iupdateorchestratoractioncallback-reportfailed.md) is called.

## See Also

[IUpdateOrchestratorActionCallback](iupdateorchestratoractioncallback.md)

[IUpdateOrchestratorActionCallback::ReportFailed](iupdateorchestratoractioncallback-reportfailed.md)

[IUpdateOrchestratorActionCallback::ReportProgress](iupdateorchestratoractioncallback-reportprogress.md)