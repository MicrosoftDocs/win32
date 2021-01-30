---
title: IUpdateOrchestratorUpdate::PerformAction method
description: Performs the given action.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::PerformAction method

Performs the given action.

## Syntax
```cpp
HRESULT PerformAction(
        [in] IUpdateOrchestratorAction* action,
        [in] IUpdateOrchestratorActionCallback* actionCallback);
```

## Parameters

`action`
the action to be performed.

`actionCallback`
callback to be called with progress, failures and when the action completes.

## Returns
Returns **S_OK** if the PerformAction was able to start the action, or a failure if not. 

If S_OK is returned, then the Update Orchestrator will wait until either [IUpdateOrchestratorActionCallback::ReportCompleted](iupdateorchestratoractioncallback-reportcompleted.md) or [IUpdateOrchestratorActionCallback::ReportFailed](iupdateorchestratoractioncallback-reportfailed.md) is called. If an HRESULT error is returned instead, the Update Orchestrator was not able to start the given action and thus will not wait for ReportCompleted or ReportFailed.

## Remarks

Update Orchestrator will keep the machine awake to perform updates until PerformAction is called and returns either S_OK, ReportCompleted or ReportFailed.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::Pause](iupdateorchestratorupdate-pause.md)

[IUpdateOrchestratorUpdate::Serialize](iupdateorchestratorupdate-serialize.md)