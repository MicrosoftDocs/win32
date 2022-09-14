---
description: The Unlock method unlocks the critical section object.
ms.assetid: 61811e0e-df77-48e9-96d5-b7dff8c8db9b
title: CCritSec.Unlock method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCritSec.Unlock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCritSec.Unlock method

The **Unlock** method unlocks the critical section object.

## Syntax


```C++
void Unlock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method calls the [**LeaveCriticalSection**](/windows/desktop/api/synchapi/nf-synchapi-leavecriticalsection) function. Call this method once for each call to the [**CCritSec::Lock**](ccritsec-lock.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

