---
Description: 'The DisplaySampleTimes method draws the time stamps of a media sample on top of the video image.'
ms.assetid: '3741dc74-5311-4cb1-9e6b-4a8bf6113477'
title: 'CDrawImage.DisplaySampleTimes method'
---

# CDrawImage.DisplaySampleTimes method

The `DisplaySampleTimes` method draws the time stamps of a media sample on top of the video image.

## Syntax


```C++
void DisplaySampleTimes(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](imediasample.md) interface of the sample.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method is called only in debug builds.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




