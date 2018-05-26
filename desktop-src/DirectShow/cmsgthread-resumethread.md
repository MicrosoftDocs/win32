---
Description: Uses the Microsoft Win32 ResumeThread function to continue the operation of the worker thread after a previous call to the CMsgThreadSuspendThread member function.
ms.assetid: 5c94a079-5c74-4024-8fb0-71c7ef9c7e73
title: CMsgThread.ResumeThread method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMsgThread.ResumeThread method

Uses the Microsoft Win32 **ResumeThread** function to continue the operation of the worker thread after a previous call to the [**CMsgThread::SuspendThread**](cmsgthread-suspendthread.md) member function.

## Syntax


```C++
DWORD ResumeThread();
```



## Parameters

This method has no parameters.

## Return value

If the member function succeeds, the return value is the previous suspend count of the thread. If the member function fails, the return value is 0xFFFFFFFF. To obtain extended error information, call the Microsoft Win32 **GetLastError** function.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




