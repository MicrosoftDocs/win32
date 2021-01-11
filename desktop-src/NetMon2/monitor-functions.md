---
description: This section describes the helper functions you can use to develop custom monitors.
ms.assetid: 2c019183-9823-4e34-bb41-cf35f2731b8f
title: Monitor Functions
ms.topic: article
ms.date: 05/31/2018
---

# Monitor Functions

This section describes the helper functions you can use to develop custom monitors.



| Function                                       | Description                                                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DllGetMonitorObject](dllgetmonitorobject.md) | Creates an instance of the monitor.                                                                                                                              |
| [HTMLValueToUnicode](htmlvaluetounicode.md)   | Converts an HTML CP\_UTF8 version string to Unicode.                                                                                                             |
| [LoadDWORD](loaddword.md)                     | Loads a **DWORD** from an HTML configuration string.                                                                                                             |
| [LoadIPAddresses](loadipaddresses.md)         | Loads an IP address list from an HTML TEXTAREA configuration string.                                                                                             |
| [LoadIPXAddresses](loadipxaddresses.md)       | Loads an IPX address list from an HTML TEXTAREA configuration string.                                                                                            |
| [LoadMACAddresses](loadmacaddresses.md)       | Loads a MAC address list from an HTML TEXTAREA configuration string.                                                                                             |
| [LoadStringAddr](loadstringaddr.md)           | Transforms a string (such as "157.54.32.45") to a **DWORD** address.                                                                                             |
| [LoadTCHAR](loadtchar.md)                     | Searches for a requested variable name in the configuration string, and allocates sufficient space (by using **HeapAllocMemory**) to store, copy, and return it. |
| [OnLoadingDLL](onloadingdll.md)               | Indicates that the DLL has begun to load. The MCSVC calls this function when it first loads the monitor DLL.                                                     |



 

 

 



