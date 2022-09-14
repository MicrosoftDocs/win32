---
description: The MakeIdentityPalette method attempts to make an &\#0034;identity palette,&\#0034; defined as one that maps directly to the palette selected in the display device.
ms.assetid: 08a0cf67-f43f-44c0-bfb3-6527fd434ea4
title: CImagePalette.MakeIdentityPalette method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImagePalette.MakeIdentityPalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImagePalette.MakeIdentityPalette method

The `MakeIdentityPalette` method attempts to make an "identity palette," defined as one that maps directly to the palette selected in the display device.

## Syntax


```C++
HRESULT MakeIdentityPalette(
   PALETTEENTRY *pEntry,
   INT          iColours,
   LPSTR        szDevice
);
```



## Parameters

<dl> <dt>

*pEntry* 
</dt> <dd>

Pointer to an array of palette entries.

</dd> <dt>

*iColours* 
</dt> <dd>

Number of palette entries in *pEntry*.

</dd> <dt>

*szDevice* 
</dt> <dd>

Pointer to a string that contains the name of the display device, as returned by the GDI **EnumDisplayDevices** function. To use the main display device, set this parameter to **NULL**.

</dd> </dl>

## Return value

Returns S\_OK if successful or S\_FALSE if unsuccessful.

## Remarks

This method compares the reserved entries in the system palette against the corresponding entries in the *pEntry* array. If they match exactly, the method sets the PC\_NOCOLLAPSE flag in the remaining (non-reserved) palette entries in *pEntry*. This flag prevents GDI from trying map logical palette entries to system palette entries.

The [**CImagePalette::MakePalette**](cimagepalette-makepalette.md) method calls this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




