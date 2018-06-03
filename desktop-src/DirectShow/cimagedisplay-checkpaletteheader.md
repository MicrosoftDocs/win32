---
Description: The CheckPaletteHeader method validates the palette entries in a VIDEOINFO structure.
ms.assetid: bc18cbe6-0446-43a6-a50c-e587815b789d
title: CImageDisplay.CheckPaletteHeader method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CImageDisplay.CheckPaletteHeader method

The `CheckPaletteHeader` method validates the palette entries in a [**VIDEOINFO**](/windows/desktop/api/amvideo/ns-amvideo-tagvideoinfo) structure.

## Syntax


```C++
BOOL CheckPaletteHeader(
   const VIDEOINFO *pInput
);
```



## Parameters

<dl> <dt>

*pInput* 
</dt> <dd>

Pointer to a **VIDEOINFO** structure.

</dd> </dl>

## Return value

Returns **TRUE** if the palette entries are valid, or **FALSE** otherwise.

## Remarks

If the image format is not palettized, the method verifies that **biClrUsed** equals zero. Otherwise, the method verifies that the **biCompression** flag is BI\_RGB; **biClrImportant** is not greater than **biClrUsed**; and the number of palette entries does not exceed the maximum, given the color depth.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




