---
description: Handle to the thread.
ms.assetid: 93d1182a-58f0-4570-8568-fe0fded762cb
title: CAMThread::m_hThread member (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_hThread
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread::m\_hThread member

Handle to the thread.

## Syntax


```C++
HANDLE m_hThread;
```



## Remarks

This variable is initialized as **NULL**. The [**CAMThread::Create**](camthread-create.md) method sets this variable to the thread handle. To determine whether the thread exists, call the [**CAMThread::ThreadExists**](camthread-threadexists.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




