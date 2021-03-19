---
description: The SetDefaultTargetRect method sets the default target video rectangle (pure virtual). This is an internal member function that gets called when the source rectangle is reset.
ms.assetid: bb7e32b2-f02c-465f-a8cb-6172d9724790
title: CBaseControlVideo.SetDefaultTargetRect method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.SetDefaultTargetRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.SetDefaultTargetRect method

The `SetDefaultTargetRect` method sets the default target video rectangle (pure virtual). This is an internal member function that gets called when the source rectangle is reset.

## Syntax


```C++
virtual HRESULT SetDefaultTargetRect() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

Derived classes should override this to reset the destination video rectangle. It is called from the [**CBaseControlVideo::SetDefaultDestinationPosition**](cbasecontrolvideo-setdefaultdestinationposition.md) member function.

The following example demonstrates an implementation of this function in a derived class.


```C++
// This is called when you reset the default target rectangle.
HRESULT CVideoText::SetDefaultTargetRect()
{
    VIDEOINFO *pVideoInfo = (VIDEOINFO *) m_pRenderer->m_mtIn.Format();
    BITMAPINFOHEADER *pHeader = HEADER(pVideoInfo);
    RECT TargetRect = {0,0,m_Size.cx,m_Size.cy};
    m_pRenderer->m_DrawImage.SetTargetRect(&TargetRect);
    return NOERROR;
}
```



In this example, CVideoText is a class derived from [**CBaseControlVideo**](cbasecontrolvideo.md), m\_pRenderer holds an object of a class derived from [**CBaseVideoRenderer**](cbasevideorenderer.md), and the m\_DrawImage data member, defined in the derived class, holds a [**CDrawImage**](cdrawimage.md) object. The m\_mtIn data member, also defined in the derived class, holds a [**CMediaType**](cmediatype.md) object with the media type of the input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




