---
description: The get\_Jitter method retrieves the standard deviation of time in milliseconds between each frame and the next for all frames since streaming started.
ms.assetid: 629e725e-7dee-4824-8f79-cd3335f4901b
title: CBaseVideoRenderer.get_Jitter method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.get_Jitter
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.get\_Jitter method

The `get_Jitter` method retrieves the standard deviation of time in milliseconds between each frame and the next for all frames since streaming started.

## Syntax


```C++
HRESULT get_Jitter(
   int *piJitter
);
```



## Parameters

<dl> <dt>

*piJitter* 
</dt> <dd>

Pointer to the standard deviation of the interframe time, in milliseconds.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IQualProp::get\_Jitter**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-iqualprop-get_jitter) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




