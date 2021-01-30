---
title: IUpdateOrchestratorActionCallback::ReportFailed method
description: Called if the action fails instead of completing.
ms.date: 01/29/2020
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
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

If [IUpdateOrchestratorUpdate::PerformAction](iupdateorchestratorupdate-performaction.md) returns S_OK, it will wait until either [IUpdateOrchestratorActionCallback::ReportCompleted](iupdateorchestratoractioncallback-reportcompleted.md) or IUpdateOrchestratorActionCallback::ReportFailed is called.

## See Also

[IUpdateOrchestratorActionCallback](iupdateorchestratoractioncallback.md)

[IUpdateOrchestratorActionCallback::ReportCompleted](iupdateorchestratoractioncallback-reportcompleted.md)

[IUpdateOrchestratorActionCallback::ReportProgress](iupdateorchestratoractioncallback-reportprogress.md)