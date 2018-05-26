---
Description: The OnWaitStart method is called when the filter starts waiting for a samples presentation time.
ms.assetid: 598cd676-3afe-4ec9-ae38-83971412e6a7
title: CBaseRenderer.OnWaitStart method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer.OnWaitStart method

The `OnWaitStart` method is called when the filter starts waiting for a sample's presentation time.

## Syntax


```C++
virtual void OnWaitStart();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The [**CBaseRenderer::WaitForRenderTime**](cbaserenderer-waitforrendertime.md) method calls this method when it begins waiting for a sample's presentation time. This method does not do anything in the base class, but the derived class can override it.

If you are implementing quality control, you might override this method along with the [**CBaseRenderer::OnWaitEnd**](cbaserenderer-onwaitend.md) method. You can use these methods to track the filter's performance.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




