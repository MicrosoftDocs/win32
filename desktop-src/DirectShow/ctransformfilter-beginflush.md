---
description: CTransformFilter.BeginFlush method - The BeginFlush method begins a flush operation.
ms.assetid: 15bea993-f862-4791-b784-0d0468c6c05c
title: CTransformFilter.BeginFlush method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.BeginFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformFilter.BeginFlush method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `BeginFlush` method begins a flush operation.

## Syntax


```C++
virtual HRESULT BeginFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

At the start of a flush operation, the input pin's [**CTransformInputPin::BeginFlush**](ctransforminputpin-beginflush.md) method calls this method. This method passes the `BeginFlush` call downstream.

If the derived class uses a worker thread to deliver samples, it should discard any queued data during a flush operation. That can be done either in the `BeginFlush` method, or in the [**EndFlush**](ctransformfilter-endflush.md) method. However, note that calls to `BeginFlush` are not synchronized with the streaming thread. If the `BeginFlush` method discards the queued data, the filter must be careful not to process any more data between the `BeginFlush` and **EndFlush** calls. For more information, see [Data Flow for Filter Developers](data-flow-for-filter-developers.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




