---
description: The IncrementPaletteVersion method increments the palette version. Call this method if the media type changes to a new palettized format.
ms.assetid: 1ce77f97-d225-45f5-a259-1dcca1272d15
title: CDrawImage.IncrementPaletteVersion method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.IncrementPaletteVersion
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.IncrementPaletteVersion method

The `IncrementPaletteVersion` method increments the palette version. Call this method if the media type changes to a new palettized format.

## Syntax


```C++
void IncrementPaletteVersion();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method increments the value of the **m\_PaletteVersion** member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CDrawImage::GetPaletteVersion**](cdrawimage-getpaletteversion.md)
</dt> <dt>

[**CDrawImage::ResetPaletteVersion**](cdrawimage-resetpaletteversion.md)
</dt> </dl>

 

 




