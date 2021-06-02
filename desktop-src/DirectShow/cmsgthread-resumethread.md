---
description: Uses the Microsoft Win32 ResumeThread function to continue the operation of the worker thread after a previous call to the CMsgThread::SuspendThread member function.
ms.assetid: 5c94a079-5c74-4024-8fb0-71c7ef9c7e73
title: CMsgThread.ResumeThread method (Msgthrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.ResumeThread
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




