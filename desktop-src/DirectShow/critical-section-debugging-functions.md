---
description: Critical Section Debugging Functions
ms.assetid: 2e58ff06-d9b2-45fe-bd40-d637aa434339
title: Critical Section Debugging Functions
ms.topic: article
ms.date: 05/31/2018
---

# Critical Section Debugging Functions

These functions help to debug critical sections in your code, which can make it easier to find the cause of a deadlock. These functions use the [**CCritSec**](ccritsec.md) helper class.



| Function                             | Description                                                                  |
|--------------------------------------|------------------------------------------------------------------------------|
| [**CritCheckIn**](critcheckin.md)   | Returns **TRUE** if the current thread owns the specified critical section.  |
| [**CritCheckOut**](critcheckout.md) | Returns **FALSE** if the current thread owns the specified critical section. |
| [**DbgLockTrace**](dbglocktrace.md) | Enables or disables debug logging for a given critical section.              |



 

## Related topics

<dl> <dt>

[Debugging Utilities](debugging-utilities.md)
</dt> </dl>

 

 



