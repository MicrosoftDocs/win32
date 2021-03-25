---
description: Constructor method.
ms.assetid: 35c9ac07-8756-42b1-beeb-5f0e79466742
title: CAMEvent.CAMEvent constructor (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMEvent.CAMEvent
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMEvent.CAMEvent constructor

Constructor method.

## Syntax


```C++
CAMEvent(
   BOOL    fManualReset,
   HRESULT *phr
);
```



## Parameters

<dl> <dt>

*fManualReset* 
</dt> <dd>

Boolean value that specifies whether the object is a manual-reset event or an auto-reset event. If **TRUE**, the object is a manual-reset event. Otherwise, it is an auto-reset event.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. If the constructor fails, this parameter receives an error code. If this occurs, the object is not in a valid state.

For backward compatibility with earlier versions of strmbase.lib, this parameter defaults to **NULL**. However, passing a non-**NULL** value is preferred, so that the caller can check the status of the object.

</dd> </dl>

## Remarks

The event begins in a nonsignaled state.

With an auto-reset event, the [**CAMEvent::Wait**](camevent-wait.md) method resets the event to nonsignaled when the method returns. With a manual-reset event, the event remains signaled until you call the [**CAMEvent::Reset**](camevent-reset.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMEvent Class**](camevent.md)
</dt> </dl>

 

 




