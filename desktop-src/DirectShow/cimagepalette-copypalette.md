---
description: The CopyPalette method copies the palette from any VIDEOINFO structure to any palettized VIDEOINFO structure.
ms.assetid: ea06b40b-3f96-4c11-921c-52f3a44e0a30
title: CImagePalette.CopyPalette method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImagePalette.CopyPalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CImagePalette.CopyPalette method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CopyPalette` method copies the palette from any [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure to any palettized **VIDEOINFO** structure.

## Syntax


```C++
HRESULT CopyPalette(
   const CMediaType *pSrc,
   const CMediaType *pDest
);
```



## Parameters

<dl> <dt>

*pSrc* 
</dt> <dd>

Pointer to the source media type.

</dd> <dt>

*pDest* 
</dt> <dd>

Pointer to the destination media type.

</dd> </dl>

## Return value

Returns S\_OK if the palette was copied. Returns S\_FALSE if either the source or destination media type does not have a palette.

## Remarks

The *pDest* media type must be a palettized format with a color depth of 8 bits or less. The *pSrc* media type can be any [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) type with a palette, including YUV and true-color formats with palette entries. The method copies the palette entries from *pSrc* into a new palette, and attaches the new palette to *pDest*.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImagePalette Class**](cimagepalette.md)
</dt> </dl>

 

 




