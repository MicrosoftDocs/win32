---
title: IUniversalOrchestrator::WorkCompleted
Description: Calls Universal Orchestrator to indicate work is complete
ms.topic: method
ms.date: 03/20/2020
---

# IUniversalOrchestrator::WorkCompleted method

> This API belongs to v1 of the Update Orchestrator API, previously known as Universal Orchestrator API.

Allows clients to inform Universal Orchestrator that the previously scheduled work has been completed and stop callbacks to perform work until the next successful ScheduleWork call.

## Syntax

```C++
HRESULT WorkCompleted(
  LPCWSTR callerIdentifier,
  BOOL    workCompleted);
```

## Parameters

`callerIdentifier`

A unique string that identifies all calls from this specific client.

`workCompleted`

**TRUE** if the work successfully completed. Otherwise, **FALSE** if the work attempt failed and should be retried in the future. 

## Return value
If this method succeeds, it returns **S_OK**.  Otherwise, it returns an **HRESULT** error code.

## Requirements

|   |   |
|---|---|
| **Minimum supported client** | Windows 10 1903 |
|   |   |



 

 



