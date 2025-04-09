---
UID: NF:winuser.GetCurrentMonitorTopologyId
description: Retrieves the ID of the current monitor topology.
tech.root: winmsg
title: GetCurrentMonitorTopologyId function
ms.topic: reference
ms.date: 10/28/2024
req.lib: 
req.dll: User32.dll
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - GetCurrentMonitorTopologyId
f1_keywords:
 - GetCurrentMonitorTopologyId
 - winuser/GetCurrentMonitorTopologyId
dev_langs:
 - c++
helpviewer_keywords:
 - GetCurrentMonitorTopologyId
targetos: Windows
ms.localizationpriority: low
---

# GetCurrentMonitorTopologyId function

Retrieves the ID of the current monitor topology.

## Syntax

```cpp
UINT GetCurrentMonitorTopologyId();
```

## Return value

Type: **UINT**

ID of the current monitor topology.

## Remarks

> [!TIP]
> At this time, this function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`User32.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

The value returned from **GetCurrentMonitorTopologyId** will be different any time the monitor topology changes. It is also guaranteed to never return **INVALID_MONITOR_TOPOLOGY_ID**. The monitor topology changes when:
- A monitor is added or removed.
	- The number of monitors can be queried using <a href="/windows/desktop/api/winuser/nf-winuser-getsystemmetrics">GetSystemMetrics</a> with <b>SM_CMONITORS</b>.
- A monitor’s display rectangle changes.
	- A monitor’s rectangle can be obtained by calling <a href="/windows/desktop/api/winuser/ns-winuser-monitorinfo">GetMonitorInfo</a> and then checking the value of rcMonitor on the <a href="/windows/desktop/api/winuser/ns-winuser-monitorinfo">MONITORINFO</a> returned.
- A monitor’s work area rectangle changes
	- A monitor’s work area can be obtained by calling <a href="/windows/desktop/api/winuser/nf-winuser-getmonitorinfoa">GetMonitorInfo</a> and then checking the value of rcWork on the <a href="/windows/desktop/api/winuser/ns-winuser-monitorinfo">MONITORINFO</a> returned.
- A monitor’s DPI changes
	- The DPI of a monitor can be obtained by calling <a href="/windows/desktop/api/shellscalingapi/nf-shellscalingapi-getdpiformonitor">GetDpiForMonitor</a>.
- A monitor’s handle changes
	- The monitor’s handle can be obtained with <a href="/windows/desktop/api/winuser/nf-winuser-enumdisplaymonitors">EnumDisplayMonitors</a>
-A monitor’s name changes
	- The name of a monitor can be obtained with <a href="/windows/desktop/api/winuser/nf-winuser-getmonitorinfoa">GetMonitorInfo</a> using the <a href="/windows/desktop/api/winuser/ns-winuser-monitorinfoexa">MONITORINFOEX</a> structure. Each time the topology changes, the current monitor topology ID will change. In other words, topologies with two different IDs may have identical topologies.
Note that the items that define a topology may expand in the future, but it is guaranteed that items will not be removed.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | User32.dll |
