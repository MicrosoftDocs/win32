---
description: Enables or disables debug logging of a given critical section.
ms.assetid: 6e6e3de4-8bea-4e28-b04e-54a52226b59a
title: DbgLockTrace function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgLockTrace
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# DbgLockTrace function

Enables or disables debug logging of a given critical section.

## Syntax


```C++
void WINAPI DbgLockTrace(
   CCritSec *pcCrit,
   BOOL     fTrace
);
```



## Parameters

<dl> <dt>

*pcCrit* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) critical section.

</dd> <dt>

*fTrace* 
</dt> <dd>

Value specifying whether logging is enabled. Use **TRUE** to enable logging or **FALSE** to disable it.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use this function to trace a specific critical section. By default, debug logging of critical sections is disabled, because of the large number of critical sections.

To trace a critical section, perform the following steps:

1.  Define DEBUG or \_DEBUG before you include the DirectShow headers.
2.  Enable debug logging for critical sections, by calling [**DbgSetModuleLevel**](dbgsetmodulelevel.md) with the LOG\_LOCKING flag.
3.  Call **DbgLockTrace** on the critical section you want to trace.

In retail builds, the **DbgLockTrace** function has no effect.

## Examples

The following code example shows how to trace a critical section.


```
DbgInitialise(g_hInst);
DbgSetModuleLevel(LOG_LOCKING, 3);

{
    CCritSec MyLock;
    DbgLockTrace(&MyLock, TRUE);
    
    CAutoLock cObjectLock(&MyLock);

    // Protected section of code.    
    DbgOutString("This code is inside a critical section.\n");

} // Lock goes out of scope here.

DbgTerminate();
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Critical Section Debugging Functions](critical-section-debugging-functions.md)
</dt> </dl>

 

 




