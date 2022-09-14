---
description: Waits for an object to become signaled.
ms.assetid: 5fbcccd9-9db7-4834-852a-86f28218e92e
title: DbgWaitForSingleObject function (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgWaitForSingleObject
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# DbgWaitForSingleObject function

Waits for an object to become signaled.

In a debug build, this function triggers an assert if the time-out interval expires before the object is signaled. To set the time-out interval, call the [**DbgSetWaitTimeout**](dbgsetwaittimeout.md) function.

In a retail build, this function is equivalent to the **WaitForSingleObject** function with a time-out interval of INFINITE.

## Syntax


```C++
DWORD DbgWaitForSingleObject(
   HANDLE h
);
```



## Parameters

<dl> <dt>

*h* 
</dt> <dd>

Handle to the object.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Wait Debugging Functions](wait-debugging-functions.md)
</dt> </dl>

 

 




