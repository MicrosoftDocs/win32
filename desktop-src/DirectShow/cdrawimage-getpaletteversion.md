---
description: The GetPaletteVersion method retrieves the current palette version.
ms.assetid: 9f97a810-04a4-4ea3-8918-416e9cd8e5e4
title: CDrawImage.GetPaletteVersion method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.GetPaletteVersion
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.GetPaletteVersion method

The `GetPaletteVersion` method retrieves the current palette version.

## Syntax


```C++
LONG GetPaletteVersion();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of the **m\_PaletteVersion** member variable.

## Remarks

The value returned by this method applies only when the allocator is a [**CImageAllocator**](cimageallocator.md) object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CDrawImage::IncrementPaletteVersion**](cdrawimage-incrementpaletteversion.md)
</dt> <dt>

[**CDrawImage::ResetPaletteVersion**](cdrawimage-resetpaletteversion.md)
</dt> </dl>

 

 




