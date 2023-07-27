---
description: The CBaseBasicVideo class implements the IDispatch methods of the IBasicVideo interface. The remaining IBasicVideo methods are left as pure virtual methods, and must be implemented by a derived class.
ms.assetid: 58396c81-8a06-4b82-b278-a98573e9d5b3
title: CBaseBasicVideo class (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseBasicVideo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseBasicVideo class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cbasebasicvideo class hierarchy](images/wctrl02.png)

The `CBaseBasicVideo` class implements the **IDispatch** methods of the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface. The remaining **IBasicVideo** methods are left as pure virtual methods, and must be implemented by a derived class.

The **IDispatch** methods in this class are standard implementations, and are not described in detail here.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> <dt>

[**CBaseDispatch Class**](cbasedispatch.md)
</dt> </dl>

 

 




