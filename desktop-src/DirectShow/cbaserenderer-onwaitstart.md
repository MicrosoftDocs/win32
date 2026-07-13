---
description: The OnWaitStart method is called when the filter starts waiting for a sample's presentation time.
ms.assetid: 598cd676-3afe-4ec9-ae38-83971412e6a7
title: CBaseRenderer.OnWaitStart method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.OnWaitStart
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.OnWaitStart method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `OnWaitStart` method is called when the filter starts waiting for a sample's presentation time.

## Syntax


```C++
virtual void OnWaitStart();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The [**CBaseRenderer::WaitForRenderTime**](cbaserenderer-waitforrendertime.md) method calls this method when it begins waiting for a sample's presentation time. This method does not do anything in the base class, but the derived class can override it.

If you are implementing quality control, you might override this method along with the [**CBaseRenderer::OnWaitEnd**](cbaserenderer-onwaitend.md) method. You can use these methods to track the filter's performance.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




