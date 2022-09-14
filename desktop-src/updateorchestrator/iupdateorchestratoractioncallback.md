---
title: IUpdateOrchestratorActionCallback interface
description: Callback interface supplied by the UpdateOrchestrator to the PerformAction method of the IUpdateOrchestratorUpdate object so that the UpdateOrchestratorUpdateProvider can provide progress and status on the state of the action.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorActionCallback interface

Callback interface supplied by the UpdateOrchestrator to the PerformAction method of the IUpdateOrchestratorUpdate object so that the UpdateOrchestratorUpdateProvider can provide progress and status on the state of the action. 

## Methods

|Method | Description |
|---|---|
|[::ReportCompleted](iupdateorchestratoractioncallback-reportcompleted.md) | Called when the action is complete, and has not failed.  |
|[::ReportFailed](iupdateorchestratoractioncallback-reportfailed.md) | Called if the action fails instead of completing.  |
|[::ReportProgress](iupdateorchestratoractioncallback-reportprogress.md) | Called to report progress.  |

## Remarks
The updater should call Complete when the action is done, or report a failure if the action cannot be completed.

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |