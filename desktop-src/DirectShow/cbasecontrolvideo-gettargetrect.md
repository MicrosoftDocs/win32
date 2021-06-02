---
description: The GetTargetRect method retrieves the destination rectangle. This is an internal helper member function.
ms.assetid: bf9d95c9-eee8-46b8-bdee-a7d16777ed83
title: CBaseControlVideo.GetTargetRect method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetTargetRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.GetTargetRect method

The `GetTargetRect` method retrieves the destination rectangle. This is an internal helper member function.

## Syntax


```C++
virtual HRESULT GetTargetRect(
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

This member function must be overridden in the derived class to return the target rectangle held by the video renderer. It is called from the following [**CBaseControlVideo**](cbasecontrolvideo.md) member functions.

-   [**CBaseControlVideo::GetDestinationPosition**](cbasecontrolvideo-getdestinationposition.md)
-   [**CBaseControlVideo::put\_DestinationLeft**](cbasecontrolvideo-put-destinationleft.md)
-   [**CBaseControlVideo::get\_DestinationLeft**](cbasecontrolvideo-get-destinationleft.md)
-   [**CBaseControlVideo::put\_DestinationWidth**](cbasecontrolvideo-put-destinationwidth.md)
-   [**CBaseControlVideo::get\_DestinationWidth**](cbasecontrolvideo-get-destinationwidth.md)
-   [**CBaseControlVideo::put\_DestinationTop**](cbasecontrolvideo-put-destinationtop.md)
-   [**CBaseControlVideo::get\_DestinationTop**](cbasecontrolvideo-get-destinationtop.md)
-   [**CBaseControlVideo::put\_DestinationHeight**](cbasecontrolvideo-put-destinationheight.md)
-   [**CBaseControlVideo::get\_DestinationHeight**](cbasecontrolvideo-get-destinationheight.md)

The following example demonstrates an implementation of this function in a derived class.


```C++
// Return the current destination rectangle.
HRESULT CVideoText::GetTargetRect(RECT *pTargetRect)
{
    ASSERT(pTargetRect);
    m_pRenderer->m_DrawImage.GetTargetRect(pTargetRect);
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

 

 




