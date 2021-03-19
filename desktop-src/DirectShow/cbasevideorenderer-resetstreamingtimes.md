---
description: The ResetStreamingTimes method resets all times that control the streaming.
ms.assetid: 8a596760-a45a-4486-bb91-aab10bbf927f
title: CBaseVideoRenderer.ResetStreamingTimes method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.ResetStreamingTimes
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.ResetStreamingTimes method

The `ResetStreamingTimes` method resets all times that control the streaming.

## Syntax


```C++
virtual HRESULT ResetStreamingTimes();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

The times are set so that frames will not be initially dropped and so that the first frame will be drawn.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




