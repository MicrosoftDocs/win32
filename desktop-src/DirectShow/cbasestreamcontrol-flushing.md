---
description: The Flushing method notifies the base class that the pin has started or stopped flushing.
ms.assetid: a3c000e1-18a1-48f7-9e2e-fe63cf13fc5c
title: CBaseStreamControl.Flushing method (Strmctl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseStreamControl.Flushing
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseStreamControl.Flushing method

The `Flushing` method notifies the base class that the pin has started or stopped flushing.

## Syntax


```C++
void Flushing(
   BOOL bInProgress
);
```



## Parameters

<dl> <dt>

*bInProgress* 
</dt> <dd>

Specifies a Boolean value that indicates whether the pin is flushing. Use the value **TRUE** when the pin begins a flush operation, and **FALSE** when the pin ends a flush operation.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The pin must call this method from within its [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) and [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) methods. Specify **TRUE** in **BeginFlush** and **FALSE** in **EndFlush**.

This method causes the [**CBaseStreamControl::CheckStreamState**](cbasestreamcontrol-checkstreamstate.md) method to stop waiting. While the pin is flushing, **CheckStreamState** always returns STREAM\_DISCARDING.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




