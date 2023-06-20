---
description: The OnStopStreaming method is called at the end of streaming to fix times for the property page report.
ms.assetid: 92174edb-2f6c-4bad-91c5-769aaebcc495
title: CBaseVideoRenderer.OnStopStreaming method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.OnStopStreaming
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseVideoRenderer.OnStopStreaming method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `OnStopStreaming` method is called at the end of streaming to fix times for the property page report.

## Syntax


```C++
HRESULT OnStopStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

This member function is called twice, once when pausing and again when the stream is actually stopped.

This member function overrides [**CBaseRenderer::OnStopStreaming**](cbaserenderer-onstopstreaming.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




