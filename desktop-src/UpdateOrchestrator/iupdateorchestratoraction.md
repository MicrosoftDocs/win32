---
title: IUpdateOrchestratorAction  interface
ms.date: 03/20/2020
ms.topic: interface
---

# IUpdateOrchestratorAction interface

Tells the UpdateOrchestrator about the next action to be performed on an update.

## Methods

|Method | Description |
|---|---|
|[IUpdateOrchestratorAction::get_ActionKind](iupdateorchestratoraction-actionkind.md) | Returns the action kind.  |
|[IUpdateOrchestratorAction::get_IsExclusive](iupdateorchestratoraction-isexclusive.md) | Determines if no two actions of its kind can be performed at the same time.  |
|[IUpdateOrchestratorAction::get_IsPausable](iupdateorchestratoraction-ispausable.md) | Determines if an action can be paused.  |
|[IUpdateOrchestratorAction::get_Name](iupdateorchestratoraction-name.md) | Returns the action name.  |
|[IUpdateOrchestratorAction::get_RequiresNetwork](iupdateorchestratoraction-requiresnetwork.md) | Determines if an action needs a network connection.  |

## Requirements

|   |   |
|---|---|
| **Minimum supported client** | Windows 10 1903 |
|   |   |
