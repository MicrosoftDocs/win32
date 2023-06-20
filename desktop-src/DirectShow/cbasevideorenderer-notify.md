---
description: The Notify method receives a notification that a quality change is requested.
ms.assetid: bb9aa1c3-caef-42fb-87d2-75cc3691f64f
title: CBaseVideoRenderer.Notify method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.Notify
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseVideoRenderer.Notify method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Notify` method receives a notification that a quality change is requested.

## Syntax


```C++
HRESULT Notify(
  [in] IBaseFilter *pSelf,
  [in] Quality     q
);
```



## Parameters

<dl> <dt>

*pSelf* \[in\]
</dt> <dd>

Pointer to the filter that is sending the quality notification.

</dd> <dt>

*q* \[in\]
</dt> <dd>

Quality notification structure.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualityControl::Notify**](/windows/desktop/api/Strmif/nf-strmif-iqualitycontrol-notify) method on the video renderer. This is called, typically by the filter graph manager, when the quality must be cut back. This might occur when the quality of audio playback has been increased to the point that the video playback quality must be decreased.

`Notify` sets the **m\_trThrottle** data member to a delay value to be inserted between frames by [**ThrottleWait**](cbasevideorenderer-throttlewait.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




