---
Description: 'Uses the Microsoft Win32 SuspendThread function to suspend the operation of a running thread.'
ms.assetid: '07d919a2-797d-47c3-83e3-c8e2d2b2cddd'
title: 'CMsgThread.SuspendThread method'
---

# CMsgThread.SuspendThread method

Uses the Microsoft Win32 **SuspendThread** function to suspend the operation of a running thread.

## Syntax


```C++
DWORD SuspendThread();
```



## Parameters

This method has no parameters.

## Return value

If the member function succeeds, the return value is the previous suspend count of the thread. If the member function fails, the return value is 0xFFFFFFFF. To obtain extended error information, call the Microsoft Win32 **GetLastError** function.

## Remarks

The client thread calls this member function to suspend the operation of the worker thread. The worker thread remains suspended and will not execute until an additional call to the [**CMsgThread::ResumeThread**](cmsgthread-resumethread.md) member function is made.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




