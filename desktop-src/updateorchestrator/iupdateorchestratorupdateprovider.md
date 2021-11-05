---
title: IUpdateOrchestratorUpdateProvider interface
description: This interface is implemented by the caller and is created using the CLSID provided to IUpdateOrchestrator::Register.
ms.date: 01/29/2020
ms.topic: interface
---

# IUpdateOrchestratorUpdateProvider interface

This interface is implemented by the caller and is created using the CLSID provided to IUpdateOrchestrator::Register. 

## Methods

|Method | Description |
|---|---|
|[::CancelScan](iupdateorchestratorupdateprovider-cancelscan.md) | Cancel a scan that is in progress.  |
|[::Deserialize](iupdateorchestratorupdateprovider-deserialize.md) | Deserialize the bytes into an update.  |
|[::get_ScanAttemptFrequencyInMinutes](iupdateorchestratorupdateprovider-scanattemptfrequencyinminutes.md) | Get the scan attempt frequency.  |
|[::ScanForPendingUpdates](iupdateorchestratorupdateprovider-scanforpendingupdates.md) | Scan for pending updates.  ||[::get_ScanSlaInMinutes](iupdateorchestratorupdateprovider-scanslainminutes.md) | Gets the Default Scan Sla.  |


## Remarks
USO (Windows Update Session Orchestrator) will call the provider daily in order to get the collection of updates the Updater wishes to perform.

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |