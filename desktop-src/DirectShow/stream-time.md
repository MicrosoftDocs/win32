---
description: Note  This API is deprecated. New applications should not use it. The STREAM\_TIME data type is used to express reference times in Microsoft DirectShow multimedia streaming. Units are 100 nanoseconds.
ms.assetid: eff79c58-09d8-4665-9138-752ffaf02e26
title: STREAM_TIME (Mmstream.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# STREAM\_TIME

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This API is deprecated. New applications should not use it.

 

The STREAM\_TIME data type is used to express reference times in Microsoft DirectShow multimedia streaming. Units are 100 nanoseconds.


```C++
typedef LONGLONG STREAM_TIME;
```



## Remarks

This data type is equivalent to the DirectShow [**REFERENCE\_TIME**](reference-time.md) data type.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mmstream.h</dt> </dl> |



## See also

<dl> <dt>

[Multimedia Streaming Data Types](multimedia-streaming-data-types.md)
</dt> </dl>

 

 




