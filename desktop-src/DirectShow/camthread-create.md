---
description: The Create method creates the thread.
ms.assetid: 453972eb-7cf6-43c6-820e-c1992675260e
title: CAMThread.Create method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.Create
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.Create method

The `Create` method creates the thread.

## Syntax


```C++
BOOL Create();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

This method creates the thread, using the [**CAMThread::InitialThreadProc**](camthread-initialthreadproc.md) method for the thread procedure and `this` for the thread argument.

The method fails if the thread already exists.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




