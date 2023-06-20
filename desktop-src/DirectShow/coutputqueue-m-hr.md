---
description: HRESULT value that indicates whether the object will accept samples. If the value is S\_OK, the object will accept samples. Otherwise, it rejects samples.
ms.assetid: e05d4d2e-cc3e-4b83-8531-bc4bd6d665ac
title: COutputQueue::m_hr member (Outputq.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_hr
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COutputQueue::m\_hr member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

**HRESULT** value that indicates whether the object will accept samples. If the value is S\_OK, the object will accept samples. Otherwise, it rejects samples.

## Syntax


```C++
HRESULT m_hr;
```



## Remarks

This member variable is used to coordinate activities across threads. If the downstream input pin rejects a sample, or if the object begins flushing, the value is set to S\_FALSE or an error code. The object will not deliver any more samples until flushing is complete, or until the [**COutputQueue::Reset**](coutputqueue-reset.md) method is called.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




