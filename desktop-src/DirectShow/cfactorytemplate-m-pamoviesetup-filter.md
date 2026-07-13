---
description: Pointer to an AMOVIESETUP\_FILTER structure.
ms.assetid: 72db601b-78a3-484a-a27f-147ec36022ab
title: CFactoryTemplate::m_pAMovieSetup_Filter member (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_pAMovieSetup_Filter
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CFactoryTemplate::m\_pAMovieSetup\_Filter member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Pointer to an [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md) structure.

## Syntax


```C++
const AMOVIESETUP_FILTER *m_pAMovieSetup_Filter;
```



## Remarks

Use this structure to make a filter self-registering. If your component is not a filter, this member variable can be **NULL**. For more information, see How to Register DirectShow Filters.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




