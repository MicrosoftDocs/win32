---
title: IUpdateOrchestratorUpdate::Serialize method
description: The UpdateOrchestrator will call this method when it is saving the database for later deserialization.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::Serialize method

The UpdateOrchestrator will call this method when it is saving the database for later deserialization.


## Syntax
```cpp
HRESULT Serialize(
    [out, size_is(,*numBytes)] BYTE** bytes, 
    [out] DWORD* numBytes);
```

## Parameters

`bytes`

out pointer to a buffer. Caller needs to free the memory using CoTaskMemFree

`numBytes`

out pointer to the number of bytes in the buffer.

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks

The implementer should allocate the memory using CoTaskMemAllocation since UpdateOrchestrator will use CoTaskMemFree to free the memory.

## See Also

[IUpdateOrchestratorUpdate](iupdateorchestratorupdate.md)

[IUpdateOrchestratorUpdate::Pause](iupdateorchestratorupdate-pause.md)

[IUpdateOrchestratorUpdate::PerformAction](iupdateorchestratorupdate-performaction.md)