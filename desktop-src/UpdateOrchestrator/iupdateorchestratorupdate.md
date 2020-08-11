---
title: IUpdateOrchestratorUpdate interface
ms.date: 03/20/2020
ms.topic: interface
---

# IUpdateOrchestratorUpdate  interface

Implemented by the caller for each update the caller wishes to be called to complete. 

## Methods

|Method | Description |
|---|---|
|[IUpdateOrchestratorUpdate::get_UniqueId ](iupdateorchestratorupdate-uniqueid.md) | Get the updates unique id  |
|[IUpdateOrchestratorUpdate::get_Title ](iupdateorchestratorupdate-title.md) | Get the update title to display - note for now this is only going to be used for telemetry  |
|[IUpdateOrchestratorUpdate::get_Description ](iupdateorchestratorupdate-description.md) | Get the update description to display - future use for display  |
|[IUpdateOrchestratorUpdate::get_IsSecurity ](iupdateorchestratorupdate-issecurity.md) | Is this update a security update  |
|[IUpdateOrchestratorUpdate::get_Deadline ](iupdateorchestratorupdate-deadline.md) | What is the deadline for this update  |
|[IUpdateOrchestratorUpdate::get_Action ](iupdateorchestratorupdate-action.md) |Get the action that needs to be performed  |
|[IUpdateOrchestratorUpdate::PerformAction ](iupdateorchestratorupdate-performaction.md) |Perform the given action  |
|[IUpdateOrchestratorUpdate::Serialize ](iupdateorchestratorupdate-serialize.md) |Perform the given action  |
|[IUpdateOrchestratorUpdate::Pause ](iupdateorchestratorupdate-pause.md) |Pause the current action   |

## Requirements

|   |   |
|---|---|
| **Minimum supported client** | Windows 10 1903 |
|   |   |
