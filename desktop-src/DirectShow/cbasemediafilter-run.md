---
Description: 'The Run method runs the object. This method implements the IMediaFilter::Run method.'
ms.assetid: 'a59180df-46b4-4c23-973f-2931d95ace55'
title: 'CBaseMediaFilter.Run method'
---

# CBaseMediaFilter.Run method

The `Run` method runs the object. This method implements the [**IMediaFilter::Run**](imediafilter-run.md) method.

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

Reference time corresponding to stream time 0.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

If the object is stopped, this method pauses the object by calling the [**CBaseMediaFilter::Pause**](cbasemediafilter-pause.md) method. It then sets the [**CBaseMediaFilter::m\_State**](cbasemediafilter-m-state.md) member variable to State\_Running.

Stream time is calculated as the current reference time minus *tStart*. A media sample with a time stamp of zero should be rendered at time *tStart*.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




