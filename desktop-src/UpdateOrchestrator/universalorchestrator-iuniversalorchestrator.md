---
title: IUniversalOrchestrator interface
ms.date: 07/23/2019
ms.topic: interface
---

# IUniversalOrchestrator interface

> This API belongs to v1 of the Update Orchestrator API, previously known as Universal Orchestrator API.

**IUniversalOrchestrator** is a COM interface that provides the following methods to allow a client to communicate with the Universal Orchestrator.

## Methods

|Method | Description |
|---|---|
|[IUniversalOrchestrator::ScheduleWork](universalorchestrator-schedulework.md) | Registers pending work with the Universal Orchestrator. |
|[IUniversalOrchestrator::WorkCompleted](universalorchestrator-workcompleted.md) | Informs the Universal Orchestrator that all work is complete. |
|[IUniversalOrchestrator::HasMoratoriumPassed](universalorchestrator-hasmoratoriumpassed.md) | Queries Universal Orchestrator to determine if it is operating immediately after the new device Out of Box Experience. |


## Requirements

|   |   |
|---|---|
| **Minimum supported client** | Windows 10 1903 |
|   |   |