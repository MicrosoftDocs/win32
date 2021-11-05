---
title: IUpdateOrchestratorUpdate interface
description: Implemented by the caller for each update the caller wishes to be called to complete.
ms.date: 01/29/2020
ms.topic: interface
---

# IUpdateOrchestratorUpdate interface

Implemented by the caller for each update the caller wishes to be called to complete. 

## Methods

|Method | Description |
|---|---|
|[::get_Action](iupdateorchestratorupdate-get-action.md) | Gets the action that needs to be performed.  |
|[::get_Deadline](iupdateorchestratorupdate-get-deadline.md) | Gets the deadline for an update.  |
|[::get_Description](iupdateorchestratorupdate-get-description.md) | Gets the update’s description for telemetry and diagnostic purposes.  |
|[::get_IsSecurity](iupdateorchestratorupdate-get-issecurity.md) | Gets whether or not the update is a security update.  |
|[::get_Title](iupdateorchestratorupdate-get-title.md) | Gets the update's title for telemetry and diagnostic purposes.  |
|[::get_UniqueId](iupdateorchestratorupdate-get-uniqueid.md) | Gets the update's unique id.  |
|[::Pause](iupdateorchestratorupdate-pause.md) | Pauses the current action.   |
|[::PerformAction](iupdateorchestratorupdate-performaction.md) |Performs the given action.  |
|[::Serialize](iupdateorchestratorupdate-serialize.md) |Performs the given action.  |

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |
