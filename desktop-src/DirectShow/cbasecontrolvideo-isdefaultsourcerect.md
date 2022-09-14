---
description: The IsDefaultSourceRect method determines if the renderer is using the default source rectangle (pure virtual).
ms.assetid: 08c7a365-585c-47e6-9c26-6aa1fa3625e7
title: CBaseControlVideo.IsDefaultSourceRect method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.IsDefaultSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.IsDefaultSourceRect method

The `IsDefaultSourceRect` method determines if the renderer is using the default source rectangle (pure virtual).

## Syntax


```C++
virtual HRESULT IsDefaultSourceRect() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if the renderer is using the default source; otherwise, returns S\_FALSE.

## Remarks

This member function must be implemented in the derived class. It is called by the [**CBaseControlVideo::IsUsingDefaultSource**](cbasecontrolvideo-isusingdefaultsource.md) member function.

The following example demonstrates an implementation of this function in a derived class.


```C++
// Return S_OK if using the default source; otherwise, S_FALSE.
HRESULT CVideoText::IsDefaultSourceRect()
{
    RECT SourceRect;

    VIDEOINFO *pVideoInfo = (VIDEOINFO *) m_pRenderer->m_mtIn.Format();
    BITMAPINFOHEADER *pHeader = HEADER(pVideoInfo);
    m_pRenderer->m_DrawImage.GetSourceRect(&SourceRect);

    // Check the coordinates that match the video dimensions.

    if (SourceRect.left != 0 || SourceRect.top != 0 ||
            SourceRect.right != pHeader->biWidth ||
                SourceRect.bottom != pHeader->biHeight) {
                    return S_FALSE;
    }
    return S_OK;
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

 

 




