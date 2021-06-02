---
description: The CheckRequest method checks if there is a thread request, without blocking.
ms.assetid: b4691dde-abec-4671-bea6-0f22cc4e7c61
title: CSourceStream.CheckRequest method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.CheckRequest
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.CheckRequest method

The `CheckRequest` method checks if there is a thread request, without blocking.

## Syntax


```C++
BOOL CheckRequest(
   Command *pCom
);
```



## Parameters

<dl> <dt>

*pCom* 
</dt> <dd>

Pointer to a variable that receives the value passed in the last call to the [**CAMThread::CallWorker**](camthread-callworker.md) method.

</dd> </dl>

## Return value

Returns **TRUE** if there is a pending request, or **FALSE** otherwise.

## Remarks

This method overrides the [**CAMThread::CheckRequest**](camthread-checkrequest.md) method to perform type-checking. The **CSourceStream** class defines the following enumerated type for the *pCom* parameter:


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

 

 




