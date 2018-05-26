---
Description: Critical section that locks the thread from being accessed by other threads.
ms.assetid: 9bc360be-52d6-4db1-b384-8bc9e25c0914
title: CAMThreadm\_AccessLock member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CAMThread::m\_AccessLock member

Critical section that locks the thread from being accessed by other threads.

## Syntax


```C++
CCritSec m_AccessLock;
```



## Remarks

The [**CAMThread::Create**](camthread-create.md) and [**CAMThread::CallWorker**](camthread-callworker.md) methods hold this lock, to serialize operations on the thread.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




