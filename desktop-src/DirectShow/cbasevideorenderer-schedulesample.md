---
Description: 'The ScheduleSample method overrides the base class that does the main work to keep a count of samples drawn and dropped (which are used by the IQualProp implementation).'
ms.assetid: '66e4e318-a7ff-4ba0-9ac5-24ba39ac86f1'
title: 'CBaseVideoRenderer.ScheduleSample method'
---

# CBaseVideoRenderer.ScheduleSample method

The `ScheduleSample` method overrides the base class that does the main work to keep a count of samples drawn and dropped (which are used by the [**IQualProp**](iqualprop.md) implementation).

## Syntax


```C++
BOOL ScheduleSample(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the media sample.

</dd> </dl>

## Return value

Returns **TRUE** if the sample is scheduled; otherwise, returns **FALSE**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




