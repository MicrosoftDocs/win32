---
title: IUpdateOrchestratorUpdate interface
ms.date: 03/20/2020
ms.topic: interface
---

# IUpdateOrchestratorUpdate interface

Implemented by the caller for each update the caller wishes to be called to complete. 

## Methods

|Method | Description |
|---|---|
|[::get_Action](iupdateorchestratorupdate-get-action.md) |Get the action that needs to be performed.  |
|[::get_Deadline](iupdateorchestratorupdate-get-deadline.md) | What is the deadline for this update.  |
|[::get_Description](iupdateorchestratorupdate-get-description.md) | Get the update description to display - future use for display.  |
|[::get_IsSecurity](iupdateorchestratorupdate-get-issecurity.md) | Is this update a security update.  |
|[::get_Title](iupdateorchestratorupdate-get-title.md) | Get the update title to display - note for now this is only going to be used for telemetry.  |
|[::get_UniqueId](iupdateorchestratorupdate-get-uniqueid.md) | Get the updates unique id.  |
|[::Pause](iupdateorchestratorupdate-pause.md) |Pause the current action.   |
|[::PerformAction](iupdateorchestratorupdate-performaction.md) |Perform the given action.  |
|[::Serialize](iupdateorchestratorupdate-serialize.md) |Perform the given action.  |

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |
