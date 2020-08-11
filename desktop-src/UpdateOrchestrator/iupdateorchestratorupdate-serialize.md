---
title: IUpdateOrchestratorUpdate::Serialize method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorUpdate::Serialize method



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