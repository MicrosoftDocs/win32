---
title: IUniversalOrchestrator::HasMoratoriumPassed
description: Queries Universal Orchestrator to determine if post-OOBE period has been surpassed.
ms.topic: method
ms.date: 01/14/2021
---

# IUniversalOrchestrator::HasMoratoriumPassed method

> [!NOTE] 
> This API belongs to the Universal Orchestrator API.

Allows clients to determine if Universal Orchestrator is operating immediately after the new device Out of Box Experience, which limits work attempts to minimize user interruption. 

## Syntax

```C++
HRESULT HasMoratoriumPassed(
  LPCWSTR callerIdentifier,
  BOOL*   moratoriumPassed);
```

## Parameters

`callerIdentifier`

A unique string that identifies all calls from this specific client.

`hasMoratoriumPassed`

Output parameter that stores the result of the query.

## Return value
If this method succeeds, it returns **S_OK**.  Otherwise, it returns an **HRESULT** error code.

## Requirements

| Requirement | Version |
|---|---|
| Minimum supported client | Windows 10 1903 |
|   |   |



 

 



