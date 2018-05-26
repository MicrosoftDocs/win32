---
Description: Number of outstanding locks on this object.
ms.assetid: 27506c1d-6a9a-4410-80fb-6d4f2fd2f824
title: CCritSecm\_lockCount member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CCritSec::m\_lockCount member

Number of outstanding locks on this object.

## Syntax


```C++
DWORD m_lockCount;
```



## Remarks

This member variable is defined only in the debug version of the base class. The [Critical Section Debugging Functions](critical-section-debugging-functions.md) functions use this member.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

 




