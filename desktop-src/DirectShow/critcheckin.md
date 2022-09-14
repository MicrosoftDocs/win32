---
description: Returns TRUE if the current thread is the owner of the specified critical section.
ms.assetid: 96158f08-07a0-42a9-b173-0a05456a5f3a
title: CritCheckIn function (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CritCheckIn
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CritCheckIn function

Returns **TRUE** if the current thread is the owner of the specified critical section.

## Syntax


```C++
BOOL WINAPI CritCheckIn(
   CCritSec *pcCrit
);
```



## Parameters

<dl> <dt>

*pcCrit* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) critical section.

</dd> </dl>

## Return value

In debug builds, returns **TRUE** if the current thread is the owner of this critical section, or **FALSE** otherwise. In retail builds, always returns **TRUE**.

## Remarks

This function is especially useful within the [**ASSERT**](assert.md) macro, to test whether a thread owns a given lock.

## Examples

The following code example shows how to use this function:


```
{
    CCritSec MyLock;  // Critical section is not locked yet.
    
    ASSERT(CritCheckIn(&MyLock)); // This assert will fire.

    // Lock the critical section.    
    CAutoLock cObjectLock(&MyLock);
     
    ASSERT(CritCheckIn(&MyLock)); // This assert will not fire.

} // Lock goes out of scope here.
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

 

 




