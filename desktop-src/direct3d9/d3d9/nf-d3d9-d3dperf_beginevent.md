---
title: D3DPERF_BeginEvent function
description: Marks the beginning of a user-defined event. PIX can use this event to trigger an action.
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
- D3DPERF_BeginEvent
targetos: Windows
---

# D3DPERF_BeginEvent function

Marks the beginning of a user-defined event. PIX can use this event to trigger an action.

## Syntax

```cpp
int WINAPI D3DPERF_BeginEvent(
  D3DCOLOR col,
  LPCWSTR wszName
);
```

## Parameters

`col`

Event color. This is the color to display the event in the event view.

`wszName`

Event name.

## Return value

The zero-based level of the hierarchy that this event is starting in. If an error occurs, the return value will be negative.

## Remarks

User-defined events group together other events in a way that is meaningful to the target program so that they can be better represented in performance profiling tools. For example, a *Draw Spaceship* event might bracket a number of Direct3D calls that handle drawing a spaceship in a game. Events can be nested.

Each **D3DPERF_BeginEvent** call should have a matching **D3DPERF_EndEvent** call. Instantaneous events (which do not bracket other events) should be labeled by using **D3DPERF_SetMarker** rather than by **D3DPERF_BeginEvent** and **D3DPERF_EndEvent**.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d9.h |
| **Library** | d3d9.lib |
| **DLL** | d3d9.dll |
