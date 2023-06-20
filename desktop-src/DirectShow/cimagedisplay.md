---
description: The CImageDisplay class is a helper class for GDI video renderers to manage the display format.
ms.assetid: c9221e5c-30c6-489a-89d7-132203314dc8
title: CImageDisplay class (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CImageDisplay class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cimagedisplayclasshierarchy](images/wutil06.png)

The `CImageDisplay` class is a helper class for GDI video renderers to manage the display format. The object stores a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure that describes the current display mode, which is initialized in the object's constructor method. The object's **CheckMediaType** method checks whether a proposed media type can be rendered efficiently using GDI.



| Protected Member Variables                                       | Description                                                                            |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**m\_Display**](cimagedisplay-m-display.md)                    | **VIDEOINFO** structure that describes the current display format.                     |
| Protected Methods                                                | Description                                                                            |
| [**CheckBitFields**](cimagedisplay-checkbitfields.md)           | Validates the color masks in a **VIDEOINFO** structure.                                |
| [**CountPrefixBits**](cimagedisplay-countprefixbits.md)         | Calculates the number of zero bits at the start of a specified bit field.              |
| [**CountSetBits**](cimagedisplay-countsetbits.md)               | Returns the number of bits set to 1 in a specified bit field.                          |
| Public Methods                                                   | Description                                                                            |
| [**CheckHeaderValidity**](cimagedisplay-checkheadervalidity.md) | Validates a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure.                    |
| [**CheckMediaType**](cimagedisplay-checkmediatype.md)           | Determines whether a proposed media type is compatible with the display format.        |
| [**CheckPaletteHeader**](cimagedisplay-checkpaletteheader.md)   | Validates the palette entries in a **VIDEOINFO** structure.                            |
| [**CheckVideoType**](cimagedisplay-checkvideotype.md)           | Checks whether a specified **VIDEOINFO** format is compatible with the display format. |
| [**CImageDisplay**](cimagedisplay-cimagedisplay.md)             | Constructor method.                                                                    |
| [**GetBitMasks**](cimagedisplay-getbitmasks.md)                 | Retrieves the color masks for a specified **VIDEOINFO** format.                        |
| [**GetColourMask**](cimagedisplay-getcolourmask.md)             | Retrieves the color masks for the current display format.                              |
| [**GetDisplayDepth**](cimagedisplay-getdisplaydepth.md)         | Retrieves the bit depth of the current display mode.                                   |
| [**GetDisplayFormat**](cimagedisplay-getdisplayformat.md)       | Retrieves a video format that describes the current display mode.                      |
| [**IsPalettised**](cimagedisplay-ispalettised.md)               | Retermines whether the current display format is palettized.                           |
| [**RefreshDisplayType**](cimagedisplay-refreshdisplaytype.md)   | Updates the object's video format to match the specified display                       |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




