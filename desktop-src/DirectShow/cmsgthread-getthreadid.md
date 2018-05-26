---
Description: Retrieves the threads identifier.
ms.assetid: c2b25342-841a-46cb-862c-01761fc60363
title: CMsgThread.GetThreadID method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




