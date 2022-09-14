---
title: D3DPERF_GetStatus function
description: Determine the current state of the profiler from the target program.
ms.topic: reference
ms.date: 04/06/2020
req.lib: d3d9.lib
req.dll: d3d9.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- d3d9.dll
api_name:
- D3DPERF_GetStatus
targetos: Windows
---

# D3DPERF_GetStatus function

Determine the current state of the profiler from the target program.

## Syntax

```cpp
DWORD WINAPI D3DPERF_GetStatus( void );
```

## Return value

A non-zero value when PIX is profiling the target program; otherwise, zero.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d9.h |
| **Library** | d3d9.lib |
| **DLL** | d3d9.dll |
