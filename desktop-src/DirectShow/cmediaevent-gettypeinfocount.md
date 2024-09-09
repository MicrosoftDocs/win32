---
description: CMediaEvent.GetTypeInfoCount method - Retrieves the number of type-information interfaces provided by an object.
ms.assetid: e16bc324-bb49-4df2-afeb-2c2cd1620693
title: CMediaEvent.GetTypeInfoCount method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaEvent.GetTypeInfoCount
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaEvent.GetTypeInfoCount method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Retrieves the number of type-information interfaces provided by an object.

## Syntax


```C++
HRESULT GetTypeInfoCount(
   UINT *pctinfo
);
```



## Parameters

<dl> <dt>

*pctinfo* 
</dt> <dd>

Pointer to number of type-information interfaces that the object provides. If the object provides type information, this number is 1; otherwise, the number is 0.

</dd> </dl>

## Return value

Returns E\_POINTER if *pctinfo* is invalid; otherwise, returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaEvent Class**](cmediaevent.md)
</dt> </dl>

 

 




