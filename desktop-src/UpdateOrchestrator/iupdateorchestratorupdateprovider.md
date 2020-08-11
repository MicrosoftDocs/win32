---
title: IUpdateOrchestratorUpdateProvider interface
ms.date: 03/20/2020
ms.topic: interface
---

# IUpdateOrchestratorUpdateProvider interface

Enumerates the keys in the registry location and creates an Update for each entry.

## Methods

|Method | Description |
|---|---|
|[IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates ](iupdateorchestratorupdateprovider-scanforpendingupdates.md) | Scan for pending updates.  |
|[IUpdateOrchestratorUpdateProvider::CancelScan ](iupdateorchestratorupdateprovider-cancelscan.md) | cancel a scan that is in progress.  |
|[IUpdateOrchestratorUpdateProvider::Deserialize ](iupdateorchestratorupdateprovider-deserialize.md) | Deserialize the bytes into an update.  |
|[IUpdateOrchestratorUpdateProvider::ScanAttempFrequencyInMinutes ](iupdateorchestratorupdateprovider-scanattemptfrequencyinminutes.md) | Get the scan attempt frequency.  |
|[IUpdateOrchestratorUpdateProvider::ScanSlaInMinutes ](iupdateorchestratorupdateprovider-scanslainminutes.md) | Gets the Default Scan Sla.  |


## Remarks
This interface is implemented by the caller and is created
using the CLSID provided to IUpdateOrchestrator::Register. 

USO (Windows Update Session Orchestrator) will call the provider daily in order to get the collection of updates the Updater wishes to perform.

## Requirements

|   |   |
|---|---|
| **Minimum supported client** | Windows 10 1903 |
|   |   |