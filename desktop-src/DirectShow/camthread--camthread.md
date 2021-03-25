---
description: Destructor method.
ms.assetid: eed6c566-8a03-4a97-9d99-8e500ce2954c
title: CAMThread.~CAMThread destructor (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.~CAMThread
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.~CAMThread destructor

Destructor method.

## Syntax


```C++
virtual ~CAMThread();
```



## Remarks

The destructor calls the [**CAMThread::Close**](camthread-close.md) method, which waits for the thread to exit.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




