---
description: The PreparePalette method sets up a palette, based on a media type from the owning filter.
ms.assetid: cb012391-39ab-4ad1-aeb7-ec25010ac64a
title: CImagePalette.PreparePalette method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImagePalette.PreparePalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImagePalette.PreparePalette method

The `PreparePalette` method sets up a palette, based on a media type from the owning filter.

## Syntax


```C++
HRESULT PreparePalette(
   const CMediaType *pmtNew,
   const CMediaType *pmtOld,
         LPSTR      szDevice
);
```



## Parameters

<dl> <dt>

*pmtNew* 
</dt> <dd>

Pointer to the new media type. The format block must be a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure.

</dd> <dt>

*pmtOld* 
</dt> <dd>

Pointer to the old media type. If the media type is being set for the first time, this parameter can be an empty type with no format block. Otherwise, the format block must be a **VIDEOINFOHEADER** structure.

</dd> <dt>

*szDevice* 
</dt> <dd>

Pointer to a string that contains the name of the display device, as returned by the GDI **EnumDisplayDevices** function. To use the main display device, set this parameter to **NULL**.

</dd> </dl>

## Return value

Returns S\_OK if the palette was updated, or S\_FALSE if the palette did not change.

## Remarks

If the palette needs to be updated, this method performs the following actions:

-   Calls [**CImagePalette::MakePalette**](cimagepalette-makepalette.md) to create a new logical palette.
-   Sends an [**EC\_PALETTE\_CHANGED**](ec-palette-changed.md) event to the Filter Graph Manager.
-   Calls [**CBaseWindow::SetPalette**](cbasewindow-setpalette.md) on the **CBaseWindow** object.
-   Calls [**CDrawImage::IncrementPaletteVersion**](cdrawimage-incrementpaletteversion.md) on the **CDrawImage** object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




