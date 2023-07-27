---
description: The SetAbortSignal method sets a flag which indicates whether to stop rendering and reject further samples.
ms.assetid: 2dbf3b4d-e285-4d17-a77c-01a16c09d148
title: CBaseRenderer.SetAbortSignal method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.SetAbortSignal
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.SetAbortSignal method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetAbortSignal` method sets a flag which indicates whether to stop rendering and reject further samples.

## Syntax


```C++
void SetAbortSignal(
   BOOL bAbort
);
```



## Parameters

<dl> <dt>

*bAbort* 
</dt> <dd>

Boolean value indicating whether to stop rendering. If **TRUE**, the filter will not render any more samples.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method sets the [**CBaseRenderer::m\_bAbort**](cbaserenderer-m-babort.md) flag.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




