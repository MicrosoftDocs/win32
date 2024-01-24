---
description: The AllocFormatBuffer method allocates memory for the format block.
ms.assetid: 5ff716c7-f9cf-4b1c-9d3a-62ab955c1392
title: CMediaType.AllocFormatBuffer method (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.AllocFormatBuffer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaType.AllocFormatBuffer method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `AllocFormatBuffer` method allocates memory for the format block.

## Syntax


```C++
BYTE* AllocFormatBuffer(
   ULONG length
);
```



## Parameters

<dl> <dt>

*length* 
</dt> <dd>

Size required for the format block, in bytes.

</dd> </dl>

## Return value

Returns a pointer to the new block if successful. Otherwise, returns **NULL**.

## Remarks

If the method successfully allocates a new format block, it frees the existing format block. If the allocation fails, the method leaves the existing format block.

The method updates the **cbFormat** and **pbFormat** members of the **AM\_MEDIA\_TYPE** structure.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




