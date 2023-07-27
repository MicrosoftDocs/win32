---
description: The SetSourceRect method sets the current source video rectangle (pure virtual). This is an internal member function that gets called when the source rectangle changes.
ms.assetid: 13bb594b-b154-40a2-ad00-f1e86781074d
title: CBaseControlVideo.SetSourceRect method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.SetSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.SetSourceRect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetSourceRect` method sets the current source video rectangle (pure virtual). This is an internal member function that gets called when the source rectangle changes.

## Syntax


```C++
virtual HRESULT SetSourceRect(
   RECT *pSourceRect
) = 0;
```



## Parameters

<dl> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to the source rectangle.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Derived classes should override this member function to know when the source rectangle changes. It is called from the following member functions.

-   [**CBaseControlVideo::SetSourcePosition**](cbasecontrolvideo-setsourceposition.md)
-   [**CBaseControlVideo::put\_SourceLeft**](cbasecontrolvideo-put-sourceleft.md)
-   [**CBaseControlVideo::put\_SourceWidth**](cbasecontrolvideo-put-sourcewidth.md)
-   [**CBaseControlVideo::put\_SourceTop**](cbasecontrolvideo-put-sourcetop.md)
-   [**CBaseControlVideo::put\_SourceHeight**](cbasecontrolvideo-put-sourceheight.md)

The following example demonstrates an implementation of this function in a derived class.


```C++
HRESULT CVideoText::SetSourceRect(RECT *pSourceRect)
{
    m_pRenderer->m_DrawImage.SetSourceRect(pSourceRect);
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

 

 




