---
Description: The ScheduleSample method overrides the base class that does the main work to keep a count of samples drawn and dropped (which are used by the IQualProp implementation).
ms.assetid: 66e4e318-a7ff-4ba0-9ac5-24ba39ac86f1
title: CBaseVideoRenderer.ScheduleSample method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseVideoRenderer.ScheduleSample method

The `ScheduleSample` method overrides the base class that does the main work to keep a count of samples drawn and dropped (which are used by the [**IQualProp**](/windows/desktop/api/Amvideo/nn-amvideo-iqualprop) implementation).

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

 

 




