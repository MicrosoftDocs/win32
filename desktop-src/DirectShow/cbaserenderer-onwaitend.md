---
description: The OnWaitEnd method is called when the filter is done waiting for a sample's presentation time.
ms.assetid: 47ff8f79-da69-4dcf-8cbb-02c1b56e382e
title: CBaseRenderer.OnWaitEnd method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.OnWaitEnd
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.OnWaitEnd method

The `OnWaitEnd` method is called when the filter is done waiting for a sample's presentation time.

## Syntax


```C++
virtual void OnWaitEnd();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The [**CBaseRenderer::WaitForRenderTime**](cbaserenderer-waitforrendertime.md) method calls this method when it has finished waiting for a sample's presentation time. This method does not do anything in the base class, but the derived class can override it.

If you are implementing quality control, you might override this method along with the [**CBaseRenderer::OnWaitStart**](cbaserenderer-onwaitstart.md) method. You can use these methods to track the filter's performance.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




