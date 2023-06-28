---
description: The GetStdDev method estimates the standard deviation in milliseconds between when each frame is due and when it is actually rendered, for per-frame statistics.
ms.assetid: 1a4d5c8d-38de-434f-b218-412d45976b8c
title: CBaseVideoRenderer.GetStdDev method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.GetStdDev
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseVideoRenderer.GetStdDev method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetStdDev` method estimates the standard deviation in milliseconds between when each frame is due and when it is actually rendered, for per-frame statistics.

## Syntax


```C++
HRESULT GetStdDev(
   int      nSamples,
   int      *piResult,
   LONGLONG llSumSq,
   LONGLONG iTot
);
```



## Parameters

<dl> <dt>

*nSamples* 
</dt> <dd>

Integer value that contains the number of video samples received by the video renderer.

</dd> <dt>

*piResult* 
</dt> <dd>

Pointer to an integer value that will contain the standard deviation.

</dd> <dt>

*llSumSq* 
</dt> <dd>

Value that represents the standard deviation, in milliseconds, of all rendered video samples. The lower the value, the more consistent the rendering.

</dd> <dt>

*iTot* 
</dt> <dd>

Value that represents the mean value, in milliseconds, between the stamped time and rendered time for all rendered video samples.

</dd> </dl>

## Return value

Returns NOERROR.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




