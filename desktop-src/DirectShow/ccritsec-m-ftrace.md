---
description: Boolean value that specifies whether to trace this lock.
ms.assetid: 23417410-cfdc-426e-a662-7d6580b43a28
title: CCritSec::m_fTrace member (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_fTrace
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCritSec::m\_fTrace member

Boolean value that specifies whether to trace this lock.

## Syntax


```C++
BOOL m_fTrace;
```



## Remarks

This member variable is defined only in the debug version of the base class. If the value is **TRUE**, a trace of the lock state is written to the debug log. (Debug logging for critical sections must be active.) For more information, see [**DbgLockTrace**](dbglocktrace.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

 




