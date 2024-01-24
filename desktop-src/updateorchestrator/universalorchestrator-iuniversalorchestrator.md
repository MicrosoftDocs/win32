---
title: IUniversalOrchestrator interface
description: A COM interface that provides methods to allow a client to communicate with the Universal Orchestrator.
ms.date: 01/14/2021
ms.topic: reference
---

# IUniversalOrchestrator interface

> [!NOTE] 
> This API belongs to the Universal Orchestrator API.

**IUniversalOrchestrator** is a COM interface that provides the following methods to allow a client to communicate with the Universal Orchestrator.

## Methods

|Method | Description |
|---|---|
|[::ScheduleWork](universalorchestrator-schedulework.md) | Registers pending work with the Universal Orchestrator. |
|[::WorkCompleted](universalorchestrator-workcompleted.md) | Informs the Universal Orchestrator that all work is complete. |
|[::HasMoratoriumPassed](universalorchestrator-hasmoratoriumpassed.md) | Queries Universal Orchestrator to determine if it is operating immediately after the new device Out of Box Experience. |


## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |