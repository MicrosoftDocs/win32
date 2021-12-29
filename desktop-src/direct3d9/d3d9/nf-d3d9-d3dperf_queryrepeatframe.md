---
title: D3DPERF_QueryRepeatFrame function
description: Determine whether a performance profiler is requesting that the current frame be resubmitted to Direct3D for performance analysis. This function is not currently supported by PIX.
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
- D3DPERF_QueryRepeatFrame
targetos: Windows
---

# D3DPERF_QueryRepeatFrame function

Determine whether a performance profiler is requesting that the current frame be resubmitted to Direct3D for performance analysis. This function is not currently supported by PIX.

## Syntax

```cpp
BOOL WINAPI D3DPERF_QueryRepeatFrame( void );
```

## Return value

If the return value is TRUE, the caller should repeat the same sequence of calls. If FALSE, the caller should continue.

## Remarks

The function should be called immediately after **IDirect3DDevice9::Present** is called.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d9.h |
| **Library** | d3d9.lib |
| **DLL** | d3d9.dll |
