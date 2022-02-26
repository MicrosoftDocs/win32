---
title: D3DPERF_EndEvent function
description: Marks the end of a user-defined event. PIX can use this event to trigger an action.
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
- D3DPERF_EndEvent
targetos: Windows
---

# D3DPERF_EndEvent function

Marks the end of a user-defined event. PIX can use this event to trigger an action.

## Syntax

```cpp
int WINAPI D3DPERF_EndEvent(void);
```

## Return value

The level of the hierarchy in which the event is ending. If an error occurs, this value is negative.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d9.h |
| **Library** | d3d9.lib |
| **DLL** | d3d9.dll |
