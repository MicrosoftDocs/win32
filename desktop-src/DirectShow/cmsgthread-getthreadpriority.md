---
description: Uses the Microsoft Win32 GetThreadPriority function to retrieve the priority of the current worker thread.
ms.assetid: a9db15cf-2c22-4c61-a817-20af5ade434b
title: CMsgThread.GetThreadPriority method (Msgthrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.GetThreadPriority
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.GetThreadPriority method

Uses the Microsoft Win32 **GetThreadPriority** function to retrieve the priority of the current worker thread.

## Syntax


```C++
int GetThreadPriority();
```



## Parameters

This method has no parameters.

## Return value

Returns the thread priority as an integer.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




