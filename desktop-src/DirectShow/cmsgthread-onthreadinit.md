---
description: Provides initialization on a thread.
ms.assetid: a9c330bb-0a2b-45bf-9b24-d03dd61d7dbf
title: CMsgThread.OnThreadInit method (Msgthrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.OnThreadInit
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.OnThreadInit method

Provides initialization on a thread.

## Syntax


```C++
virtual void OnThreadInit();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Override this function if you want to do your own specific initialization on thread startup.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




