---
Description: 'The ContainsPalette function determines whether a specified VIDEOINFOHEADER structure contains a palette.'
ms.assetid: 'e87ab1af-a822-45d8-9326-08b450e11279'
title: ContainsPalette function
---

# ContainsPalette function

The **ContainsPalette** function determines whether a specified [**VIDEOINFOHEADER**](videoinfoheader.md) structure contains a palette.

## Syntax


```C++
BOOL ContainsPalette(
   const VIDEOINFOHEADER *pVideoInfo

);
```



## Parameters

<dl> <dt>

*pVideoInfo* 
</dt> <dd>

Pointer to a [**VIDEOINFOHEADER**](videoinfoheader.md) structure.

</dd> </dl>

## Return value

Returns **TRUE** if the bitdepth is 8 or less (**bmiHeader.biBitCount**), or the number of color indexes is more than zero (**bmiHeader.biClrUsed**). Returns **FALSE** otherwise.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




