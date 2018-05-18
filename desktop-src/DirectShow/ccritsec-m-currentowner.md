---
Description: 'Thread identifier of the owning thread.'
ms.assetid: '495598db-a0c9-473b-8184-121a1939b55a'
title: 'CCritSec::m\_currentOwner member'
---

# CCritSec::m\_currentOwner member

Thread identifier of the owning thread.

## Syntax


```C++
DWORD m_currentOwner;
```



## Remarks

This member variable is defined only in the debug version of the base class. The [Critical Section Debugging Functions](critical-section-debugging-functions.md) use this member.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

 




