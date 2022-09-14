---
description: The Run method switches to running mode so that commands that are deferred by the stream time can be run.
ms.assetid: c529ae84-c9b7-46f1-a1e4-716fc9e9df13
title: CCmdQueue.Run method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.Run
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCmdQueue.Run method

The `Run` method switches to running mode so that commands that are deferred by the stream time can be run.

## Syntax


```C++
virtual HRESULT Run(
   REFERENCE_TIME tStreamTimeOffset
);
```



## Parameters

<dl> <dt>

*tStreamTimeOffset* 
</dt> <dd>

Offset time.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

During running mode, stream-time-to-presentation-time mapping is known.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




