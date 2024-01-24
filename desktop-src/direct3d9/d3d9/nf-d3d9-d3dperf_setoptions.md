---
title: D3DPERF_SetOptions function
description: Set profiler options specified by the target program.
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
- D3DPERF_SetOptions
targetos: Windows
---

# D3DPERF_SetOptions function

Set profiler options specified by the target program.

## Syntax

```cpp
int WINAPI D3DPERF_SetOptions(
  DWORD dwOptions
);
```

## Parameters

`dwOptions`

User options recognizable by PIX. Set this to 1 to notify PIX that the target program does not give permission to be profiled.

## Return value

This function doesn't return a value.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d9.h |
| **Library** | d3d9.lib |
| **DLL** | d3d9.dll |
