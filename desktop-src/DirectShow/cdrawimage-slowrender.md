---
Description: 'The SlowRender method draws the video image using the SetDIBitsToDevice or StretchDIBits functions.'
ms.assetid: 'e1d8b189-b588-48eb-988a-3e5dedb38dbd'
title: 'CDrawImage.SlowRender method'
---

# CDrawImage.SlowRender method

The `SlowRender` method draws the video image using the **SetDIBitsToDevice** or **StretchDIBits** functions.

## Syntax


```C++
void SlowRender(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](imediasample.md) interface of the sample that contains the image.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If [**CDrawImage::UsingImageAllocator**](cdrawimage-usingimageallocator.md) returns **FALSE**, the [**CDrawImage::DrawImage**](cdrawimage-drawimage.md) method uses `SlowRender` to draw the video image. Otherwise, DrawImage uses the **FastRender** method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CDrawImage::FastRender**](cdrawimage-fastrender.md)
</dt> </dl>

 

 




