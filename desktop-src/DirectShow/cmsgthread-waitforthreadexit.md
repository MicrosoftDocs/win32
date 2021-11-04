---
description: Blocks until the thread exits.
ms.assetid: 1ee547b5-cd73-4ce8-8e66-c2062714d0f0
title: CMsgThread.WaitForThreadExit method (Msgthrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.WaitForThreadExit
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.WaitForThreadExit method

Blocks until the thread exits.

## Syntax


```C++
BOOL WaitForThreadExit(
   LPDWORD lpdwExitCode
);
```



## Parameters

<dl> <dt>

*lpdwExitCode* 
</dt> <dd>

Pointer to the exit code returned by the thread.

</dd> </dl>

## Return value

Returns either **TRUE** or **FALSE**, the meaning of which is determined by the class supplying the overridden [**CMsgThread::ThreadMessageProc**](cmsgthread-threadmessageproc.md) member function and the calling member function.

## Remarks

Ensure that the worker thread has exited completely before completing the destruction of your derived class; otherwise, the thread might still execute after your dynamic-link library (DLL) has been unloaded from the address space of the process. Even if the only instruction left to exit is a single-return instruction, this would cause an exception. The only reliable way to ensure that the thread has exited is to signal the thread to exit (using a privately negotiated [**CMsg**](cmsg.md) object sent to the [**CMsgThread::PutThreadMsg**](cmsgthread-putthreadmsg.md) member function) and then call this member function. You should do this in the destructor for your derived class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




