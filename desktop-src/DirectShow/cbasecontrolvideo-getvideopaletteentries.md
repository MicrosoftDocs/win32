---
description: The GetVideoPaletteEntries method retrieves a range of palette entries for the video.
ms.assetid: 7ac12e28-daa7-4d6c-9983-401971e6704d
title: CBaseControlVideo.GetVideoPaletteEntries method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetVideoPaletteEntries
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.GetVideoPaletteEntries method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetVideoPaletteEntries` method retrieves a range of palette entries for the video.

## Syntax


```C++
HRESULT GetVideoPaletteEntries(
   long StartIndex,
   long Entries,
   long *pRetrieved,
   long *pPalette
);
```



## Parameters

<dl> <dt>

*StartIndex* 
</dt> <dd>

Zero-based start palette entry.

</dd> <dt>

*Entries* 
</dt> <dd>

Number of entries required.

</dd> <dt>

*pRetrieved* 
</dt> <dd>

Pointer to the number of colors obtained.

</dd> <dt>

*pPalette* 
</dt> <dd>

Pointer to output buffer for colors.

</dd> </dl>

## Return value

Returns NOERROR if successful, VFW\_E\_NO\_PALETTE\_AVAILABLE if the video samples has no color palette, E\_OUTOFMEMORY if there is not enough memory available, E\_INVALIDARG if *StartIndex* is invalid, or S\_FALSE if there are no colors in the palette.

## Remarks

This member function returns the current palette of the video as an array allocated by the user. To remain consistent, use the members in the Win32 **PALETTEENTRY** structure to return the colors, rather than the members in the **RGBQUAD** structure (although the parameter is a **LONG**). The memory is allocated by the caller, so simply copy each in turn. Determine that the number of entries requested and the start position offset are both valid. If the number of entries evaluates to zero, return an S\_FALSE code.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




