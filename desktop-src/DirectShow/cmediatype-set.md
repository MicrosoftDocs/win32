---
description: "The CMediaType.Set method (Mtype.h) sets the media type from another media type. The method uses the 'cmtype' parameter."
ms.assetid: 71c19d0f-93b6-41db-8659-c64411b83e7c
title: CMediaType.Set method (Mtype.h) - cmtype [ref] parameter
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.Set
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaType.Set method (Mtype.h) - cmtype [ref] parameter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Set` method sets the media type from another media type.

## Syntax


```C++
HRESULT Set(
  [ref] const CMediaType &cmtype
);
```



## Parameters

<dl> <dt>

*cmtype* \[ref\]
</dt> <dd>

Reference to a [**CMediaType**](cmediatype.md) object.

</dd> </dl>

## Return value

Returns S\_OK or E\_OUTOFMEMORY.

## Remarks

This method copies the entire media type from *cmtype*.

## Requirements

| Requirement                   | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Mtype.h (include Streams.h)                                                                                     |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




