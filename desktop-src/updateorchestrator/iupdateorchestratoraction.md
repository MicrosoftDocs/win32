---
title: IUpdateOrchestratorAction  interface
description: Tells the UpdateOrchestrator about the next action to be performed on an update.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorAction interface

Tells the UpdateOrchestrator about the next action to be performed on an update.

## Methods

|Method | Description |
|---|---|
|[::get_ActionKind](iupdateorchestratoraction-get-actionkind.md) | Returns the action kind.  |
|[::get_IsExclusive](iupdateorchestratoraction-get-isexclusive.md) | Determines if no two actions of its kind can be performed at the same time.  |
|[::get_IsPausable](iupdateorchestratoraction-get-ispausable.md) | Determines if an action can be paused.  |
|[::get_Name](iupdateorchestratoraction-get-name.md) | Returns the action name.  |
|[::get_RequiresNetwork](iupdateorchestratoraction-get-requiresnetwork.md) | Determines if an action needs a network connection.  |

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |
