---
description: The ScaleSourceRect method scales a rectangle, if there is a difference between the native video size and the media type format.
ms.assetid: 7bd4d555-5782-4ce5-9f0d-928b199ef897
title: CDrawImage.ScaleSourceRect method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.ScaleSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.ScaleSourceRect method

The `ScaleSourceRect` method scales a rectangle, if there is a difference between the native video size and the media type format.

## Syntax


```C++
virtual RECT ScaleSourceRect(
   const RECT *pSource
);
```



## Parameters

<dl> <dt>

*pSource* 
</dt> <dd>

Pointer to an unscaled rectangle.

</dd> </dl>

## Return value

Returns the scaled rectangle.

## Remarks

In the **CDrawImage** class, this method returns *pSource* without any change. You can override this method if the filter stretches the incoming video image. For example, the native video size might be 320   240, but the media type on the input pin might be 640   480. In that case the filter would need to scale the source rectangle by a factor of 2.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




