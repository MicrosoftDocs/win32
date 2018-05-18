---
Description: 'Handle to the thread.'
ms.assetid: '93d1182a-58f0-4570-8568-fe0fded762cb'
title: 'CAMThread::m\_hThread member'
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




