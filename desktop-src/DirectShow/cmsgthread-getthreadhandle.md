---
Description: Retrieves the handle to the thread in the CMsgThread object.
ms.assetid: dacbdc68-91a0-46d4-805f-fe51cb047e19
title: CMsgThread.GetThreadHandle method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.GetThreadHandle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.GetThreadHandle method

Retrieves the handle to the thread in the [**CMsgThread**](cmsgthread.md) object.

## Syntax


```C++
HANDLE GetThreadHandle();
```



## Parameters

This method has no parameters.

## Return value

Returns the thread handle.

## Remarks

The thread handle can be passed to wait functions, such as [**WaitForMultipleObjects**](https://docs.microsoft.com/windows/desktop/api/synchapi/nf-synchapi-waitformultipleobjects). The thread handle is signaled when the thread has exited.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




