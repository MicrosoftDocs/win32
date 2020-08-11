---
title: IUpdateOrchestratorActionCallback interface
ms.date: 03/20/2020
ms.topic: interface
---

# IUpdateOrchestratorActionCallback interface

Callback interface supplied by the UpdateOrchestrator to the PerformAction method of the user's IUpdateOrchestratorUpdate object. 

## Methods

|Method | Description |
|---|---|
|[IUpdateOrchestratorActionCallback::ReportCompleted ](iupdateorchestratoractioncallback-reportcompleted.md) | Called when the action is complete, and has not failed.  |
|[IUpdateOrchestratorActionCallback::ReportFailed ](iupdateorchestratoractioncallback-reportfailed.md) | Called if the action fails instead of completing.  |
|[IUpdateOrchestratorActionCallback::ReportProgress ](iupdateorchestratoractioncallback-reportprogress.md) | Called to report progress.  |

## Remarks
The updater should call Complete when the action is done, or report a failure if the action cannot be completed.

## Requirements

|   |   |
|---|---|
| **Minimum supported client** | Windows 10 1903 |
|   |   |