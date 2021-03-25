---
description: The EndRun method switches to the stopped or paused mode.
ms.assetid: 2c41262c-a809-4f3b-898c-02c0891dc6f8
title: CCmdQueue.EndRun method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.EndRun
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCmdQueue.EndRun method

The `EndRun` method switches to the stopped or paused mode.

## Syntax


```C++
virtual HRESULT EndRun();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value that depends on the implementation.

## Remarks

Time mapping between stream time and presentation time is not known after this member function has been called. Call the [**CCmdQueue::Run**](ccmdqueue-run.md) member function to carry out this mapping.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




