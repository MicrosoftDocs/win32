---
description: The get\_FramesDrawn method retrieves the m\_cFramesDrawn member variable, giving the number of frames drawn since streaming started.
ms.assetid: 486b5541-2952-47ce-944e-4efb8e5af9dd
title: CBaseVideoRenderer.get_FramesDrawn method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.get_FramesDrawn
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.get\_FramesDrawn method

The `get_FramesDrawn` method retrieves the **m\_cFramesDrawn** member variable, giving the number of frames drawn since streaming started.

## Syntax


```C++
HRESULT get_FramesDrawn(
   int *pcFramesDrawn
);
```



## Parameters

<dl> <dt>

*pcFramesDrawn* 
</dt> <dd>

Pointer to the number of frames drawn.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualProp::get\_FramesDrawn**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-iqualprop-get_framesdrawn) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




