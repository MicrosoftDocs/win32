---
description: The GetRequest method waits for the next thread request.
ms.assetid: 2938374b-174f-4276-98a2-20a084bd9bbd
title: CSourceStream.GetRequest method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.GetRequest
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.GetRequest method

The `GetRequest` method waits for the next thread request.

## Syntax


```C++
Command GetRequest();
```



## Parameters

This method has no parameters.

## Return value

Returns the next thread request.

## Remarks

This method overrides the [**CAMThread::GetRequest**](camthread-getrequest.md) method. The return value is cast to the following enumerated type:


```C++
enum Command {CMD_INIT, CMD_PAUSE, CMD_RUN, CMD_STOP, CMD_EXIT};
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




