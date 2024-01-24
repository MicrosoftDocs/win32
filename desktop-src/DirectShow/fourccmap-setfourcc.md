---
description: Sets the FOURCC portion of the FOURCCMap object.
ms.assetid: cc821e39-e565-4255-a289-2c9507d43433
title: FOURCCMap::SetFOURCC method (Fourcc.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FOURCCMap.SetFOURCC
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# FOURCCMap::SetFOURCC method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Sets the **FOURCC** portion of the [**FOURCCMap**](fourccmap.md) object.

## Syntax


```C++
void SetFOURCC(
   const GUID *pguid
);
```



## Parameters

<dl> <dt>

*pguid* 
</dt> <dd>

Pointer to the returned globally unique identifier (**GUID**) part of the **FOURCCMap** object.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Fourcc.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**FOURCCMap Class**](fourccmap.md)
</dt> </dl>

 

 




