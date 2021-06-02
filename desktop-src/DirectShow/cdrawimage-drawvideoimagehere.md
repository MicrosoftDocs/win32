---
description: The DrawVideoImageHere method draws an image from a media sample to a specified device context.
ms.assetid: b11e1c6b-5a29-444f-a0a9-049cd9d49b13
title: CDrawImage.DrawVideoImageHere method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.DrawVideoImageHere
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.DrawVideoImageHere method

The `DrawVideoImageHere` method draws an image from a media sample to a specified device context.

## Syntax


```C++
BOOL DrawVideoImageHere(
   HDC          hdc,
   IMediaSample *pMediaSample,
   RECT         *lprcSrc,
   RECT         *lprcDst
);
```



## Parameters

<dl> <dt>

*hdc* 
</dt> <dd>

Handle to a device context, where the drawing will occur.

</dd> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the sample that contains the image.

</dd> <dt>

*lprcSrc* 
</dt> <dd>

Pointer to a source rectangle to use for drawing. If **NULL**, the rectangle in [**CDrawImage::m\_SourceRect**](cdrawimage-m-sourcerect.md) is used.

</dd> <dt>

*lprcDst* 
</dt> <dd>

Pointer to a target rectangle to use for drawing. If **NULL**, the rectangle in [**CDrawImage::m\_TargetRect**](cdrawimage-m-targetrect.md) is used.

</dd> </dl>

## Return value

Returns **TRUE** if successful.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




