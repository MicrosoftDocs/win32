---
description: The SetTargetRect method sets the current target rectangle (pure virtual). This is an internal member function that gets called when the destination rectangle changes.
ms.assetid: 9e48989d-5995-4f9d-82b2-01229473c3e8
title: CBaseControlVideo.SetTargetRect method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.SetTargetRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.SetTargetRect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetTargetRect` method sets the current target rectangle (pure virtual). This is an internal member function that gets called when the destination rectangle changes.

## Syntax


```C++
virtual HRESULT SetTargetRect(
   RECT *pTargetRect
) = 0;
```



## Parameters

<dl> <dt>

*pTargetRect* 
</dt> <dd>

Pointer to the destination rectangle.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Derived classes should override this to know when the destination rectangle changes. It is called from the following member functions.

-   [**CBaseControlVideo::SetDestinationPosition**](cbasecontrolvideo-setdestinationposition.md)
-   [**CBaseControlVideo::put\_DestinationLeft**](cbasecontrolvideo-put-destinationleft.md)
-   [**CBaseControlVideo::put\_DestinationWidth**](cbasecontrolvideo-put-destinationwidth.md)
-   [**CBaseControlVideo::put\_DestinationTop**](cbasecontrolvideo-put-destinationtop.md)
-   [**CBaseControlVideo::put\_DestinationHeight**](cbasecontrolvideo-put-destinationheight.md)

The following example demonstrates an implementation of this function in a derived class.


```C++
HRESULT CVideoText::SetTargetRect(RECT *pTargetRect)
{
    m_pRenderer->m_DrawImage.SetTargetRect(pTargetRect);
    return NOERROR;
}
```



In this example, CVideoText is a class derived from [**CBaseControlVideo**](cbasecontrolvideo.md), m\_pRenderer holds an object of a class derived from [**CBaseVideoRenderer**](cbasevideorenderer.md), and the m\_DrawImage data member, defined in the derived class, holds a [**CDrawImage**](cdrawimage.md) object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




