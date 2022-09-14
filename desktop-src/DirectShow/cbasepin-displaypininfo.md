---
description: The DisplayPinInfo method traces a pin connection during debugging.
ms.assetid: 3c1aa5ab-7f6b-4518-abf3-b5138f6267ee
title: CBasePin.DisplayPinInfo method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.DisplayPinInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.DisplayPinInfo method

The `DisplayPinInfo` method traces a pin connection during debugging.

## Syntax


```C++
void DisplayPinInfo(
   IPin *pReceivePin
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the receiving pin.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

In debug builds, this method calls the [**DbgLog**](dbglog.md) function to trace a connection attempt. In retail builds, this method does nothing.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




