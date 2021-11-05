---
title: IUpdateOrchestratorUpdateCollection interface
description: A collection of IUpdateOrchestratorUpdate updates returned by the provider when a Scan is done.
ms.date: 01/29/2020
ms.topic: interface
---

# IUpdateOrchestratorUpdateCollection  interface

A collection of IUpdateOrchestratorUpdate updates returned by the provider when a Scan is done.

## Methods

|Method | Description |
|---|---|
|[::get_Count](iupdateorchestratorupdatecollection-get-count.md) | Get the number of updates contained in the collection.  |
|[::get_Item](iupdateorchestratorupdatecollection-get-item.md) | Get the update with the given index.  |


## Remarks
These are the set of updates that the UpdateOrchestratorProvider wishes to perform actions on. The UpdateOrchestrator will call PerformAction at an appropriate time.

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |
