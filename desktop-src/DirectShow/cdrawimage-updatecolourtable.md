---
Description: 'The UpdateColourTable method updates the color table with a new palette.'
ms.assetid: '61ad98c6-a526-4aac-ad68-d44fadc668de'
title: 'CDrawImage.UpdateColourTable method'
---

# CDrawImage.UpdateColourTable method

The `UpdateColourTable` method updates the color table with a new palette.

## Syntax


```C++
void UpdateColourTable(
   HDC              hdc,
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

Pointer to a [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure containing the new palette.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




