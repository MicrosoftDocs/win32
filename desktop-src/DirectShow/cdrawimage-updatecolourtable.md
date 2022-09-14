---
description: The UpdateColourTable method updates the color table with a new palette.
ms.assetid: 61ad98c6-a526-4aac-ad68-d44fadc668de
title: CDrawImage.UpdateColourTable method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.UpdateColourTable
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.UpdateColourTable method

The `UpdateColourTable` method updates the color table with a new palette.

## Syntax


```C++
void UpdateColourTable(
   HDC              hdc,
   BITMAPINFOHEADER *pbmi
);
```



## Parameters

<dl> <dt>

*hdc* 
</dt> <dd>

Device context containing the image.

</dd> <dt>

*pbmi* 
</dt> <dd>

Pointer to a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure containing the new palette.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




