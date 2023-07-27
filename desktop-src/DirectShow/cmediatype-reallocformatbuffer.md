---
description: The ReallocFormatBuffer method reallocates the format block to a new size.
ms.assetid: 49bec677-09cc-4e1a-994a-13e873e61713
title: CMediaType.ReallocFormatBuffer method (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.ReallocFormatBuffer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaType.ReallocFormatBuffer method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ReallocFormatBuffer` method reallocates the format block to a new size.

## Syntax


```C++
BYTE* ReallocFormatBuffer(
   ULONG length
);
```



## Parameters

<dl> <dt>

*length* 
</dt> <dd>

New size required for the format block, in bytes. Must be greater than zero.

</dd> </dl>

## Return value

Returns a pointer to the new block if successful. Otherwise, returns either a pointer to the old format block, or **NULL**.

## Remarks

This method allocates a new format block. It copies as much of the existing format block as possible into the new format block. If the new block is smaller than the existing block, the existing format block is truncated. If the new block is larger, the contents of the additional space are undefined. They are not explicitly set to zero.

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

 

 




