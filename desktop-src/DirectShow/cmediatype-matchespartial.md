---
description: The MatchesPartial method determines if this media type matches a partially specified media type.
ms.assetid: 62d531f3-5aa2-4af2-b951-584a49a849fc
title: CMediaType.MatchesPartial method (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.MatchesPartial
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaType.MatchesPartial method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `MatchesPartial` method determines if this media type matches a partially specified media type.

## Syntax


```C++
BOOL MatchesPartial(
   const CMediaType *ppartial
) const;
```



## Parameters

<dl> <dt>

*ppartial* 
</dt> <dd>

Pointer to the media type to match.

</dd> </dl>

## Return value

Returns **TRUE** if the media types match. Otherwise, returns **FALSE**.

## Remarks

The media type specified by *ppartial* can have a value of GUID\_NULL for the major type, subtype, or format type. Any members with GUID\_NULL values are not tested. (In effect, GUID\_NULL acts as a wildcard.) Members with values other than GUID\_NULL must match for the media type to match.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




