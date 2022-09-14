---
description: The Run method notifies the pin that the filter is now running.
ms.assetid: 74aafc89-2d3c-4259-a5b7-d4fb7628f539
title: CBasePin.Run method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.Run
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.Run method

The `Run` method notifies the pin that the filter is now running.

## Syntax


```C++
HRESULT Run(
   REFERENCE_TIME tStart
);
```



## Parameters

<dl> <dt>

*tStart* 
</dt> <dd>

Start time as passed to the filter's [**IMediaFilter::Run**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-run) method.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

When the filter goes from paused to running, the [**CBaseFilter**](cbasefilter.md) class calls this method on all of the filter's pins.

This method does nothing in the base class. Derived classes can override this method. For example, a pin might start a worker thread that delivers samples.

The filter graph manager's internal state is not updated until after this member function returns, so do not test the state from this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




