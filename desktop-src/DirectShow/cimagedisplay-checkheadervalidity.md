---
description: The CheckHeaderValidity method validates a BITMAPINFOHEADER structure. This method is useful only for uncompressed RGB types, not for compressed types or YUV types.
ms.assetid: 24b547b6-b730-48b2-9a1b-6e77f9cb1ce1
title: CImageDisplay.CheckHeaderValidity method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay.CheckHeaderValidity
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CImageDisplay.CheckHeaderValidity method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CheckHeaderValidity` method validates a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure. This method is useful only for uncompressed RGB types, not for compressed types or YUV types.

## Syntax


```C++
BOOL CheckHeaderValidity(
   const VIDEOINFO *pInput
);
```



## Parameters

<dl> <dt>

*pInput* 
</dt> <dd>

Pointer to a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure containing the **BITMAPINFOHEADER** structure.

</dd> </dl>

## Return value

Returns **TRUE** if the **BITMAPINFOHEADER** is valid, or **FALSE** otherwise.

## Remarks

This method checks that the image dimensions are non-negative; the compression type is BI\_RGB or BI\_BITFIELDS; the color depth and color masks are valid; the **biPlanes** member equals one; and the **biSize** and **biSizeImage** members are correct. It also checks for common errors in the palette entries, if any.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




