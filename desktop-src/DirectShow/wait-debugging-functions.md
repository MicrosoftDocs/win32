---
description: Wait Debugging Functions
ms.assetid: 784ef76e-3c17-45e0-9a0b-656c11c71322
title: Wait Debugging Functions
ms.topic: article
ms.date: 05/31/2018
---

# Wait Debugging Functions

Microsoft DirectShow provides several functions for debugging infinite waits.

In retail builds, the [**DbgWaitForMultipleObjects**](dbgwaitformultipleobjects.md) and [**DbgWaitForSingleObject**](dbgwaitforsingleobject.md) functions work like their Windows API counterparts, **WaitForMultipleObjects** and **WaitForSingleObject**, with infinite time-out intervals.

In debug builds, these functions use a global time-out value. If the time-out expires, the function triggers an assert. The following registry key specifies the time-out value, in milliseconds:

**HKEY\_LOCAL\_MACHINE\\&lt;DebugRoot&gt;\\\<Module Name\>\\TIMEOUT**

where *&lt;DebugRoot&gt;* is the registry path described in the topic [Debug Output Functions](debug-output-functions.md).

If the key does not exist, the time-out value defaults to INFINITE. You can use the [**DbgSetWaitTimeout**](dbgsetwaittimeout.md) function to override the registry entry.



| Function                                                       | Description                                                     |
|----------------------------------------------------------------|-----------------------------------------------------------------|
| [**DbgSetWaitTimeout**](dbgsetwaittimeout.md)                 | Sets the debugging time-out value.                              |
| [**DbgWaitForMultipleObjects**](dbgwaitformultipleobjects.md) | Waits for any (or all) of the specified objects to be signaled. |
| [**DbgWaitForSingleObject**](dbgwaitforsingleobject.md)       | Waits for an object to become signaled.                         |



 

 

 



