---
description: The JoinFilterGraph method notifies the filter that it has joined or left a filter graph. This method implements the IBaseFilter::JoinFilterGraph method.
ms.assetid: ee02650c-aaf0-4a0e-914f-180230010709
title: CBaseFilter.JoinFilterGraph method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.JoinFilterGraph
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseFilter.JoinFilterGraph method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `JoinFilterGraph` method notifies the filter that it has joined or left a filter graph. This method implements the [**IBaseFilter::JoinFilterGraph**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-joinfiltergraph) method.

## Syntax


```C++
HRESULT JoinFilterGraph(
       IFilterGraph *pGraph,
  [in] LPCWSTR      pName
);
```



## Parameters

<dl> <dt>

*pGraph* 
</dt> <dd>

Pointer to the filter graph manager's [**IFilterGraph**](/windows/desktop/api/Strmif/nn-strmif-ifiltergraph) interface, or **NULL** if the filter is leaving the graph.

</dd> <dt>

*pName* \[in\]
</dt> <dd>

Pointer to a Unicode string containing a name for the filter.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method sets the [**CBaseFilter::m\_pGraph**](cbasefilter-m-pgraph.md) member variable equal to the *pGraph* parameter. It also queries for an [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink) interface pointer and stores it in the [**CBaseFilter::m\_pSink**](cbasefilter-m-psink.md) member variable. However, the filter does not keep a reference count on either of these interfaces. Doing so would create a circular reference count, because the filter graph manager keeps a reference count on the filter.

The method copies the string specified by *pName* into the [**CBaseFilter::m\_pName**](cbasefilter-m-pname.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




