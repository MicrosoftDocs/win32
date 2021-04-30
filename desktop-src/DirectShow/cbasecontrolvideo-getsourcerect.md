---
description: The GetSourceRect method retrieves the source rectangle. This is an internal method.
ms.assetid: 51028b79-6aab-4abc-8ee8-2965bda9d191
title: CBaseControlVideo.GetSourceRect method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.GetSourceRect method

The `GetSourceRect` method retrieves the source rectangle. This is an internal method.

## Syntax


```C++
virtual HRESULT GetSourceRect(
   RECT *pSourceRect
) = 0;
```



## Parameters

<dl> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to the retrieved source rectangle.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function must be overridden in the derived class to return the source rectangle held by the video renderer. It is called from the following [**CBaseControlVideo**](cbasecontrolvideo.md) member functions.

-   [**CBaseControlVideo::GetSourcePosition**](cbasecontrolvideo-getsourceposition.md)
-   [**CBaseControlVideo::put\_SourceLeft**](cbasecontrolvideo-put-sourceleft.md)
-   [**CBaseControlVideo::get\_SourceLeft**](cbasecontrolvideo-get-sourceleft.md)
-   [**CBaseControlVideo::put\_SourceWidth**](cbasecontrolvideo-put-sourcewidth.md)
-   [**CBaseControlVideo::get\_SourceWidth**](cbasecontrolvideo-get-sourcewidth.md)
-   [**CBaseControlVideo::put\_SourceTop**](cbasecontrolvideo-put-sourcetop.md)
-   [**CBaseControlVideo::get\_SourceTop**](cbasecontrolvideo-get-sourcetop.md)
-   [**CBaseControlVideo::put\_SourceHeight**](cbasecontrolvideo-put-sourceheight.md)
-   [**CBaseControlVideo::get\_SourceHeight**](cbasecontrolvideo-get-sourceheight.md)

The following example demonstrates an implementation of this function in a derived class.


```C++
// Return the current source rectangle
HRESULT CVideoText::GetSourceRect(RECT *pSourceRect)
{
    ASSERT(pSourceRect);
    m_pRenderer->m_DrawImage.GetSourceRect(pSourceRect);
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

 

 




