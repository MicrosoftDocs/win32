---
description: The SetTargetRect method sets the current target rectangle (pure virtual). This is an internal member function that gets called when the destination rectangle changes.
ms.assetid: 9e48989d-5995-4f9d-82b2-01229473c3e8
title: CBaseControlVideo.SetTargetRect method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# CBaseControlVideo.SetTargetRect method

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

 

 




