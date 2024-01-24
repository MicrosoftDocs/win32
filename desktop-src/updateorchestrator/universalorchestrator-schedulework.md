---
title: IUniversalOrchestrator::ScheduleWork
description: Calls Universal Orchestrator to schedule work
ms.topic: reference
ms.date: 01/14/2021
---

# IUniversalOrchestrator::ScheduleWork method

> [!NOTE] 
> This API belongs to the Universal Orchestrator API.

Allows clients to inform Universal Orchestrator that work is pending and provide a binary that will be called by Universal Orchestrator to perform the update work at a later time.

The callback binary must be signed with a valid Microsoft certificate, and the caller must be invoking the ScheduleWork call from SYSTEM context.

## Syntax

```C++
HRESULT ScheduleWork(
  LPCWSTR callerIdentifier,
  LPCWSTR cmdLine
  LPCWSTR startArg,
  LPCWSTR pauseArg);
```

## Parameters

`callerIdentifier`

A unique string that identifies all calls from this specific client.

`cmdLine`

The full path to the callback binary that will be invoked by Universal Orchestrator to perform work.

`startArg`

Parameters to pass to the callback binary to indicate Start is requested.

`pauseArg`

*(optional)* Parameters to pass to the callback binary to indicate Pause is requested.

## Return value
If this method succeeds, it returns **S_OK**.  Otherwise, it returns an **HRESULT** error code.

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |



 

 



