---
description: The SetDefaultSourceRect method sets the default source video rectangle (pure virtual). This in an internal member function that gets called when the source rectangle is reset.
ms.assetid: d0dae0a9-8763-485e-b9d3-80076a3f2f35
title: CBaseControlVideo.SetDefaultSourceRect method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.SetDefaultSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.SetDefaultSourceRect method

The `SetDefaultSourceRect` method sets the default source video rectangle (pure virtual). This in an internal member function that gets called when the source rectangle is reset.

## Syntax


```C++
virtual HRESULT SetDefaultSourceRect() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

Derived classes should override this to reset the source rectangle. It is called from [**CBaseControlVideo::SetDefaultSourcePosition**](cbasecontrolvideo-setdefaultsourceposition.md).

The following example demonstrates an implementation of this function in a derived class.


```C++
// This is called when you reset the default source rectangle.
HRESULT CVideoText::SetDefaultSourceRect()
{
    VIDEOINFO *pVideoInfo = (VIDEOINFO *) m_pRenderer->m_mtIn.Format();
    BITMAPINFOHEADER *pHeader = HEADER(pVideoInfo);
    RECT SourceRect = {0,0,pHeader->biWidth,pHeader->biHeight};
    m_pRenderer->m_DrawImage.SetSourceRect(&SourceRect);
    return NOERROR;
}
```



In this example, CVideoText is a class derived from [**CBaseControlVideo**](cbasecontrolvideo.md), m\_pRenderer holds an object of a class derived from [**CBaseVideoRenderer**](cbasevideorenderer.md), and the m\_DrawImage data member, defined in the derived class, holds a [**CDrawImage**](cdrawimage.md) object. The m\_mtIn data member, also defined in the derived class, holds a [**CMediaType**](cmediatype.md) object with media type of the input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




