---
description: The m\_bInit member variable indicates whether the CImageSample object has been initialized. If so, the value if TRUE. Otherwise, it is FALSE.
ms.assetid: bd508622-356e-46fe-98aa-c001c7742383
title: CImageSample::m_bInit member (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bInit
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CImageSample::m\_bInit member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `m_bInit` member variable indicates whether the **CImageSample** object has been initialized. If so, the value if **TRUE**. Otherwise, it is **FALSE**.

## Syntax


```C++
BOOL m_bInit;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageSample Class**](cimagesample.md)
</dt> <dt>

[**CImageSample::GetDIBData**](cimagesample-getdibdata.md)
</dt> <dt>

[**CImageSample::SetDIBData**](cimagesample-setdibdata.md)
</dt> </dl>

 

 




