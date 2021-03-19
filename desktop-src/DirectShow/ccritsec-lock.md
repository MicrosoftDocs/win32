---
description: The Lock method locks the critical section object.
ms.assetid: b08be5ec-3f02-4ed8-8791-20e4d2a0c55f
title: CCritSec.Lock method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCritSec.Lock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCritSec.Lock method

The **Lock** method locks the critical section object.

## Syntax


```C++
void Lock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method calls the [**EnterCriticalSection**](/windows/desktop/api/synchapi/nf-synchapi-entercriticalsection) function.

Call the [**CCritSec::Unlock**](ccritsec-unlock.md) member function to unlock the critical section. You can make multiple calls to the **Lock** method on the same thread; be sure to call **Unlock** a corresponding number of times.

If the object is already locked by another thread, the **CCritSec::Lock** method blocks until the object is released, or until a possible-deadlock exception occurs.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

