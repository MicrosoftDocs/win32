---
description: Retrieves the thread's identifier.
ms.assetid: c2b25342-841a-46cb-862c-01761fc60363
title: CMsgThread.GetThreadID method (Msgthrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.GetThreadID
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.GetThreadID method

Retrieves the thread's identifier.

## Syntax


```C++
DWORD GetThreadID();
```



## Parameters

This method has no parameters.

## Return value

Returns the **m\_ThreadId** private data member.

## Remarks

This function returns the Microsoft Win32 identifier for the worker thread. You can call this member function on either the worker thread or a client thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




