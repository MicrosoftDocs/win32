---
description: The ContainsPalette function determines whether a specified VIDEOINFOHEADER structure contains a palette.
ms.assetid: e87ab1af-a822-45d8-9326-08b450e11279
title: ContainsPalette function (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ContainsPalette
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# ContainsPalette function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ContainsPalette** function determines whether a specified [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure contains a palette.

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

Pointer to a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure.

</dd> </dl>

## Return value

Returns **TRUE** if the bitdepth is 8 or less (**bmiHeader.biBitCount**), or the number of color indexes is more than zero (**bmiHeader.biClrUsed**). Returns **FALSE** otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




