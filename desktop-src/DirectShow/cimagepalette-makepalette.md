---
Description: The MakePalette method creates a logical palette from the color table in a video format.
ms.assetid: f158e529-d683-4210-818d-21a834fc7683
title: CImagePalette.MakePalette method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CImagePalette.MakePalette method

The `MakePalette` method creates a logical palette from the color table in a video format.

## Syntax


```C++
HPALETTE MakePalette(
   const VIDEOINFOHEADER *pVideoInfo,
         LPSTR           szDevice
);
```



## Parameters

<dl> <dt>

*pVideoInfo* 
</dt> <dd>

Pointer to a [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure that contains the color table.

</dd> <dt>

*szDevice* 
</dt> <dd>

Pointer to a string that contains the name of the display device, as returned by the GDI **EnumDisplayDevices** function. To use the main display device, set this parameter to **NULL**.

</dd> </dl>

## Return value

If successful, returns a handle to the palette. Otherwise, returns **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




