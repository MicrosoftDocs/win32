---
title: IUpdateOrchestrator interface
description: The caller should use this interface to register their updater CLSID for work.
ms.date: 01/29/2020
ms.topic: interface
---

# IUpdateOrchestrator interface

The caller should use this interface to register their updater CLSID for work.

## Methods

|Method | Description |
|---|---|
|[::RegisterProvider](iupdateorchestrator-registerprovider.md) | Registers the update provider with the given CLSID.  |
|[::UnregisterProvider](iupdateorchestrator-unregisterprovider.md) | Unregisters the given update provider.  |

## Remarks
Once registered, the USO (Windows Update Session Orchestrator) will create the IUpdateOrchestratorUpdateProvider and attempt a scan on it. 

At this point, the updater should determine if it has updates that need work and return the collection of them. At an appropriate time to do work, the UpdateOrchestrator will call the updates supplied to perform the work.

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |